import numpy as np
import pygame
from environment import Environment

def main():
    # Define the grid size and obstacles
    grid_size = 10
    obstacles = [[1, 2], [2, 3], [3, 4]]

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("2D Obstacle Avoidance Car")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)

    # Function to draw the grid
    def draw_grid(state):
        block_size = 500 // grid_size
        for x in range(0, 500, block_size):
            for y in range(0, 500, block_size):
                rect = pygame.Rect(x, y, block_size, block_size)
                pygame.draw.rect(screen, WHITE, rect, 1)
                i, j = y // block_size, x // block_size
                if state[i, j] == -1:
                    pygame.draw.rect(screen, RED, rect)
                elif state[i, j] == 1:
                    pygame.draw.rect(screen, BLUE, rect)
                elif state[i, j] == 2:
                    pygame.draw.rect(screen, GREEN, rect)

    # Load the trained Q-table
    try:
        q_table = np.load('q_table.npy')
    except FileNotFoundError:
        print("Error: Q-table not found. Please run the training script first.")
        return

    # Create the environment
    env = Environment(grid_size, obstacles)

    # Main loop
    running = True
    state = env.reset()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        action = np.argmax(q_table[env.car_position[0], env.car_position[1]])
        next_state, reward, done = env.step(action)

        screen.fill(WHITE)
        draw_grid(env.get_state())
        pygame.display.flip()

        if done:
            state = env.reset()

    pygame.quit()

if __name__ == "__main__":
    main()
