import sys
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    AsteroidField()
    player = Player(x = (SCREEN_WIDTH / 2), y = (SCREEN_HEIGHT / 2))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collide_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000.0
   
#    print("Starting Asteroids with pygame version: " + pygame.version.ver)
#   print(f"Screen width: {SCREEN_WIDTH} Screen height: {SCREEN_HEIGHT}")
    
if __name__ == "__main__":
    main()
