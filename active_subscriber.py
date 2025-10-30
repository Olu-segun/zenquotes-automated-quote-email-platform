from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

conn = psycopg2.connect(
    host = os.getenv(""),
    dbname = os.getenv("PGDATABASE"),
    user = os.getenv("PGUSER"),
    password = os.getenv("PGPASSWORD"),
    port = os.getenv("PGPORT")
)

cur = conn.cursor()
# Extract active subscriber from database
cur.execute("""
                SELECT first_name, last_name, email_address, subscription_status
                FROM users
                WHERE subscription_status = 'active';
            
            
""")

cur.close()
conn.close()