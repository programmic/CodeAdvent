def gridSearch(g, w):
    rows = len(g)
    cols = len(g[0])
    word_len = len(w)
    instances = []  # Liste für Positionen gefundener Wörter

    # Funktion zum Prüfen einer Richtung
    def checkDir(x, y, dx, dy):
        positions = []  # Speichert Positionen der Buchstaben des Wortes
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or g[nx][ny] != w[i]:
                return None
            positions.append((nx, ny))
        return positions

    # Richtungen: R, D, DR, DL, L, U, UL, UR
    directions = [
        (0, 1),   # R
        (1, 0),   # D
        (1, 1),   # DR
        (1, -1),  # DL
        (0, -1),  # L
        (-1, 0),  # U
        (-1, -1), # UL
        (-1, 1),  # UR
    ]

    # Über alle Positionen im Grid iterieren
    for x in range(rows):
        for y in range(cols):
            if g[x][y] == w[0]:  # Erstes Zeichen passt
                for dx, dy in directions:
                    positions = checkDir(x, y, dx, dy)
                    if positions:
                        instances.append(positions)

    return instances

def readFileToGrid(path: str) -> list:
    with open(path, "r", encoding="utf-8") as dataIn:
        data = dataIn.read().strip().split("\n")
        grid = [list(line) for line in data]
    return grid

# Beispiel
grid = readFileToGrid("Dez04/input.txt")

word = "XMAS"
instances = gridSearch(grid, word)
print(f"'{word}' gefunden: {len(instances)} Mal\n")

# Markiertes Grid ausgeben
highlighted = [[False for _ in row] for row in grid]  # Tracking für grüne Buchstaben

# Markiere gefundene Buchstaben
for instance in instances:
    for x, y in instance:
        highlighted[x][y] = True

# Grid anzeigen
for x, row in enumerate(grid):
    for y, char in enumerate(row):
        if highlighted[x][y]:  # Markierter Buchstabe
            print(f"\033[32m{char}", end="")
        else:  # Nicht markierter Buchstabe
            print(f"\033[31m{char}", end="")
    print("\033[0m")  # Reset nach jeder Zeile
