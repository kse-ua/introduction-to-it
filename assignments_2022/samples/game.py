import random

import pgzrun
from pgzero.actor import Actor

from old.vector import Vector


class Spaceship:
    def __init__(self):
        self.actor = Actor('spaceship', center=(400, 400))
        self.velocity = Vector(0, 0)
        self.goal = Vector(0, 0)

    def draw(self):
        self.actor.draw()

    def position(self):
        return Vector(self.actor.x, self.actor.y)

    def look_at(self, pos):
        self.goal = Vector(pos[0], pos[1])
        self.actor.angle = self.actor.angle_to((pos[0] + self.velocity.x, pos[1] + self.velocity.y)) - 90

    def update(self, dt):
        position = Vector(self.actor.x, self.actor.y)
        desired = self.goal - position
        desired = desired.normalized() * 10
        self.velocity += desired
        if self.velocity.magnitude() > 150:
            self.velocity = self.velocity.normalized() * 150
        self.actor.x += self.velocity.x * dt
        self.actor.y += self.velocity.y * dt


class Asteroid:
    def __init__(self, pos: Vector):
        self.position = pos
        self.velocity = Vector(0, 100)
        self.goal = Vector(0, 0)

    def move(self, dt):
        self.position += self.velocity * dt

    def draw(self):
        screen.draw.filled_circle((self.position.x, self.position.y), 5, "yellow")

    def hits(self, spaceship:Spaceship):
        distance = (spaceship.position() - self.position).magnitude()
        return distance < 20


WIDTH = 800
HEIGHT = 800
points = 0

ship = Spaceship()
asteroids = []


def draw():
    screen.clear()
    ship.draw()
    screen.draw.text(f"points: {points}", (20, 20), color=(200, 200, 200))
    for asteroid in asteroids:
        asteroid.draw()


def update(dt):
    # move ship
    ship.update(dt)

    # spawn and move asteroid
    if random.random() < 0.05:
        asteroids.append(Asteroid(Vector(random.randint(0, WIDTH), -5)))
    for asteroid in asteroids:
        asteroid.move(dt)
        if asteroid.hits(ship):
            global points
            points += 1
            asteroids.remove(asteroid)


def on_mouse_move(pos):
    ship.look_at(pos)


pgzrun.go()
