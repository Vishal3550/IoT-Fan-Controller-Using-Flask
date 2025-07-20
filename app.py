from flask import Flask, render_template, jsonify
from master import Master
from slave import Slave
from utils import get_limits
import threading
import time

app = Flask(__name__)
master = Master()
slave = Slave("http://159.89.165.196:5003/sample_temperature")

temperature_high, temperature_low = get_limits()
current_temp = 0.0

def temperature_monitor():
    global current_temp
    while True:
        temp = slave.get_temperature()
        if temp is not None:
            current_temp = temp
            if temp > temperature_high:
                master.motor_on()
            elif temp < temperature_low:
                master.motor_off()
        time.sleep(10)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/status')
def status():
    return jsonify({
        "temperature": current_temp,
        "motor": master.get_motor_state(),
        "limits": {"high": temperature_high, "low": temperature_low}
    })

if __name__ == '__main__':
    t1 = threading.Thread(target=temperature_monitor)
    t1.daemon = True
    t1.start()
    app.run(debug=True)
