import serial


class Hardware:

    def __init__(self):
        self.serial_connection = serial.Serial()
        self.serial_connection.baudrate = 19200
        self.serial_connection.port = "COM1"
        # self.serial_connection.open()

    def __del__(self):
        pass  # self.serial_connection.close()

    def read_from_port(self):
        print(self.serial_connection.readline())

    def increment_position(self, position):
        if 'Saddle' in position:
            self.increment_saddle()
        elif "Handlebars" in position:
            self.increment_handlebars()

    def decrement_position(self, position):
        if 'Saddle' in position:
            self.decrement_saddle()
        elif "Handlebars" in position:
            self.decrement_handlebars()

    def increment_saddle(self, amount=0.5):
        print("TO DO: write hexademical command for decrement saddle to port", self.serial_connection)
        # self.serial_connection.write(command)

    def decrement_saddle(self, amount=0.5):
        print("TO DO: write hexademical command for increment saddle to port", self.serial_connection)
        # self.serial_connection.write(command)

    def increment_handlebars(self, amount=0.5):
        print("TO DO: write hexademical command for increment handlebars to port", self.serial_connection)
        # self.serial_connection.write(command)

    def decrement_handlebars(self, amount=0.5):
        print("TO DO: write hexademical command for decrement handlebars to port", self.serial_connection)
        # self.serial_connection.write(command)
