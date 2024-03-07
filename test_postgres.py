import psycopg2

from postgres_config import db_params

def test_connection():
    try:
        # Attempt connection to DB
        conn = psycopg2.connect(**db_params)
        print("Successfully connected to Database!")
        conn.close()
    except psycopg2.DatabaseError as e:
        print(f"Failed to connect to database: {e}")

if __name__ == "__main__":
    test_connection()
