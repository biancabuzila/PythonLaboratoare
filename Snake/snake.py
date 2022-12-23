import random
import sys
import json
import time
import tkinter as tk


def config_game():
    """Retrieves the game configurations from the json file given in the command line.
    
    If the json file is not provided in the command line or it does not exist 
    or it cannot be read or opened or it cannot be loaded, then it returns an 
    error message. If one of the keys 'rows', 'columns', 'size', 'obstacles' 
    is not found in the provided json file then it returns an error message. 
    If there is one obstacle that is positioned outside the game board the it 
    returns an error message. It creates a dictionary that contains the 
    informations regarding the game board: width, height, rows, columns, size, 
    obstacles.

    :returns: A string representing the first error occured OR a dictionary
    which contains the data for the game
    :rtype: str or dict
    """
    try:
        file_name = sys.argv[1]
    except Exception as e:
        return "[ERROR] - Second argument (json file) not provided. Exception: " + str(e)
    
    try:
        game_configurations = open(file_name, "r").read()
    except Exception as e:
        return "[ERROR] - File " + file_name + " could not be opened/read. Exception: " + str(e)
    
    try:
        game_configurations = json.loads(game_configurations)
    except Exception as e:
        return "[ERROR] - File " + file_name + " could not be loaded. Exception: " + str(e)
    
    try:
        rows = game_configurations["rows"]
        columns = game_configurations["columns"]
        size = game_configurations["size"]
        obstacles = game_configurations["obstacles"]
    except Exception as e:
        return "[ERROR] - Key " + str(e) + " could not be found in " + file_name

    for obstacle in obstacles:
        if obstacle[0] < 0 or obstacle[0] > rows - 1 or obstacle[1] < 0 or obstacle[1] > columns - 1:
            return "[ERROR] - Obstacle not inside game board: " + str(obstacle)

    width = rows * size
    height = columns * size
    for i in range(len(obstacles)):
        obstacles[i][0] *= size
        obstacles[i][1] *= size
    
    configurations = {"rows":rows, "columns":columns, "width":width, "height":height, "size":size, "obstacles":obstacles}
    return configurations


