# Saulderson_SOP_Bot

This repository contains code for a handbook retrieval system. The goal is to ingest and index SOPs and related documents for semantic search.

## Ingestion

Run `ingest.py` to scan the `handbook` directory and output document metadata.

```
python ingest.py
```

Set `HANDBOOK_DIR` environment variable to target a different folder.
