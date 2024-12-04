import generatePatterns
def isRelevantPosition(i: int, j: int) -> bool:
    return ( 
        (i == 0 and j == 0) or
        (i == 0 and j == 2) or
        (i == 2 and j == 0) or
        (i == 2 and j == 2) or
        (i == 1 and j == 1)
    )

def isPatternMatch(grid, x: int, y: int, pattern: list) -> bool:
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            if isRelevantPosition(i, j):  # Relevante Positionen prüfen
                nx, ny = x + i, y + j
                # Sicherstellen, dass der Index im Grid liegt und das Muster passt
                if nx >= len(grid) or ny >= len(grid[0]) or (pattern[i][j] != '.' and pattern[i][j] != grid[nx][ny]):
                    return False
    return True


# Lade das Grid
with open("Dez04/input.txt", "r", encoding="utf-8") as dataIn:
    grid = [list(line) for line in dataIn.read().strip().split("\n")]

# Definiere das Muster
pattern: list = [
    ['M', '.', 'M'],
    ['.', 'A', '.'],
    ['S', '.', 'S']
]

patterns = generatePatterns.generateFunctions()
instances: list = []  # Liste zur Speicherung der Instanzen
counter: int = 0      # Zähler für die Instanzen

# Gehe durch alle Positionen im Grid und prüfe alle Muster
for x in range(len(grid) - len(pattern) + 1):
    for y in range(len(grid[0]) - len(pattern[0]) + 1):
        for p in patterns:
            if isPatternMatch(grid, x, y, p):
                counter += 1
                # Speichern der Instanz-Positionen (die relevanten Punkte)
                for i in range(len(p)):
                    for j in range(len(p[i])):
                        if isRelevantPosition(i, j):
                            instances.append((x + i, y + j))

# Setze markierte Instanzen
highlighted: list = [[False for _ in row] for row in grid]

# Markiere nur die relevanten Buchstaben der gefundenen Instanzen
for x, y in instances:
    highlighted[x][y] = True

# Ausgabe der Anzahl der gefundenen Instanzen
print(f"Anzahl der gefundenen Instanzen: {counter}")

# Ausgabe des Grids mit farbiger Markierung
for x in range(len(grid)):
    for y in range(len(grid[x])):
        if highlighted[x][y]:
            print(f"\033[32m{grid[x][y]}", end="")
        else:
            print(f"\033[31m{grid[x][y]}", end="")
    print("\033[0m")
print(counter)