import PySimpleGUI as sg


class Layouts:

    def __init__(self):
        self.plot_size = (1500, 800)
        self.timer64 = 'data:image/png;base64,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'
        self.close64 = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsSAAALEgHS3X78AAAE30lEQVRIiZ2VXYgdRRqGn6+quvucM/85iRoTNevMBJFEWY0GFQTBC1HBlaz/jMpoFFfXBdmFvdiLvRIEFRHFGBXMjUQhF/6Bol6sSNaIruCNir/R/Dlx5iRzck736e6qby/6JDlx9CIWFN10Ue/7vW+9X7XcDn8bryWPL2vERkNQQPj9Q72K7F3s7Hxb9bZ98L0bj91jt1y23kxNTxIEGUQ/aTYR6WW9cud/Prx01zf7/7FP5EHXHG7Y6bVTpBPLMSegCWKEEMKvkihgjEWDP+FbEjxTa1bjv9l/CsIKF3ypHhUDSFGACCKC956iKKjV6/hfkCjgUNK0TW1oCA3h+EJk8UUBYFCsQaSyRajArUWLnEONcTrT68nTLtZaEKmmMTiUlsREGy9HO0dgcL1y6lgtZrAsEYFexhwxq2buYfru+1mcOo+828UYg4rgUH7OSkY3zbDq1lkaV1yFP9TqEyy18jiBCMF7DjYmOOu+hxifnCSKItZuvp/F6fPJ05TEwE+dHhN33MfpGy4iFAVjf7qF8etvBV9y1IilBApGIMt6TExOM372JKqKqhLFMdOz93Jk6jx+bHVoztzLyj9eiHqP2Gq7O3UlGAuq1RwYDlUwhoChMdSAz3ZxaEeD8T/fBggaAnGtxpqZWdKFBSbOPLMCCQGJItJPdrHw4lOYRgNsBM6dSCDGErIuodtGkhoyPEr68U5svcbI1ZsQY0CV2vAw9ZGRKjEiSBTR/fQjDm9/AddcjqoSul182kYHVDhJauRffUH7wD7ilatxzVOwI6PM7XiJLO2x4rob0CgGVTSEKigidD94j/ltW9Dg0b0/4BfmyQ8ewKUdWLZ6wCIB9SXFXJvQ+hLkc6QeEznHf199jY1rpjh1w0ZUFTGm7z18/tSj2Hffor5shKLdhhJCADMcw7IlKRIkAqkJRIa4LPl6d5c/PPJkBd5vpArcArD+ue101l1Md08bFxuIBUlOyOUggUIAVIl94Kv5wKqtz7L+7r/0bRHEmApcFbwnHhljw6tv0b3kEtK5gDWmj/GbfQAWZbdaztjyPOfP3oN6D8GDCO133uDAvx9CyxKsRX1JMjbBBa+8Rnbl5RSpR35RfXUGfVLnYGFBcTfdwLo77yLkPYy14CLa773JngfuoNy7QOh2WPnw09WVkufUm8s598G/s+eT9wmBJZ1m+sVTFNBc4Wi8vJ3v//kAJk7AOhbf3MGezTfjWwuYCcv8s1s58K+/okWOxDGdjz5g7+YZtKRSoL+igCp5FKVntGk48sTTzDWb1C+4mB833wgETD2CELBjEfNbtyAjo4xdcz27N11L6B5GGoZQhN+26KiSoII9LebnJx9BkggzNIQkyfEdItiRQGvbM7S2bQHJMGN1NO8ds2dQhBORYBCjAFEE1kFSw0QxuAiTJCAGce64vz4gviTkOTJcErIMMRbyDIxg7bHTFnc47clcmpdj43VkeBRJEkytgdTqSL2OiRMkSRDroH9t4EtCUaBZhmYpIUurZ9pFfVnuX+w62xfjeq3D3/6vbifXrT1XkzgWdREmipA4RlwMUYRY21cg/X+lJ5gSbIHGOVovCHmOCSX7DrbMx599icIhVI2cA5c5mC1gbGnITm4oqAOr0PoOXs9g51HAGiITyCDByXDp4KuiaoESmP8/YC0Y5GajmEsAAAAASUVORK5CYII='
        self.psg64 = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAMAAADXqc3KAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAABlbkiVhkyZikyFjmShjkyhlly1mli5nlylnmS5olyppnC5qmi5rmzBpmDBpmTFqmDFqmTFqmjNrmzFrnDNsmzJsnDJtnTFunjNvnzRsmTRtmzVunTVunjVvnzZwnjlxny5toDFvozJwoTNzpjVwoDRzpDRzqDd4rThyojp0ozl1pTt2pjt3pz11ozt4qDl4qTp6rTl6rzx4qD55qTx5qj97qz17rT58rD98rT9+rz5+sEB3pEF9rkB+r0F+sEF/sT2AtD6AtT6Btk+Aqk2CrEOBs0GBtEKCtEGCtUSBskWBs0SCtEWDtUaEtkWFt0aGt0KFuUCEukOGu0eFuEWHu0eJvEiGuUiHukiIuUiIukmJu0uKvEyKvFCAp1CCqlODrVKCrl2Kr1OEs1KGsFWGsFaIsVaPvFqKsl6NsmKNsWeTuG6YvHadvlySwV6UxF+YxW+bxW6dxnKewHGex3SdwHSfx3egwXGizHmgwHqkxnyjxHio0f/RMf7QMv/TMf/SMv3SNf7UOv7UO//UPP/UPf/UPv/VP//WPP/XPv/VQ//WQv7XQ//WRP/XRf/WR//YRv/YSP/YSf/YSv/ZS//aS//ZTf/aTP7aTf7aTv7bT//cT//bUP/cUP7cUv/cU/7cVf/eVf/fVv/eV/7dWP/eWP/eWf/fWv/fW//fYvzcaf/hW//gXP/gXv/gX//hYP/hYf/hY//iYP/jY//gZf/iZP7iZf/jZv/iZ//lZv/jaf/kav7ka//maf/ma//kbf/lbv7mbP/mbv/mb//id//mcP/ncv/nc//ld//ndv/meP/ocf/ocv/oc//odP/odf/odv/peP/pff/qfY+11ZSzz5G41qC81aW/1P/jgf/qiv/qjv7qoMnZ5szb587d6eDm2+fo1+7v3e/x3vXw1fHx3gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJblQd8AAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAABcQAAAXEAEYYRHbAAAAGHRFWHRTb2Z0d2FyZQBwYWludC5uZXQgNC4xLjFjKpxLAAABzUlEQVQoU2P4jwNAJZIEuLJA9M2u/iNgAaiEELOgIFPc//+r6puaalvAQmAJdg4pPj4h5oT/2+raWtqaGmAS/PxC/IJAGdbEB7saW5pb20AyQAkFNiFhUSEgkGZNfjizua29u70XJJHr8j+eV0RGVkRMTJb56u2mvt7eSR0gCT2gPsbMGzbi8hJyPDl3OidPnDRlwhagRHbG/zTXe5WSqqqqmpzXb/VMmz5jztSVIDtSWFLvl3Jrampq8ZY8WThj1tx586ZCXFV9t1xRR1tbR6Lw0f6ZC+YvWDAb6tz/xUom+rrGymWPD8xaunjZ0oUgMZBEsYqZqampWsnTY/PWLF+xZhFIHCRRpW5raWFhUPT/3IJ1a9euW/H//5oTYAlDezs7Kwvv//+XbN6wcev6//+3/z8FltDwcrC3N8/7v3rHtu07Nv3/vxVo0CWQhJGPm5ubdf7/TXt279699//JnTA70j38fH19wv//33b00OGj+w6fPXz5KMRVTiH+/gHuFf//7zl+5szZs2fO7YPo+H/FOSIyPMqz5v//g+dAMocvQCX+XwsMjYmNdgSy9p0/d/bgRZAYWOL//4LgoDAwY+++02AaJoEJcEj8/w8A4UqG4COjF7gAAAAASUVORK5CYII='
        self.github64 = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAMAAADXqc3KAAAABGdBTUEAALGPC/xhBQAAAwBQTFRFAAAADAwMDQ0NAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAhyjGAAAAQB0Uk5T////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////AFP3ByUAAAAJcEhZcwAADdUAAA3VAT3WWPEAAAAYdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjEuMWMqnEsAAABzSURBVChTbYxRFoAgDMPQ+98Z1zbIeJqPbU3RMRfDECqyGpjMg6ivT6NBbKTw5WySq0jKt/sHrXiJ8PwpAAVIgQGkwABSYAApMIAUGEAalFmK9UJ24dC1i7qdj6IO5F+xnxfLu0jS0c7kqxd3Dk+JY8/5AKFrLuM7mfCAAAAAAElFTkSuQmCC'

    def create_menu(self):
        menu_def = [['Rocket Bicycle Studio', ['Help', 'About']],
                    ['File', ['Export Fit', 'Import Fit', 'Exit']]]
        toolbar_buttons = [[sg.Button('', image_data=self.close64[22:],
                                      button_color=('white', sg.COLOR_SYSTEM_DEFAULT),
                                      pad=(0, 0), key='-close-',
                                      tooltip="Exit"),
                            sg.Button('', image_data=self.timer64[22:],
                                      button_color=('white', sg.COLOR_SYSTEM_DEFAULT),
                                      pad=(0, 0), key='-timer-',
                                      tooltip="Link to bike database"),
                            sg.Button('', image_data=self.github64[22:],
                                      button_color=('white', sg.COLOR_SYSTEM_DEFAULT),
                                      tooltip='User manual',
                                      pad=(0, 0), key='-github-'),
                            sg.Button('', image_data=self.psg64[22:],
                                      button_color=('white', sg.COLOR_SYSTEM_DEFAULT),
                                      pad=(0, 0), key='-psg-',
                                      tooltip="Submit an issue to request a bug fix or new feature."),
                            ]]
        layout = [[sg.Menu(menu_def, )],
                  [sg.Frame('', toolbar_buttons, title_color='white',
                            background_color=sg.COLOR_SYSTEM_DEFAULT, pad=(0, 0))],
                  ]
        return layout

    @staticmethod
    def create_file_browser():
        return [[
            sg.In(size=(25, 1), enable_events=True, key="-FILE-"),
            sg.FileBrowse(key="file_window.browse",
                          # file_types=(("Raw Data Files", "*.zda"))
                          )],
            [sg.Button("Open", key='file_window.open')]]

    @staticmethod
    def create_save_as_browser(file_types):
        return [[
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FileSaveAs(key="save_as_window.browse", file_types=file_types)],
            [sg.Button("Save", key='save_as_window.open')]]

    def create(self, dfu):
        main_layout = self.create_main_layout(dfu)
        toolbar_menu = self.create_menu()
        return [[toolbar_menu],
                main_layout]

    @staticmethod
    def create_arrowed_field(position_name, x, y):
        up_symbol = '▲'
        left_symbol = '◀'
        right_symbol = '▶'
        down_symbol = '▼'
        corner_spaces = (12, 1)
        edge_spaces = (3, 1)
        button_size = (6, 1)
        half_button_size = (5, 1)
        return [
            [
                sg.Text('', size=corner_spaces),
                sg.Button(up_symbol, size=button_size, key=position_name + '_y+', enable_events=True),
                sg.Text(position_name, size=corner_spaces)],
            [
                sg.Text('', size=edge_spaces),
                sg.Button(left_symbol, size=button_size, key=position_name + '_x-', enable_events=True),
                sg.InputText(default_text=x.get_value(), size=half_button_size, enable_events=False, key=position_name + '_x',
                             tooltip="Horizontal " + position_name + " Measurement (mm)", disabled=True),
                sg.InputText(default_text=y.get_value(), size=half_button_size, enable_events=False, key=position_name + '_y',
                             tooltip="Vertical " + position_name + " Measurement (mm)", disabled=True),
                sg.Button(right_symbol, size=button_size, key=position_name + '_x+', enable_events=True),
                sg.Text('', size=edge_spaces)],
            [
                sg.Text('', size=corner_spaces),
                sg.Button(down_symbol, size=button_size, key=position_name + '_y-', enable_events=True),
                sg.Text('(mm)', size=corner_spaces)]
        ]

    def create_main_layout(self, dfu):
        button_size = (6, 1)
        long_button_size = (10, 1)
        return [
            [sg.Column(self.create_arrowed_field(dfu.handlebars.name,
                                                 dfu.handlebars.x,
                                                 dfu.handlebars.y)),
             sg.Column([[sg.Image(key="RBS IMAGE")]]),
             sg.Column(self.create_arrowed_field(dfu.saddle.name,
                                                 dfu.saddle.x,
                                                 dfu.saddle.y))],
            [sg.Slider(range=(1, 10),
                       default_value=dfu.step_size,
                       resolution=1,
                       enable_events=True,
                       size=(20, 40),
                       orientation='horizontal',
                       tooltip="Adjusts the step size from 1-10 mm",
                       key="step size")],
            [sg.Button("Reset",
                       key="reset",
                       size=button_size,
                       enable_events=True),
             sg.Button("Find Bikes",
                       key="find bikes",
                       size=long_button_size,
                       enable_events=True)
             ],
            [sg.Image(key="BIKE IMAGE")],
            [sg.HorizontalSeparator()],
        ]
