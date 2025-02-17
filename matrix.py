import random
import string
import sys
from PIL import Image, ImageDraw, ImageFont

class Matrix:
    def __init__(self, size: int):
        """Initializes an NxN matrix with random capitalized English letters."""
        self.size = size
        self.matrix = [[random.choice(string.ascii_uppercase) for _ in range(size)] for _ in range(size)]
    
    def print_matrix(self):
        """Prints the matrix in a formatted way."""
        for row in self.matrix:
            print(" ".join(row))
    
    def save_as_image(self, filename="matrix.png", cell_size=50):
        """Saves the matrix as a PNG image using PIL."""
        img_size = self.size * cell_size
        image = Image.new("RGB", (img_size, img_size), "white")
        draw = ImageDraw.Draw(image)
        
        try:
            font = ImageFont.truetype("arial.ttf", cell_size // 2)
        except IOError:
            font = ImageFont.load_default()
        
        for i, row in enumerate(self.matrix):
            for j, char in enumerate(row):
                x = j * cell_size + cell_size // 4
                y = i * cell_size + cell_size // 4
                draw.text((x, y), char, fill="black", font=font)
        
        image.save(filename)

# Example usage
if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except ValueError:
            print("Please provide a valid integer for matrix size.")
            sys.exit(1)
    else:
        n = 5  # Default size if no argument is given
    
    matrix = Matrix(n)
    matrix.print_matrix()
    matrix.save_as_image(filename="tmp/matrix.png")
