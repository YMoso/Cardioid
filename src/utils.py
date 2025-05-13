from src.points import Point
from config import config
import pygame
import numpy as np
import random
import colorsys


class Cardioid:
    def __init__(self):
        self.screen_resolution = config["screen_resolution"]
        self.total_points = config["total_points"]
        self.radius = config["radius"]
        self.center = (self.screen_resolution[0] // 2, self.screen_resolution[1] // 2)
        self.points: list[Point] = []
        self.multiplier = config["multiplier"]
        self.background = config["color_background"]
        self.frames = config["frames"]
        self.running = config["running"]
        if config["random_lines_color"]:
            self.lines_color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )
        else:
            self.lines_color = config["line_color"]
        self.points_on_circle()
        self.initialise()

    def points_on_circle(self):
        for i in range(self.total_points):
            angle = 2 * np.pi * i / self.total_points
            x = self.center[0] + self.radius * np.cos(angle + np.pi)
            y = self.center[1] + self.radius * np.sin(angle + np.pi)
            self.points.append(Point(x, y))

    def get_color(self, i, total):
        hue = i / total
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        return int(r * 255), int(g * 255), int(b * 255)

    def initialise(self):
        pygame.init()
        screen = pygame.display.set_mode(self.screen_resolution)
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.running = not self.running

            screen.fill(self.background)
            pygame.draw.circle(screen, self.background, self.center, self.radius, 1)

            for i in range(self.total_points):
                j = int((i * self.multiplier) % self.total_points)
                p1 = self.points[i]
                p2 = self.points[j]
                if config["random_lines_color"]:
                    color = self.get_color(i, self.total_points)
                else:
                    color = self.lines_color
                pygame.draw.line(screen, color, (p1.x, p1.y), (p2.x, p2.y), 1)

            pygame.display.flip()

            clock.tick(self.frames)
            if self.running:
                self.multiplier += 0.01

        pygame.quit()
