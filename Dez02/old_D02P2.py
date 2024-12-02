with open( "Dez02/sampleinput.txt", "r", encoding = "utf-8" ) as dataIn:
    tmpData = dataIn.read( ).split( "\n" )
data = []
for i in tmpData: data.append([int("".join(n)) for n in i.split(" ")])

def test(input: list) -> bool:
    lastDigit = None
    increasing: bool = False
    error = False
    if input[0] < input[1]:
        increasing = True
    for i in input:
        if not lastDigit == None:
            if i == lastDigit:
                if not error: error = True
                else:
                    print(f"X {n} two equal characters found: {i}")
                    return False
            if abs ( i - lastDigit ) > 3:
                if not error: error = True
                else:
                    print(f"X {n} value difference too high: {lastDigit} | {i}")
                    return False
            if increasing and i < lastDigit:
                if not error: error = True
                else:
                    print(f"X {n} value breaking tendency: {lastDigit} | {i}")
                    return False
            if not increasing and i > lastDigit:
                if not error: error = True
                else:
                    print(f"X {n} value breaking tendency: {lastDigit} | {i}")
                    return False
        lastDigit = i
    print(f"  {n}")
    return True

c: int = 0

for n in data:
    if test(n): c += 1
print(f"  {c}")