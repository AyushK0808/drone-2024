import pandas as pd
import matplotlib.pyplot as plt
import ast

# Load the data from the CSV file
file_path = 'sensor_data.csv'  # Replace with the correct path to your file
data = pd.read_csv(file_path)

# Convert the 'Date' column to datetime for better plotting
data['Date'] = pd.to_datetime(data['Date'])

# Parse accelerometer and gyroscope data from string to dictionary
data['Accelerometer'] = data['Accelerometer'].apply(ast.literal_eval)
data['Gyroscope'] = data['Gyroscope'].apply(ast.literal_eval)

# Extract x, y, z components for accelerometer and gyroscope
data['Accel_X'] = data['Accelerometer'].apply(lambda d: d['x'])
data['Accel_Y'] = data['Accelerometer'].apply(lambda d: d['y'])
data['Accel_Z'] = data['Accelerometer'].apply(lambda d: d['z'])
data['Gyro_X'] = data['Gyroscope'].apply(lambda d: d['x'])
data['Gyro_Y'] = data['Gyroscope'].apply(lambda d: d['y'])
data['Gyro_Z'] = data['Gyroscope'].apply(lambda d: d['z'])

# Plot Temperature, Humidity, Pressure, Magnetometer, Accelerometer, and Gyroscope data
plt.figure(figsize=(16, 12))

# Temperature
plt.subplot(3, 2, 1)
plt.plot(data['Date'], data['Temperature (°C)'], label='Temperature (°C)', linewidth=1.5)
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.grid(True)
plt.legend()

# Humidity
plt.subplot(3, 2, 2)
plt.plot(data['Date'], data['Humidity (%)'], label='Humidity (%)', color='orange', linewidth=1.5)
plt.xlabel('Time')
plt.ylabel('Humidity (%)')
plt.title('Humidity Over Time')
plt.grid(True)
plt.legend()

# Pressure
plt.subplot(3, 2, 3)
plt.plot(data['Date'], data['Pressure (hPa)'], label='Pressure (hPa)', color='green', linewidth=1.5)
plt.xlabel('Time')
plt.ylabel('Pressure (hPa)')
plt.title('Pressure Over Time')
plt.grid(True)
plt.legend()

# Magnetometer
plt.subplot(3, 2, 4)
plt.plot(data['Date'], data['Magnetometer'], label='Magnetometer', color='red', linewidth=1.5)
plt.xlabel('Time')
plt.ylabel('Magnetometer')
plt.title('Magnetometer Over Time')
plt.grid(True)
plt.legend()

# Accelerometer
plt.subplot(3, 2, 5)
plt.plot(data['Date'], data['Accel_X'], label='Accel_X', linewidth=1.5)
plt.plot(data['Date'], data['Accel_Y'], label='Accel_Y', linewidth=1.5)
plt.plot(data['Date'], data['Accel_Z'], label='Accel_Z', linewidth=1.5)
plt.xlabel('Time')
plt.ylabel('Acceleration (g)')
plt.title('Accelerometer Over Time')
plt.grid(True)
plt.legend()

# Gyroscope
plt.subplot(3, 2, 6)
plt.plot(data['Date'], data['Gyro_X'], label='Gyro_X', linewidth=1.5)
plt.plot(data['Date'], data['Gyro_Y'], label='Gyro_Y', linewidth=1.5)
plt.plot(data['Date'], data['Gyro_Z'], label='Gyro_Z', linewidth=1.5)
plt.xlabel('Time')
plt.ylabel('Angular Velocity (°/s)')
plt.title('Gyroscope Over Time')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
