import PySimpleGUI as sg

from source.layouts import Layouts
from source.field import EventMapping
from source.dynamic_fit_unit import DynamicFitUnit
from source.hardware import Hardware


class Controller:

    def __init__(self):
        sg.theme('DarkBlue12')
        self.layouts = Layouts()

        # Default positions
        self.handlebars_default = [0, 0]
        self.saddle_default = [0, 0]
        self.saddle_bounds = [[-250, 250], [-250, 250]]
        self.handlebars_bounds = [[-250, 250], [-250, 250]]
        self.step_size = 10
        self.dfu = DynamicFitUnit(self.saddle_default,
                                  self.handlebars_default,
                                  self.saddle_bounds,
                                  self.handlebars_bounds,
                                  self.step_size)

        self.hardware = Hardware()
        if not self.hardware.is_hardware_connected():
            self.notify_window("Hardware not connected",
                               "The serial port for the Dynamic Fitting Unit, COM5,"
                               " could not be opened.")
        self.event_handler = EventMapping(self.dfu)

        self.title = "Cyclist Fitting Session"
        self.window = None
        self.main_workflow()

    def main_workflow(self):

        layout = self.layouts.create(self.dfu)

        self.window = sg.Window(self.title,
                                layout,
                                finalize=True,
                                element_justification='center',
                                resizable=True,
                                font='Helvetica 18')
        self.window["BIKE IMAGE"].update(filename='source/images/bike.png')
        self.window["RBS IMAGE"].update(filename='source/images/rbs.png')

        self.create_field_bindings(self.dfu.get_fields())

        #self.window.Maximize()
        self.main_workflow_loop()
        self.window.close()

    def main_workflow_loop(self, debug=False, window=None, exit_event="Exit"):
        if window is None:
            window = self.window
        events = ''
        while True:
            event, values = window.read()
            if debug and event is not None:
                print(event)
            if event == exit_event or event == sg.WIN_CLOSED or event == '-close-':
                break
            if event in ["Import Fit", "Export Fit"]:
                self.file_handler(event)
            if event == "step size":
                self.set_step_size(values[event])
            if event == "reset":
                self.event_handler.saturate_lower_limits(["Saddle_x", "Saddle_y", "Handlebars_x", "Handlebars_y"],
                                                         self.saddle_bounds + self.handlebars_bounds)
            else:
                self.event_handler.handle_event(event)

    def create_field_bindings(self, field_list):
        for f in field_list:
            f.gui_element = self.window[f.field_name]
            f.hardware = self.hardware

    def file_handler(self, event):
        if event == "Import Fit":
            file = self.browse_for_file()
            if file is not None:
                self.event_handler.import_file(file)
        elif event == 'Export Fit':
            file = self.browse_for_save_as_file()
            if file is not None:
                self.event_handler.export_file(file)

    def browse_for_file(self, file_extensions=('json')):

        layout_choice = self.layouts.create_file_browser()
        file_window = sg.Window('File Browser',
                                layout_choice,
                                finalize=True,
                                element_justification='center',
                                resizable=True,
                                font='Helvetica 18')
        file = None
        # file browser event loop
        while True:
            event, values = file_window.read()
            if event == sg.WIN_CLOSED or event == "Exit":
                file_window.close()
                return
            elif event == "file_window.open":
                file = values["file_window.browse"]
                file_ext = file.split('.')
                if len(file_ext) > 0:
                    file_ext = file_ext[-1]
                else:
                    file_ext = ''
                if file_ext not in file_extensions:
                    supported_file_str = " ".join(file_extensions)
                    self.notify_window("File Type",
                                       "Unsupported file type.\nSupported: " + supported_file_str)
                else:
                    break

        file_window.close()
        return file

    @staticmethod
    def notify_window(title, message):
        layout = [[sg.Column([
            [sg.Text(message)],
            [sg.Button("OK")]])]]
        wind = sg.Window(title, layout, finalize=True)
        while True:
            event, values = wind.read()
            # End intro when user closes window or
            # presses the OK button
            if event == "OK" or event == sg.WIN_CLOSED:
                break
        wind.close()

    def browse_for_save_as_file(self, file_types=(("JSON file", "*.json"),)):
        w = sg.Window('Save As',
                      self.layouts.create_save_as_browser(file_types),
                      finalize=True,
                      element_justification='center',
                      resizable=True,
                      font='Helvetica 18')
        new_file = None
        # file browser event loop
        while True:
            event, values = w.read()
            if event == sg.WIN_CLOSED or event == "Exit":
                w.close()
                return
            elif event == "save_as_window.open":
                new_file = values["save_as_window.browse"]
                break

        w.close()
        if new_file is None or len(new_file) < 1:
            return None
        return new_file

    def set_step_size(self, size):
        self.dfu.step_size = size

