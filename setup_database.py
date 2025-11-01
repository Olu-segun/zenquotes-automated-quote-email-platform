from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

conn = psycopg2.connect( 
    host = os.getenv("PGHOST"), 
    dbname = os.getenv("PGDATABASE"), 
    user = os.getenv("PGUSER"), 
    password = os.getenv("PGPASSWORD"), 
    port = os.getenv("PGPORT")
)

#Connect to postgres database and create table

cur = conn.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS users (
            user_id INT PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            email_address VARCHAR(255) NOT NULL,
            subscription_status VARCHAR(255) NOT NULL,
            email_frequency VARCHAR(255)
            );
             """)

#Insert subscribers' record to the database.

cur.execute(""" INSERT INTO users(user_id, first_name, last_name, email_address, 
            subscription_status, email_frequency)
    VALUES
    (1, 'Olusegun', 'Fakayode', 'fakayodeoluseguno@gmail.com', 'active', 'daily'),
    (2, 'Omosola', 'Olukayode', 'omosoladaramola@gmail.com', 'active', 'weekly'),
    (3, 'Obaloluwa', 'Adebisi', 'ericolukayodeo@gmail.com', 'active', 'daily'),
    (4, 'Beejan', 'Davis', 'beejan@dataengineeringcommunity.com', 'active', 'weekly'),
    (5, 'Feyisayo', 'Ajiboye', 'solapeajiboye@gmail.com', 'inactive', 'daily'),
    (6, 'Esther', 'Ogunrinde', 'ogunrindee2@gmail.com', 'active', 'daily'),
    (7, 'Oluwakemi', 'Akinyede', 'akinyedeoluwakemi@gmail.com', 'active', 'Daily'),
    (8, 'Paul', 'Oyelaran', 'oyelaranpaul@gmail.com', 'active', 'Daily'),
    (9, 'Yusuf', 'Alade', 'aladeyussuf.kofo@gmail.com', 'active', 'daily'),
    (10, 'Ibrahim', 'Akinyele', 'iakinyele3@gmail.com', 'inactive', 'weekly'),
    (11, 'William', 'Jackson', 'william.jackson@example.com', 'active', 'daily'),
    (12, 'Isabella', 'White', 'isabella.white@example.com', 'inactive', 'daily'),
    (13, 'Ethan', 'Harris', 'ethan.harris@example.com', 'active', 'weekly'),
    (14, 'Mia', 'Martin', 'mia.martin@example.com', 'active', 'daily'),
    (15, 'Alexander', 'Thompson', 'alexander.thompson@example.com', 'inactive', 'weekly'),
    (16, 'Charlotte', 'Garcia', 'charlotte.garcia@example.com', 'inactive', 'daily'),
    (17, 'Benjamin', 'Clark', 'benjamin.clark@example.com', 'inactive', 'daily'),
    (18, 'Amelia', 'Rodriguez', 'amelia.rodriguez@example.com', 'inactive', 'weekly'),
    (19, 'Lucas', 'Lewis', 'lucas.lewis@example.com', 'inactive', 'daily'),
    (20, 'Harper', 'Lee', 'harper.lee@example.com', 'inactive', 'weekly');
""")
cur.close()
conn.close()

