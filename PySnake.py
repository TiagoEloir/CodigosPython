import curses
import random
import time

def game_loop(window, game_speed):
    #Setup Inicial
    curses.curs_set(0)
    snake = [[10, 10],[9,10],[8,10],[7,10]]
    current_direction = curses.KEY_DOWN
    fruit = get_new_fruit_position(window= window)
    snake_ate_fruit = False
    score = 0

    #Loop do Jogo
    while True:
        curses.curs_set(0)
        draw_screen(window= window)
        draw_snake(snake = snake, window= window)
        draw_actor(actor= fruit, window= window, char= curses.ACS_DIAMOND)
        direction = get_new_direction(window= window, timeout= game_speed)
        if direction is None:
            direction = current_direction
        if direction_is_opposite(current_direction =  current_direction, direction = direction):
            direction = current_direction
        snake = move_snake(snake = snake, direction= direction, snake_ate_fruit= snake_ate_fruit)
        if snake_hit_self(snake = snake):
            breakpoint
        if snake_hit_border(snake = snake, window= window):
            break
        if snake_hit_fruit(snake = snake, fruit = fruit):
            score += 1
            fruit = get_new_fruit_position(window= window)
            snake_ate_fruit = True
        else:
            snake_ate_fruit = False
        current_direction = direction

    finish_game(window= window, score= score)

def finish_game(window, score):
    height, width = window.getmaxyx()
    message = "Game Over! Your score was: " + str(score)
    window.addstr(int(height/2), int((width - len(message))/2), message)
    window.refresh()
    time.sleep(2)

def direction_is_opposite(current_direction, direction):
    if current_direction == curses.KEY_UP and direction == curses.KEY_DOWN:
        return True
    if current_direction == curses.KEY_DOWN and direction == curses.KEY_UP:
        return True
    if current_direction == curses.KEY_LEFT and direction == curses.KEY_RIGHT:
        return True
    if current_direction == curses.KEY_RIGHT and direction == curses.KEY_LEFT:
        return True
    return False

def snake_hit_fruit(snake, fruit):
    head = snake[0]
    return head == fruit

def get_new_fruit_position(window):
    height, width = window.getmaxyx()
    return [random.randint(1, height - 2), random.randint(1, width - 2)]

def draw_screen(window):
    window.clear()
    window.border(0)


def draw_snake(snake,window):
    head = snake[0]
    draw_actor(actor= head, window= window, char= '@')
    body = snake[1:]
    for part in body:
        draw_actor(actor= part, window= window, char= 's')
    return snake

def draw_actor(actor,window,char):
    window.addch(actor[0],actor[1],char)

def get_new_direction(window, timeout):
    window.timeout(timeout)
    direction = window.getch()
    if direction in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
        return direction
    return None

def move_snake(snake,direction, snake_ate_fruit):
    head = snake[0].copy()
    move_actor(actor = head,direction = direction)
    snake.insert(0,head)
    if not snake_ate_fruit:
        snake.pop()
    return snake

def move_actor(actor, direction):
    if direction == curses.KEY_UP:
        actor[0] -= 1
    elif direction == curses.KEY_DOWN:
        actor[0] += 1
    elif direction == curses.KEY_LEFT:
        actor[1] -= 1
    elif direction == curses.KEY_RIGHT:
        actor[1] += 1
    return actor

def snake_hit_border(snake,window):
    head = snake[0]
    return actor_hit_border(actor = head,window = window)

def snake_hit_self(snake):
    head = snake[0]
    body = snake[1:]
    return head in body

def actor_hit_border(actor,window):
    height, width = window.getmaxyx()
    if (actor[0] <= 0 or actor[0] == height - 1):
        return True
    if (actor[1] <= 0 or actor[1] == width - 1):
        return True
    return False

def select_speed():

    while True:
        try:
            print("Select the game speed:")
            print("1 - Slow")
            print("2 - Normal")
            print("3 - Fast")
            speed = int(input())
            if speed == 1:
                return 150
            if speed == 2:
                return 100
            if speed == 3:
                return 50
            if speed not in [1,2,3]:
                print("Invalid selection. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid selection. Please try again.")
            continue
    
        
if __name__ == '__main__':
    curses.wrapper(game_loop,game_speed= select_speed())