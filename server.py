import os

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Update(BaseModel):
    command: str


updates_queue = []


@app.get("/process/shutdown")
async def shutdown():
    updates_queue.append(Update(command="shutdown"))
    os.system("shutdown /s /t 1")


@app.get("/process/sleep")
async def sleep():
    updates_queue.append(Update(command="sleep"))

    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


class FetchUpdatesResponse(BaseModel):
    updates: list[Update]


@app.get("/updates/fetch", response_model=FetchUpdatesResponse)
async def fetch_updates():
    updates = updates_queue.copy()
    updates_queue.clear()
    return FetchUpdatesResponse(updates=updates)
