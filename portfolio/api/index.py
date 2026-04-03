from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContactMessage(BaseModel):
    name: str
    email: str
    subject: str
    message: str

PROFILE_DATA = {
    "name": "Getaye Fiseha Tadesse",
    "titles": ["System Administrator", "Network and Electronic Communication Engineer", "Full Stack Developer", "AI Engineer"],
    "location": "Addis Ababa, Ethiopia",
    "email": "getayefiseha21@gmail.com",
    "phone": "+251-980574725",
    "bio": "System and database administrator at Ahadu Bank. Expert in Active Directory, Oracle DB, Nutanix Prism, full-stack development, and AI research.",
    "experiences": [
        {"title": "Junior System and Database Officer", "company": "Ahadu Bank", "period": "Apr 2025 - Present", "location": "Addis Ababa", "description": "AD Administration, Oracle Database, Nutanix Prism, Virtualization"},
        {"title": "Full Stack Developer", "company": "Freelance", "period": "2024 - Present", "location": "Remote", "description": "React, Node.js, Python, REST APIs"},
        {"title": "AI Engineer", "company": "AAU Research", "period": "2025 - Present", "location": "Addis Ababa", "description": "ML models with AdaBoost for addiction detection"},
        {"title": "IT Trainee", "company": "Ahadu Bank", "period": "Jul 2024 - Mar 2025", "location": "Ethiopia", "description": "Network monitoring, Active Directory, VM management"}
    ],
    "education": [
        {"degree": "MSc in Computer Science", "school": "Addis Ababa University", "year": "2025-2028"},
        {"degree": "BSc in Electrical & Computer Engineering", "school": "Wollo University", "year": "2018-2023", "gpa": "3.91"}
    ],
    "certifications": [
        {"name": "Introduction to Cybersecurity", "issuer": "Cisco", "year": "Mar 2026"},
        {"name": "Networking Basics", "issuer": "Cisco", "year": "Feb 2026"},
        {"name": "NCA 6.10 Practice Exam", "issuer": "Nutanix", "year": "Jul 2025"},
        {"name": "Android Developer Fundamentals", "issuer": "Udacity", "year": "May 2025"},
        {"name": "Artificial Intelligence Fundamentals", "issuer": "Udacity", "year": "Apr 2025"}
    ],
    "skills": ["Active Directory", "Oracle DB", "Nutanix Prism", "Python", "React", "Node.js", "Machine Learning", "REST APIs", "JavaScript", "Tailwind CSS", "Docker", "Git"],
    "social": {
        "github": "https://github.com/getnet21",
        "linkedin": "https://www.linkedin.com/in/getaye-fiseha-tadesse/"
    }
}

saved_messages = []

@app.get("/api/profile")
async def get_profile():
    return PROFILE_DATA

@app.get("/api/github/repos")
async def get_github_repos():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/users/getnet21/repos?sort=updated&per_page=6")
        if response.status_code == 200:
            repos = response.json()
            return [{"name": r["name"], "description": r["description"] or "", "stars": r["stargazers_count"], "forks": r["forks_count"], "url": r["html_url"], "language": r["language"] or "Unknown"} for r in repos]
        return []

@app.post("/api/contact")
async def send_contact_message(message: ContactMessage):
    saved_messages.append({**message.dict(), "timestamp": datetime.now().isoformat()})
    print(f"Message from {message.name}: {message.message}")
    return {"success": True, "message": "Message received! I'll respond soon."}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}
