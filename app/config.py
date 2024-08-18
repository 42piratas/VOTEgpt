from decouple import config

class Config:
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL')
    OPENAI_API_KEY = config('OPENAI_API_KEY')
