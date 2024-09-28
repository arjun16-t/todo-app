import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in  a to-do")                 # A Text Label
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add", bind_return_key=True)                       # A Button

layout = [ [label],                                 # The Layout of Window
           [input_box, add_button]                  # Each item in separate row is shown in different row
         ]                                          # input box and button show on single row

window = sg.Window("To-Do App",                     # Window Definition
                   layout, font=('Montserrat', 12),
                   )

while True:
    event, values = window.read()                               # Display Window
    print(event)                                                # shows the button used
    print(values)                                               # returns the user input
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.write_todos(todos)

        case sg.WIN_CLOSED:
            break


