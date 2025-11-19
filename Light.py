from gpiozero import InputDevice
import time
import csv
import matplotlib.pyplot as plt

light = InputDevice(26)
light_data= []

with open ("/home/pi/light_data.csv", mode= "w", newline= "") as file:
    writer = csv.writer(file)
    writer.writerow(["Time (s)", "Light Detected"])
   
    for i in range(30):
        if light.is_active:
            led.off()
            light_data.append (1)
        else:
           light_data.append(0)
           time.sleep(1)

plt.plot(light_data)
plt.title("Light Level Over Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Light Intensity (%)")
plt.show()