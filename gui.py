import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in  a to-do")                 # A Text Label
input_box = sg.InputText(tooltip="Enter to-do")      # Input Box
add_button = sg.Button("Add")                         # A Button

layout = [ [label],                                 # The Layout of Window
           [input_box, add_button]                      # Each item in separate row is shown in different row
         ]                                          # input box and button show on single row

window = sg.Window("To-Do App", layout)             # Window Definition
window.read()                                       # Display Window
window.close()                                      # Closes Window on doing any interaction
