import PySimpleGUI as sg
import cv2
import multiprocessing as mp
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
from matplotlib.figure import Figure
import sqlite3

power_db = "/home/pi/LCM-AutoBoat/testScripts/actuation_power.db"

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def gui_func():
    sg.theme('Black')

    left_col = [[sg.Text('Camera View')],
                [sg.Canvas(background_color=sg.theme_button_color()[1], size=(640,480))],
                [sg.Text('Camera View')]]

    right_col = [[sg.Text('Computation Power')],
                [sg.Canvas(background_color=sg.theme_button_color()[1], size=(640,225), key='-CANVAS-')],
                [sg.Text('Actuation Power')],
                [sg.Canvas(background_color=sg.theme_button_color()[1], size=(640,225))]]



    layout = [[sg.Frame(layout=left_col, title=''), sg.Frame(layout=right_col, title='')]]


    window = sg.Window('LEAN Robot GUI', layout, finalize=True)

    canvas_elem = window['-CANVAS-']
    canvas = canvas_elem.TKCanvas

    fig = Figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.grid()
    fig_agg = draw_figure(canvas, fig)

    while True:
        event, values = window.read(timeout=10)
        if event in ('Exit', None):
            exit(69)
            break

        ax.cla()                    # clear the subplot
        ax.grid()                   # draw the grid

        with sqlite3.connect(power_db) as c:
            data_entries = c.execute('''SELECT * FROM actuation_power_data WHERE source = ? ORDER BY rowid DESC LIMIT 5;''', ("ACTUATION",)).fetchall()
            power_y = []
            time_x = []
            for entry in data_entries:
                power_y.append(entry[3])
                time_x.append(entry[4])

        ax.plot(time_x, power_y,  color='purple')
        fig_agg.draw()

    window.close()

gui_func()