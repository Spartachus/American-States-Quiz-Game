import turtle
from turtle import Turtle
import pandas

turt = turtle.Turtle()
screen = turtle.Screen()
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
screen.title("Us states")

regions =  pandas.read_csv("50_states.csv")
states = regions.state.to_list()

geused=[]

while len(geused) < 50:
    answer = screen.textinput(title = f"{len(geused)}/50 Guess the state", prompt = "What's another state").title()
    cor = regions[regions.state == answer]
    print(answer)
    if answer == "Exit":
        break
    if answer in states:
        geused.append(answer)
        cor = regions[regions.state == answer]
        turt.goto(int(cor.x),int(cor.y))
        turt.write(answer)

