import os

env = os.getenv("ENVIRONMENT", "")
print(f"Environment under test: {env}")

dev = {
    "BASE_URL": "https://jsonplaceholder.typicode.com",
    "TRACE_API_CALLS": "true"
}

test = {
    "BASE_URL": "https://jsonplaceholder.typicode.com",
    "TRACE_API_CALLS": "false"
    
}

release = {
    "BASE_URL": "https://jsonplaceholder.typicode.com",
    "TRACE_API_CALLS": "false"
}

environment = {
    "dev": dev,
    "test": test,
    "release": release,
}


class ConfigManager:
    def __init__(self, config):
        self.config = config

    def get_config(self, env):
        return self.config[env]


configManager = ConfigManager(environment)

ENV = configManager.get_config(env)

print("ENVIRONMENT:", ENV)
