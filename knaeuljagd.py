import pygame
import random


class Katze(pygame.sprite.Sprite):
    def __init__(self, F_BREITE, F_HOEHE):
        super().__init__()
        self.F_BREITE = F_BREITE
        self.F_HOEHE = F_HOEHE
        self.image = pygame.image.load("katze.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.F_BREITE / 2, self.F_HOEHE / 2)
        self.punkte = 0
        self.leben = 7

    def update(self):
        gedrueckt = pygame.key.get_pressed()
        if gedrueckt[pygame.K_UP]:
            self.rect.y -= 8
        if gedrueckt[pygame.K_DOWN]:
            self.rect.y += 8
        if gedrueckt[pygame.K_LEFT]:
            self.rect.x -= 8
        if gedrueckt[pygame.K_RIGHT]:
            self.rect.x += 8
        self.rect.clamp_ip(pygame.Rect(0, 0, self.F_BREITE, self.F_HOEHE))


class ZufallsObjekt(pygame.sprite.Sprite):
    maus = pygame.image.load("maus.png")
    falter = pygame.image.load("falter.png")
    knaeul = pygame.image.load("knaeul.png")
    wasser = pygame.image.load("wasser.png")
    laerm = pygame.image.load("laerm.png")
    hund = pygame.image.load("hund.png")
    bilder_top = [[maus,2], [falter,1], [knaeul,3]]
    bilder_flop = [[wasser,-5], [laerm,-10], [hund,-15]]

    def __init__(self, F_BREITE, F_HOEHE):
        super().__init__()
        self.F_BREITE = F_BREITE
        self.F_HOEHE = F_HOEHE

        self.gut = random.choice((True, False))

        if self.gut:
            objekt = random.choice(ZufallsObjekt.bilder_top)
            self.image = objekt[0]
            self.value = objekt[1]
        else:
            objekt = random.choice(ZufallsObjekt.bilder_flop)
            self.image = objekt[0]
            self.value = objekt[1]

        self.rect = self.image.get_rect()

        self.rect.center = (random.randint(0, self.F_BREITE),
                            random.randint(-self.F_HOEHE, -self.rect.height))

        self.x_speed = random.randint(-2, 2)
        self.y_speed = random.randint(1, 5)

    def update(self):
        if self.rect.top > self.F_HOEHE:
            self.kill()
        else:
            self.rect.x += self.x_speed
            self.rect.y += self.y_speed
            if random.randint(0, 120) == 0:
                self.x_speed = random.randint(-2, 2)


def text(text, fenster, position, groesse):
    font = pygame.font.SysFont('arial', groesse)
    text = font.render(text, False, (0, 0, 0))
    F_BREITE = text.get_rect().width
    fenster.blit(text, (position[0] - (F_BREITE / 2), position[1]))
