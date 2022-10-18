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

# create snake and random food:
snake = Snake()
food = Food()
score = ScoreBoard()

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

screen.exitonclick()
