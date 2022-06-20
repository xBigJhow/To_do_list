import PySimpleGUI as sg
from matplotlib.pyplot import eventplot

def create_window():

    sg.theme(sg.user_settings_get_entry('theme', None))
    
    line = [
        [sg.Checkbox('', key='check'), sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas',layout=line,key='container')],
        [sg.Button(button_text='New Assignment', key='tarefa'), sg.Button(button_text='Reset', key='reset'), sg.Button('Theme', key='-THEME-')]
        
    ]
    return sg.Window('To Do List', layout=layout, finalize=True)

window = create_window()

while True:
    events, values = window.Read()
    if events in (sg.WINDOW_CLOSED, 'Cancel'):
        break
    elif events == 'tarefa':
        window.extend_layout(window['container'], [[sg.Checkbox(''), sg.Input('')]])
    elif events =='reset':
        window.close()
        window = create_window()
    elif events == '-THEME-':
        ev, vals = sg.Window('Choose Theme', [[sg.Combo(sg.theme_list(), k='-THEME LIST-'), sg.OK(), sg.Cancel()]]).read(close=True)
        if ev == 'OK':
            window.close()
            sg.user_settings_set_entry('theme', vals['-THEME LIST-'])
            window = create_window()
            