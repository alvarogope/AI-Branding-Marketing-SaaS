# AI-Powered Branding Tool

> Generates branding keywords and copy snippets from a simple text input.

**This is an ongoing project. Features and structure are actively being developed.**

---

## What is this?

An AI-powered branding tool built on top of the Anthropic API. You provide a short input describing your brand, product, or idea, and it returns relevant branding keywords and a copy snippet to help kickstart your creative process.

Currently running as a Python CLI tool with a FastAPI REST layer, it is being expanded into a full-stack SaaS application with cloud infrastructure and a modern frontend.

---

## Current Features

- Input validation (max 20 characters)
- AI-generated branding keywords via Anthropic API
- AI-generated branding copy snippet via Anthropic API
- `.env` support for secure API key management
- REST API with three endpoints via FastAPI

---

## Tech Stack (Current)

- **Python** — core logic and CLI
- **Anthropic API** — AI-powered text generation
- **FastAPI** — REST API layer
- **python-dotenv** — environment variable management
- **argparse** — CLI argument parsing

---

## Getting Started

### Prerequisites

- Python 3.8+
- An [Anthropic API key](https://console.anthropic.com)

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/generate_snippet` | Generate a branding copy snippet |
| GET | `/generate_keywords` | Generate branding keywords |
| GET | `/generate_snippet_and_keywords` | Generate both at once |

All endpoints accept a `user_input` query parameter:
```
http://127.0.0.1:8000/generate_snippet?user_input=Nike shoes
```

---

## Project Structure

```
AI-powered SaaS App/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── main_API.py
├── .env
├── .gitignore
└── README.md
```

---

## Roadmap

- [x] **Python CLI** — core logic and argument parsing
- [x] **FastAPI** — REST API layer with three endpoints
- [ ] **AWS Lambda** — deploy backend as a serverless function
- [ ] **API Gateway** — finish backend with AWS API Gateway integration
- [ ] **React Frontend** — build a modern, responsive UI
- [ ] **TailwindCSS** — style the frontend
