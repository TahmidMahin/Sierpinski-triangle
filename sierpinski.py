import pygame as pg
import math

pg.init()

black = (0, 0, 0)
white = (255, 255, 255)

width = 1000
height = 1000

screen = pg.display.set_mode((width, height))

font = pg.font.SysFont('Liberation Serif', 32, False, False)

pg.display.set_caption("Sierpinski Traingle")

running = True
t_level = 1

def draw_triangle(x, y, a):
	points = ((round(x - a/2), round(y - a/(2*math.sqrt(3)))), (round(x + a/2), round(y - a/(2*math.sqrt(3)))), (round(x), round(y + a/math.sqrt(3))))
	pg.draw.polygon(screen, white, points, 1)

def triangle_level(x, y, a, level):
	draw_triangle(x, y, a)
	if level == 1:
		return
	triangle_level(x, y - a/math.sqrt(3), a/2, level - 1)
	triangle_level(x - a/2, y + a/(2*math.sqrt(3)), a/2, level -1)
	triangle_level(x + a/2, y + a/(2*math.sqrt(3)), a/2, level -1)

while running:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_UP:
				if t_level < 10:
					t_level = t_level + 1
			if event.key == pg.K_DOWN:
				if t_level > 1:
					t_level = t_level - 1

	screen.fill(black)
	text = font.render("Level = " + str(t_level), False, white, black)
	screen.blit(text, (10, 10))
	triangle_level(width/2, height/2, 400, t_level)
	pg.display.update()
