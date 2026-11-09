//! Probe for forming_chess: which of the 20 strategy templates show up where.
//!
//!   chess_probe archive <games_dir>                 tally the strategy flags stored in archived games
//!   chess_probe sans <games.txt> <out_dir>          replay SAN games, store them in a general-bank archive, tally
//!   chess_probe positions <positions.txt>           check hand-made positions against their expected strategy
use forming_chess::{
    archive::{Archive, GENERAL},
    board::*,
    drill,
    history::WINDOW,
    index::{goal_after, GameResult, Status},
    normalize::{self, Cat},
    strategies::{self, Ctx, TurnInfo, NAMES},
};
use std::{
    fs,
    io::{BufRead, BufReader},
};

#[derive(Clone)]
struct Tally {
    games: u64,
    positions: u64,
    pos_bits: [[u64; 3]; 20],
    game_bits: [[u64; 3]; 20],
    first: [[String; 3]; 20],
}

impl Tally {
    fn new() -> Tally {
        Tally { games: 0, positions: 0, pos_bits: [[0; 3]; 20], game_bits: [[0; 3]; 20], first: Default::default() }
    }
    fn add_position(&mut self, flags: &[u8; 20], label: &str) {
        self.positions += 1;
        for s in 0..20 {
            for bit in 0..3 {
                if flags[s] & (1 << bit) != 0 {
                    self.pos_bits[s][bit] += 1;
                    if self.first[s][bit].is_empty() {
                        self.first[s][bit] = label.to_string();
                    }
                }
            }
        }
    }
    fn end_game(&mut self, seen: &[u8; 20]) {
        self.games += 1;
        for s in 0..20 {
            for bit in 0..3 {
                if seen[s] & (1 << bit) != 0 {
                    self.game_bits[s][bit] += 1;
                }
            }
        }
    }
    fn best_stage(&self, s: usize) -> &'static str {
        if self.pos_bits[s][2] > 0 {
            "COMPLETION"
        } else if self.pos_bits[s][1] > 0 {
            "progress"
        } else if self.pos_bits[s][0] > 0 {
            "foundation"
        } else {
            "-"
        }
    }
    fn print(&self, title: &str, show_first: bool) {
        println!("== {} ==", title);
        println!("games: {}   positions with flags counted: {}", self.games, self.positions);
        println!("{:>2}  {:<30} {:>12} {:>12} {:>12}   {:>9} {:>9} {:>9}   best stage", "#", "strategy", "foundation", "progress", "completion", "g:found", "g:prog", "g:compl");
        let mut seen = 0;
        for s in 0..20 {
            if self.pos_bits[s][0] + self.pos_bits[s][1] + self.pos_bits[s][2] > 0 {
                seen += 1;
            }
            println!(
                "{:>2}  {:<30} {:>12} {:>12} {:>12}   {:>9} {:>9} {:>9}   {}",
                s + 1,
                NAMES[s],
                self.pos_bits[s][0],
                self.pos_bits[s][1],
                self.pos_bits[s][2],
                self.game_bits[s][0],
                self.game_bits[s][1],
                self.game_bits[s][2],
                self.best_stage(s)
            );
        }
        println!("strategies seen at least once: {} of 20", seen);
        if show_first {
            for s in 0..20 {
                for (bit, name) in ["foundation", "progress", "completion"].iter().enumerate() {
                    if !self.first[s][bit].is_empty() {
                        println!("   first {} of #{} {}: {}", name, s + 1, NAMES[s], self.first[s][bit]);
                    }
                }
            }
        }
    }
}

