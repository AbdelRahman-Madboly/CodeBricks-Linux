#!/usr/bin/env python3
"""
Generates realistic log files for the HiveMind AI practice environment.
Run this script to populate logs/ with content for grep/tail/pipe exercises.
"""

import random
import os
from datetime import datetime, timedelta

random.seed(42)

# ── Training log generator ────────────────────────────────────────────────────

def generate_training_log(run_id, model, epochs, start_dt, output_path):
    lines = []
    dt = start_dt
    lines.append(f"{dt.strftime('%Y-%m-%d %H:%M:%S')} INFO  [{run_id}] Starting training run")
    lines.append(f"{dt.strftime('%Y-%m-%d %H:%M:%S')} INFO  [{run_id}] Model: {model}")
    lines.append(f"{dt.strftime('%Y-%m-%d %H:%M:%S')} INFO  [{run_id}] Loading dataset...")
    dt += timedelta(seconds=random.randint(30, 120))
    lines.append(f"{dt.strftime('%Y-%m-%d %H:%M:%S')} INFO  [{run_id}] Dataset loaded: 48203 samples")
    dt += timedelta(seconds=10)
    lines.append(f"{dt.strftime('%Y-%m-%d %H:%M:%S')} INFO  [{run_id}] GPU: NVIDIA A100 80GB | VRAM: 79.2GB available")

    train_loss = 0.9 + random.uniform(-0.1, 0.1)
    val_loss   = train_loss + 0.08

    for epoch in range(1, epochs + 1):
        lines.append(f"{dt.strftime('%Y-%m-%d %H:%M:%S')} INFO  [{run_id}] ── Epoch {epoch}/{epochs} ──────────────")
        steps_per_epoch = 400
        for step in range(0, steps_per_epoch + 1, 50):
            dt += timedelta(seconds=random.randint(20, 45))
            step_loss = train_loss - (epoch - 1) * 0.08 - step * 0.0002 + random.uniform(-0.02, 0.02)
            lr = 1e-5 * (0.95 ** (epoch - 1))
            if random.random() < 0.03:
                lines.append(f"{dt.strftime('%Y-%m-%d %H:%M:%S')} WARNING [{run_id}] Gradient norm spike: 12.41 (clipping)")
            lines.append(f"{dt.strftime('%Y-%m-%d %H:%M:%S')} INFO  [{run_id}] step={step:4d}/{steps_per_epoch} loss={step_loss:.4f} lr={lr:.2e}")
        val_loss_e = val_loss - (epoch - 1) * 0.06 + random.uniform(-0.01, 0.02)
        acc = 0.78 + epoch * 0.04 + random.uniform(-0.01, 0.01)
        f1  = acc - 0.01 + random.uniform(-0.005, 0.005)
        dt += timedelta(minutes=random.randint(2, 5))
        lines.append(f"{dt.strftime('%Y-%m-%d %H:%M:%S')} INFO  [{run_id}] Epoch {epoch} complete | val_loss={val_loss_e:.4f} accuracy={acc:.4f} f1={f1:.4f}")
        lines.append(f"{dt.strftime('%Y-%m-%d %H:%M:%S')} INFO  [{run_id}] Checkpoint saved: checkpoints/{run_id}_epoch{epoch}.pt")
        if epoch == epochs:
            lines.append(f"{dt.strftime('%Y-%m-%d %H:%M:%S')} INFO  [{run_id}] Best model saved: checkpoints/{run_id}_best.pt")

    lines.append(f"{dt.strftime('%Y-%m-%d %H:%M:%S')} INFO  [{run_id}] Training complete")
    lines.append(f"{dt.strftime('%Y-%m-%d %H:%M:%S')} INFO  [{run_id}] Total time: {(dt - start_dt).seconds // 3600}h {((dt - start_dt).seconds % 3600) // 60}m")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"  generated: {output_path} ({len(lines)} lines)")


# ── API log generator ─────────────────────────────────────────────────────────

