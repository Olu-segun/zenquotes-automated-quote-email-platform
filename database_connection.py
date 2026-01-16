import psycopg2
import time
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    for attempt in range(5):
        try:
            conn = psycopg2.connect(
                
                    host=os.getenv("PGHOST"),
                    dbname=os.getenv("PGDATABASE"),
                    user=os.getenv("PGUSER"),
                    password=os.getenv("PGPASSWORD"),
                    port=os.getenv("PGPORT")
                    
                        )
            print("Database connection established.")
            return conn
        except psycopg2.OperationalError as e:
            print(f"Database connection failed (attempt {attempt+1}/5): {e}")
            time.sleep(5)
    raise Exception("Could not connect to Postgres after 5 attempts")
