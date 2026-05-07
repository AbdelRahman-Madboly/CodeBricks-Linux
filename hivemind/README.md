# HiveMind AI

A repository for the HiveMind AI project — a filesystem for the CodeBricks Linux CLI course.

HiveMind AI is a fictional AI startup building RAG pipelines, LLM APIs, and ML automation tools.
Their server is your practice environment. You have been given access to investigate, automate, and fix things.

## Directory Structure

```
hivemind/
├── private/
│   ├── api_keys/        ← secrets (chmod 600 practice)
│   ├── customers/       ← user data (permissions practice)
│   ├── experiments/     ← training run results
│   ├── infra/           ← server configs
│   └── models/          ← model checkpoints and registry
├── public/
│   ├── datasets/        ← CSV data for grep/awk/sort exercises
│   ├── docs/            ← company documentation
│   └── pipelines/       ← pipeline scripts (shebang practice)
├── logs/
│   ├── api/             ← API request logs
│   ├── system/          ← system/kernel logs
│   └── training/        ← model training logs
├── scripts/             ← generator scripts (run these first)
├── config.yaml          ← server + model config
├── models.csv           ← model registry
├── nginx.conf           ← reverse proxy config
└── servers.txt          ← GPU server inventory
```

## Setup

Generate all log and dataset files before starting the exercises:

```bash
python scripts/generate_logs.py
python scripts/generate_datasets.py
```

Good luck.
