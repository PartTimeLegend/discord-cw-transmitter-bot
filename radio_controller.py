import serial
import serial.tools.list_ports

class RadioController:
    @staticmethod
    def autodetect_radio():
        ports = serial.tools.list_ports.comports()

        for port in ports:
            try:
                ser = serial.Serial(port.device, baudrate=9600, timeout=1)
                ser.write(b'IDN?\n')
                response = ser.readline().strip().decode()
                ser.close()

                if "IC-7300" in response:
                    return port.device
            except serial.SerialException:
                continue

        return None

    @staticmethod
    def send_message_to_radio(frequency, message):
        radio_port = RadioController.autodetect_radio()
        if radio_port:
            try:
                ser = serial.Serial(radio_port, baudrate=9600, timeout=1)
                ser.write(f'F{frequency}\n'.encode())
                ser.write(message.encode())
                ser.close()
                print(f"Message sent to radio on frequency {frequency}:", message)
            except Exception as e:
                print("Error:", e)
        else:
            print("No IC-7300 radio found.")
