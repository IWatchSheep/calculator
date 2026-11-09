fn main() {
    use forming_chess::drill::start_sequence;
    let seq = start_sequence(1);
    println!("len {}", seq.len());
    for i in 0..5 {
        println!("start{} {}", i, seq[i].key());
    }
}
