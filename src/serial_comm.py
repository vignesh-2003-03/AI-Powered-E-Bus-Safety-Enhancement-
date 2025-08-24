# serial_comm.py
import serial
import threading

class SerialComm:
    def __init__(self, port='COM6', baudrate=115200):
        self.ser = serial.Serial(port, baudrate)
        self.exit_program = False
        self.thread = threading.Thread(target=self.receive_data)
        self.thread.daemon = True
        self.thread.start()

    def send(self, message: str):
        """Send a message to Arduino"""
        if self.ser.is_open:
            self.ser.write(message.encode())

    def receive_data(self):
        """Run in a background thread to receive messages"""
        try:
            while not self.exit_program:
                if self.ser.in_waiting > 0:
                    data = self.ser.readline().decode('utf-8').rstrip()
                    print(f"[Arduino] {data}")
        except serial.SerialException as e:
            print(f"[Serial Error] {e}")

    def close(self):
        """Close serial safely"""
        self.exit_program = True
        if self.ser.is_open:
            self.ser.write("rst".encode())  # send reset
            self.ser.close()
        self.thread.join()
