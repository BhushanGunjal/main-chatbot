

### 📂 Phase 1 — Setup & Configuration

1. `requirements.txt` → dependencies
2. `config/settings.py` → environment & API key handling
3. `.env` → store keys safely

---

### 📂 Phase 2 — API Skeleton (FastAPI)

4. `API/main.py` → FastAPI entry point
5. `API/routes/chat.py` → `/chat` endpoint (just echo first, later connect LangGraph)
6. `API/routes/upload.py` → `/upload` endpoint (just accept file, later process)
7. `API/models/chat_models.py` → request/response schemas

---

### 📂 Phase 3 — Agents (LangGraph - Dummy)

8. `AGENTS/graph.py` → define dummy nodes (planner, retrieval, reasoning)
9. `AGENTS/planner.py` → stub planner (just routes randomly for now)
10. `AGENTS/retrieval.py` → dummy retrieval (returns “no docs yet”)
11. `AGENTS/reasoning.py` → dummy reasoning (returns “I’m thinking…”)
12. `AGENTS/summarizer.py` → dummy summarizing (returns “Summary…”)

---

### 📂 Phase 4 — Real Logic

13. `UPLOAD/processor.py` → parse files into text
14. `UPLOAD/embeddings.py` → embed text + store in Chroma
15. Update `AGENTS/retrieval.py` → real ChromaDB search
16. Update `AGENTS/reasoning.py` → OpenAI call
17. Update `AGENTS/planner.py` → add retrieval → reasoning fallback

---

### 📂 Phase 5 — UI (Streamlit)

18. `UI/app.py` → connect to FastAPI, send chat, display response

---
### FOLDER STRUCUTRE 

MAIN-CHATBOT
├── AGENTS
│   ├── graph.py
│   ├── orchestrator.py
│   ├── planner.py
│   ├── reasoning.py
│   ├── retrieval.py
│   └── summarizer.py
├── API
│   ├── models
│   │   ├── chat_models.py
│   │   └── upload_models.py
│   ├── routes
│   │   ├── chat.py
│   │   ├── history.py
│   │   └── upload.py
│   └── main.py
├── DB
│   └── chroma
├── UI
│   └── app.py
├── UPLOADS
│   ├── embeddings.py
│   └── processor.py
├── config
│   ├── logging.yaml
│   └── settings.py
├── test
│   ├── test_agents.py
│   ├── test_api.py
│   ├── test_config.py
│   └── test_upload.py
├── uploads
│   └── dummy.docx
├── .env
├── README.md
├── docker-compose.yml
└── requirements.txt
---

