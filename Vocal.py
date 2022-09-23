x = (input(""))

vocal = ["a","i","u","e","o","A","I","U","E","O"]
result = ""

for i in x:
    if i not in vocal:
        result += i

print("Result : ", result)
