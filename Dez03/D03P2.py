def isLegalSubstring(c: str, legalChars: str = "0123456789,") -> bool:
    for i in c: 
        if i not in legalChars: 
            return False
    return True

def removeSections(t: str) -> str:
    inKey: str = "don't()" ; outKey: str = "do()"

    while True:
        sIdx = t.find(inKey)
        if sIdx == -1: break  # No more "don't()" markers

        eIdx = t.find(outKey, sIdx + len(inKey))
        if eIdx == -1: break  # No "do()" marker after "don't()"

        t = t[:sIdx] + t[eIdx + len(outKey):]
    return t


with open("Dez03/input.txt", "r", encoding="utf-8") as dataIn:
    data = dataIn.read()

data = removeSections(data).split("mul")
mul: list = []

for i in data: 
    if i.startswith("(") and ")" in i:
        tmp = i.index(")")
        if isLegalSubstring(i[1:tmp]):
            mul.append(i[1:tmp].split(","))

counter: int = 0

for i in mul:
    if len(i) == 2:
        i[0], i[1] = int(i[0]), int(i[1])
        if 1 <= len(str(i[0])) <= 3 and 1 <= len(str(i[1])) <= 3:
            counter += i[0] * i[1]
            print(f"{i}: {i[0]} * {i[1]} = {i[0]*i[1]}  -  Total: {counter}")
        else:
            print(f"{i} segment illegal: Number length out of range.")

print(counter)
