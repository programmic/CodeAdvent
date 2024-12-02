with open( "Dez02/input.txt", "r", encoding = "utf-8" ) as dataIn:
    tmpData = dataIn.read( ).split( "\n" )
data = []
for cnt in tmpData: data.append([int("".join(n)) for n in cnt.split(" ")])


def isLegal(input: list) -> bool:
    lastDigit = None
    increasing: bool = False
    if input[0] < input[1]:
        increasing = True
    for i in input:
        if not lastDigit == None:
            if i == lastDigit:
                print(f"X {input} two equal characters found: {i}")
                return False
            if abs ( i - lastDigit ) > 3:
                print(f"X {input} value difference too high: {lastDigit} | {i}")
                return False
            if increasing:
                if i < lastDigit:
                    print(f"X {input} value breaking tendency: {lastDigit} | {i}")
                    return False
            else:
                if i > lastDigit:
                    print(f"X {input} value breaking tendency: {lastDigit} | {i}")
                    return False
        lastDigit = i
    print(f"  {input}")
    return True

c: int = 0
for n in data:
    tmpC = 0
    for idx in range(len(n)):
        if isLegal( n[:idx] + n[idx + 1:] ): tmpC += 1

    if tmpC >= 1: c += 1 ; print(f"\033[1;32m{'#'*15}  -  {c}  -  {'#'*15}\033[0;0m")
    else:                 print(f"\033[1;31m{'#'*15}  -  {c}  -  {'#'*15}\033[0;0m")
