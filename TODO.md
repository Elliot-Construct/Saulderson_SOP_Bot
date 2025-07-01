# 📋 Project To-Do

1. **Document Prep & Ingestion**  
   - [ ] Audit existing `.md` files; ensure consistent front-matter (title, type).  
   - [ ] Write ingestion script to traverse handbook folder.  

2. **Metadata & Classification**  
   - [ ] Define and implement metadata schema.  
   - [ ] Build doc-type classifier (rules or lightweight ML).  

3. **Chunking Engine**  
   - [ ] Develop parser to split by headers/paragraphs (~200–300 words).  
   - [ ] Attach metadata to each chunk.  

4. **Embedding Pipeline**  
   - [ ] Select embedding model; prototype on sample chunks.  
   - [ ] Write batch embedding script.

5. **Vector Database Setup**  
   - [ ] Provision vector DB instance (Pinecone/Weaviate).  
   - [ ] Create index with metadata fields.

6. **Search & Retrieval**  
   - [ ] Implement title-level semantic search.  
   - [ ] Implement chunk-level semantic search within selected SOP.  
   - [ ] Build policy cross-reference using shared tags.

7. **API & Response Formatting**  
   - [ ] Define API schema (query → structured JSON response).  
   - [ ] Assemble response templates (SOP excerpt, related policies, links).

8. **Testing & QA**  
   - [ ] Write unit tests for ingestion, chunking, metadata.  
   - [ ] Conduct integration tests: sample queries → expected docs.  
   - [ ] Solicit user feedback on relevance & clarity.

9. **Deploy & Monitor**  
   - [ ] Containerise services (Docker).  
   - [ ] Deploy to staging; set up monitoring dashboards.  
   - [ ] Roll out to production; schedule regular embedding refresh.

10. **Future Enhancements**  
   - [ ] Add cross-encoder reranking.  
   - [ ] Integrate role-based access controls.  
   - [ ] Expand to multilingual support.  

> _Tip: Tackle items in vertical slices (end-to-end MVP → incremental refinements)._  

