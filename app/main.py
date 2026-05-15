from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse # أضفنا هذا السطر
import redis

app = FastAPI()

# الاتصال بـ Redis
r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

@app.middleware("http")
async def rate_limiter(request: Request, call_next):
    client_ip = request.client.host
    key = f"rate_limit:{client_ip}"
    
    current_count = r.incr(key)
    
    if current_count == 1:
        r.expire(key, 60)
    
    # التعديل هنا: بدلاً من raise HTTPException، نستخدم JSONResponse
    if current_count > 5:
        return JSONResponse(
            status_code=429,
            content={"detail": "Too Many Requests! Only 5 per minute allowed."}
        )
    
    response = await call_next(request)
    return response

@app.get("/")
def read_root():
    return {"message": "Welcome to the API with Rate Limiting"}