def generate_api_log(date_str, output_path):
    endpoints = ["/v1/chat/completions", "/v1/embeddings", "/v1/models", "/health"]
    clients   = ["alice@techcorp.io", "bruno@datascience.co", "hiroshi@robotics.jp",
                 "eva@nlplab.dk", "faisal@llmconsult.ae", "grace@deeplearn.ng"]
    statuses  = [200]*18 + [200]*5 + [429, 429, 503, 500, 400]
    methods   = ["POST", "POST", "GET", "GET"]

    lines = []
    dt = datetime.strptime(date_str, "%Y-%m-%d")

    for _ in range(2000):
        dt += timedelta(seconds=random.randint(1, 60))
        status  = random.choice(statuses)
        client  = random.choice(clients)
        ep      = random.choice(endpoints)
        method  = "GET" if ep in ["/v1/models", "/health"] else "POST"
        latency = random.randint(40, 3200) if status == 200 else random.randint(1, 100)
        tokens  = random.randint(50, 4000) if ep == "/v1/chat/completions" else random.randint(10, 512)

        if status == 503:
            lines.append(f'{dt.strftime("%Y-%m-%d %H:%M:%S")} ERROR  {method} {ep} {status} {latency}ms client={client} ERROR: worker unavailable')
        elif status == 429:
            lines.append(f'{dt.strftime("%Y-%m-%d %H:%M:%S")} WARNING {method} {ep} {status} {latency}ms client={client} rate_limited')
        elif status == 500:
            lines.append(f'{dt.strftime("%Y-%m-%d %H:%M:%S")} ERROR  {method} {ep} {status} {latency}ms client={client} ERROR: internal server error')
        elif status == 400:
            lines.append(f'{dt.strftime("%Y-%m-%d %H:%M:%S")} WARNING {method} {ep} {status} {latency}ms client={client} bad_request: max_tokens exceeded')
        else:
            lines.append(f'{dt.strftime("%Y-%m-%d %H:%M:%S")} INFO   {method} {ep} {status} {latency}ms client={client} tokens={tokens}')

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"  generated: {output_path} ({len(lines)} lines)")


# ── System log generator ──────────────────────────────────────────────────────

def generate_system_log(date_str, output_path):
    messages = [
        ("INFO",    "systemd: hivemind-worker.service started"),
        ("INFO",    "systemd: hivemind-worker.service: active (running)"),
        ("INFO",    "kernel: NVIDIA A100 driver loaded"),
        ("INFO",    "cron: backup job started"),
        ("INFO",    "cron: backup job complete — 42GB archived"),
        ("WARNING", "kernel: GPU memory at 87% on nietzsche"),
        ("WARNING", "kernel: GPU memory at 92% on nietzsche"),
        ("ERROR",   "kernel: OOM killer invoked — killed hivemind-worker (pid 18423)"),
        ("INFO",    "systemd: hivemind-worker.service: restarting"),
        ("INFO",    "kernel: GPU memory normalized — 41% on nietzsche"),
        ("INFO",    "sshd: Accepted publickey for hivemind from 10.0.1.42"),
        ("INFO",    "sshd: Accepted publickey for tomas from 10.0.1.10"),
        ("WARNING", "sshd: Failed password attempt for root from 185.220.101.47"),
        ("WARNING", "sshd: Failed password attempt for root from 185.220.101.47"),
        ("ERROR",   "sshd: Too many authentication failures from 185.220.101.47 — blocked"),
        ("INFO",    "nginx: config reloaded"),
        ("INFO",    "cron: log rotation complete"),
    ]

    lines = []
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    for _ in range(500):
        dt += timedelta(seconds=random.randint(10, 300))
        level, msg = random.choice(messages)
        lines.append(f"{dt.strftime('%Y-%m-%d %H:%M:%S')} {level:7s} {msg}")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"  generated: {output_path} ({len(lines)} lines)")


# ── Main ──────────────────────────────────────────────────────────────────────

BASE = os.path.join(os.path.dirname(__file__), "../../..")

if __name__ == "__main__":
    print("\nGenerating HiveMind AI log files...\n")

    # Training logs
    runs = [
        ("run-010", "mistral-7b",   5, "2024-02-01"),
        ("run-012", "llama-2-13b",  5, "2024-02-15"),
        ("run-014", "codellama-7b", 5, "2024-03-01"),
    ]
    for run_id, model, epochs, date in runs:
        generate_training_log(
            run_id, model, epochs,
            datetime.strptime(date, "%Y-%m-%d"),
            os.path.join(BASE, f"logs/training/{run_id}.log")
        )

    # API logs
    for date in ["2024-03-01", "2024-03-02", "2024-03-03"]:
        generate_api_log(date, os.path.join(BASE, f"logs/api/{date}.log"))

    # System logs
    for date in ["2024-03-01", "2024-03-02"]:
        generate_system_log(date, os.path.join(BASE, f"logs/system/{date}.log"))

    print("\nDone. Log files are in hivemind/logs/")
