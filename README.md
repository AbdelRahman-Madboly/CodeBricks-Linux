# CodeBricks · Linux CLI

A hands-on Linux command line reference and practice repo built for AI/ML engineering work.
Every command is documented, every concept is grounded in a real use case.

**GitHub:** [AbdelRahman-Madboly/CodeBricks-Linux](https://github.com/AbdelRahman-Madboly/CodeBricks-Linux)
**Environment:** WSL 2 + Ubuntu on Windows · VS Code with WSL extension

---

## Why This Repo

Before you can build RAG pipelines, run LLM inference, manage GPU servers,
or automate data workflows — you need to be fluent in the terminal.
This repo documents that fluency: one chapter at a time, with every command
explained in the context of real AI engineering work.

---

## Roadmap

```
CH1 ──► CH2 ──► CH3 ──► CH4 ──► CH5 ──► CH6 ──► CH7+ (Advanced)
Shells  Files   Perms   Progs   I/O     Pkgs    Scripting · SSH · Envs
```

---

## Chapters

### Boot.dev Course (6 chapters)

| # | Chapter | Key Commands | Status |
|---|---------|-------------|--------|
| 01 | [Terminals & Shells](./01_terminals_shells/) | `echo`, `export`, `history`, `!!`, `ctrl+r` | 🔲 |
| 02 | [Filesystems](./02_filesystems/) | `pwd`, `ls`, `cd`, `cat`, `grep`, `mv`, `cp`, `rm` | 🔲 |
| 03 | [Permissions](./03_permissions/) | `chmod`, `chown`, `sudo`, `whoami`, `ls -l` | 🔲 |
| 04 | [Programs](./04_programs/) | `which`, `export PATH`, `source`, shebang, `.bashrc` | 🔲 |
| 05 | [Input/Output](./05_input_output/) | `>`, `>>`, `\|`, `2>`, `kill`, `ps`, `top`, `man` | 🔲 |
| 06 | [Packages](./06_packages/) | `apt`, `nvim`, `lsd`, VS Code WSL | 🔲 |

### Advanced Topics (beyond Boot.dev)

| # | Chapter | Key Skills | Status |
|---|---------|-----------|--------|
| 07 | [Bash Scripting](./07_bash_scripting/) | loops, functions, args, error handling | 🔲 |
| 08 | [SSH & Remote Servers](./08_ssh_remote/) | SSH keys, tmux, rsync, port forwarding | 🔲 |
| 09 | [Environment Management](./09_environment_management/) | conda, .env, direnv, venv | 🔲 |

---

## Folder Structure (per chapter)

```
<N>_<chapter>/
├── README.md       — concept, mental model, AI engineer angle
├── notes.md        — personal learning journal
├── commands.md     — quick reference card for this chapter
├── practice.sh     — runnable: all key commands with comments
└── exercises/
    ├── 01_<name>.sh — easy, guided
    ├── 02_<name>.sh — medium, combined
    └── 03_<name>.sh — hard, real AI engineer scenario
```

---

## How to Use This Repo

1. Read the chapter `README.md` — understand the concept before touching the terminal
2. Open `practice.sh` — read it, predict each output, then run it: `bash practice.sh`
3. Attempt each `exercises/` file — write your solution first
4. Check `commands.md` — add anything you didn't know to your personal notes
5. Fill in `notes.md` — in your own words, with your own examples
6. Update `CHEATSHEET.md` — add commands you'll use constantly

---

## Quick Setup

```bash
# Clone the repo (WSL terminal)
git clone https://github.com/AbdelRahman-Madboly/CodeBricks-Linux.git
cd CodeBricks-Linux

# Run any practice file
bash 01_terminals_shells/practice.sh

# Run any exercise
bash 02_filesystems/exercises/01_navigate.sh
```

---

## Connection to AI Engineering

Every chapter connects to real work:

```bash
# CH2 — navigate model checkpoints
ls -lh checkpoints/ | sort -k5 -rh | head -5

# CH3 — secure your API key file
chmod 600 ~/.env && echo "Key file secured"

# CH4 — confirm which Python your project uses
which python3 && python3 --version

# CH5 — save training logs while watching them live
python train.py 2>&1 | tee logs/run_$(date +%Y%m%d_%H%M).log

# CH5 — kill a runaway training job
ps aux | grep train.py | grep -v grep | awk '{print $2}' | xargs kill -9

# CH7 — run a full pipeline from one script
bash scripts/run_experiment.sh --model bert-base --epochs 5 --lr 2e-5
```

---

## Resources

- [The Linux Command Line](https://linuxcommand.org/tlcl.php) — free book, excellent reference
- [Boot.dev Linux Course](https://boot.dev) — the course this repo is built around
- [tldr pages](https://tldr.sh/) — simplified man pages
- [explainshell.com](https://explainshell.com/) — paste any command and get it explained

---

## Progress

Track your progress in [`PROGRESS.md`](./PROGRESS.md).
Quick command reference in [`CHEATSHEET.md`](./CHEATSHEET.md).
Generate chapter folders using [`SKILL_LINUX.md`](./SKILL_LINUX.md).