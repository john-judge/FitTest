import serial
import time


class Hardware:

    def __init__(self):
        self.is_comm_enabled = True
        self.serial_connection = self.motor_init()
        if self.is_comm_enabled:
            try:
                self.serial_connection.open()
                time.sleep(1)
                print(self.serial_connection)
            except serial.serialutil.SerialException:
                print("Failed to open serial port")

            if self.serial_connection.isOpen():
                try:
                    self.serial_connection.flushInput()
                    self.serial_connection.flushOutput()
                    self.motor_setup()  # Complete motor setup and enable motor

                except Exception as e1:
                    print("Error Communicating...: " + str(e1))
            else:
                print("Cannot open serial port ")

    def __del__(self):
        if self.is_comm_enabled:
            self.serial_connection.close()

    @staticmethod
    def motor_init():
        ser = serial.Serial()
        ser.port = "COM5"
        ser.baudrate = 9600
        ser.bytesize = serial.EIGHTBITS
        ser.parity = serial.PARITY_NONE
        ser.stopbits = serial.STOPBITS_ONE
        ser.timeout = .1
        ser.xonxoff = False
        ser.rtscts = False
        ser.dsrdtr = False
        ser.writeTimeout = 0
        return ser

    def motor_setup(self):
        """
        Setup initial motor parameters, also resets alarm
        """
        self.write_serial_command('EG20000') # Sets microstepping to 20,000 steps per revolution
        self.write_serial_command('IFD') # Sets the format of drive responses to decimal
        self.write_serial_command('SP0') # Sets the starting position at 0
        self.write_serial_command('AR') # Alarm reset
        self.write_serial_command('AC10') # Acceleration
        self.write_serial_command('DE15') # Deceleration
        self.write_serial_command('VE10') # Velocity
        self.write_serial_command('ME')  # Enable Motor

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
        return str(int(millimeters * 10000))

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
        print("Writing: ", command,
              " to serial connection:", self.serial_connection)
        if self.is_comm_enabled:
            # When we send a serial command, the program will check and print
            # the response given by the drive.
            self.serial_connection.write((command + '\r').encode())
            response = self.serial_connection.read(15).decode()
            if len(response) > 0:
                print(response)
