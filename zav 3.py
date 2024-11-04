start = int(input("Vvedit pochatok diapasonu: "))
end = int(input("Vvedit kinets diapasonu: "))
for i in range(start,end+1):
    print(f"table of {i}")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print()