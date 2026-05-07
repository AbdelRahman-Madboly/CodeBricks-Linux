#!/usr/bin/env python3
"""
Generates synthetic dataset files for the HiveMind AI practice environment.
Run this to populate public/datasets/ with content for grep/awk/sort exercises.
"""

import random
import csv
import os

random.seed(99)

BASE = os.path.join(os.path.dirname(__file__), "../../..")

# ── RAG QA pairs dataset ──────────────────────────────────────────────────────

def generate_qa_dataset(output_path, n=200):
    questions = [
        "What is retrieval-augmented generation?",
        "How does chunking affect RAG performance?",
        "What embedding model should I use for code search?",
        "Explain the difference between BM25 and dense retrieval.",
        "How do I reduce hallucinations in an LLM pipeline?",
        "What is a vector store and how does it work?",
        "How does re-ranking improve RAG results?",
        "What is the optimal chunk size for technical documents?",
        "How do I evaluate a RAG pipeline?",
        "What is hybrid search in the context of RAG?",
        "How does temperature affect LLM output quality?",
        "What is the difference between fine-tuning and RAG?",
        "How do I handle long documents in a RAG system?",
        "What metrics should I use to evaluate retrieval quality?",
        "How do I prevent prompt injection in an LLM API?",
    ]
    sources = ["docs/rag-guide.md", "docs/llm-ops.md", "docs/embeddings.md",
               "papers/survey-2023.pdf", "wiki/internal-kb.md"]
    ratings = [1, 2, 3, 4, 5]

    rows = []
    for i in range(n):
        q = random.choice(questions)
        rows.append({
            "id": f"qa-{i+1:04d}",
            "question": q,
            "source": random.choice(sources),
            "retrieval_score": round(random.uniform(0.41, 0.99), 4),
            "answer_rating": random.choice(ratings),
            "latency_ms": random.randint(120, 2800),
            "tokens_used": random.randint(180, 3900),
            "date": f"2024-0{random.randint(1,3)}-{random.randint(1,28):02d}",
        })

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"  generated: {output_path} ({n} rows)")


# ── API usage dataset ─────────────────────────────────────────────────────────

def generate_usage_dataset(output_path, n=500):
    clients = ["alice@techcorp.io", "bruno@datascience.co", "hiroshi@robotics.jp",
               "eva@nlplab.dk", "faisal@llmconsult.ae", "grace@deeplearn.ng",
               "chloe@airesearch.org", "dmitri@mlops.dev"]
    models  = ["mistral-7b-instruct", "llama-2-13b-chat", "all-MiniLM-L6-v2"]
    plans   = {"alice@techcorp.io": "enterprise", "hiroshi@robotics.jp": "enterprise",
               "eva@nlplab.dk": "enterprise"}

    rows = []
    for i in range(n):
        client = random.choice(clients)
        rows.append({
            "id": f"usage-{i+1:05d}",
            "client": client,
            "plan": plans.get(client, "pro"),
            "model": random.choice(models),
            "input_tokens": random.randint(50, 2000),
            "output_tokens": random.randint(20, 800),
            "latency_ms": random.randint(80, 4000),
            "cost_usd": round(random.uniform(0.0001, 0.08), 6),
            "date": f"2024-0{random.randint(1,3)}-{random.randint(1,28):02d}",
            "status": random.choices(["success", "success", "success", "rate_limited", "error"],
                                     weights=[85, 5, 5, 4, 1])[0],
        })

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"  generated: {output_path} ({n} rows)")


# ── Embeddings benchmark ──────────────────────────────────────────────────────

def generate_benchmark(output_path):
    models = [
        ("all-MiniLM-L6-v2",       0.09,  80.1, 12.4),
        ("bge-large-en-v1.5",       1.20,  86.3, 42.1),
        ("text-embedding-ada-002",  0.00,  87.1, 18.2),
        ("e5-large-v2",             1.30,  85.9, 39.8),
        ("instructor-xl",           4.96,  88.4, 110.3),
        ("gte-large",               0.67,  85.2, 38.1),
    ]
    rows = []
    for name, size, ndcg, latency in models:
        rows.append({
            "model": name,
            "size_gb": size,
            "ndcg_at_10": ndcg,
            "avg_latency_ms": latency,
            "cost_per_1m_tokens": round(random.uniform(0.0, 0.13), 4),
            "self_hosted": "yes" if size > 0 else "no",
        })

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"  generated: {output_path}")


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\nGenerating HiveMind AI datasets...\n")

    generate_qa_dataset(
        os.path.join(BASE, "public/datasets/raw/rag_eval.csv"), n=200)
    generate_usage_dataset(
        os.path.join(BASE, "public/datasets/raw/api_usage.csv"), n=500)
    generate_benchmark(
        os.path.join(BASE, "public/datasets/processed/embedding_benchmark.csv"))

    print("\nDone. Datasets are in hivemind/public/datasets/")
