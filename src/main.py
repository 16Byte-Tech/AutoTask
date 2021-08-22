from json import load, dumps
import PySimpleGUI as sg
from pynput import mouse
from multiprocessing import Process

### Functions to Tasks
from time import sleep
import pyautogui as pag

def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        print('Pressed Left Click')
        return False

def configure_tasks(datajson):
    data_json = datajson

    layout = [
        # Menu
        [sg.Button("Add Sleep", key="-sleep-"), sg.Button("Click Location", key="-click-")],
        [sg.HorizontalSeparator()],
        [sg.Listbox(data_json["tasks"], size=(100, 100))]
    ]
    window = sg.Window("Configure Tasks", layout, size=(600,500))
    while True:
        event, values = window.read()
        exit_type = ""

        if event == sg.WINDOW_CLOSED:
            break
        if event == '-sleep-':
            sleep_num = sg.popup_get_text("Insert sleep Time in Seconds:")
            data_json["tasks"].append(f"sleep({sleep_num})")
            
            exit_type = "reload"
            break
        if event == '-click-':            
            listener = mouse.Listener(on_click=on_click)
            listener.start()
            listener.join()
            
            x, y = pag.position()
            data_json["tasks"].append(f"pag.click({x}, {y})")
            
            exit_type = "reload"
            break
    
    if exit_type == "reload":
        window.close()
        data_json = configure_tasks(data_json)
    else:
        window.close()

    return data_json

layout = [
    [sg.Button("Exec Automation Task", key="-exec-"), sg.Button("New Automation Task", key="-configure-")],
    [sg.HorizontalSeparator()]
]
window = sg.Window("Automation", layout)
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == '-exec-': # Exec a Task
        data = load(open('data.json', 'r'))
        for line in data["tasks"]:
            eval(line)
    if event == '-configure-': # Configure a Task
        data_json = configure_tasks({"tasks":[]})
        print(data_json)

        # Sava Tasks
        data = open('data.json', 'w')
        data.write(dumps(data_json))
        data.close()

window.close()
