# AI-Powered Branding Tool
 
> Generates branding keywords and copy snippets from a simple text input.
 
**This is an ongoing project. Features and structure are actively being developed.**
 
---

## What is this?
 
An AI-powered branding tool built on top of the Anthropic API. You provide a short input describing your brand, product, or idea, and it returns relevant branding keywords and a copy snippet to help kickstart your creative process.
 
Currently running as a Python CLI tool, it is being expanded into a full-stack SaaS application with a REST API, cloud infrastructure, and a modern frontend.
 
---
 
## Current Features
 
- Input validation (max 20 characters)
- AI-generated branding keywords via Anthropic API
- AI-generated branding copy snippet via Anthropic API
- `.env` support for secure API key management
 
---
 
## Tech Stack (Current)
 
- **Python** — core logic and CLI
- **Anthropic API** — AI-powered text generation
- **python-dotenv** — environment variable management
- **argparse** — CLI argument parsing
 
---
 
## Getting Started
 
### Prerequisites
 
- Python 3.8+
- An [Anthropic API key](https://console.anthropic.com)

 
---
 
## Project Structure
 
```
AI-powered SaaS App/
├── app/
│   └── main.py
├── .env
├── .gitignore
└── README.md
```
 
---
 
## Roadmap
 
This project is under active development. Planned updates include:
 
- [ ] **FastAPI** — build out a REST API layer
- [ ] **AWS Lambda** — deploy backend as a serverless function
- [ ] **API Gateway** — finish backend with AWS API Gateway integration
- [ ] **React Frontend** — build a modern, responsive UI
- [ ] **TailwindCSS** — style the frontend
