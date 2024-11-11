# utils.py
import pygame
import os

# Function to draw text to the screen
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

# Function to load sounds
def load_sounds():
    menu_music = "../sounds/Cocoon.mp3"  # Music for menu
    game_music = "../sounds/GenerousPalmstroke.wav"  # Music for in-game
    brick_sound = pygame.mixer.Sound("../sounds/brick.wav")
    paddle_sound = pygame.mixer.Sound("../sounds/paddle.wav")
    wall_sound = pygame.mixer.Sound("../sounds/wall.wav")
    return menu_music, game_music, brick_sound, paddle_sound, wall_sound


def load_image(image_path, base_dir=None):
    """Loads an image from the given path, with an optional base directory."""
    try:
        # If no base directory is provided, use the current script's directory
        if base_dir is None:
            base_dir = os.path.dirname(__file__)

        # Make the path absolute by joining with the base directory
        image = pygame.image.load(os.path.join(base_dir, image_path))
        return image
    except pygame.error as e:
        print(f"Error loading image {image_path}: {e}")
        return None
