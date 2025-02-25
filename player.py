from circleshape import *
from constants import (
    PLAYER_RADIUS, 
    PLAYER_SPEED, 
    PLAYER_TURN_SPEED,
    PLAYER_SHOT_SPEED,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SHOT_RADIUS,
    PLAYER_SHOT_COOLDOWN
)
import pygame


class Player(CircleShape): 
    

    def __init__(self, x, y, PLAYER_RADIUS):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        super().draw(screen)    
        pygame.draw.polygon(screen, color=255, points=self.triangle(), width=2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt   
    
    def shoot(self):
        
        if self.timer <= 0:
            self.timer = PLAYER_SHOT_COOLDOWN
            velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED       
            Shot(self.position.x, self.position.y, SHOT_RADIUS, velocity)
        
        



class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x,self.position.y) , self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
        if (self.position.x < 0 or 
            self.position.x > SCREEN_WIDTH or 
            self.position.y < 0 or 
            self.position.y > SCREEN_HEIGHT):
            self.kill()