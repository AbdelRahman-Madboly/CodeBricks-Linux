# HiveMind AI — Public Model Cards

Model cards for externally available models.
Weights and checkpoints are in private/models/ — not publicly accessible.

## Available Models

### mistral-7b-instruct (hm-001)
- **Type:** Chat / Instruction following
- **Context:** 4096 tokens
- **Use case:** General Q&A, RAG responses, summarisation
- **API endpoint:** POST /v1/chat/completions
- **Status:** Production

### all-MiniLM-L6-v2 (hm-004)
- **Type:** Embeddings
- **Dimensions:** 384
- **Use case:** Semantic search, document retrieval
- **API endpoint:** POST /v1/embeddings
- **Status:** Production

### hivemind-classifier-v2 (hm-007)
- **Type:** Text classification
- **Classes:** support / billing / technical / other
- **Use case:** Incoming ticket routing
- **API endpoint:** POST /v1/classify
- **Status:** Production
