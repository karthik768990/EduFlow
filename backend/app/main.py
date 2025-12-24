print("🔥🔥🔥 THIS MAIN.PY IS RUNNING 🔥🔥🔥")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.modules.doubts.router import router as doubts_router
from app.modules.auth.router import router as auth_router
from app.modules.users.router import router as users_router
from app.modules.assignments.router import router as assignments_router
from app.modules.study_sessions.router import router as study_router
from app.modules.reflections.router import router as reflections_router
from app.modules.analytics.router import router as analytics_router


app = FastAPI(title="EduFlow API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173",
    "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(assignments_router, prefix="/assignments", tags=["Assignments"])
app.include_router(study_router, prefix="/study-sessions", tags=["Study Sessions"])      
app.include_router(reflections_router, prefix="/reflections", tags=["Reflections"])
app.include_router(doubts_router,prefix="/doubts",tags=["Doubts"])
app.include_router(analytics_router,prefix="/analytics",tags=["Analytics"])

@app.get("/health")
def health():
    return {"status": "ok"}
