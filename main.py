from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
import requests
#import redis

#redis_client = redis.StrictRedis(host='0.0.0.0', port=6379, db=0, decode_responses=True)

app = FastAPI()
app.mount("/.well-known", StaticFiles(directory=".well-known"), name="static")

# Route to get a quote
@app.get("/quote")
def get_quote():
    
    response = requests.get("https://zenquotes.io/api/random")
    return response.json()[0]['q']


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")