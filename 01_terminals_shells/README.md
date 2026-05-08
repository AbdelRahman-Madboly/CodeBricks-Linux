# CH1: Terminals and Shells

## What This Is

When you open a terminal window, you're running two separate things: a **terminal emulator** and a **shell**. The terminal emulator is just a window that draws text on screen. The shell is the program that reads what you type, interprets it as commands, and runs them. On Ubuntu and WSL, that shell is called **bash**.

Understanding this distinction matters because when something goes wrong, you need to know whether it's a display problem or an execution problem. Usually it's the shell.

## Mental Model

Think of the terminal as a phone screen and bash as the operating system running on it. The screen renders what the OS tells it. You interact with the OS — the screen just shows you the result. When you change your shell settings, you're configuring bash, not the terminal.

## Key Concepts

**Shell variables** are like sticky notes that bash holds for the current session. You create one with `MY_VAR="hello"` — no spaces around the `=`. Read it back with `echo $MY_VAR`. The variable disappears when you close the terminal.

**export** promotes a variable so that any program you launch from this shell can also read it. Without export, only bash itself can see the variable. With it, Python scripts, other shell scripts, and tools like `curl` can all access it via `os.environ` or `$MY_VAR`. This is how you pass API keys to programs without hardcoding them.

**Command history** is stored in `~/.bash_history`. Press the up arrow to cycle through previous commands. Press `ctrl+r` and start typing to search backwards through history — this is much faster than pressing up 40 times. `!!` replays the last command exactly (useful for `sudo !!` when you forget sudo). `!$` pastes the last argument of the last command.

**WSL 2** is a full Linux kernel running inside Windows. Your Windows C: drive appears at `/mnt/c/`. Your WSL home directory (`~`) is a separate Linux filesystem at something like `C:\Users\you\AppData\Local\Packages\...\LocalState\rootfs\home\you`. Keep your code in the Linux filesystem — not in `/mnt/c/` — for better performance.

## AI Engineering Connection

Environment variables are the standard way to pass secrets to programs. Before running a training script that calls an API, you do:

```bash
export OPENAI_API_KEY="sk-..."
python train.py
```

The script reads it with `os.environ["OPENAI_API_KEY"]`. The key never appears in your code or git history.

HiveMind's `warning.sh` script uses this pattern — it checks for a required env variable and warns you if it's missing. Open it to see:

```bash
cat ~/hivemind/public/pipelines/warning.sh
```

The `onboard.sh` script reads from stdin — it's how automated setup scripts ask you questions interactively:

```bash
bash ~/hivemind/public/pipelines/onboard.sh
```

## Try It

```bash
# Create a variable
MY_NAME="HiveMind"
echo "Hello from $MY_NAME"
# Expected: Hello from HiveMind

# Export it so child processes can see it
export API_ENV="production"
bash -c 'echo "Environment: $API_ENV"'
# Expected: Environment: production

# Search your history for a command you ran before
ctrl+r
# Type part of the command — bash finds the most recent match
```

## What's Next

Chapter 2 covers the filesystem — how to navigate directories, read files, and search through logs with `grep`. You'll use these skills constantly when working with model checkpoints and training logs.