import app.rate_limit

from fastapi import HTTPException


class FakeClient:
    def __init__(self, host):
        self.host = host


class FakeRequest:
    def __init__(self, host):
        self.client = FakeClient(host)


def test_rate_limit_allows_requests(monkeypatch):
    app.rate_limit._requests.clear()

    request = FakeRequest("127.0.0.1")

    for _ in range(5):
        app.rate_limit.rate_limit(request)

    assert len(app.rate_limit._requests["127.0.0.1"]) == 5


def test_rate_limit_blocks_sixth_request(monkeypatch):
    app.rate_limit._requests.clear()

    request = FakeRequest("127.0.0.1")

    for _ in range(5):
        app.rate_limit.rate_limit(request)

    try:
        app.rate_limit.rate_limit(request)
        assert False
    except HTTPException as error:
        assert error.status_code == 429
        assert error.detail == "Rate limit exceeded. Try again later."


def test_rate_limit_removes_old_requests(monkeypatch):
    app.rate_limit._requests.clear()

    request = FakeRequest("127.0.0.1")

    current_time = 1000

    monkeypatch.setattr(
        app.rate_limit.time,
        "time",
        lambda: current_time,
    )

    for _ in range(5):
        app.rate_limit.rate_limit(request)

    assert len(app.rate_limit._requests["127.0.0.1"]) == 5

    current_time = 1061

    app.rate_limit.rate_limit(request)

    assert len(app.rate_limit._requests["127.0.0.1"]) == 1