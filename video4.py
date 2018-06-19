from moviepy.editor import *
import pygame

pygame.display.set_caption('choice 1')

clip = VideoFileClip('video4.mp4')
clip.preview()

pygame.quit()
