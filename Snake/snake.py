import random
import sys
import json
import tkinter as tk


def config_game():
    global ROWS, COLUMNS, WIDTH, HEIGHT, SIZE, OBSTACLES

    try:
        file_name = sys.argv[1]
    except Exception as e:
        print("[ERROR] - Second argument (json file) not provided. Exception: ", str(e), sep="")
        return False
    
    try:
        game_configurations = open(file_name, "r").read()
    except Exception as e:
        print("[ERROR] - File ", file_name, " could not be opened/read. Exception: ", str(e), sep="")
        return False
    
    try:
        game_configurations = json.loads(game_configurations)
    except Exception as e:
        print("[ERROR] - File ", file_name, " could not be loaded. Exception: ", str(e), sep="")
        return False
    
    try:
        ROWS = game_configurations["rows"]
        COLUMNS = game_configurations["columns"]
        SIZE = game_configurations["size"]
        OBSTACLES = game_configurations["obstacles"]
    except Exception as e:
        print("[ERROR] - Key ", str(e), " could not be found in ", file_name, sep="")
        return False

    for obstacle in OBSTACLES:
        if obstacle[0] < 0 or obstacle[0] > ROWS - 1 or obstacle[1] < 0 or obstacle[1] > COLUMNS - 1:
            print("[ERROR] - Obstacle not inside game table: ", obstacle, sep="")
            return False

    WIDTH = ROWS * SIZE
    HEIGHT = COLUMNS * SIZE
    for i in range(len(OBSTACLES)):
        OBSTACLES[i][0] *= SIZE
        OBSTACLES[i][1] *= SIZE
    
    return True

