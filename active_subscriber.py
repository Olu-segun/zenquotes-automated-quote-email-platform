from database_connection import get_connection

conn = get_connection()
cur = conn.cursor()

def fetch_user():
    cur.execute("""
                SELECT
                        u.user_id,
                        u.first_name,
                        u.email_address
                FROM users u
                LEFT JOIN email_logs e
                ON u.user_id = e.user_id
                AND e.quote_date = CURRENT_DATE
                WHERE u.subscription_status = 'active'
                AND e.user_id IS NULL;
            """)
    users = cur.fetchall()

    cur.close()
    conn.close()
    return users
