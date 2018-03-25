import sys, os, pygame, random
from pygame.locals import *

# Инициализируем переменные
# Начальное положение корабля
x_coord = 1
y_coord = 320
# Начальная скорость корабля
x_speed = 0
y_speed = 0
# Количество жизненной энергии корабля и очки
score = 1000
score1 = 0

def init_window():
    # Инициализируем pygame
    pygame.init()
    # Создаём игровое окно
    window = pygame.display.set_mode((500, 400))
    # Ставим свой заголовок окна
    pygame.display.set_caption('Космическое путешествие')


# Функция отображения картинок
def load_image(name, colorkey=None):
    # Добавляем к имени картинки имя папки
    fullname = os.path.join('Images', name)
    # Загружаем картинку
    image = pygame.image.load(fullname)
    image = image.convert()
    # Если второй параметр =-1 делаем прозрачным
    # цвет из точки 0,0
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def draw_background():
    # Получаем поверхность, на которой будем рисовать
    screen = pygame.display.get_surface()
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    # загружаем картинку космоса
    back, back_rect = load_image("sky_1.jpg")
    # и рисуем ее
    screen.blit(back, (0, 0))
    pygame.display.flip()
    return back


screen = pygame.display.set_mode((500, 400))
screen_rect = (0, 0, 500, 400)

