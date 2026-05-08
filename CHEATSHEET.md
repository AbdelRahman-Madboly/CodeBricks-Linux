# Linux CLI Cheatsheet — CodeBricks

> Master reference. Updated after each chapter.
> Use this as your first stop before opening a man page.

---

## Terminals and Shells (CH1)

| Command | What it does |
|---------|-------------|
| `echo $VAR` | print the value of a variable |
| `MY_VAR="value"` | create a shell variable (no spaces around =) |
| `export VAR="value"` | create and export in one step (visible to child processes) |
| `env` | list all exported environment variables |
| `unset VAR` | remove a variable |
| `history` | show command history |
| `!!` | repeat the last command (e.g. `sudo !!`) |
| `!$` | last argument of the last command |
| `source ~/.bashrc` | reload bash config without restarting shell |

---

## Navigation (CH2)

| Command | What it does |
|---------|-------------|
| `pwd` | print current directory |
| `ls -lah` | list all files, long format, human-readable sizes |
| `ls -R` | list recursively |
| `cd ~` | go to home directory |
| `cd -` | go to previous directory |

*(add more as you complete each chapter)*

---

## File Operations (CH2)

| Command | What it does |
|---------|-------------|
| `cat file` | print entire file |
| `head -n 20 file` | first 20 lines |
| `tail -n 20 file` | last 20 lines |
| `tail -f file` | follow a live file (training logs) |
| `grep -rni "pattern" .` | search recursively, case-insensitive, with line numbers |
| `mv src dst` | move or rename |
| `cp -r src dst` | copy directory recursively |
| `rm -rf dir` | delete directory (no undo) |
| `mkdir -p a/b/c` | create nested directories |

---

## Permissions (CH3)

| Command | What it does |
|---------|-------------|
| `ls -l` | show permissions |
| `chmod +x script.sh` | make executable |
| `chmod 600 .env` | owner read/write only (secure secrets) |
| `chmod 755 dir/` | standard directory permissions |
| `chown -R $USER dir/` | reclaim ownership (e.g. after Docker) |
| `sudo command` | run as root |
| `whoami` | current user |

---

## Programs and PATH (CH4)

| Command | What it does |
|---------|-------------|
| `which python3` | find where a command lives |
| `echo $PATH` | show current PATH |
| `export PATH="$PATH:/new/dir"` | add to PATH for this session |
| `source ~/.bashrc` | reload shell config |

---

## Input/Output (CH5)

| Pattern | What it does |
|---------|-------------|
| `cmd > file` | redirect stdout to file (overwrite) |
| `cmd >> file` | append stdout to file |
| `cmd 2> err.log` | redirect stderr |
| `cmd 2>&1` | merge stderr into stdout |
| `cmd 2>/dev/null` | silence errors |
| `cmd1 \| cmd2` | pipe stdout of cmd1 to stdin of cmd2 |
| `python train.py 2>&1 \| tee run.log` | log and display simultaneously |
| `echo $?` | check last exit code |
| `ps aux \| grep python` | find running Python processes |
| `kill -9 PID` | force kill a process |

---

## Packages (CH6)

| Command | What it does |
|---------|-------------|
| `sudo apt update` | refresh package list |
| `sudo apt install pkg` | install a package |
| `apt list --installed \| grep pkg` | check if installed |
| `which tool` | confirm install location |

---

## AI Engineering Quick Reference

```bash
# Pass an API key to a script without hardcoding it
export OPENAI_API_KEY="sk-..."
python infer.py

# Watch a live training log
tail -f ~/hivemind/logs/training/run-012.log

# Find all API errors in a log file
grep "ERROR\|500\|503" ~/hivemind/logs/api/2024-03-01.log | wc -l

# Kill a runaway training job
ps aux | grep train.py | grep -v grep | awk '{print $2}' | xargs kill -9

# Save logs while watching them live
python train.py 2>&1 | tee logs/run_$(date +%Y%m%d_%H%M).log

# Check which Python your project uses
which python3 && python3 --version

# Secure your API key file
chmod 600 ~/.env

# Sync project to remote GPU server
rsync -avz --exclude '.git' . user@gpu-server:~/project/
```