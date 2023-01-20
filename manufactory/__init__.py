from flask import Flask
import os
import psycopg2.extras
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
uri = os.getenv("DATABASE_URI")
connection=psycopg2.connect(uri)

from manufactory import routes
