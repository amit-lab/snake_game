from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.speed('fastest')
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
