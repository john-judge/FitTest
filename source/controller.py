import numpy as np
import threading
import time
import string
import PySimpleGUI as sg


class Controller:

    def __init__(self, data, production_mode=True):
        sg.theme('DarkBlue12')

        self.title = "Rocket Bicycle Studio Fitting Session"
        self.window = None
        self.main_workflow()

    def main_workflow(self):
        right_col = self.layouts.create_right_column(self)
        left_col = self.layouts.create_left_column(self)
        toolbar_menu = self.layouts.create_menu()

        layout = [[toolbar_menu],
                  [sg.Column(left_col),
                   sg.VSeperator(),
                   sg.Column(right_col)]]

        self.window = sg.Window(self.title,
                                layout,
                                finalize=True,
                                element_justification='center',
                                resizable=True,
                                font='Helvetica 18')
        self.window.Maximize()
        self.main_workflow_loop()
        self.window.close()

    def main_workflow_loop(self, history_debug=False, window=None, exit_event="Exit"):
        if window is None:
            window = self.window
        events = ''
        while True:
            event, values = window.read()
            if history_debug and event is not None and not self.production_mode:
                events += str(event) + '\n'
            if event == exit_event or event == sg.WIN_CLOSED or event == '-close-':
                if self.is_recording():
                    self.data.save_metadata_to_json()
                    print("Cleaning up hardware before exiting. Waiting until safe to exit (or at most 3 seconds)...")

                    self.hardware.set_stop_flag(True)
                    timeout = 3
                    while self.hardware.get_stop_flag() and timeout > 0:
                        time.sleep(1)
                        timeout -= 1
                        print(timeout, "seconds")
                break
            elif event not in self.event_mapping or self.event_mapping[event] is None:
                print("Not Implemented:", event)
            else:
                ev = self.event_mapping[event]
                if event in values:
                    ev['args']['window'] = window
                    ev['args']['values'] = values[event]
                    ev['args']['event'] = event
                ev['function'](**ev['args'])
        if history_debug and not self.production_mode:
            print("**** History of Events ****\n", events)
