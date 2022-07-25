import os
import pygame

def Substring(string: str, start: int, end: int):
    return string[start:end]

def Main():
    pygame.init()
    loaded = False
    searched = False
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Wikipydia 0.1.1")
    clock = pygame.time.Clock()
    page = "main-page"
    leInput = ""
    margin = 7
    border = 3
    scrollspeed = 2
    (x,y) = (0,0)

    headerFont = pygame.font.Font("data/Roboto-Bold.ttf", 40)
    searchFont = pygame.font.Font("data/Roboto-Italic.ttf", 20)
    bodyFont = pygame.font.Font("data/Roboto-Regular.ttf", 14)
    
    while True:
        mousePos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        

        screen.fill((255, 255, 255))

        try:
            open("data/pages/" + page + ".wikipy", "r")
        except FileNotFoundError:
            print("Page not found: " + leInput)
            page = "main-page"

        with open("data/pages/" + page + ".wikipy", "r") as f:
            text = f.read().split("\n")
            title = headerFont.render(text[0], True, (15, 15, 15))
            screen.blit(title, (x+margin, y+margin))

            for line in range(1, len(text)):
                body = bodyFont.render(text[line], True, (31,31,31))
                screen.blit(body, (x+margin, y+(margin * line * 3) + title.get_height()))

            pygame.draw.rect(screen, (171, 171, 171), (800 - 100 - margin, margin, 100, 50))
            pygame.draw.rect(screen, (207, 207, 207), (800 - 100 - margin + border, margin + border, 100 - (border*2), 50 - (border*2)))
            search = searchFont.render("Search", True, (63, 63, 63))
            screen.blit(search, (800 - 100 - margin + (100 - search.get_width()) / 2, margin + (50 - search.get_height()) / 2))

            searched = False

        # If the search button is pressed, input("Search for page: ")
        # and set page to that page
        # If the page is not found, print "Page not found"
        if mousePos[0] > 800 - 100 - margin and mousePos[0] < 800 - margin and mousePos[1] > margin and mousePos[1] < margin + 50:
            if click[0] and not searched:
                searched = True
                leInput = input("Search: ")

                if leInput.replace(" ", "") != "":
                    page = leInput.lower().replace(" ", "-")
                    loaded = False

        # Scrolling using arrow keys
        if keys[pygame.K_UP]:
            y -= scrollspeed
        if keys[pygame.K_DOWN]:
            y += scrollspeed
        if keys[pygame.K_LEFT]:
            x -= scrollspeed
        if keys[pygame.K_RIGHT]:
            x += scrollspeed
        if keys[pygame.K_HOME]:
            x = 0
            y = 0

        pygame.display.update()
        clock.tick(60)
Main()