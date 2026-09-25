import time

from fastapi import HTTPException, Request


RATE_LIMIT = 5
WINDOW_SECONDS = 60

_requests = {}


def rate_limit(request: Request):
    client_ip = request.client.host

    current_time = time.time()

    request_times = _requests.get(client_ip, [])

    request_times = [
        timestamp
        for timestamp in request_times
        if current_time - timestamp < WINDOW_SECONDS
    ]

    if len(request_times) >= RATE_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded. Try again later.",
        )

    request_times.append(current_time)
    _requests[client_ip] = request_times