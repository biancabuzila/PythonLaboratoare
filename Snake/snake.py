import random
import sys
import json
import tkinter as tk

def config_game():
    try:
        file_name = sys.argv[1]
    except Exception as e:
        print("[ERROR] - Second argument (json file) not provided. Exception: ", str(e), sep="")
        return
    
    try:
        game_configurations = open(file_name, "r").read()
    except Exception as e:
        print("[ERROR] - File ", file_name, " could not be opened/read. Exception: ", str(e), sep="")
        return
    
    try:
        game_configurations = json.loads(game_configurations)
    except Exception as e:
        print("[ERROR] - File ", file_name, " could not be loaded. Exception: ", str(e), sep="")
        return
    
    try:
        ROWS = game_configurations["rows"]
        COLUMNS = game_configurations["columns"]
        SIZE = game_configurations["size"]
        OBSTACLES = game_configurations["obstacles"]
    except Exception as e:
        print("[ERROR] - Key ", str(e), " could not be found in ", file_name, sep="")
        return

    WIDTH = ROWS * SIZE
    HEIGHT = COLUMNS * SIZE
    return ROWS, COLUMNS, WIDTH, HEIGHT, SIZE, OBSTACLES


def draw_game_interface():
    window.title("Snake")
    window.geometry(str(WIDTH + 100) + "x" + str(HEIGHT + 150) + "+100+100")
    window.config(background="#6aa84f")

    frame_score = tk.Frame(master=window)
    var.set('Score: ' + str(score))
    label_score = tk.Label(master=frame_score, textvariable=var, background="#38761d", foreground="white", font=("Arial", 25), width=WIDTH, pady=10)
    label_score.pack()
    frame_score.pack()

    frame_game = tk.Frame(master=window)
    frame_game.pack(expand=True)

    canvas_game = tk.Canvas(master=frame_game, width=WIDTH, height=HEIGHT, background="#38761d", highlightbackground="black")
    canvas_game.pack(anchor=tk.CENTER, expand=True)
    return frame_score, frame_game, canvas_game


def getAction(event):
    global action
    key = event.keysym
    if key == 'Left' and action != 'Right':
        action = key
    if key == 'Right' and action != 'Left':
        action = key
    if key == 'Up' and action != 'Down':
        action = key
    if key == 'Down' and action != 'Up':
        action = key


def draw_game():
    redraw = canvas_game.after(200, draw_game)
    canvas_game.delete(tk.ALL)
    move_snake()
    eat_apple()
    if not is_game_over():
        draw_snake()
        draw_apple()
    else:
        draw_game_over() 
        canvas_game.after_cancel(redraw)


def draw_snake():
    for body_part in range(1, len(snake)):
        canvas_game.create_rectangle(snake[body_part][0], snake[body_part][1], snake[body_part][0] + SIZE, snake[body_part][1] + SIZE, fill="black")
    canvas_game.create_rectangle(snake[0][0], snake[0][1], snake[0][0] + SIZE, snake[0][1] + SIZE, fill="white")


def generate_apple():
    row = random.randint(0, ROWS - 1) * SIZE
    col = random.randint(0, COLUMNS - 1) * SIZE
    return (row, col)


def draw_apple():
    canvas_game.create_oval(apple[0], apple[1], apple[0] + SIZE, apple[1] + SIZE, fill="red")


def move_snake():
    global snake
    for body_part in range(len(snake) - 1, 0, -1):
        snake[body_part] = snake[body_part - 1]
    snake_head = list(snake[0])
    if action == 'Left':
        snake_head[0] -= SIZE
    elif action == 'Right':
        snake_head[0] += SIZE
    elif action == 'Up':
        snake_head[1] -= SIZE
    elif action == 'Down':
        snake_head[1] += SIZE
    snake[0] = tuple(snake_head[:])


def eat_apple():
    global snake, apple, score
    if snake[0][0] == apple[0] and snake[0][1] == apple[1]:
        new_body_part = snake[-1]
        snake.append(new_body_part)
        score += 1
        var.set('Score: ' + str(score))
        window.update()
        apple = generate_apple()


def is_game_over():
    for body_part in range(2, len(snake)):
        if snake[0] == snake[body_part]:
            return True
    if snake[0][0] < 0 or snake[0][0] > (ROWS - 1) * SIZE or snake[0][1] < 0 or snake[0][1] > (COLUMNS - 1) * SIZE:
        return True
    return False


def draw_game_over():
    canvas_game.delete(tk.ALL)
    canvas_game.create_text(WIDTH //2, HEIGHT //2, font="Times 20 italic bold", text="GameOver!")


ROWS, COLUMNS, WIDTH, HEIGHT, SIZE, OBSTACLES = config_game()
snake = [(ROWS // 2 * SIZE, COLUMNS // 2 * SIZE)]
score = 0
high_score = 0
actions = ['Left', 'Right', 'Up', 'Down']
action = actions[random.randint(0,3)]

window = tk.Tk()
var = tk.StringVar()
frame_score, frame_game, canvas_game = draw_game_interface()
apple = generate_apple()
draw_apple()
draw_snake()
draw_game()
window.bind('<Key>', getAction)
window.mainloop()