fn tally_archive(dirs: &[String]) {
    let dir = dirs.join(" + ");
    let dir = dir.as_str();
    let mut t = Tally::new();
    let mut files: Vec<std::path::PathBuf> = Vec::new();
    for d in dirs {
        let mut part: Vec<_> = fs::read_dir(d).expect("games dir").filter_map(|e| e.ok()).map(|e| e.path()).collect();
        part.sort();
        files.extend(part);
    }
    let mut counts = (0u64, 0u64, 0u64, 0u64); // white wins, black wins, draws, other
    let mut moves_total = 0u64;
    for path in &files {
        let f = fs::File::open(path).expect("open");
        let mut seen = [0u8; 20];
        let mut game = String::new();
        let mut in_game = false;
        let mut ply = 0u32;
        for line in BufReader::new(f).lines().map_while(Result::ok) {
            if line.starts_with("GAME START") {
                seen = [0; 20];
                in_game = true;
                ply = 0;
                game = format!("{} {}", path.file_name().unwrap().to_string_lossy(), line);
            } else if line.starts_with("GAME END") || line.starts_with("GAME STOPPED") {
                if in_game {
                    t.end_game(&seen);
                    if line.contains("white-wins") {
                        counts.0 += 1;
                    } else if line.contains("black-wins") {
                        counts.1 += 1;
                    } else if line.contains("draw") {
                        counts.2 += 1;
                    } else {
                        counts.3 += 1;
                    }
                }
                in_game = false;
            } else if in_game && (line.starts_with("m\t") || line.starts_with("M\t")) {
                let parts: Vec<&str> = line.split('\t').collect();
                let flags = if line.starts_with("m\t") {
                    strategies::flags_from_sparse(parts.get(2).copied().unwrap_or("-"))
                } else {
                    strategies::flags_from_text(parts.get(5).copied().unwrap_or(""))
                };
                ply += 1;
                moves_total += 1;
                for s in 0..20 {
                    seen[s] |= flags[s];
                }
                if flags.iter().any(|&x| x != 0) {
                    t.add_position(&flags, &format!("{} ply {}", game.chars().take(110).collect::<String>(), ply));
                }
            }
        }
    }
    println!("archive files read: {}   moves read: {}", files.len(), moves_total);
    println!("results: white wins {}  black wins {}  draws {}  other {}", counts.0, counts.1, counts.2, counts.3);
    t.print(&format!("Strategy flags found in the archive {}", dir), false);
}

fn result_of(s: &str) -> GameResult {
    match s {
        "1-0" => GameResult::WhiteWin,
        "0-1" => GameResult::BlackWin,
        _ => GameResult::Draw,
    }
}

/// Play SAN games, store them in a general-bank archive, tally the mover's flags (as the program stores them)
/// and both sides' flags after every ply.
fn play_sans(file: &str, out: &str) {
    let text = fs::read_to_string(file).expect("games file");
    let archive = Archive::new(std::path::Path::new(out));
    let mut mover_tally = Tally::new();
    let mut both_tally = Tally::new();
    let mut problems = 0;
    for line in text.lines().map(str::trim).filter(|l| !l.is_empty() && !l.starts_with('#')) {
        let mut parts = line.splitn(3, '|');
        let (name, res, moves) = (parts.next().unwrap(), parts.next().unwrap(), parts.next().unwrap());
        let mut b = Board::start();
        let start = b;
        let mut writer = archive.begin_game(GENERAL, &start, None).expect("begin game");
        let mut windows: [Vec<TurnInfo>; 2] = [Vec::new(), Vec::new()];
        let mut seen_mover = [0u8; 20];
        let mut seen_both = [0u8; 20];
        let mut ply = 0u32;
        let mut ok = true;
        for tok in moves.split_whitespace() {
            if tok.ends_with('.') || tok.chars().next().map_or(false, |c| c.is_ascii_digit()) && tok.contains('.') {
                continue;
            }
            let Some(m) = b.parse_move(tok) else {
                println!("PROBLEM {}: ply {} cannot read move {:?} in position {}", name, ply + 1, tok, b.key());
                problems += 1;
                ok = false;
                break;
            };
            let white = b.white_to_move;
            let w = &mut windows[if white { 0 } else { 1 }];
            w.push(TurnInfo { white, from: m.from, to: m.to, piece: b.sq[m.from as usize], captured: b.captured_piece(&m) });
            if w.len() > WINDOW {
                w.remove(0);
            }
            let after = b.make(&m);
            ply += 1;
            let mover = strategies::flags_all(&Ctx { b: &after, white, window: &windows[if white { 0 } else { 1 }] });
            let other_w = &windows[if white { 1 } else { 0 }];
            let other = strategies::flags_all(&Ctx { b: &after, white: !white, window: other_w });
            let label = format!("{} ply {} ({}) {}", name, ply, if white { "White" } else { "Black" }, tok);
            mover_tally.add_position(&mover, &label);
            both_tally.add_position(&mover, &label);
            both_tally.add_position(&other, &format!("{} ply {} ({} side)", name, ply, if white { "Black" } else { "White" }));
            for s in 0..20 {
                seen_mover[s] |= mover[s];
                seen_both[s] |= mover[s] | other[s];
            }
            writer.add_move(ply, &b, &m, &mover).expect("write move");
            b = after;
        }
        let _ = writer.finish(if ok { result_of(res) } else { GameResult::Stopped });
        mover_tally.end_game(&seen_mover);
        both_tally.end_game(&seen_both);
        println!("played {:<28} {} plies  result {}", name, ply, res);
    }
    println!("problems: {}", problems);
    mover_tally.print("Strategy flags of the MOVER after each ply (what the program stores in the archive)", false);
    both_tally.print("Strategy flags of BOTH sides after each ply", true);
}

