import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in  a to-do")                         # A Text Label
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
list_display = sg.Listbox(values=functions.get_todos(), key="list_todos",
                          enable_events=True, size=[45,10])
add_button = sg.Button("Add")                               # A Button
edit_button = sg.Button("Edit")

layout = [ [label],                                 # The Layout of Window
           [input_box, add_button],                  # Each item in separate row is shown in different row
           [list_display, edit_button]
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
            todos_list = functions.get_todos()
            todos_list.append(values["todo"] + "\n")
            functions.write_todos(todos_list)
            window["list_todos"].update(values=todos_list)
            window["todo"].update("")

        case "Edit":
            todo_to_edit = values["list_todos"][0]
            new_todo = values["todo"]

            todos_list = functions.get_todos()
            index = todos_list.index(todo_to_edit)
            todos_list[index] = new_todo + "\n"
            functions.write_todos(todos_list)
            window["list_todos"].update(values=todos_list)

        case "list_todos":
            window["todo"].update(value=values['list_todos'][0])

        case sg.WIN_CLOSED:
            break


