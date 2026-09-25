import app.auth

from fastapi import HTTPException

from app.auth import verify_api_key


def test_verify_api_key_accepts_valid_key(monkeypatch):
    monkeypatch.setattr(
        app.auth,
        "API_KEY",
        "test-secret-key",
    )

    result = verify_api_key(
        x_api_key="test-secret-key"
    )

    assert result is True


def test_verify_api_key_rejects_invalid_key(monkeypatch):
    monkeypatch.setattr(
        app.auth,
        "API_KEY",
        "test-secret-key",
    )

    try:
        verify_api_key(
            x_api_key="wrong-key"
        )
        assert False
    except HTTPException as error:
        assert error.status_code == 401
        assert error.detail == "Invalid or missing API key"


def test_verify_api_key_rejects_missing_key(monkeypatch):
    monkeypatch.setattr(
        app.auth,
        "API_KEY",
        "test-secret-key",
    )

    try:
        verify_api_key(
            x_api_key=None
        )
        assert False
    except HTTPException as error:
        assert error.status_code == 401
        assert error.detail == "Invalid or missing API key"