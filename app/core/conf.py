import os


class Config:
    """Application config class"""

    def __init__(self):
        self.token = os.getenv("TOKEN", "token-telegram")
        self.port = os.getenv("PORT", "8000")