class Spark(pygame.sprite.Sprite):
    # сгенерируем искры разного размера
    a, b = load_image("shine_1.png", -1)
    fire = [a]
    for scale in (5,10,20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        # у каждой искры своя скорость - это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой
        self.gravity = 1

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если искра ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()

def create_particles(position):
    # количество создаваемых искр
    spark_count = 1
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(spark_count):
        Spark(position, random.choice(numbers), random.choice(numbers))

all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()


# Класс описывающий летающие объекты
class Skything(pygame.sprite.Sprite):
    def __init__(self, img, cX, cY):
        # Создаем спрайт из картинки
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(img, -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        # Перемещаем картинку в её начальные координаты
        self.rect.x = cX
        self.rect.y = cY


# Создаём класс корабль, наследующийся от Skything
class Rocket(Skything):
    def __init__(self, cX, cY):
        Skything.__init__(self, "rocket.png", cX, cY)


# Создаём класс астероид, наследующийся от Skything
class Asteroid(Skything):
    def __init__(self, cX, cY):
        Skything.__init__(self, "asteroid.png", cX, cY)

# Создаём класс звезда, наследующийся от Skything
class Star(Skything):
    def __init__(self, cX, cY):
        Skything.__init__(self, "star1.png", cX, cY)


def input(events):
    global x_coord, y_coord, x_speed, y_speed, life, screen
    # Перехватываем нажатия клавиш на клавиатуре
    for event in events:
        if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit(0)
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -5
            if event.key == pygame.K_RIGHT:
                x_speed = 5
            if event.key == pygame.K_UP:
                y_speed = -5
            if event.key == pygame.K_DOWN:
                y_speed = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0

    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    if (x_coord < 0):
        x_coord = 0
    if (x_coord > 430):
        x_coord = 430
    if (y_coord < 0):
        y_coord = 0
    if (y_coord > 320):
        y_coord = 320


def action(bk):
    global x_coord, y_coord, score, score1, shag, go1, go2, go3, go4, go5, go6
    screen = pygame.display.get_surface()
    # Создаём корабль, звёзды и астероиды
    rocket = Rocket(1, 320)
    asteroid = Asteroid(500, 100)
    asteroid2 = Asteroid(800, 200)
    asteroid3 = Asteroid(1200, 350)
    star1 = Star(500, 150)
    star2 = Star(700, 300)
    star3 = Star(1000, 400)
    # Добавляем их в три массива
    asterow = []
    asterow.append(asteroid)
    asterow.append(asteroid2)
    asterow.append(asteroid3)
    air = []
    air.append(rocket)
    stars = []
    stars.append(star1)
    stars.append(star2)
    stars.append(star3)
    # Рисуем их
    asteroids = pygame.sprite.RenderPlain(asterow)
    rocket_ = pygame.sprite.RenderPlain(air)
    stars_ = pygame.sprite.RenderPlain(stars)
    timer = pygame.time.Clock()
    # Запускаем бесконечный цикл
    while 1:
        # Создаем паузу
        timer.tick(60)
        # Ждём нажатий клавиатуры
        input(pygame.event.get())
        # Проверяем столкновения
        blocks_hit_list = pygame.sprite.spritecollide(rocket, asteroids, False)
        # Если есть столкновения с метеоритами, уменьшаем жизнь
        if len(blocks_hit_list) > 0:
            score -= len(blocks_hit_list)
            create_particles((x_coord, y_coord))
            asteroids.draw(screen)
            rocket_.draw(screen)

        blocks_hit_list = pygame.sprite.spritecollide(rocket, stars_, False)
        # Если есть столкновения со звездами, увеличиваем очки
        if len(blocks_hit_list) > 0 and score > 0:
            score1 += len(blocks_hit_list)
            stars_.draw(screen)
            rocket_.draw(screen)
        # Обновляем координаты корабля
        rocket.rect.x = x_coord
        rocket.rect.y = y_coord
        # Изменяем положение астероидов и звезд
        asteroid.rect.x = asteroid.rect.x - 7
        asteroid2.rect.x = asteroid2.rect.x - 5
        asteroid3.rect.x = asteroid3.rect.x - 6
        star1.rect.x = star1.rect.x - 6
        star2.rect.x = star2.rect.x - 7
        star3.rect.x = star3.rect.x - 5
        if (asteroid.rect.x < -50):
            asteroid.rect.x = 500
            asteroid.rect.y = 10
        if (asteroid2.rect.x < -50):
            asteroid2.rect.x = 888
            asteroid2.rect.y = 130
        if (asteroid3.rect.x < -50):
            asteroid3.rect.x = 1233
            asteroid3.rect.y = 300
        if (star1.rect.x < -50):
            star1.rect.x = 969
            star1.rect.y = 70
        if (star2.rect.x < -50):
            star2.rect.x = 3000
            star2.rect.y = 200
        if (star3.rect.x < -50):
            star3.rect.x = 1423
            star3.rect.y = 250

        # Заново прорисовываем объекты
        screen.blit(bk, (0, 0))
        font = pygame.font.Font(None, 30)
        white = (255, 255, 255)
        life = int(score / 10)
        points = int(score1/10)
        text = font.render("Жизнь: " + str(life), True, white)
        text_2 = font.render("Очки: " + str(points), True, white)
        # Рисуем надпись с жизнями и с очками
        screen.blit(text, [10, 10])
        screen.blit(text_2, [400, 10])
        # Обновляем положение объектов
        asteroids.update()
        stars_.update()
        rocket_.update()
        # Обновляем кадр
        if score < 1:
            final, final_background = load_image('sky_2.jpg')
            screen.blit(final, (0, 0))
            font_1 = pygame.font.Font(None, 60)
            font = pygame.font.Font(None, 70)
            text = font_1.render('Кажется, вы остались', True, white)
            text_1 = font_1.render('без корабля...', True, white)
            text_2 = font.render('Очки: ' + str(points), True, white)
            text_3 = font.render('Game Over!', True, white)
            screen.blit(text, [30, 60])
            screen.blit(text_1, [90, 120])
            screen.blit(text_2, [110, 200])
            screen.blit(text_3, [90, 270])
        if points >= 500:
            final ,final_background = load_image('sky_2.jpg')
            screen.blit(final, (0, 0))
            font_1 = pygame.font.Font(None, 55)
            font = pygame.font.Font(None, 70)
            text = font_1.render('Вам удалось преодолеть', True, (255, 255, 255))
            text_1 = font_1.render('метеоритный дождь,', True, (255, 255, 255))
            text_2 = font_1.render('и скоро вы будете дома!', True, (255, 255, 255))
            text_3 = font.render('Game Over!', True, (255, 255, 255))
            screen.blit(text, [20, 60])
            screen.blit(text_1, [50, 120])
            screen.blit(text_2, [20, 180])
            screen.blit(text_3, [90, 270])
        else:
            if score > 0:
                asteroids.draw(screen)
                all_sprites.update()
                all_sprites.draw(screen)
                stars_.draw(screen)
                rocket_.draw(screen)
        pygame.display.flip()


init_window()
bk = draw_background()
action(bk)
