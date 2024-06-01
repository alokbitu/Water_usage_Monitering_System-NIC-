import os

import mysql.connector
import time

# MySQL database configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "admin123",
    "database": "hindalco2",
}

def fetch_data_from_mysql():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = "SELECT station_id, parameter_code, recorded_time, recorded_level FROM real_pollutant_level_infos"
        cursor.execute(query)
        data = cursor.fetchall()

        cursor.close()
        connection.close()

        return data

    except mysql.connector.Error as err:
        print("Error:", err)
        return None


def write_data_to_text_file(data):
    if data is not None:
        desktop_path = os.path.expanduser("~\Desktop")
        file_path = os.path.join(desktop_path, "data_output.txt")

        with open(file_path, "w") as file:
            for row in data:
                formatted_row = [str(value) for value in row]
                file.write(", ".join(formatted_row) + "\n")
        print("Data written to", file_path)
if __name__ == "__main__":
    while True:
        data = fetch_data_from_mysql()
        write_data_to_text_file(data)
        time.sleep(60)  # Wait for 1 minute
