def generateFunctions():
    # Define the original pattern
    original_pattern = [
        ['M', '.', 'M'],
        ['.', 'A', '.'],
        ['S', '.', 'S']
    ]

    # Function to rotate the pattern 90 degrees clockwise
    def rotate_90(pattern):
        return [list(row) for row in zip(*pattern[::-1])]

    # Function to flip the pattern horizontally
    def flip_horizontal(pattern):
        return [row[::-1] for row in pattern]

    # Function to flip the pattern vertically
    def flip_vertical(pattern):
        return pattern[::-1]

    # Create a list to store all the variations
    patterns = [
        original_pattern,                            # Original
        flip_horizontal(original_pattern),           # Horizontal Flip
        flip_vertical(original_pattern),             # Vertical Flip
        rotate_90(original_pattern),                 # Rotate 90 degrees
        rotate_90(flip_horizontal(original_pattern)), # Rotate 90 degrees after horizontal flip
        rotate_90(flip_vertical(original_pattern)),   # Rotate 90 degrees after vertical flip
        rotate_90(flip_horizontal(flip_vertical(original_pattern))), # Rotate 90 degrees after both flips
    ]


    res = []
    [res.append(val) for val in patterns if val not in res]

    # Print all variations
    for idx, pattern in enumerate(res):
        print(f"Pattern {idx + 1}:")
        for row in pattern:
            print(row)
        print()
    return(res)

if __name__ == "__main__":
    generateFunctions()