#name
name = input("Input you name: ")
print("Hello, " + name)

#task 1:CHANGE CALCULATOR

amount = int(input("Enter amount in pesos: "))

pesos100 = amount // 100
amount = amount % 100

pesos20 = amount // 20
amount = amount % 20

pesos5 = amount // 5
amount = amount % 5

pesos = amount // 1
amount = amount % 1

print("100 pesos:", pesos100)
print("20 pesos:", pesos20)
print("5 pesos:", pesos5)
print("1 peso:", pesos)