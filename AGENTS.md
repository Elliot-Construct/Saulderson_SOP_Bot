# Handbook Retrieval Agent

## 1. Purpose  
This agent empowers end-users to query a company handbook (SOPs, policies, FAQs) and receive:  
- The most relevant Standard Operating Procedure (SOP)  
- Any cross-referenced policies or guidelines  
- Direct links back to the original document sections  

## 2. High-Level Workflow  
1. **Document Ingestion**  
   - Load all `.md` files from the handbook folder.  
2. **Classification & Tagging**  
   - Detect document type: SOP, Policy, FAQ, etc.  
   - Extract metadata: `title`, `section_headers`, `doc_type`, `tags`.  
3. **Chunking**  
   - Split each document into semantic chunks (~200–300 words or logical subsections).  
   - Assign each chunk its parent document’s metadata.  
4. **Embedding**  
   - Use a transformer-based embedding model (e.g. OpenAI’s embeddings or Sentence-Transformers) to vectorize each chunk and each title.  
5. **Indexing**  
   - Store vectors in a vector database (e.g. Pinecone, Weaviate), alongside metadata.  
6. **Query Handling**  
   - **Title match**: embed the user query and perform fast nearest-neighbour search among *titles* to identify the primary SOP.  
   - **Deep dive**: within the chosen SOP, re-embed and search its chunks to extract precise instructions.  
   - **Cross-policy retrieval**: use metadata tags from the primary SOP to fetch related policy chunks.  
7. **Response Assembly**  
   - Compile a structured response:  
     1. **SOP summary** (from top-scoring chunk)  
     2. **Related policies** (list with short excerpts)  
     3. **Links** to full SOP and policy files with section anchors  

## 3. Metadata Schema  
| Field             | Type   | Description                                 |
|-------------------|--------|---------------------------------------------|
| `doc_id`          | string | Unique ID (e.g. filename without extension) |
| `doc_type`        | string | SOP / Policy / FAQ / …                      |
| `title`           | string | Document title                              |
| `section`         | string | Section/header text                         |
| `tags`            | array  | Keywords for cross-reference                 |
| `source_path`     | string | Relative file path                          |
| `anchor`          | string | Markdown anchor for the section             |

## 4. Tools & Libraries  
- **Markdown parsing**: `python-markdown` or `mistune`  
- **Embedding**: OpenAI Embeddings or HuggingFace Sentence-Transformers  
- **Vector DB**: Pinecone, Weaviate or Elasticsearch + KNN plugin  
- **Backend**: FastAPI / Flask for query APIs  
- **Monitoring**: Prometheus + Grafana (latency, error-rates)  

## 5. Performance & Quality  
- **Chunk size tuning**: balance between context richness and vector noise.  
- **Reranking**: optionally apply a fine-tuned cross-encoder on top K candidates for precision.  
- **Logging**: record query → chunks → final selection for audit.  

## 6. Extension Points  
- Support for additional document formats (PDF, Word).  
- Multilingual embedding & retrieval.  
- Role-based access control (restrict certain SOPs).  


