# Tasks for lecture 7: programming basics (max +30)

- Create `github` repository (max +2)
  - Click `+` button in the right-top corner in github browser UI
  - Give repository proper name
  - Select `public` repo type
  - Check check-boxes for two files `README.md` and license
  - Select license: MIT
- Take example from `introduction-to-it/lecture_notes/07 basics/0-buggy.*`
  - Clone two repositories from github to your laptop: `introduction-to-it` and your new one
    - `git clone https://github.com/kse-ua/introduction-to-it.git`
    - `git clone https://github.com/YOUR-NAME/SUPER-DUPER-REPO.git`
  - Copy 3 files `0-buggy.*` from `introduction-to-it` to your repo
  - Hold this files untouched, make copies `1-fixed.*`
- Fix bugs for your language (select one or more: C++, JavaScript, Python) (max +3)
  - Change files `1-fixed.*` to fix bugs
  - Compile c++ example: `c++ 1-fixed.cpp`
  - Execute c++ example: `./a.out`
  - Run JavaScript example: `node 1-fixed.js`
  - Run Python example: `python 1-fixed.py`
- Provide step-by-step code improvements: `1-fixed-somethin.*`, `2-improved.*`, etc. (max +10)
  - Just fixed bugs `1-fixed.*`
  - Implement function `add(x, y)` and save new versions into files `2-improved.*`
  - Optional: prepare more improvements in files `3-something.*`, `4-name.*`, etc.
- Make branch, commit and PR (pull request)
  - Create new branch `git checkout -b new-branch`
  - Add changes to commit `git add file-name`
  - You can see status at all steps: `git status`
  - Create commit: `git commit`
  - Push branch to github: `git push`
  - Open github browser UI and create PR (pull request)
- Review code for your colleague and ask to review your (max +5)
- Land PR to main (master) branch
  - Use green button "Rebase and merge"
  - Delete branch after landing
- Create another branch `loop`
  - `git checkout -b loop`
- Create function `sum(...args)` returning sum of arguments (max +10)
  - Create alternative implementation of `sum`
  - Using `for..of` (for JavaScript) and `for..in` (for Python)
  - Using c-style `for` loop like in `2-for-loop.*`
  - Implement it in 2 languages and create 2 commits
  - Implement it in C++ (optional)
  - Create PR, review and land, like we did before
