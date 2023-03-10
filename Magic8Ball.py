import pygame
import random

# Set up the window and font
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FONT_SIZE = 32
font = pygame.font.SysFont(None, FONT_SIZE)
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Bubble Sort Visualizer")

# Set up the array and variables
ARRAY_SIZE = 50
array = [random.randint(1, 100) for _ in range(ARRAY_SIZE)]
i = 0
j = 0
done = False

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# Draw the array on the screen
def draw_array():
    bar_width = WINDOW_WIDTH // ARRAY_SIZE
    bar_height_scale = (WINDOW_HEIGHT - FONT_SIZE) // max(array)
    for index, value in enumerate(array):
        bar_height = value * bar_height_scale
        bar_x = index * bar_width
        bar_y = WINDOW_HEIGHT - bar_height
        bar_color = WHITE if index != i and index != j else BLUE
        pygame.draw.rect(window, bar_color, (bar_x, bar_y, bar_width, bar_height))

# Draw the current step on the screen
def draw_step():
    text = font.render(f"Step {i * ARRAY_SIZE + j + 1}", True, BLACK)
    window.blit(text, (10, 10))
    pygame.display.update()

# Bubble Sort algorithm
def bubble_sort():
    global i, j, done
    if i == ARRAY_SIZE - 1:
        done = True
        return
    if j == ARRAY_SIZE - i - 1:
        i += 1
        j = 0
    if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]
    j += 1

# Main loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # Update the array and display
    bubble_sort()
    window.fill(GRAY)
    draw_array()
    draw_step()
    pygame.display.update()

pygame.quit()
