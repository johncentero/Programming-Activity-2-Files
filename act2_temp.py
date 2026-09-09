#name
name = input("Input you name: ")
print("Hello, " + name)

#task 4: TEMPERATURE CHECK

celsius = float(input("Enter temperature in °C: "))
fahrenheit = celsius * 9 / 5 + 32

print(f"Fahrenheit: {fahrenheit}")
print(f"Between 20 and 30 °C: {20 <= celsius <= 30}")

