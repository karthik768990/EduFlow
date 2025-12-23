# EduFlow - – Smart Academic Workflow Platform

## Overview

EduFlow is a lightweight, web-based academic workflow and study accountability platform designed to improve learning discipline and teaching visibility without using AI or machine learning. The platform helps students plan, track, and reflect on their studies while enabling teachers to assign work, monitor progress, and provide feedback through a clean, intuitive interface.

EduFlow focuses on organization, accountability, and reflection, addressing a real gap between complex LMS platforms and unstructured personal study habits.

## 🎯 Problem Statement

Students often struggle with missed deadlines, poor study consistency, and lack of structured reflection. Teachers, on the other hand, spend excessive time manually tracking assignments and student progress. Existing learning platforms are either too complex or not student-centric.

EduFlow solves this by offering a simple, role-based academic workflow system that improves discipline, transparency, and productivity for both students and educators.

## ✨ Key Features
### 👨‍🎓 Student Features

Subject-wise task planner

Study session tracking (Pomodoro-style)

Daily & weekly study reflections

Progress analytics dashboard

Deadline urgency heatmap

Study streak tracking

### 👩‍🏫 Teacher Features

Assignment creation & scheduling

Class-wise progress monitoring

Deadline compliance overview

Student reflection review

Feedback & remarks system

## 📊 Analytics (Rule-Based, No AI)

Study consistency score

Assignment completion rate

Time-on-task analysis

Missed deadline penalties

## 🏗️ System Architecture

Frontend: React-based client application

Backend: FastAPI (Python)

Database: PostgreSQL / SQLite (for demo)/Supabase(Production)

Authentication: JWT-based role authentication/Google authentication(Production)

Deployment: Cloud-compatible (Vercel + Render)

## 🧠 Design Principles

No AI / ML / LLM usage

Deterministic, explainable logic

Clean REST API design

Scalable modular backend

Privacy-by-design (no real student data)

## 🧰 Tech Stack
Frontend

React

Vite

Tailwind CSS

Chart.js

Backend

Python 3.10+

FastAPI

SQLAlchemy

Pydantic

JWT Authentication

Database

PostgreSQL (production)

SQLite (local demo)

## 📂 Repository Structure
```bash
EduFlow/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── routes/
│   │   ├── auth/
│   │   └── utils/
│   ├── requirements.txt
│   └── README.md
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── README.md
│
├── docs/
│   ├── architecture.md
│   └── api-spec.md
│
└── README.md


```

### Backend Architecture 
```bash


backend/
│
├── app/
│   ├── main.py
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── database.py
│   │
│   ├── modules/
│   │   ├── auth/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   ├── schemas.py
│   │   │   └── dependencies.py
│   │   │
│   │   ├── users/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   ├── repository.py
│   │   │   ├── models.py
│   │   │   └── schemas.py
│   │   │
│   │   ├── assignments/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   ├── repository.py
│   │   │   ├── models.py
│   │   │   └── schemas.py
│   │   │
│   │   ├── study_sessions/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   ├── repository.py
│   │   │   ├── models.py
│   │   │   └── schemas.py
│   │   │
│   │   ├── reflections/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   ├── repository.py
│   │   │   ├── models.py
│   │   │   └── schemas.py
│   │
│   └── shared/
│       ├── responses.py
│       └── exceptions.py
│
├── requirements.txt
└── README.md

```


## 🧠 BACKEND ARCHITECTURE: MODULE-COMMUNICATION DRIVEN (FastAPI)

We will follow a Clean + Layered + Domain-oriented architecture
(No MVC confusion, no spaghetti routes)

### 🔑 CORE IDEA

Routes NEVER talk to the database directly
Business logic NEVER lives in routes
Each module communicates via services & schemas

1️⃣ HIGH-LEVEL MODULE COMMUNICATION FLOW
Client
  ↓
API Routes
  ↓
Service Layer (Business Logic)
  ↓
Repository Layer (DB Access)
  ↓
Database


### Frontend architecture 

```bash

frontend/
│
├── src/
│   ├── app/
│   │   ├── App.jsx
│   │   ├── router.jsx
│   │   └── ProtectedRoute.jsx
│   │
│   ├── auth/
│   │   ├── LoginPage.jsx
│   │   ├── authService.js
│   │   └── authContext.jsx
│   │
│   ├── features/
│   │   ├── assignments/
│   │   │   ├── AssignmentPage.jsx
│   │   │   ├── AssignmentCard.jsx
│   │   │   ├── assignmentService.js
│   │   │   └── assignmentHooks.js
│   │   │
│   │   ├── study/
│   │   │   ├── StudyPage.jsx
│   │   │   ├── StudyTimer.jsx
│   │   │   ├── studyService.js
│   │   │   └── studyHooks.js
│   │   │
│   │   ├── reflections/
│   │   │   ├── ReflectionPage.jsx
│   │   │   ├── ReflectionForm.jsx
│   │   │   └── reflectionService.js
│   │   │
│   │   └── dashboard/
│   │       ├── DashboardPage.jsx
│   │       ├── ProgressChart.jsx
│   │       └── dashboardService.js
│   │
│   ├── shared/
│   │   ├── components/
│   │   │   ├── Navbar.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   └── Loader.jsx
│   │   │
│   │   ├── api/
│   │   │   └── apiClient.js
│   │   │
│   │   ├── hooks/
│   │   │   └── useFetch.js
│   │   │
│   │   └── utils/
│   │       └── dateUtils.js
│   │
│   └── main.jsx
│
└── index.html

```



## ⚙️ Setup Instructions
### Backend Setup (FastAPI)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

```
Backend runs at:
```bash
http://localhost:8000

```
Interactive API docs:
```bash
http://localhost:8000/docs
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:

http://localhost:5173

## 🔐 Authentication Flow

JWT-based authentication

Role-based access (Student / Teacher)

Protected routes for sensitive operations

Secure password hashing

## 📽️ Demo Flow (For Judges)

Teacher logs in and creates an assignment

Student logs in and plans the task

Student starts a study session

Student submits reflection

Teacher views analytics dashboard

Deadline compliance & progress displayed

## 🚧 Limitations

No mobile app (web-only prototype)

Demo uses simulated academic data

Notifications are in-app only

## 🚀 Future Scope

Mobile application

Calendar integration

Exportable academic reports

Institutional deployment support

Mutli platform authentication 


## 📜 License

This project is open-source and intended for educational purposes. Any reused libraries comply with their respective licenses.

## 🧭 MERMAID ARCHITECTURE DIAGRAM


TODO -----  FILL THIS WITH ARCHITECTURE



## 🏁 Final Note (Important)

This solution is:
✅ Rule-compliant
✅ Architecturally strong
✅ Demo-friendly
✅ Judge-aligned
✅ Finale-worthy































