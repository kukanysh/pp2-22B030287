#imports
import pygame
import random
import psycopg2
import time

connection = psycopg2.connect(host = "localhost", dbname = "postgres", user = "postgres", password = "password", port = "5432")
cur = connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(255) NOT NULL
);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS user_score (
    user_score INT NOT NULL,
    user_level INT NOT NULL,
    username VARCHAR(255) NOT NULL
);
""")
#initialization
pygame.init()

username = input('Enter your username: ')
cur.execute("""INSERT INTO users VALUES ('{}')""".format(username))
cur.execute("SELECT * FROM users WHERE username = %s", (username,))
existing_user = cur.fetchone()

if existing_user:
    print('Welcome back, {}!'.format(username))
else:
    print('Welcome, {}!'.format(username))

cur.execute("""SELECT user_score, user_level FROM user_score WHERE username = %s""", (username,))
scores = cur.fetchall()
length = len(scores)
if scores:
    print('Your previous score and level: ', scores[length-1])

time.sleep(3)
#variables and colors
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
COLOR = (0, 255, 0)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
clock = pygame.time.Clock()
font = pygame.font.SysFont("SF Pro", 42)
pygame.display.set_caption("Snake")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#declaring Snake class
class Snake:
    def __init__(self):
        self.body = [
            Point(
                x=WIDTH // BLOCK_SIZE // 2,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
            Point(
                x=WIDTH // BLOCK_SIZE // 2 + 1,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
        ]

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.body[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )
    #moving the snake
    def move(self, dx, dy):
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y
        # [Point(0, 1), Point(2, 5), Point(5, 9)]
        # [Point(0, 0), Point(0, 1), Point(2, 5)]
        self.body[0].x += dx
        self.body[0].y += dy

    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True
    
    def wall_collision(self):
        if self.body[0].x >= 20 or self.body[0].x <= 0:
            return True
        if self.body[0].y >= 20 or self.body[0].y <= 0:
            return True
        return False

#drawing the grid
def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)

#declaring Food class
class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            COLOR,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )

#main loop
def main():
    running = True
    snake = Snake()
    food = Food(5, 5)
    dx, dy = 0, 0
    score = 0
    level = 0
    weight = 1
    speed = 5

    time = 0
    food_timer = 2
    

    while running:
        SCREEN.fill((54, 123, 32))

        dt = clock.tick(60)/100
        time += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                cur.execute("""INSERT INTO user_score VALUES ({}, {})""".format(score, level))
                

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, +1
                elif event.key == pygame.K_RIGHT:
                    dx, dy = 1, 0
                elif event.key == pygame.K_LEFT:
                    dx, dy = -1, 0
        if score != 0 and score%3 == 0:
            SCREEN.fill((255, 191, 0))
            weight = random.randint(2, 3)
        else:
            weight = 1

        if score!= 0 and score%5 == 0:
            if time >= food_timer:
                food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
                time = 0

        snake.move(dx, dy)
        if snake.check_collision(food):
            snake.body.append(
                Point(snake.body[-1].x, snake.body[-1].y)
            )
            score += weight
            if score%4 == 0:
                level += 1
                speed += 2
            
            food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
        
        if snake.wall_collision():
            running = False
            cur.execute("""INSERT INTO user_score VALUES ({}, {}, '{}')""".format(score, level, username))
            
        
        snake.draw()
        food.draw()
        draw_grid()
        text = font.render("Your score: " + str(score), True, RED)
        level_text = font.render("Current level: " + str(level), True, RED)
        SCREEN.blit(text, (0, 0))
        SCREEN.blit(level_text, (500, 0))
        pygame.display.flip()
        clock.tick(speed)


if __name__ == '__main__':
    main()



connection.commit()
cur.close()
connection.close()