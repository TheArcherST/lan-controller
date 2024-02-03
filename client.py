import os
import time

import requests

from config import environment
from server import Update, FetchUpdatesResponse


def shutdown():
    os.system("shutdown /s /t 1")


def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


while True:
    try:
        response = requests.get(f"{environment.app_protocol}://{environment.app_host}:{environment.app_port}/updates/fetch")
    except requests.exceptions.RequestException as e:
        print(e)
        time.sleep(5)
        continue

    data = FetchUpdatesResponse(**response.json())
    for i in data.updates:
        if i.command == "sleep":
            sleep()
        elif i.command == "shutdown":
            shutdown()
        else:
            pass

    time.sleep(1)
