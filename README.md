Simple API Gateway with Redis Rate Limiter

A lightweight, high-performance API built with FastAPI, featuring a custom Rate Limiting middleware powered by Redis. The entire stack is containerized using Docker Compose for easy deployment and scalability.

 Features
- FastAPI Backend: High-performance Python web framework.
- Redis Integration: Uses Redis as an in-memory data store for tracking request counts.
- Rate Limiting Middleware: Limits users to a maximum of 5 requests per minute (Fixed Window algorithm).
- Graceful Error Handling: Returns a standard `429 Too Many Requests` response when limits are exceeded.
- Dockerized Architecture: Fully isolated environment for the web app and the Redis cache.

 Tech Stack
- Language: Python 3.10+
- Framework: FastAPI
- Database: Redis (Alpine)
- Containerization: Docker & Docker Compose
- Platform: Optimized for GitHub Codespaces / Linux / macOS

 Project Structure
.
├── app/
│   ├── main.py          # FastAPI application & Rate Limit logic
│   └── requirements.txt # Python dependencies
├── docker-compose.yml   # Services orchestration
└── Dockerfile           # Web service container configuration

```
How to Run

Prerequisites

* Docker and Docker Compose installed.
* (Optional) GitHub Codespaces.
Steps

1. **Clone the repository:
```bash
git clone <your-repo-url>
cd fastapi-redis-ratelimiter

```


2. Start the containers:
```bash
docker-compose up --build

```


3. Access the API:
* Open your browser at `http://localhost:8000`
* You will see: `{"message": "Welcome to the API with Rate Limiting"}`



 Testing the Rate Limiter

1. Visit the root URL or refresh the page.
2. After 5 requests within a single minute, the API will block further attempts.
3. You will receive the following JSON response:
```json
{
  "detail": "Too Many Requests! Only 5 per minute allowed."
}

```


4. Wait for 60 seconds, and access will be automatically restored.

