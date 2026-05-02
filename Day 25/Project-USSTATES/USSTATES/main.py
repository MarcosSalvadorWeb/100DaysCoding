import turtle
import pandas as pd

# Configuração da tela
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("U.S States Game")

image = "./blank_states_img.gif"
screen.addshape(image)

bg = turtle.Turtle()
bg.shape(image)

# Carregar dados
data = pd.read_csv("./50_states.csv")
names = data.state.to_list()

# Tartaruga para escrever nomes
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

score = 0
game_is_on = True

guessed_states = []

while game_is_on:
    answer_state = screen.textinput(
        title=f"Score: {score}/{len(data)}",
        prompt="What's another state's name?"
    )

    if answer_state == "Exit":
        missing_states = [states for states in names if states not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("./missing_states.csv")
        break

    answer_state = answer_state.title()

    if answer_state in names:
        names.remove(answer_state)
        guessed_states.append(answer_state)
        score += 1

        # Buscar coordenadas corretas
        state_data = data[data.state == answer_state]

        coordx = int(state_data.x.iloc[0])
        coordy = int(state_data.y.iloc[0])

        writer.goto(coordx, coordy)
        writer.write(answer_state)

    # Vitória
    if score == 50:
        game_is_on = False

screen.exitonclick()