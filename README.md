# CodeBricks · Linux CLI

A hands-on Linux command line repo built for AI/ML engineering work.
Every command is documented, every exercise runs against a real practice environment.

**GitHub:** [AbdelRahman-Madboly/CodeBricks-Linux](https://github.com/AbdelRahman-Madboly/CodeBricks-Linux)
**Environment:** WSL 2 + Ubuntu on Windows · VS Code with WSL extension

---

## The Practice Environment

All exercises run against `hivemind/` — a fictional AI startup's server.
HiveMind AI builds RAG pipelines and LLM APIs. You have been given access.

```
hivemind/
├── logs/      ← training runs, API requests, system events
├── private/   ← model checkpoints, API keys, customer records, infra configs
├── public/    ← datasets, model cards, pipeline scripts, docs
└── scripts/   ← automation scripts (some have bugs)
```

Every `grep`, `chmod`, `pipe`, and bash script runs on real-looking data.
See [`hivemind/README.md`](./hivemind/README.md) for the full file map.

---

## Roadmap

```
CH1 ──► CH2 ──► CH3 ──► CH4 ──► CH5 ──► CH6 ──► CH7 ──► CH8 ──► CH9
Shells  Files   Perms   Progs   I/O     Pkgs    Bash    SSH     Envs
```

---

## Chapters

### Boot.dev Course (6 chapters)

| # | Chapter | Key Skills | Status |
|---|---------|-----------|--------|
| 01 | [Terminals & Shells](./01_terminals_shells/) | variables, export, history, `!!`, ctrl+r | 🔲 |
| 02 | [Filesystems](./02_filesystems/) | `ls`, `cd`, `grep`, `mv`, `cp`, `rm` | 🔲 |
| 03 | [Permissions](./03_permissions/) | `chmod`, `chown`, `sudo`, `ls -l` | 🔲 |
| 04 | [Programs](./04_programs/) | shebang, PATH, `.bashrc`, `which` | 🔲 |
| 05 | [Input/Output](./05_input_output/) | pipes, redirect, `kill`, `ps`, exit codes | 🔲 |
| 06 | [Packages](./06_packages/) | `apt`, `nvim`, `lsd`, VS Code WSL | 🔲 |

### Advanced Topics

| # | Chapter | Key Skills | Status |
|---|---------|-----------|--------|
| 07 | [Bash Scripting](./07_bash_scripting/) | functions, loops, args, `set -e` | 🔲 |
| 08 | [SSH & Remote](./08_ssh_remote/) | SSH keys, `rsync`, `tmux`, port forward | 🔲 |
| 09 | [Environments](./09_environment_management/) | conda, `.env`, `python-dotenv`, venv | 🔲 |

---

## Folder Structure (per chapter)

```
<N>_<chapter>/
├── README.md       — concept, mental model, AI engineer angle
├── notes.md        — personal learning journal (questions pre-filled)
├── commands.md     — quick reference card for this chapter
├── practice.sh     — runnable: all key commands with comments
└── exercises/
    ├── 01_<name>.sh — easy, single concept, guided
    ├── 02_<name>.sh — medium, 2–3 commands combined
    └── 03_<name>.sh — hard, real AI engineer scenario using ~/hivemind/
```

---

## Quick Setup

```bash
# Clone the repo (WSL terminal)
git clone https://github.com/AbdelRahman-Madboly/CodeBricks-Linux.git ~/CodeBricks-Linux
cd ~/CodeBricks-Linux

# Copy hivemind to your home directory (exercises expect ~/hivemind/)
cp -r hivemind/ ~/hivemind/

# Generate log and dataset files
cd ~/hivemind
python3 private/cmd/genlogs/main.py
python3 private/cmd/genmetrics/main.py

# Run any practice file
bash 01_terminals_shells/practice.sh

# Run any exercise
bash 01_terminals_shells/exercises/01_variables.sh
```

---

## Connection to AI Engineering

```bash
# CH2 — search training logs for loss values
grep "val_loss" ~/hivemind/logs/training/run-012.log | tail -5

# CH3 — secure your API key file before deploying
chmod 600 ~/hivemind/private/api_keys/keys.txt

# CH4 — confirm which Python your project uses
which python3 && python3 --version

# CH5 — save training output while watching it live
python train.py 2>&1 | tee ~/hivemind/logs/training/run-015.log

# CH5 — kill a runaway training job
ps aux | grep "train.py" | grep -v grep | awk '{print $2}' | xargs kill -9

# CH7 — run a full pipeline from one script
bash scripts/run_experiment.sh --model llama-2-13b --epochs 5 --lr 2e-5

# CH8 — sync checkpoints to a remote GPU server
rsync -avz ~/hivemind/private/models/ user@spinoza:~/hivemind/private/models/
```

---

## Resources

- [The Linux Command Line](https://linuxcommand.org/tlcl.php) — free book
- [Boot.dev Linux Course](https://boot.dev) — chapters 1–6 source
- [tldr pages](https://tldr.sh/) — simplified man pages
- [explainshell.com](https://explainshell.com/) — paste any command, get it explained

---

Track progress in [`PROGRESS.md`](./PROGRESS.md).
Quick reference in [`CHEATSHEET.md`](./CHEATSHEET.md).
HiveMind environment map in [`hivemind/README.md`](./hivemind/README.md).
Generate chapters with [`SKILL_LINUX.md`](./SKILL_LINUX.md) + [`PROMPTS_LINUX.md`](./PROMPTS_LINUX.md).