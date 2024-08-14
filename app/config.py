from decouple import config

class Config:
    SECRET_KEY = config('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL')
    OPENAI_API_KEY = config('OPENAI_API_KEY')
