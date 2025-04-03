from sense_hat import SenseHat
from time import time
import datetime
import csv
import os

sense = SenseHat()

sense.clear()

send = False
interval = 10  # 1 minute
prevSec = 0

# Path to save the CSV file
csv_file = "/home/Ardra/sensor_data.csv"  # Adjust the path if necessary

# Create a CSV file and write the header if it doesn't already exist
if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Temperature (°C)", "Humidity (%)", "Pressure (hPa)",
                         "Accelerometer", "Gyroscope", "Magnetometer"])

print("Send sensor data from Sense HAT to a CSV file on Raspberry Pi")
print()

while True:
    for event in sense.stick.get_events():
        if event.direction == "left":
            send = False
            sense.show_letter("0", text_colour=(100, 0, 0))
            print("Stop!")
            print()

        if event.direction == "right":
            send = True
            sense.show_letter("1", text_colour=(0, 100, 0))
            print("Sending data...")
            print()

    if send:
        if time() - prevSec > interval:
            prevSec = time()

            # Collect data
            date = str(datetime.datetime.now())
            temperature = sense.get_temperature()
            humidity = sense.get_humidity()
            pressure = sense.get_pressure()
            accelerometer = sense.get_accelerometer_raw()
            gyroscope = sense.get_gyroscope_raw()
            magnetometer = sense.get_compass()

            # Prepare data for CSV
            data_to_write = [
                date,
                round(temperature, 2),
                round(humidity, 2),
                round(pressure, 2),
                str(accelerometer),
                str(gyroscope),
                round(magnetometer, 2)
            ]

            # Write data to CSV
            with open(csv_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data_to_write)

            print("Data written to CSV:")
            print(data_to_write)
            print()
