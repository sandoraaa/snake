import pygame
import random

pygame.init()


class Snake():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.rect(window, 'Orange', (self.x*size+(self.x+1)*m, self.y*size+(self.y+1)*m, size, size))


class Apple():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.rect(window, 'IndianRed', (self.x*size+(self.x+1)*m, self.y*size+(self.y+1)*m, size, size))





size=30

m=3
k=20

dx=0
dy=0


width=height =size*k+m*(k+1)

snake=[Snake(3,4), Snake(4,4), Snake(5,4)]
apple= Apple(random.randint (1,k-1),random.randint(1,k-1))



size_window = (width, height)
window = pygame.display.set_mode(size_window)
pygame.display.set_caption('Game ')
run=True
while run:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        dx=1
        dy=0
    if keys[pygame.K_LEFT]:
        dx=(-1)
        dy=0
    if keys[pygame.K_DOWN]:
        dx=0
        dy=1
    if keys[pygame.K_UP]:
        dy=(-1)
        dx=0

    window.fill ('SteelBlue')


    y= m
    for a in range(k):
        x= m

        for i in range(k):
            pygame.draw.rect(window, "Indigo", (x ,y ,size, size))
            x+=size+m
        y+=size+m

        #HEAD

    head = snake[-1]
    new_head = Snake(head.x + dx, head.y + dy)
    snake.append(new_head)
    snake.pop(0)


    for t in range(len(snake)):
        #snake[t].x+=dx
        #snake[t].y+=dy
        snake[t].draw()
        if snake[t].x>k:
            snake[t].x = 0
        if snake[t].x<0:
            snake[t].x = k
        if snake[t].y<0:
            snake[t].y = k
        if snake[t].y>k:
            snake[t].y = 0
    if snake[-1].x== apple.x and snake[-1].y== apple.y:
        print('num num')
        snake.append(Snake(apple.x , apple.y))
        apple.x=random.randint(1,k-1)
        apple.y = random.randint(1, k-1)

    apple.draw()



    pygame.time.delay(150)
    pygame.display.update()

pygame.quit()