import random
import string

width = 15
height = 15

words = []

def create_grid(width, height):
    """Create a grid filled with random letters."""
    return [[" " for _ in range(width)] for _ in range(height)]

def print_grid(grid):
    """Print the grid."""
    for row in grid:
        print(' '.join(row))

def can_place_word(grid, word, x, y, direction):
    """Check if a word can be placed on the grid at a specific position and direction."""
    dx, dy = direction
    for i in range(len(word)):
        nx, ny = x + dx * i, y + dy * i
        if grid[nx][ny] != ' ' and grid[nx][ny] != word[i]:
            return False
    return True

def place_word(grid, word, x, y, direction):
    """Place a word on the grid at a specific position and direction."""
    dx, dy = direction
    for i in range(len(word)):
        nx, ny = x + dx * i, y + dy * i
        grid[nx][ny] = word[i]

def maker(words):
    grid = create_grid(width, height)

    newwords = [word[::-1] if random.choice([True, False, False]) else word for word in words]
    for word in newwords:
        placed = False
        while not placed:
            direction = random.choice([[1, 0], [0, 1], [1, 1]])
            xstart = width if direction[0] == 0 else width - len(word)
            ystart = height if direction[1] == 0 else height - len(word)

            x = random.randrange(0, xstart)
            y = random.randrange(0, ystart)
            
            if can_place_word(grid, word, x, y, direction):
                place_word(grid, word, x, y, direction)
                placed = True
    for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == " ":
                    grid[i][j] = random.choice(string.ascii_letters)
    print_grid(grid)

ready = False
width = int(input("Enter the width: "))
height = int(input("Enter the height: "))
while not ready: 
    toadd = str(input("Enter a word: "))
    words.append(toadd)
    isdone = int(input("1. to add a new word, 2. to generate the word search"))
    if isdone == 2:
        ready = True

maker(words)

