start = int(input("Vvedit pochatok diapasonu: "))
end = int(input("Vvedit kinets diapasonu: "))

print("prosti chisla v diapasoni:", end=" ")

for number in range(start, end + 1):
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                break
        else:
            print(number, end=" ")
