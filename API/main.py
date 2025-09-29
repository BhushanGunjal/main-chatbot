from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers (we'll create these files next)
from API.routes import chat, upload, history

app = FastAPI(
    title="API",
    description="Backend API for our LangGraph-powered chatbot",
    version="0.1.0",
)

# CORS (allow frontend to talk to backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later restrict to your Streamlit URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(history.router, prefix="/history", tags=["History"])

@app.get("/")
def root():
    return {"message": "Chatbot API is running!"}

