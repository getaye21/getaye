
---

### **`backend/main.py`** (Python FastAPI Backend)
```python
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import json

app = FastAPI()

# CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== DATA MODELS =====
class ContactMessage(BaseModel):
    name: str
    email: str
    subject: str
    message: str

class Subscriber(BaseModel):
    email: str

# ===== YOUR COMPLETE PORTFOLIO DATA =====
PROFILE_DATA = {
    "name": "Getaye Fiseha Tadesse",
    "titles": [
        "System Administrator",
        "Network and Electronic Communication Engineer",
        "Full Stack Developer",
        "AI Engineer"
    ],
    "location": "Addis Ababa, Ethiopia",
    "email": "getayefiseha21@gmail.com",
    "phone": "+251-980574725",
    "birthday": "May 1",
    "bio": "In addition to my academic achievements and internship experience, I am currently gaining valuable skills from my role as system and database administrator at Ahadu Bank. My responsibilities include Active Directory administration, mail exchange administration, Oracle database management, IT support, software troubleshooting, network support, and proficiency in programming languages such as HTML, CSS, and JavaScript. I am also experienced in using Nutanix Prism, AHV, and AOS Central.",
    
    "experiences": [
        {
            "title": "Junior System and Database Officer",
            "company": "Ahadu Bank",
            "period": "Apr 2025 - Present",
            "location": "Addis Ababa, Ethiopia",
            "type": "Full-time",
            "description": "AD Administration, Oracle Database Administration, Mail exchange Administration, Nutanix Prism Administration, Virtualization, System Monitoring"
        },
        {
            "title": "Full Stack Developer (Freelance)",
            "company": "Self-employed",
            "period": "2024 - Present",
            "location": "Remote",
            "type": "Contract",
            "description": "Building web applications with React, Node.js, Python/Django, and cloud deployment on Vercel. Creating REST APIs and database integrations."
        },
        {
            "title": "AI Engineer (Research)",
            "company": "Addis Ababa University",
            "period": "2025 - Present",
            "location": "Addis Ababa",
            "type": "Research",
            "description": "Developing machine learning models for social media addiction detection using AdaBoost algorithm. Working on predictive analytics and data processing."
        },
        {
            "title": "Information Technology Trainee",
            "company": "Ahadu Bank",
            "period": "Jul 2024 - Mar 2025",
            "location": "Ethiopia",
            "type": "Internship",
            "description": "Branch Support, End Device Inspection, Database Administration, System Active Directory, Mail exchange, Disk and VMs Management, Network monitoring and Troubleshooting, Software support"
        },
        {
            "title": "Salesperson",
            "company": "Safaricom Telecommunications Ethiopia PLC",
            "period": "Nov 2023 - Jun 2024",
            "location": "Remote",
            "type": "Contract",
            "description": "Customer service, sales operations, and telecommunications support"
        },
        {
            "title": "Appfactory Academy Intern",
            "company": "Wollo University",
            "period": "Feb 2023 - Jun 2023",
            "location": "Kombolcha",
            "type": "Internship",
            "description": "Project Progress on SD WSN, MATLAB coding, Electronic Engineering"
        }
    ],
    
    "education": [
        {
            "degree": "Master of Science - Computer Science",
            "school": "Addis Ababa University (AAU)",
            "year": "Oct 2025 – Jul 2028",
            "focus": "Network and Security",
            "skills": ["Data Management Systems", "Software Project Management", "Network Security"]
        },
        {
            "degree": "Bachelor of Science - Electrical and Computer Engineering",
            "school": "Wollo University",
            "year": "Oct 2018 – Sep 2023",
            "gpa": "3.91",
            "activities": "Junior Professional"
        }
    ],
    
    "certifications": [
        {"name": "Introduction to Cybersecurity", "issuer": "Cisco", "year": "Mar 2026", "credential_id": "Cisco-Cyber-001"},
        {"name": "Networking Basics", "issuer": "Cisco", "year": "Feb 2026", "credential_id": "Cisco-Net-002"},
        {"name": "NCA 6.10 Practice Exam", "issuer": "Nutanix", "year": "Jul 2025", "credential_id": "Nutanix-NCA-003"},
        {"name": "Android Developer Fundamentals", "issuer": "Udacity", "year": "May 2025", "credential_id": "Udacity-Android-004"},
        {"name": "Artificial Intelligence Fundamentals", "issuer": "Udacity", "year": "Apr 2025", "credential_id": "Udacity-AI-005"},
        {"name": "Data Analysis Fundamentals", "issuer": "Udacity", "year": "Mar 2025", "credential_id": "Udacity-Data-006"},
        {"name": "JavaScript Algorithms and Data Structures", "issuer": "freeCodeCamp", "year": "Feb 2025", "credential_id": "fccc3551c8-f905-4bb8-89d4-74920677b9a1"},
        {"name": "Responsive Web Design", "issuer": "freeCodeCamp", "year": "Feb 2025", "credential_id": "fccc3551c8-f905-4bb8-89d4-74920677b9a1-rwd"},
        {"name": "Programming Fundamentals", "issuer": "Udacity", "year": "Aug 2024", "credential_id": "Udacity-PF-007"},
        {"name": "Dereja Academy Accelerator Program", "issuer": "Dereja", "year": "Jul 2023"}
    ],
    
    "skills": [
        "Active Directory", "Oracle Database", "Nutanix Prism/AHV", "Mail Exchange",
        "HTML/CSS/JavaScript", "Python", "React.js", "Node.js", "FastAPI", "Django",
        "Machine Learning", "AdaBoost", "REST APIs", "Supabase", "Docker", "Git",
        "Virtualization", "Network Monitoring", "Kaspersky Antivirus", "MATLAB",
        "System Administration", "Database Management", "Cloud Computing"
    ],
    
    "projects": [
        {
            "name": "Social Media Addiction Risk Analyzer",
            "description": "Machine Learning application using AdaBoost algorithm for addiction test and usage analysis",
            "tech": ["Python", "Scikit-learn", "Flask", "Pandas"],
            "year": "Mar 2026 - Present"
        },
        {
            "name": "AAU Student Management System",
            "description": "Student management website built on Supabase cloud database with CRUD operations",
            "tech": ["React", "Supabase", "REST APIs", "Tailwind CSS"],
            "year": "Dec 2025"
        }
    ],
    
    "social": {
        "github": "https://github.com/getnet21",
        "linkedin": "https://www.linkedin.com/in/getaye-fiseha-tadesse/",
        "email": "getayefiseha21@gmail.com",
        "phone": "+251-980574725"
    }
}

# In-memory storage (in production, use a database)
saved_messages = []
subscribers = []

# ===== API ENDPOINTS =====
@app.get("/api/profile")
async def get_profile():
    return PROFILE_DATA

@app.get("/api/github/repos")
async def get_github_repos():
    import httpx
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/users/getnet21/repos?sort=updated&per_page=6")
        if response.status_code == 200:
            repos = response.json()
            return [{
                "name": r["name"],
                "description": r["description"] or "No description available",
                "stars": r["stargazers_count"],
                "forks": r["forks_count"],
                "url": r["html_url"],
                "language": r["language"] or "Unknown"
            } for r in repos]
        return []

@app.post("/api/contact")
async def send_contact_message(message: ContactMessage):
    # Store message
    saved_messages.append({
        **message.dict(),
        "timestamp": datetime.now().isoformat()
    })
    print(f"📧 New message from {message.name} ({message.email}): {message.subject}")
    print(f"   Message: {message.message}")
    return {"success": True, "message": "✅ Message received! I'll get back to you within 24 hours."}

@app.post("/api/subscribe")
async def subscribe(subscriber: Subscriber):
    if subscriber.email not in [s["email"] for s in subscribers]:
        subscribers.append({"email": subscriber.email, "timestamp": datetime.now().isoformat()})
        print(f"📧 New subscriber: {subscriber.email}")
    return {"success": True, "message": "✅ Subscribed successfully!"}

@app.get("/api/messages")
async def get_messages():
    # In production, add authentication
    return {"count": len(saved_messages), "messages": saved_messages[-10:]}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}
