import psycopg2
from postgres_config import db_params

def test_connection(schema='raspi_weather', table="dht22"):
    try:
        # Attempt connection to DB
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()
        # Attempt to fetch the first row from the specified table
        cur.execute(f"SELECT * FROM {schema}.{table} LIMIT 1;")
        print("Successfully connected to Database and accessed specified schema and table!")
        cur.close()
    except psycopg2.DatabaseError as e:
        print(f"Failed to connect to database: {e}")
    except Exception as e:
        print(f"Error accessing {schema}.{table}: {e}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    test_connection()
