from moviepy.editor import *
import pygame

pygame.display.set_caption('choice 1')

clip = VideoFileClip('video1.mp4')
clip.preview()

pygame.quit()
