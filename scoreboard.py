from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Cooper Black", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("scoreboard.txt") as scoreboard:
            self.high_score = int(scoreboard.read())
        self.penup()
        self.goto(0, 270)
        self.write(f"Scoreboard {self.score}", align=ALIGNMENT,
                   font=("Cooper Black", 20, "normal"))
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Scoreboard: {self.score}, Highest Score: {self.high_score}",
                   align="center", font=FONT)
    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("scoreboard.txt", mode="w") as highest_score:
                highest_score.write(f"{self.high_score}")
            self.score = 0
            self.update_scoreboard()
