# Automatic Plant Watering using Python

def automatic_watering(soil_moisture):
print("\n===== AUTOMATIC PLANT WATERING =====")
print(f"Soil Moisture: {soil_moisture}%")

```
if soil_moisture < 30:
    print("Soil Status: DRY")
    print("Water Pump: ON")
    print("Watering the plant...")

elif soil_moisture <= 60:
    print("Soil Status: MODERATE")
    print("Water Pump: OFF")
    print("Continue monitoring the soil.")

else:
    print("Soil Status: WET")
    print("Water Pump: OFF")
    print("No watering required.")
```

while True:
print("\n===== AUTOMATIC PLANT WATERING SYSTEM =====")
print("1. Check Soil Moisture")
print("2. Exit")

```
choice = input("Enter your choice: ")

if choice == "1":
    try:
        moisture = float(
            input("Enter soil moisture (0-100%): ")
        )

        if 0 <= moisture <= 100:
            automatic_watering(moisture)
        else:
            print("Please enter a value between 0 and 100.")

    except ValueError:
        print("Invalid input! Enter a number.")

elif choice == "2":
    print("Automatic Plant Watering System Closed.")
    break

else:
    print("Invalid choice! Please try again.")
```
