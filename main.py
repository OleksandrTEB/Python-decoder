# code = " #90190200739023005290820032339332002141317131410011531173115100017393710001903290610001903190710001903290610011529043410021529013510032490352005290820073902300901902"

code = input("Enter your code: ")

i = 2

firstChar = code[0]
secondChar = code[1]

currentChar = 0

while i < len(code):
    if int(code[i]) == 0 and int(code[i + 1]) == 0:
        print()
        i += 2
        continue

    if currentChar == 0:
        j = 0
        while j < int(code[i]):
            print(firstChar, end="")
            j += 1
        currentChar = 1
    else:
        k = 0
        while k < int(code[i]):
            print(secondChar, end="")
            k += 1
        currentChar = 0
    i += 1