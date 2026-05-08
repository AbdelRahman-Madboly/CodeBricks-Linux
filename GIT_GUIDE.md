# Git Guide — CodeBricks Linux

## Daily Workflow (after completing a chapter)

```bash
git add 01_terminals_shells/
git commit -m "feat(linux): add 01_terminals_shells chapter

- README: terminal vs shell, variables, export, history
- practice.sh: echo, export, env, bash -c, guard pattern
- exercises: variables/export, history/ctrl+r, env script
- commands.md: 13 commands documented
- notes.md: questions pre-filled, ready to answer"

git push origin main
```

---

## Commit Message Format

```
feat(linux): add <folder_name> chapter

- README: <key concepts covered>
- practice.sh: <commands demonstrated>
- exercises: <exercise 1 topic>, <exercise 2 topic>, <exercise 3 topic>
- commands.md: <N> commands documented
- notes.md: <what questions are pre-filled>
```

Use `chore` instead of `feat` for updates to root files:

```
chore(linux): update CHEATSHEET and PROGRESS after CH1
```

---

## Update These After Every Chapter

1. `CHEATSHEET.md` — add the chapter's commands to the master table
2. `PROGRESS.md` — mark the chapter done: `- [ ]` → `- [x]`
3. Root `README.md` — update status column: 🔲 → ✅

---

## Checking Your Work

```bash
git log --oneline          # see all commits
git diff HEAD~1            # see what changed in last commit
git status                 # see what is staged vs unstaged
```

---

## Repo Structure Check

Your repo should look like this at root level — nothing extra:

```
CodeBricks-Linux/
├── 01_terminals_shells/
├── 02_filesystems/
├── ...
├── 09_environment_management/
├── hivemind/
├── .gitignore
├── CHEATSHEET.md
├── GIT_GUIDE.md
├── LICENSE
├── PROGRESS.md
├── PROMPTS_LINUX.md
├── README.md
└── SKILL_LINUX.md
```

If you see stray files like `Microsoft` or `git` (no extension) at root,
delete them — they were created by accidentally running commands in the
wrong directory on Windows.