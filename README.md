# AI Branding & Marketing SaaS
 
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat&logo=nextdotjs&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=flat&logo=react&logoColor=61DAFB)
![Claude](https://img.shields.io/badge/Claude-Anthropic-D97757?style=flat)
![AWS Lambda](https://img.shields.io/badge/AWS%20Lambda-FF9900?style=flat&logo=awslambda&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat&logo=vercel&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-06B6D4?style=flat&logo=tailwindcss&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=flat)
 
A full-stack AI-powered SaaS application that acts as an automated branding and marketing assistant. Users provide a brief brand or product description and receive AI-generated marketing copy and SEO keywords in real time, powered by Anthropic's Claude. The backend runs serverlessly on AWS Lambda, and the frontend is deployed on Vercel.

---

## 🌐 API Endpoints
 
| Method | Endpoint | Description |
|---|---|---|
| GET | `/generate_snippet` | Returns an AI-generated marketing snippet |
| GET | `/generate_keywords` | Returns AI-generated SEO keywords |
| GET | `/generate_snippet_and_keywords` | Returns both snippet and keywords in one call |
 
All endpoints accept a `user_input` query parameter (max 20 characters).
 
**Example request:**
```
GET /generate_snippet_and_keywords?user_input=pizza
```
 
**Example response:**
```json
{
  "snippet": "Every slice tells a story. Fresh ingredients, bold flavours, unforgettable moments.",
  "keywords": ["artisan", "fresh", "handcrafted", "authentic", "flavour"]
}
```

---

## 🏗️ Architecture
 
```
┌─────────────────────┐         ┌──────────────────────────┐
│   Next.js (React)   │ ──────▶ │   FastAPI on AWS Lambda  │
│   Tailwind CSS      │         │   Serverless function    │
│   Vercel            │         │   Mangum ASGI adapter    │
└─────────────────────┘         └──────────┬───────────────┘
                                            │
                                            ▼
                                      Anthropic API
                                  (Claude claude-opus-4-6)
                               marketing copy + SEO keywords
```

---

## 🗂️ Project Structure
 
```
AI-Branding-Marketing-SaaS/
├── app/
│   ├── main.py        # Core AI logic — generate_branding_snippet, generate_keywords
│   └── app_API.py     # FastAPI app — API routes and input validation
├── .env               # Anthropic API key (excluded from version control)
├── .env.example       # Environment variable template
├── requirements.txt   # Python dependencies
└── README.md
```

---

## 🔨 In Progress
 
- [ ] Next.js frontend — input form, results display, loading states
- [ ] Vercel deployment and environment configuration
- [ ] AWS Lambda deployment via Mangum ASGI adapter
- [ ] User authentication and daily usage limits
- [ ] History of previously generated content

---

## 🛠️ Tech Stack
 
| Layer | Technology |
|---|---|
| AI | Anthropic Claude (`claude-opus-4-6`) |
| Backend | FastAPI, Python, Uvicorn |
| Frontend | Next.js, React, Tailwind CSS *(in progress)* |
| Deployment | AWS Lambda (backend), Vercel (frontend) |
