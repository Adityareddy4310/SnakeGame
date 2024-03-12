import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        # Initialize the game window
        self.master = master
        self.master.title("Snake Game")
        self.master.resizable(False, False)
        # Create a canvas for drawing the game elements
        self.canvas = tk.Canvas(master, width=400, height=400, bg="black")
        self.canvas.pack()
        # Initialize snake and food positions, direction, and score
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.create_food()
        self.direction = "Right"
        self.score = 0
        # Draw the initial snake and food
        self.draw_snake()
        self.draw_food()
        # Bind arrow keys to change snake direction
        self.master.bind("<Key>", self.change_direction)
        # Start the game loop
        self.move()

    def draw_snake(self):
        # Draw the snake on the canvas
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + 20, y + 20, fill="green", tags="snake")

    def draw_food(self):
        # Draw the food on the canvas
        self.canvas.delete("food")
        x, y = self.food
        self.canvas.create_oval(x, y, x + 20, y + 20, fill="red", tags="food")

    def create_food(self):
        # Generate random food position
        x = random.randint(0, 19) * 20
        y = random.randint(0, 19) * 20
        return x, y

    def change_direction(self, event):
        # Change snake direction based on arrow key pressed
        key = event.keysym
        if key in ["Left", "Right", "Up", "Down"]:
            if (key == "Left" and self.direction != "Right") or \
               (key == "Right" and self.direction != "Left") or \
               (key == "Up" and self.direction != "Down") or \
               (key == "Down" and self.direction != "Up"):
                self.direction = key

    def move(self):
        # Move the snake in the current direction
        head = self.snake[0]
        if self.direction == "Left":
            new_head = (head[0] - 20, head[1])
        elif self.direction == "Right":
            new_head = (head[0] + 20, head[1])
        elif self.direction == "Up":
            new_head = (head[0], head[1] - 20)
        elif self.direction == "Down":
            new_head = (head[0], head[1] + 20)

        # Check if snake eats food or collides with itself or border
        if new_head == self.food:
            self.score += 1
            self.snake.insert(0, new_head)
            self.draw_food()
        else:
            self.snake.pop()
            self.snake.insert(0, new_head)
        
        self.draw_snake()

        # Check if game over condition is met
        if (new_head[0] < 0 or new_head[0] >= 400 or
            new_head[1] < 0 or new_head[1] >= 400 or
            len(set(self.snake)) != len(self.snake)):
            self.game_over()
            return

        # Continue the game loop
        self.master.after(100, self.move)

    def game_over(self):
        # Display game over message and final score
        self.canvas.delete("all")
        self.canvas.create_text(200, 200, text=f"Game Over\nScore: {self.score}", fill="white", font=("Helvetica", 20), justify="center")

def main():
    # Create the game window and start the game
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
