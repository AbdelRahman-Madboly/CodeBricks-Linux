# Commands — CH1: Terminals and Shells

| Command | What it does | Example |
|---------|-------------|---------|
| `echo $VAR` | print the value of a variable | `echo $HOME` |
| `MY_VAR="value"` | create a shell variable (no spaces around =) | `NAME="HiveMind"` |
| `export VAR` | make a variable visible to child processes | `export API_KEY="sk-..."` |
| `export VAR="value"` | create and export in one step | `export ENV="prod"` |
| `env` | list all exported environment variables | `env \| grep PATH` |
| `printenv VAR` | print a specific env variable | `printenv HOME` |
| `unset VAR` | remove a variable | `unset MY_VAR` |
| `history` | show command history | `history \| tail -20` |
| `!!` | repeat the last command | `sudo !!` |
| `!$` | last argument of the last command | `cat !$` |
| `ctrl+r` | reverse search through history | type after pressing |
| `source ~/.bashrc` | reload bash config without restarting | after editing .bashrc |
| `bash -c 'cmd'` | run a command in a new bash subprocess | `bash -c 'echo $VAR'` |

## Patterns

```bash
# Pass a secret to a script without hardcoding it
export OPENAI_API_KEY="sk-..."
python train.py

# Check if a variable was exported (from inside a script)
if [ -z "$API_KEY" ]; then
    echo "ERROR: API_KEY is not set"
    exit 1
fi

# See what env variables a new process inherits
export MY_VAR="test"
bash -c 'echo $MY_VAR'   # prints: test

# Without export, child process can't see it
MY_VAR="test"
bash -c 'echo $MY_VAR'   # prints: (empty)
```
