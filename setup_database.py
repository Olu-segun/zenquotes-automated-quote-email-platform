
from database_connection import get_connection

conn = get_connection()
conr = conn.cursor

cur = conn.cursor()

# Create users table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email_address VARCHAR(255) UNIQUE NOT NULL,
    subscription_status VARCHAR(50) NOT NULL,
    email_frequency VARCHAR(50)
);
""")

# Create email log tables.
cur.execute( """
CREATE TABLE IF NOT EXISTS email_logs (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
	first_name VARCHAR(255) NOT NULL,
    email_address VARCHAR(255) NOT NULL,
    quote_date DATE NOT NULL,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (user_id, email_address, quote_date)
	);        
""")

#Insert subscribers' record to the database.
cur.execute("""
INSERT INTO users (
    first_name,
    last_name,
    email_address,
    subscription_status,
    email_frequency)
VALUES
    ('John', 'Doe', 'john.doe@example.com', 'active', 'daily'),
    ('Jane', 'Smith', 'jane.smith@example.com', 'inactive', 'weekly'),
    ('Michael', 'Johnson', 'michael.johnson@example.com', 'active', 'daily'),
    ('Emily', 'Davis', 'emily.davis@example.com', 'active', 'weekly'),
    ('Chris', 'Brown', 'chris.brown@example.com', 'inactive', 'daily'),
    ('Olivia', 'Taylor', 'olivia.taylor@example.com', 'active', 'daily'),
    ('Daniel', 'Wilson', 'daniel.wilson@example.com', 'inactive', 'weekly'),
    ('Sophia', 'Martinez', 'sophia.martinez@example.com', 'active', 'weekly'),
    ('James', 'Anderson', 'james.anderson@example.com', 'active', 'daily'),
    ('Ava', 'Thomas', 'ava.thomas@example.com', 'inactive', 'weekly'),
    ('William', 'Jackson', 'william.jackson@example.com', 'active', 'daily'),
    ('Isabella', 'White', 'isabella.white@example.com', 'inactive', 'daily'),
    ('Ethan', 'Harris', 'ethan.harris@example.com', 'active', 'weekly'),
    ('Mia', 'Martin', 'mia.martin@example.com', 'active', 'daily'),
    ('Alexander', 'Thompson', 'alexander.thompson@example.com', 'inactive', 'weekly'),
    ('Charlotte', 'Garcia', 'charlotte.garcia@example.com', 'active', 'daily'),
    ('Benjamin', 'Clark', 'benjamin.clark@example.com', 'inactive', 'daily'),
    ('Amelia', 'Rodriguez', 'amelia.rodriguez@example.com', 'active', 'weekly'),
    ('Lucas', 'Lewis', 'lucas.lewis@example.com', 'active', 'daily'),
    ('Harper', 'Lee', 'harper.lee@example.com', 'inactive', 'weekly');
ON CONFLICT (email_address) DO NOTHING;
""")

conn.commit()
cur.close()
conn.close()

print("✅ Database setup completed successfully")
