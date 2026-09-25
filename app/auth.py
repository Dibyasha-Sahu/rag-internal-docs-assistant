import os

from fastapi import Header, HTTPException
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv("API_KEY")


def verify_api_key(x_api_key: str = Header(default=None)):
    if not API_KEY:
        raise HTTPException(
            status_code=500,
            detail="API key is not configured",
        )

    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key",
        )

    return True