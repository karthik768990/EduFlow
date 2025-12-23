from fastapi import FastAPI
from app.modules.auth.router import router as auth_router
from app.modules.users.router import router as users_router
from app.modules.assignments.router import router as assignments_router
from app.modules.study_sessions.router import router as study_router
from app.modules.reflections.router import router as reflections_router

app = FastAPI(title="EduFlow API")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(assignments_router, prefix="/assignments", tags=["Assignments"])
app.include_router(study_router, prefix="/study-sessions", tags=["Study Sessions"])
app.include_router(reflections_router, prefix="/reflections", tags=["Reflections"])