def draw_game_interface():
    """Draws the game interface.
    
    It creates and sets globally two frame widgets and one canvas widget. 
    The first frame ``frame_score`` contains the score of the current game.
    The second frame ``frame_game`` contains the canvas. The canvas 
    ``canvas_game`` has as a parent the frame ``frame_game`` and it is used to 
    draw the objects of the game (snake, apple, possible obstacles).
    """
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
    """It is called when the user presses a key.
        
    It sets globally the variable ``action`` which represents how the snake
    is moving: to the left, to the right, up or down. If the key pressed by 
    the user represents the opposite of ``action``, then ``action`` will not 
    change because the snake cannot change its direction this way, according 
    to the game rules.

    :param tkinter.Event event: The user's input.
    """
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
    """Draws the snake.
    
    It draws the snake body on the canvas ``canvas_game`` as orange and yellow 
    rectangles and the snake head as an orange polygon using the global 
    variable ``snake`` which stores the snake's body and head positions on the 
    canvas as a list of tuple(int,int).
    """
    for body_part in range(len(snake)- 1, 0, -1):
        if body_part % 2:
            fill = "yellow"
        else:
            fill = "orange"
        canvas_game.create_rectangle(snake[body_part][0], snake[body_part][1], snake[body_part][0] + SIZE, snake[body_part][1] + SIZE, fill=fill, outline="black")
    
    canvas_game.create_rectangle(snake[0][0], snake[0][1], snake[0][0] + SIZE, snake[0][1] + SIZE, fill="orange", outline="black")
    if action == "Right":
        canvas_game.create_oval(snake[0][0] + 3*SIZE//4 - SIZE//6, snake[0][1] + SIZE//4 - SIZE//6, snake[0][0] + 3*SIZE//4 + SIZE//6, snake[0][1] + SIZE//4 + SIZE//6, fill="black", outline="white")
        canvas_game.create_oval(snake[0][0] + 3*SIZE//4 - SIZE//6, snake[0][1] + 3*SIZE//4 - SIZE//6, snake[0][0] + 3*SIZE//4 + SIZE//6, snake[0][1] + 3*SIZE//4 + SIZE//6, fill="black", outline="white")
    elif action == "Left":
        canvas_game.create_oval(snake[0][0] + SIZE//4 - SIZE//6, snake[0][1] + SIZE//4 - SIZE//6, snake[0][0] + SIZE//4 + SIZE//6, snake[0][1] + SIZE//4 + SIZE//6, fill="black", outline="white")
        canvas_game.create_oval(snake[0][0] + SIZE//4 - SIZE//6, snake[0][1] + 3*SIZE//4 - SIZE//6, snake[0][0] + SIZE//4 + SIZE//6, snake[0][1] + 3*SIZE//4 + SIZE//6, fill="black", outline="white")
    elif action == "Up":
        canvas_game.create_oval(snake[0][0] + SIZE//4 - SIZE//6, snake[0][1] + SIZE//4 - SIZE//6, snake[0][0] + SIZE//4 + SIZE//6, snake[0][1] + SIZE//4 + SIZE//6, fill="black", outline="white")
        canvas_game.create_oval(snake[0][0] + 3*SIZE//4 - SIZE//6, snake[0][1] + SIZE//4 - SIZE//6, snake[0][0] + 3*SIZE//4 + SIZE//6, snake[0][1] + SIZE//4 + SIZE//6, fill="black", outline="white")
    elif action == "Down":
        canvas_game.create_oval(snake[0][0] + SIZE//4 - SIZE//6, snake[0][1] + 3*SIZE//4 - SIZE//6, snake[0][0] + SIZE//4 + SIZE//6, snake[0][1] + 3*SIZE//4 + SIZE//6, fill="black", outline="white")
        canvas_game.create_oval(snake[0][0] + 3*SIZE//4 - SIZE//6, snake[0][1] + 3*SIZE//4 - SIZE//6, snake[0][0] + 3*SIZE//4 + SIZE//6, snake[0][1] + 3*SIZE//4 + SIZE//6, fill="black", outline="white")


def generate_apple():
    """Randomly generates the position of ``apple``.
    
    It returns a new random position that does not overlap with the snake or 
    the obstacles.

    :returns: The position of the apple on the canvas.
    :rtype: tuple(int, int)
    """
    while True:
        x = random.randint(0, ROWS - 1) * SIZE
        y = random.randint(0, COLUMNS - 1) * SIZE
        if (x, y) not in snake and [x, y] not in OBSTACLES:
            break
    return (x, y)


def draw_apple():
    """Draws the apple.
    
    It draws the apple whose position is stored in the variable ``apple`` on
    the canvas ``canvas_game`` as a red circle.
    """
    canvas_game.create_oval(apple[0], apple[1], apple[0] + SIZE, apple[1] + SIZE, fill="red")


def draw_obstacles():
    """Draws the obstacles.
    
    It draws the obstacles whose positions are stored in the constant 
    ``OBSTACLES`` on the canvas ``canvas_game`` as gray rectangles.
    """
    for obstacle in OBSTACLES:
        canvas_game.create_rectangle(obstacle[0], obstacle[1], obstacle[0] + SIZE, obstacle[1] + SIZE, fill="#d4d9d9")


def move_snake():
    """Moves the snake on the board according to the current action.
    
    It changes the values of the tuples in the list ``snake`` that represent
    the positions of each part of the snake. Each body part takes the value of
    the next body part (from tail to head), and the tuple representing the
    head is changed like so: if the ``action`` is LEFT or RIGHT (respectively
    UP or DOWN) then to the first (respectively to the second) element of the
    tuple representing the position on the x (respectively y) coordinate is
    subtracted or added the value of the constant ``SIZE``.
    """
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
    """Verifies if the apple has been eaten by the snake and if so it makes the appropriate changes.
    
    If the snake's head position is the same with the apple's position, then it
    means the snake ate the apple so a new body part is being added by
    duplicating the last one, the score is being incremented by one, the
    text of the ``label_score`` is updated and a new apple is generated and
    stored in the variable ``apple``.
    """
    global snake, apple, score

    if snake[0][0] == apple[0] and snake[0][1] == apple[1]:
        new_body_part = snake[-1]
        snake.append(new_body_part)
        score += 1
        var.set("Score: " + str(score))
        window.update()
        apple = generate_apple()


def is_game_over():
    """Verifies if the current game is over.
    
    :returns: True if the position of the snake's head is outside the board or
    if it intersects with another body part of if it intersects with an
    obstacle; False otherwise
    :rtype: bool
    """
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
    """Draws the elements of the game every 2 seconds.
    
    It moves the snake, verifies if the snake ate the apple, and if the
    game is not over then it draws the snake, the apple and the obstacles.
    Otherwise, it stops from drawing the game every 2 seconds and draws
    the game over interface. 
    """
    redraw = canvas_game.after(200, draw_game)
    canvas_game.delete(tk.ALL)
    move_snake()
    eat_apple()
    if not is_game_over():
        draw_snake()
        draw_apple()
        draw_obstacles()
    else:
        canvas_game.after_cancel(redraw)
        draw_game_over()


def draw_start_game_interface():
    """Draws the start interface of the game.
    
    It draws and sets globally the button widget ``button_start`` which
    has to be pressed to start the game.
    """
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
    """It draws the game after the ``button_start`` has been pressed.
    
    It destroys the widgets ``button_start`` and ``frame_end_game`` if they
    have been created previously. It initializes the list ``snake`` with one
    element representing the position of the head in the middle of the
    game board. It initializes ``score`` with 0 and ``action`` with a random
    value from the list ``['Left', 'Right', 'Up', 'Down']``. It calls the 
    functions that draw the game, generate an apple and draw the elements
    of the game: interface, snake, apple, obstacles.
    """
    global snake, apple, score, high_score, action, button_start, frame_score, frame_game, canvas_game, frame_end_game

    if button_start:
        button_start.destroy()
    if frame_end_game:
        frame_end_game.destroy()
    
    snake = [(ROWS // 2 * SIZE, COLUMNS // 2 * SIZE)]
    score = 0
    action = ACTIONS[random.randint(0,3)]
    
    draw_game_interface()
    apple = generate_apple()
    draw_apple()
    draw_snake()
    draw_obstacles()
    draw_game()


def draw_game_over():
    """It draws the window that shows the score and high score.
    
    It updates the variable ``high_score``, displays the score and high score
    and creates a frame widget ``frame_end_game`` that contains two buttons:
    one for playing the game again and one for exiting the game. It updates
    the dictionary ``scores`` by adding the key corresponding to the turn of 
    the game with the value of the score.
    """
    global high_score, frame_end_game, scores

    frame_score.destroy()
    frame_game.destroy()

    turn = len(scores) + 1
    scores["tura" + str(turn)] = score

    high_score = max(high_score, score)
    scores_text = "Score: " + str(score) + "\nHigh score: " + str(high_score)

    frame_end_game = tk.Frame(master=window, background="#6aa84f")
    frame_end_game.pack(anchor=tk.CENTER, expand=True)

    label_scores = tk.Label(master=frame_end_game, text=scores_text, background="#38761d", foreground="white", font="Arial " + str((WIDTH + 100)//18) + " bold", padx=10, pady=10)
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
    """Destroys the game window.
    
    It ends the game session and it writes in a json file with the name
    corresponding to the current time the scores obtained during the
    game session.
    """
    window.destroy()

    tobj = time.localtime()
    file_scores_name = time.strftime("%Y-%m-%d_%H-%M-%S_", tobj) + ".json"
    json_scores = json.dumps(scores)
    open(file_scores_name, "wt").write(json_scores)


def main():
    """It creates and starts the game.
    
    It sets globally the constants representing the configurations of the game.
    It initializes the variables used to store the snake, apple and scores.
    It initializes the frame and canvas widgets used to display different
    interfaces depending on the state of the game. It initializes the
    variable ``scores`` with an empty dictionary that will store the scores
    obtained during the game session.
    """
    global ROWS, COLUMNS, WIDTH, HEIGHT, SIZE, OBSTACLES, snake, score, high_score, ACTIONS, apple, window, frame_score, frame_game, canvas_game, frame_end_game, var, scores
    configurations = config_game()
    if type(configurations) == str:
        print(configurations)
    else:
        ROWS = configurations["rows"]
        COLUMNS = configurations["columns"]
        WIDTH = configurations["width"]
        HEIGHT = configurations["height"]
        SIZE = configurations["size"]
        OBSTACLES = configurations["obstacles"]

        snake = []
        score = None
        high_score = 0
        ACTIONS = ["Left", "Right", "Up", "Down"]
        apple = None
        frame_score = None
        frame_game = None
        canvas_game = None
        frame_end_game = None

        scores = dict()

        window = tk.Tk()
        window.bind("<Key>", getAction)
        var = tk.StringVar()
        draw_start_game_interface()
        window.mainloop()

main()