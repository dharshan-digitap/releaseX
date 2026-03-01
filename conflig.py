import os


class Configuration:
    BASE_URL = "https://digitap-ai.atlassian.net/wiki"
    EMAIL = "johnebin@digitap.ai"
    API_TOKEN = os.getenv("API_TOKEN")
    SPACE_KEY = "~71202095177ebf6ae24e6baab9f2e6a2abd1d2"
    PARENT_PAGE_ID = 1047429122
