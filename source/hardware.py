import serial


class Hardware:

    def __init__(self):
        self.serial_connection = serial.Serial()
        self.serial_connection.baudrate = 19200
        self.serial_connection.port = "COM1"
        self.is_comm_enabled = False
        if self.is_comm_enabled:
            self.serial_connection.open()

    def __del__(self):
        if self.is_comm_enabled:
            self.serial_connection.close()

    def read_from_port(self):
        print(self.serial_connection.readline())

    # Serial commands
    #
    # Handlebar
    # Forward / backward      4FL     (minus is forward)
    # up / down               2FL     (minus is down)
    #
    # Saddle
    # Forward / backward      1FL     (minus is backward)
    # up / down               3FL     (minus is down)
    #
    # 1 mm: 10000
    # 1 cm: 100000

    @staticmethod
    def get_serial_prefix(position):
        if 'Handlebars' in position:
            if "x" in position:
                return "4FL"
            elif "y" in position:
                return "2FL"
        elif "Saddle" in position:
            if "x" in position:
                return "1FL"
            elif "y" in position:
                return "3FL"
        print("Couldn't construct a serial command.")
        return ""

    @staticmethod
    def get_serial_suffix(position, millimeters=1):
        if "Saddle" in position and "x" in position:
            millimeters *= -1  # see notes, this position is flipped
        return str(millimeters * 10000)

    def increment_position(self, position, millmeters=1):
        serial_command = self.get_serial_prefix(position)
        if len(serial_command) < 1:
            return
        serial_command += self.get_serial_suffix(position, millmeters)
        self.write_serial_command(serial_command)

    def decrement_position(self, position, millimeters=-1):
        serial_command = self.get_serial_prefix(position)
        if len(serial_command) < 1:
            return
        serial_command += self.get_serial_suffix(position, millimeters)
        self.write_serial_command(serial_command)

    def write_serial_command(self, command):
        print("Writing: ", command, " to serial connection:", self.serial_connection)
        if self.is_comm_enabled:
            self.serial_connection.write(command)
