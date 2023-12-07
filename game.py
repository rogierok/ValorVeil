import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Valor veil")
clock = pygame.time.Clock()
running = True
dt = 0

inventory = []

rockhealth = 6
rock = pygame.image.load('rock.png')

treehealth = 6
tree = pygame.image.load('tree.png')

spriteUp    = pygame.image.load('man/top1.png')
spriteDown  = pygame.image.load('man/bottom1.png')
spriteLeft  = pygame.image.load('man/left1.png')
spriteRight = pygame.image.load('man/right1.png')
    
swordUp    = pygame.image.load('man/swordtop1.png')
swordDown  = pygame.image.load('man/swordbottom1.png')
swordLeft  = pygame.image.load('man/swordleft1.png')
swordRight = pygame.image.load('man/swordright1.png')

bg_music = pygame.mixer.Sound('audio/valor.wav') 
bg_music.play(loops = -1)

bg_music.set_volume(0.2)

hitsound = pygame.mixer.Sound('audio/punch-140236.mp3') 

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    background_image = pygame.image.load('grass.png')
    background_image = pygame.transform.scale(background_image, screen.get_size())
    screen.blit(background_image, (0, 0))

    character = spriteDown

    sword = swordDown

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
        character = spriteUp
        sword = swordUp
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
        character = spriteDown
        sword = swordDown
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
        character = spriteLeft
        sword = swordLeft
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        character = spriteRight
        sword = swordRight
    if keys[pygame.K_k] and "wood" in inventory and "stone" in inventory:
        inventory.append("sword")
        inventory.remove("wood")
        inventory.remove("stone")
        print(inventory)

    if event.type == pygame.MOUSEBUTTONDOWN:
        mousePos = pygame.mouse.get_pos()
        print(mousePos)
        if tree.get_rect(topleft=(160, 320)).collidepoint(mousePos) and treehealth > 0:
            treehealth = treehealth - 1
            hitsound.play()
            tree.set_alpha(125)
            print(treehealth)
            if treehealth == 0:
                tree = pygame.image.load('treekapot.png')
                tree.set_alpha(255)
                inventory.append("wood")
                print(inventory)

        if rock.get_rect(topleft=(440, 120)).collidepoint(mousePos) and rockhealth > 0:
            rockhealth = rockhealth - 1
            hitsound.play()
            rock.set_alpha(125)
            print(rockhealth)
            if rockhealth == 0:
                rock = pygame.image.load('rockkapot.png')
                rock.set_alpha(255)
                inventory.append("stone")
                print(inventory)
        
    screen.blit(rock, (440, 120))
    screen.blit(tree, (160, 320))
    screen.blit(character, (player_pos))

    if "sword" in inventory:
         screen.blit(sword, (player_pos))

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()