import os
import requests

from config import environment


async def shutdown():
    os.system("shutdown /s /t 1")


async def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")



while True:
    response = requests.get(f"{environment.app_protocol}://{environment.app_host}:{environment.app_port}/updates/fetch")
    data = response.json()
    updates = data["updates"]