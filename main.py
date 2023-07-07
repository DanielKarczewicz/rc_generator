import serial


def main():
    try:
        serial_interface = serial.Serial("COM9", 115200, timeout=1)
    except serial.SerialException:
        print("could not open port")
        exit()
    print("port opened!")
    while(True):
        try:
            msg = serial_interface.readline()
            msg = msg.decode("utf-8")
            print(msg[:-2])
        except KeyboardInterrupt: break
    serial_interface.close()

if __name__ == "__main__":
    main()