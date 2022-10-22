from turtle import Screen
from time import sleep
from snake_class import Snake
from food_class import Food
from track_score import ScoreBoard


# prepare screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("dark sea green")
screen.title("Snake Game")
screen.tracer(0)

# create random food:
food = Food()
score = ScoreBoard()

play_again = True
while play_again:
    snake = Snake()
    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")

    play = True
    while play:
        screen.update()
        sleep(0.1)
        snake.move()
        if (snake.snake_head.xcor() > 285 or snake.snake_head.xcor() < -290) or \
                (snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -285):
            score.game_over()
            play = False
        if snake.crashed_snake():
            score.game_over()
            play = False
        if snake.snake_head.distance(food) < 15:
            food.change_position()
            score.write_score()
            snake.increase_snake()

    will = screen.textinput(title="continue or not", prompt="Do You Want To Continue?").lower()
    if will == "no":
        play_again = False
    else:
        score.clear()
        score.current_score = -1
        score.write_score()
        food.clear()
        snake.reset_snake()

        
screen.exitonclick()
