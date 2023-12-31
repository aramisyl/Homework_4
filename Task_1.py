a = ["a", "b", "c"]
b = [1, 2, 3]
c = ["%", "$", "@"]

for item in list(zip(a,b,c)):
    print(item)