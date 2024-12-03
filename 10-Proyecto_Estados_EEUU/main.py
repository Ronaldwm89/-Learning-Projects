import pandas
import turtle

#lectura del csv con pandas
data = pandas.read_csv(r"50_states.csv")

#config pantalla
screen = turtle.Screen()
screen.bgpic(r"blank_states_img.gif")



#manipulacion de la data del csv (convierte los estados de la data en una lista de estados)
all_states = data["state"].to_list()

guess_states = [] 

while len(guess_states) < 50:
      
    #variable input usuario
    answer = screen.textinput(f"Has adivinado {len(guess_states)}/50", "Ingrese el nombre del estado: ").title()
     
    if answer in all_states:
        
        guess_states.append(answer)
        st = turtle.Turtle()
        st.hideturtle()
        st.penup()

        state_position = data[data["state"] == answer]
        
        st.goto(state_position.x.item(), state_position.y.item())
        st.write(answer)

        all_states.remove(answer)
        
        
    
    elif answer == "Exit":
            
       inguess_states = {
           "States": all_states
        }  

       inguess_states = pandas.DataFrame(inguess_states)
       inguess_states.to_csv(r"inguess_states.csv")
       break






#Metodologia Scrum
#Metodologia Kanban