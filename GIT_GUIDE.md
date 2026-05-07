# Git Guide — CodeBricks Linux

## Daily workflow

```bash
# After completing a chapter
git add 01_terminals_shells/
git commit -m "feat(linux): add 01_terminals_shells chapter

- README: shell vs terminal, variables, history
- practice.sh: echo, export, history, !!
- exercises: variables, history search, env script
- commands.md: 8 commands documented
- notes.md: answered — shell vs terminal, export, WSL"

git push origin main
```

## Commit message format

```
feat(linux): add <folder_name> chapter

- README: <key concepts>
- practice.sh: <commands covered>
- exercises: <scenario 1>, <scenario 2>, <scenario 3>
- commands.md: <N> commands documented
- notes.md: answered — <questions>
```

## Update CHEATSHEET.md and PROGRESS.md after every chapter.

## Checking your work

```bash
git log --oneline          # see all commits
git diff HEAD~1            # see what changed in last commit
git status                 # see what's staged vs unstaged
```
