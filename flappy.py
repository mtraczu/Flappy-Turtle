import random
from turtle import Turtle, Screen
import time

game = True
screen = Screen()
screen.bgcolor("blue")
screen.tracer(0)
screen.setup(width=600, height=600)
screen.listen()


class Bird(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("yellow")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.goto(-150, 0)
        self.setheading(90)

    def falling(self):
        self.backward(10)

    def fly(self):
        self.forward(35)


wall_positions_y = [(300, -450), (350, -400), (500, -300)]


class Wall:
    def __init__(self):
        self.wall_list = []

    def create_walls(self, y, x):
        wall = Turtle()
        wall.penup()
        wall.shape("square")
        wall.color("green")
        wall.shapesize(stretch_len=5, stretch_wid=30)
        wall.goto(300, y)

        wall1 = Turtle()
        wall1.penup()
        wall1.shape("square")
        wall1.color("green")
        wall1.shapesize(stretch_len=5, stretch_wid=30)
        wall1.goto(300, x)
        self.wall_list.append((wall, wall1))

    def wall_move(self):
        for walls in self.wall_list:
            walls[0].backward(10)
            walls[1].backward(10)

    def walls(self):
        random_wall = random.choice(wall_positions_y)
        self.create_walls(random_wall[0], random_wall[1])

    def delete_wall(self, wal):
        self.wall_list.remove(wal)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 24, 'normal'))

    def score_up(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=('Arial', 24, 'normal'))


score = Score()
bird = Bird()
screen.onkeypress(bird.fly, "Up")
wall = Wall()
wall.walls()

while game:
    time.sleep(0.05)
    screen.update()
    bird.falling()
    wall.wall_move()
    # create wall
    for walls in wall.wall_list:
        if walls[0].xcor() == 0 or walls[1].xcor() == 0:
            wall.walls()
    # delete wall
    for walls in wall.wall_list:
        if walls[0].xcor() == -400 or walls[1].xcor() == -400:
            wall.delete_wall(walls)

    # point add
    for walls in wall.wall_list:
        if walls[0].xcor() == bird.xcor():
            score.score_up()

    # collision
    for walls in wall.wall_list:
        if walls[0].ycor() > bird.ycor() + 450 and walls[0].xcor() == bird.xcor() \
                or walls[1].ycor() < bird.ycor() - 450 and walls[0].xcor() == bird.xcor():
            score.game_over()
            game = False
screen.exitonclick()
