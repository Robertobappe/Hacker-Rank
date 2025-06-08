n = int(input())
phoneBook = {}

for i in range(n):
    name,number = str(input()).split()
    phoneBook[name] = number

while True:
    try:
        nome = input()
        if nome in phoneBook:
            print(f"{nome}={phoneBook[nome]}")
        else:
            print('Not found')
    except EOFError:
        break