def draw_game_interface():
    global frame_score, frame_game, canvas_game

    frame_score = tk.Frame(master=window)
    var.set("Score: " + str(score))
    label_score = tk.Label(master=frame_score, textvariable=var, background="#38761d", foreground="white", font="Arial " + str((WIDTH + 100)//22), width=WIDTH, pady=10)
    label_score.pack()
    frame_score.pack()

    frame_game = tk.Frame(master=window)
    frame_game.pack(expand=True)

    canvas_game = tk.Canvas(master=frame_game, width=WIDTH, height=HEIGHT, background="#38761d", highlightbackground="black")
    canvas_game.pack(anchor=tk.CENTER, expand=True)


def getAction(event):
    global action

    key = event.keysym
    if key == "Left" and action != "Right":
        action = key
    elif key == "Right" and action != "Left":
        action = key
    elif key == "Up" and action != "Down":
        action = key
    elif key == "Down" and action != "Up":
        action = key


def draw_snake():
    for body_part in range(1, len(snake)):
        canvas_game.create_rectangle(snake[body_part][0], snake[body_part][1], snake[body_part][0] + SIZE, snake[body_part][1] + SIZE, fill="black", outline="white")
    canvas_game.create_rectangle(snake[0][0], snake[0][1], snake[0][0] + SIZE, snake[0][1] + SIZE, fill="white")


def generate_apple():
    while True:
        row = random.randint(0, ROWS - 1) * SIZE
        col = random.randint(0, COLUMNS - 1) * SIZE
        if (row, col) not in snake and [row, col] not in OBSTACLES:
            break
    return (row, col)


def draw_apple():
    canvas_game.create_oval(apple[0], apple[1], apple[0] + SIZE, apple[1] + SIZE, fill="red")


def draw_obstacles():
    for obstacle in OBSTACLES:
        canvas_game.create_rectangle(obstacle[0], obstacle[1], obstacle[0] + SIZE, obstacle[1] + SIZE, fill="#6aa84f")


def move_snake():
    global snake

    for body_part in range(len(snake) - 1, 0, -1):
        snake[body_part] = snake[body_part - 1]
    snake_head = list(snake[0])
    if action == "Left":
        snake_head[0] -= SIZE
    elif action == "Right":
        snake_head[0] += SIZE
    elif action == "Up":
        snake_head[1] -= SIZE
    elif action == "Down":
        snake_head[1] += SIZE
    snake[0] = tuple(snake_head[:])


def eat_apple():
    global snake, apple, score

    if snake[0][0] == apple[0] and snake[0][1] == apple[1]:
        new_body_part = snake[-1]
        snake.append(new_body_part)
        score += 1
        var.set("Score: " + str(score))
        window.update()
        apple = generate_apple()


def is_game_over():
    if snake[0][0] < 0 or snake[0][0] > (ROWS - 1) * SIZE or snake[0][1] < 0 or snake[0][1] > (COLUMNS - 1) * SIZE:
        print("in afara")
        return True

    for body_part in range(2, len(snake)):
        if snake[0] == snake[body_part]:
            print("mancat")
            return True
    
    for obstacle in OBSTACLES:
        if snake[0] == tuple(obstacle):
            print("obstacol")
            return True

    return False


def draw_game():
    redraw = canvas_game.after(200, draw_game)
    canvas_game.delete(tk.ALL)
    move_snake()
    eat_apple()
    if not is_game_over():
        draw_snake()
        draw_apple()
        draw_obstacles()
    else:
        draw_game_over()
        canvas_game.after_cancel(redraw)


def draw_start_game_interface():
    global button_start

    window.title("Snake")
    window.geometry(str(WIDTH + 100) + "x" + str(HEIGHT + 150) + "+100+100")
    window.config(background="#6aa84f")

    button_start = tk.Button(master=window, 
        text="Start\ngame session", 
        padx=10, pady=10, 
        background="#529138", foreground="white", 
        font="Arial " + str((WIDTH + 100)//22) + " bold",
        activeforeground="white", activebackground="#38761d", 
        command=start_game)
    button_start.pack(anchor=tk.CENTER, expand=True)


def start_game():
    global snake, apple, score, high_score, action, button_start, frame_score, frame_game, canvas_game, frame_end_game

    if button_start:
        button_start.destroy()
    if frame_end_game:
        frame_end_game.destroy()
    
    snake = [(ROWS // 2 * SIZE, COLUMNS // 2 * SIZE)]
    score = 0
    action = actions[random.randint(0,3)]
    
    draw_game_interface()
    apple = generate_apple()
    draw_apple()
    draw_snake()
    draw_obstacles()
    draw_game()


def draw_game_over():
    global high_score, frame_end_game

    frame_score.destroy()
    frame_game.destroy()

    high_score = max(high_score, score)
    scores = "Score: " + str(score) + "\nHigh score: " + str(high_score)

    frame_end_game = tk.Frame(master=window, background="#6aa84f")
    frame_end_game.pack(anchor=tk.CENTER, expand=True)

    label_scores = tk.Label(master=frame_end_game, text=scores, background="#38761d", foreground="white", font="Arial " + str((WIDTH + 100)//18) + " bold", padx=10, pady=10)
    label_scores.pack(anchor=tk.CENTER, expand=True)

    button_play_again = tk.Button(master=frame_end_game, 
        text="Play again", 
        padx=5, pady=5, 
        background="#529138", foreground="white", 
        font="Arial " + str((WIDTH + 100)//22) + " bold",
        activeforeground="white", activebackground="#38761d", 
        command=start_game)
    button_play_again.pack(anchor=tk.CENTER, expand=True)
    button_exit = tk.Button(master=frame_end_game, 
        text="Exit", 
        padx=5, pady=5, 
        background="#529138", foreground="white", 
        font="Arial " + str((WIDTH + 100)//22) + " bold",
        activeforeground="white", activebackground="#38761d", 
        command=exit_game)
    button_exit.pack(anchor=tk.CENTER, expand=True)


def exit_game():
    window.destroy()


ROWS = None
COLUMNS = None
WIDTH = None
HEIGHT = None
SIZE = None
OBSTACLES = None
snake = []
score = None
high_score = 0
actions = ["Left", "Right", "Up", "Down"]
apple = None
frame_score = None
frame_game = None
canvas_game = None
frame_end_game = None

if config_game():
    window = tk.Tk()
    window.bind("<Key>", getAction)
    var = tk.StringVar()
    draw_start_game_interface()
    window.mainloop()