# HiveMind AI — Practice Environment

HiveMind AI is a fictional AI startup building RAG pipelines, LLM APIs, and ML automation tools.
Their server is your practice environment. You have been given access to investigate, automate, and fix things.

This directory lives in the repo at `hivemind/` but exercises expect it at `~/hivemind/`.
Run `cp -r hivemind/ ~/hivemind/` once after cloning.

---

## File Map

```
hivemind/
│
├── logs/                               ← CH5: grep, tail, pipe, redirect practice
│   ├── api/
│   │   ├── 2024-03-01.log              — 2000 API request lines (200/429/500/503)
│   │   ├── 2024-03-02.log
│   │   └── 2024-03-03.log
│   ├── system/
│   │   ├── 2024-03-01.log              — OOM kills, SSH attempts, cron jobs
│   │   └── 2024-03-02.log
│   └── training/
│       ├── run-010.log                 — mistral-7b, 5 epochs
│       ├── run-012.log                 — llama-2-13b, 5 epochs (best run)
│       └── run-014.log                 — codellama-7b, 5 epochs
│
├── private/                            ← CH3: permissions — who can read this?
│   ├── api_keys/
│   │   └── keys.txt                    — fake API keys — chmod 600 exercise
│   ├── cmd/
│   │   ├── genlogs/main.py             — regenerates all log files
│   │   └── genmetrics/main.py          — regenerates all dataset files
│   ├── customers/
│   │   └── records.csv                 — 15 customer rows (name/email/plan/usage)
│   ├── experiments/
│   │   ├── results/summary.csv         — 15 training runs (loss/accuracy/f1/status)
│   │   └── runs/                       — (empty — populated during exercises)
│   ├── infra/
│   │   ├── nginx.conf                  — reverse proxy config (nvim editing)
│   │   └── servers.txt                 — 8 GPU servers (grep/search practice)
│   ├── models/
│   │   ├── checkpoints/
│   │   │   ├── run-010_best.meta       — checkpoint metadata
│   │   │   └── run-012_best.meta
│   │   └── registry/
│   │       └── models.csv              — 8 models (name/version/status/size)
│   └── key.txt                         — fake RSA key — chmod 600 exercise
│
├── public/                             ← readable by anyone
│   ├── datasets/
│   │   ├── processed/
│   │   │   └── embedding_benchmark.csv — 6 embedding models benchmarked
│   │   └── raw/
│   │       ├── api_usage.csv           — 500 API usage rows
│   │       └── rag_eval.csv            — 200 RAG evaluation rows
│   ├── docs/
│   │   ├── company_info.md             — CH6: nvim editing exercise
│   │   ├── incident_report.md          — grep practice (find the root cause)
│   │   └── pr_ideas.txt
│   ├── models/
│   │   └── README.md                   — public model cards
│   └── pipelines/
│       ├── config.yaml                 — inference config (nvim editing)
│       ├── onboard.sh                  — CH1: reads from stdin
│       └── warning.sh                  — CH1/CH4: uses an env variable
│
└── scripts/                            ← CH7: bash scripting exercises
    ├── backup.sh                       — has 2 bugs — find and fix them
    └── check_gpu.sh                    — GPU monitoring simulation
```

---

## Chapter Map

| Chapter | Files you work with |
|---------|-------------------|
| CH1 Terminals & Shells | `public/pipelines/onboard.sh`, `public/pipelines/warning.sh` |
| CH2 Filesystems | `logs/`, `private/infra/servers.txt`, `public/docs/` |
| CH3 Permissions | `private/api_keys/keys.txt`, `private/key.txt`, `scripts/` |
| CH4 Programs | `public/pipelines/warning.sh`, `scripts/` |
| CH5 Input/Output | `logs/api/`, `logs/training/`, `logs/system/` |
| CH6 Packages | `public/docs/company_info.md`, `private/infra/nginx.conf` |
| CH7 Bash Scripting | `scripts/backup.sh` (fix the bugs), new scripts against all files |
| CH8 SSH & Remote | `private/infra/servers.txt`, rsync the project |
| CH9 Environments | `private/cmd/` (conda env to run generators), `.env` pattern |

---

## Regenerating Content Files

Log and dataset files are generated, not hand-written. Regenerate anytime:

```bash
cd ~/hivemind
python3 private/cmd/genlogs/main.py
python3 private/cmd/genmetrics/main.py
```

Both scripts use only Python stdlib — no dependencies needed.

---

## Common Exercise Commands

```bash
# Watch a training run live
tail -f ~/hivemind/logs/training/run-012.log

# Find all API errors from a day
grep "ERROR\|500\|503" ~/hivemind/logs/api/2024-03-01.log | wc -l

# Find the best experiment by val_loss
sort -t',' -k7 -n ~/hivemind/private/experiments/results/summary.csv | head -3

# Secure the API key file
chmod 600 ~/hivemind/private/api_keys/keys.txt

# List checkpoints by size
ls -lh ~/hivemind/private/models/checkpoints/

# Sync to a remote server (CH8)
rsync -avz ~/hivemind/private/models/ user@spinoza:~/hivemind/private/models/
```