/// Hand-made positions. Line: name | strategy number 1-20 | side w/b | FEN | optional SAN moves played from the FEN.
fn check_positions(file: &str) {
    let text = fs::read_to_string(file).expect("positions file");
    let mut best = [0u8; 20];
    let mut rows = 0;
    for line in text.lines().map(str::trim).filter(|l| !l.is_empty() && !l.starts_with('#')) {
        let p: Vec<&str> = line.split('|').map(str::trim).collect();
        let (name, idx, side, fen) = (p[0], p[1].parse::<usize>().unwrap() - 1, p[2], p[3]);
        let mut b = match Board::from_fen(fen) {
            Ok(b) => b,
            Err(e) => {
                println!("BAD FEN {}: {}", name, e);
                continue;
            }
        };
        let mut windows: [Vec<TurnInfo>; 2] = [Vec::new(), Vec::new()];
        if let Some(moves) = p.get(4) {
            for tok in moves.split_whitespace() {
                let Some(m) = b.parse_move(tok) else {
                    println!("BAD MOVE {} {}", name, tok);
                    break;
                };
                let white = b.white_to_move;
                let w = &mut windows[if white { 0 } else { 1 }];
                w.push(TurnInfo { white, from: m.from, to: m.to, piece: b.sq[m.from as usize], captured: b.captured_piece(&m) });
                if w.len() > WINDOW {
                    w.remove(0);
                }
                b = b.make(&m);
            }
        }
        let white = side == "w";
        let flags = strategies::flags_all(&Ctx { b: &b, white, window: &windows[if white { 0 } else { 1 }] });
        let f = flags[idx];
        let stage = if f & 4 != 0 { "COMPLETION" } else if f & 2 != 0 { "progress" } else if f & 1 != 0 { "foundation" } else { "NOT FOUND" };
        best[idx] = best[idx].max(f);
        rows += 1;
        let others: Vec<String> = flags.iter().enumerate().filter(|(i, v)| **v != 0 && *i != idx).map(|(i, v)| format!("{}={}", i + 1, v)).collect();
        println!("#{:<2} {:<30} {:<28} -> {:<10} (flags {})   other strategies: {}", idx + 1, NAMES[idx], name, stage, f, others.join(","));
    }
    println!("\n== best stage reached per strategy over {} hand-made positions ==", rows);
    let mut found = 0;
    for s in 0..20 {
        let f = best[s];
        let stage = if f & 4 != 0 { "COMPLETION" } else if f & 2 != 0 { "progress" } else if f & 1 != 0 { "foundation" } else { "-" };
        if f != 0 {
            found += 1;
        }
        println!("{:>2}  {:<30} {}", s + 1, NAMES[s], stage);
    }
    println!("strategies found: {} of 20", found);
}


fn status_text(s: &Status) -> String {
    match s {
        Status::Win(d) => format!("PROVEN WIN for the pawn side in {} moves", d),
        Status::Draw => "PROVEN DRAW".to_string(),
        Status::Unknown => "not proven".to_string(),
    }
}

