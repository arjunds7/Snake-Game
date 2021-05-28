from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        """create the score board display"""
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.setpos(-10, 265)
        self.update_score()

    def update_score(self):
        """Updates the score everytime you gain a point"""
        self.write(f"Score = {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        """Ends the game 😐"""
        self.setpos(-10, 10)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
        """Increase the score by 1 on every point"""
        self.score += 1
        self.clear()
        self.update_score()
