ONE WORDING EACH

Put this zip's files into the calculator project, then delete the repeated
wordings, then commit and push.

Where to put them
  Unzip one-wording-each.zip.
  Copy everything inside the one-wording-each folder onto the calculator
  folder, so paths line up. README.md lands next to the project's README.md.
  algebra_word_problems.txt lands in algebra_word_problems/.
  INDEX.md lands in operators_one_algebra_word_problem_per_file/.
  Say yes when the copy asks to replace a file.

Then delete the repeats
  DELETE_THESE.txt lists 1,563 paths. Each path is a repeated wording:
  the same sentence with different numbers. From the calculator folder:

    while read -r path; do rm -rf -- "$path"; done < DELETE_THESE.txt

  Do not delete DELETE_THESE.txt until that command has finished.
  Empty category folders can stay or go. The project does not need them.

What you should have afterwards
  479 stored wordings, one of each sentence.
  235 Ready (220 word solver, 15 number puzzle).
  The solver's wrong count on these 479 is 0.

This is the same change as pull request 5:
  https://github.com/IWatchSheep/calculator/pull/5
