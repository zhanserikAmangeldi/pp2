import pygame

pygame.init()
clock = pygame.time.Clock()
img = pygame.image.load('img/air.png')
angular = 0
screen = pygame.display.set_mode((300,300))
w, h = img.get_size()
def rotate():
    global img
    global angular
    image_rect = img.get_rect(topleft = (screen.get_width()/2 - w/2, screen.get_height()/2- h/2))
    offset_center_to_pivot = pygame.math.Vector2((screen.get_width()/2, screen.get_height()/2)) - image_rect.center
    
    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angular)

    # roatetd image center
    rotated_image_center = (screen.get_width()/2 - rotated_offset.x, screen.get_height()/2 - rotated_offset.y)
    
    rotate_image = pygame.transform.rotate(img, angular)
    rotated_image_rect = rotate_image.get_rect(center = rotated_image_center)
    screen.blit(rotate_image, rotated_image_rect)





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0,0,0))
    rotate()
    angular -= 1

    pygame.display.flip()
    clock.tick(60)