/// Read a solved king-and-pawn index: totals, principal variations, and a check of the stored distances.
fn kpk(dir: &str, fens: &[String]) {
    let archive = Archive::new(std::path::Path::new(dir));
    let (ix, merged, notes) = archive.open_index();
    println!("index loaded: {} stored positions, {} games merged. notes: {:?}", ix.nodes.len(), merged, notes);
    let (mut wins, mut draws, mut unknown) = (0u64, 0u64, 0u64);
    let mut longest = 0u32;
    for n in ix.nodes.iter().filter(|n| n.cat == Cat::Kpk) {
        match n.status {
            Status::Win(d) => {
                wins += 1;
                longest = longest.max(d);
            }
            Status::Draw => draws += 1,
            Status::Unknown => unknown += 1,
        }
    }
    println!("king and pawn against king, positions in the index: {}", wins + draws + unknown);
    println!("  proven wins for the pawn side: {}   proven draws: {}   not proven: {}   longest forced win: {} moves", wins, draws, unknown, longest);

    for fen in fens {
        let Ok(mut b) = Board::from_fen(fen) else {
            println!("bad fen {}", fen);
            continue;
        };
        let n = normalize::normalize(&b);
        let st = ix.lookup(&n.key()).map(|i| ix.nodes[i].status).unwrap_or(Status::Unknown);
        println!("\nposition {}\n  {}", fen, status_text(&st));
        let mut line = String::new();
        let mut moveno = 1;
        for ply in 0..60 {
            let Some(m) = drill::choose(&ix, &b) else { break };
            let san = b.san(&m);
            if b.white_to_move {
                line.push_str(&format!("{}. {} ", moveno, san));
            } else {
                if ply == 0 {
                    line.push_str(&format!("{}... ", moveno));
                }
                line.push_str(&format!("{} ", san));
                moveno += 1;
            }
            let after = b.make(&m);
            if let Some(r) = goal_after(&b, &m, &after) {
                line.push_str(&format!("   -> {}", r.text()));
                break;
            }
            b = after;
        }
        println!("  best play: {}", line);
    }

    // check: from a spread of proven-win positions, play both sides by the index and compare plies with the stored distance
    let all = normalize::kpk_positions(true);
    let (mut checked, mut exact, mut plus_one, mut off_by, mut never_finished, mut not_win) = (0u64, 0u64, 0u64, 0u64, 0u64, 0u64);
    let mut worst: i64 = 0;
    for (i, b0) in all.iter().enumerate() {
        if i % 60 != 0 {
            continue;
        }
        let n = normalize::normalize(b0);
        let Some(id) = ix.lookup(&n.key()) else { continue };
        let Status::Win(d) = ix.nodes[id].status else { continue };
        let mut b = *b0;
        let mut plies = 0i64;
        let mut finished = None;
        for _ in 0..300 {
            let Some(m) = drill::choose(&ix, &b) else { break };
            let after = b.make(&m);
            plies += 1;
            if let Some(r) = goal_after(&b, &m, &after) {
                finished = Some(r);
                break;
            }
            b = after;
        }
        checked += 1;
        match finished {
            Some(GameResult::WhiteWin) | Some(GameResult::BlackWin) => {
                if plies == d as i64 {
                    exact += 1;
                } else if plies == d as i64 + 1 {
                    plus_one += 1;
                } else {
                    off_by += 1;
                    worst = worst.max((plies - d as i64).abs());
                }
            }
            Some(_) => not_win += 1,
            None => never_finished += 1,
        }
    }
    println!("\ndistance check on {} proven wins sampled across the whole endgame:", checked);
    println!("  pawn side won by promotion after exactly the stored number of plies: {}   one ply more than stored (the promoting move): {}", exact, plus_one);
    println!("  won, but a different number of moves: {} (largest gap {})   did not end in a win: {}   did not finish in 300 plies: {}", off_by, worst, not_win, never_finished);
}

fn main() {
    let a: Vec<String> = std::env::args().collect();
    match a.get(1).map(|s| s.as_str()) {
        Some("archive") => tally_archive(&a[2..]),
        Some("sans") => play_sans(&a[2], &a[3]),
        Some("positions") => check_positions(&a[2]),
        Some("kpk") => kpk(&a[2], &a[3..]),
        _ => eprintln!("usage: chess_probe archive <games_dir> | sans <games.txt> <out_dir> | positions <positions.txt>"),
    }
}
