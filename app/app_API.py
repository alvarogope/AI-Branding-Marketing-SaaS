from fastapi import HTTPException
from fastapi import FastAPI
from app.main import generate_branding_snippet, generate_keywordsS, MAX_INPUT_LENGTH

app = FastAPI()

MAX_INPUT_LENGTH = 20

@app.get("/generate_snippet")
async def generate_snippet_api(user_input: str):
    validate_input_length(user_input)
    snippet = generate_branding_snippet(user_input)
    return {"snippet": snippet, "keywords": []}


@app.get("/generate_keywords")
async def generate_keywords_api(user_input: str):
    validate_input_length(user_input)
    keywords = generate_keywords(user_input)
    return {"snippet": None, "keywords": keywords}


@app.get("/generate_snippet_and_keywords")
async def generate_keywords_api(user_input: str):
    validate_input_length(user_input)
    snippet = generate_branding_snippet(user_input)
    keywords = generate_keywords(user_input)
    return {"snippet": snippet, "keywords": keywords}

def validate_input_length(user_input: str):
    if len(user_input) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"The maximum input length is {MAX_INPUT_LENGTH} characters long."
        )
