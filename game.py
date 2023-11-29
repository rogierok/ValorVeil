import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
running = True
dt = 0

inventory = []

campfireinv = []

playerpos = []

rockhealth = 1
rock = pygame.image.load('rock.png')

treehealth = 1
tree = pygame.image.load('tree.png')

campfire = pygame.image.load('campfire.png')

def my_function():
        screen.blit(campfire, (100, 100))

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bg_music = pygame.mixer.Sound('audio/valor.wav') 
    bg_music.play(loops = -1)

    background_image = pygame.image.load('grass.png').convert()
    background_image = pygame.transform.scale(background_image, screen.get_size())
    screen.blit(background_image, (0, 0))
    
    
    spriteUp    = pygame.image.load('man/top1.png')
    spriteDown  = pygame.image.load('man/bottom1.png')
    spriteLeft  = pygame.image.load('man/left1.png')
    spriteRight = pygame.image.load('man/right1.png')

    character = spriteDown

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
        character = spriteUp
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
        character = spriteDown
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
        character = spriteLeft
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        character = spriteRight
    if keys[pygame.K_k] and "wood" in inventory and "stone" in inventory:
        campfireinv.append("campfire")
        playerpos.append(player_pos)


    if "campfire" in campfireinv:
         screen.blit(campfire, (200, 200))

    if event.type == pygame.MOUSEBUTTONDOWN:
        mousePos = pygame.mouse.get_pos()
        print(mousePos)
        if tree.get_rect(topleft=(160, 320)).collidepoint(mousePos):
            treehealth = treehealth - 1
            print(treehealth)
            if treehealth == 0:
                tree = pygame.image.load('treekapot.png')
                inventory.append("wood")
                print(inventory)

        if rock.get_rect(topleft=(440, 120)).collidepoint(mousePos):
            rockhealth = rockhealth - 1
            print(rockhealth)
            if rockhealth == 0:
                rock = pygame.image.load('rockkapot.png')
                inventory.append("stone")
                print(inventory)
            
    
    screen.blit(rock, (440, 120))
    screen.blit(tree, (160, 320))
    screen.blit(character, (player_pos))

    

    pygame.display.flip()

    dt = clock.tick(120) / 1000

pygame.quit()