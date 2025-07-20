# 🌬️ IoT Fan Controller (Flask + JS + HTML/CSS)

A simulated **IoT Fan Controller** web app built with Flask, HTML, CSS, and JavaScript. It mimics a wireless temperature monitoring system, where a **Slave (Sensor)** sends temperature data to a **Master (Controller)**, which decides whether to turn a **Fan ON or OFF** based on predefined limits.

---

## 📌 Features

- 📡 Real-time temperature updates via HTTP request
- ⚙️ Automatically turns Fan ON/OFF based on thresholds
- 🧠 Uses threading for async sensor updates
- 🌐 Beautiful responsive UI with dynamic status cards
- 📊 REST API endpoints for frontend integration

---

## 📁 Project Structure

```

iot-fan-controller/
│
├── app.py               # Flask app with threading logic
├── master.py            # Master controller logic (fan ON/OFF)
├── slave.py             # Slave client logic (temperature fetch)
├── utils.py             # Utility to fetch limits
│
├── static/
│   ├── background.jpg   # Background image for the UI
│   └── style.css        # Custom CSS styles
│
├── templates/
│   └── index.html       # Main HTML frontend
│
└── README.md            # You're here!

````

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/iot-fan-controller.git
cd iot-fan-controller
````

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install flask requests
```

### 4. Run the App

```bash
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔄 How It Works

* **Slave** fetches temperature from:

  ```
  http://159.89.165.196:5003/sample_temperature
  ```
* **Master** checks the temperature:

  * `> high limit`: Fan ON
  * `< low limit`: Fan OFF
* Limits fetched once from:

  ```
  http://159.89.165.196:5003/sample_limits
  ```
* Uses `threading` to continuously update temperature every 10 seconds.

---

## 📷 UI Preview

![Screenshot](static/background.jpg)

---

## 📦 API Endpoints

| Route     | Method | Description                      |
| --------- | ------ | -------------------------------- |
| `/`       | GET    | Loads the web dashboard          |
| `/status` | GET    | Returns current temp & fan state |

---

## 🧑‍💻 Author

**Vishal Kumar**
Full Stack Python Developer
[LinkedIn](https://www.linkedin.com/in/vk959)

---

## 📝 License

This project is licensed under the MIT License.
