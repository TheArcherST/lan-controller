from pydantic_settings import BaseSettings

import dotenv


class Environment(BaseSettings):
    app_host: str
    app_port: str
    app_protocol: str = 'http'


def load_env(filename: str) -> Environment:
    dotenv.load_dotenv(filename)

    return Environment()


environment = load_env('.env')
