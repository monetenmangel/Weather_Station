# import libraries

import time
import adafruit_dht
import board
import psycopg2
from datetime import datetime
from postgres_config import db_params


# declare variables

dht_device = adafruit_dht.DHT22(board.D4)

# declare functions

def read_sensor(max_attempts=5):
    """
    Read the DHT22 Sensor and store the results in 2 seperate variables (temperature, humidity)

    The sensor tends to error for, so the functions runs n times (default 5 times) that if an error occurs it does not lead to a major problem
    """
    for attempt in range(max_attempts):
        try:
            temperature = dht_device.temperature
            humidity = dht_device.humidity

            if humidity is not None and temperature is not None:
                return temperature, humidity

            else:
                raise Exception("Read failed, try again")

        except RuntimeError as error:
            print(f"{datetime.now()}: {error}")

        raise Exception(f"Sensor failed more than {max_attempts} times.")

def insert_data(temperature, humidity):
    conn = None
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor() # necessary for SQL commands
        insert_query = """
        INSERT INTO RaspberryPi_Weather_Station.dht22 (temperature, humidity)
        VALUES (%s, %s);
        """
        cursor.execute(insert_query, (temperature, humidity))
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not null:
            conn.close()

while True:
    temperature, humidity = read_sensor()
    print(f"Temperature: {temperature}°C | Humidity: {humidity}%")
    insert_data(temperature, humidity)
    print("Data have been inserted")
    time.sleep(10.0)