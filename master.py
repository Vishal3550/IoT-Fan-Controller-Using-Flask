class Master:
    def __init__(self):
        self.motor_state = "OFF"

    def motor_on(self):
        if self.motor_state != "ON":
            self.motor_state = "ON"
            print("Turning MOTOR: ON")

    def motor_off(self):
        if self.motor_state != "OFF":
            self.motor_state = "OFF"
            print("Turning MOTOR: OFF")

    def get_motor_state(self):
        return self.motor_state
