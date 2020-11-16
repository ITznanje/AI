import wolframalpha
client = wolframalpha.Client("5PP9E9-Q6T7495XT8")
import PySimpleGUI as sg

sg.theme('Dark Blue 3')	
layout = [  
            [sg.Text('What you want to search'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    res = client.query(values[0])
    sg.Popup(next(res.results).text)

window.close()
