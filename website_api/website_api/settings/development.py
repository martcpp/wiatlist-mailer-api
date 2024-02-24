from .base import *
from .db import set_database


'''
DONT US THIS IN PROUCTION EDIT YOU PRODUCTION FIEL IN production.py
'''


# Quick-start development settings - unsuitable for production
ALLOWED_HOSTS = ['*']


# SET THIS TO TRUE TO USE POSTGRESQL instead of SQliteDB


set_database()


