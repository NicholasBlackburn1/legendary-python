from moviepy.editor import *
import pygame

pygame.display.set_caption('choice 1')

clip = VideoFileClip('video2.mp4')
clip.preview()

pygame.quit()
