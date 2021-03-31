'''

main script  Hornetparking.py 

'''
import RPi.GPIO as GPIO
from flask import Flask, render_template
import datetime

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#define actuators GPIOs
operat = 13
l1full = 19
l2full = 26
#initialize GPIO status variables
operatSts = 0
l1fullSts = 0
l2fullSts = 0
# Define led pins as output
GPIO.setup(operat, GPIO.OUT)   
GPIO.setup(l1full, GPIO.OUT) 
GPIO.setup(l2full, GPIO.OUT) 
# turn leds OFF 
GPIO.output(operat, GPIO.LOW)
GPIO.output(l1full, GPIO.LOW)
GPIO.output(l2full, GPIO.LOW)

@app.route('/')
def page():
   now = datetime.datetime.now()
   timeString = now.strftime("%H:%M") 
   datestamp = now.strftime("%Y-%m-%d")  
   # Read Sensors Status
   operatSts = GPIO.input(operat)
   l1fullSts = GPIO.input(l1full)
   l2fullSts = GPIO.input(l2full)
   templateData = {
      'title' : 'Hornet Parking',
      'greeting' : 'Welcome to Hornet Parking',
      'csus' : 'California State University, Sacramento',
      'saying' : "Sac State's best parking",
      'date': datestamp,
      'time': timeString,
      'operat'  : operatSts,
      'l1full'  : l1fullSts,
      'l2full'  : l2fullSts  
   }
   return render_template('hornetparking.html', **templateData)

@app.route('/login')
def login():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d, %H:%M")
   templateData = {
      'title' : 'Hornet Parking',
      'greeting' : 'Welcome to Hornet Parking',
      'csus' : 'California State University, Sacramento',
      'saying' : "Sac State's best parking",
      'time': timeString
    }
   return render_template('log_in.html', **templateData)

@app.route("/home")
def hornet():
   now = datetime.datetime.now()
   timeString = now.strftime("%H:%M") 
   datestamp = now.strftime("%Y-%M-%D")  
      # Read Sensors Status
   operatSts = GPIO.input(operat)
   l1fullSts = GPIO.input(l1full)
   l2fullSts = GPIO.input(l2full)
   templateData = {
      'title' : 'Hornet Parking',
      'greeting' : 'Welcome to Hornet Parking',
      'csus' : 'California State University, Sacramento',
      'saying' : "Sac State's best parking",
      'date': datestamp,
      'time': timeString,
      'operat'  : operatSts,
      'l1full'  : l1fullSts,
      'l2full'  : l2fullSts  
   }
   return render_template('hornet.html', **templateData)

@app.route('/override')
def override():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d, %H:%M")
   # Read Sensors Status
   operatSts = GPIO.input(operat)
   l1fullSts = GPIO.input(l1full)
   l2fullSts = GPIO.input(l2full)
   templateData = {
      'time': timeString,
      'operat'  : operatSts,
      'l1full'  : l1fullSts,
      'l2full'  : l2fullSts    
   }
   return render_template('override.html', **templateData)

@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	now = datetime.datetime.now()
	timeString = now.strftime("%Y-%m-%d, %H:%M")

	if deviceName == 'operat':
		actuator = operat		
	if deviceName == 'l1full':
		actuator = l1full
	if deviceName == 'l2full':
		actuator = l2full

	if action == "on":
		GPIO.output(actuator, GPIO.HIGH)
	if action == "off":
		GPIO.output(actuator, GPIO.LOW)
		
	operatSts = GPIO.input(operat)
	l1fullSts = GPIO.input(l1full)
	l2fullSts = GPIO.input(l2full)
	
	templateData = {
	      'time': timeString,
         'operat'  : operatSts,
         'l1full'  : l1fullSts,
         'l2full'  : l2fullSts,
	}
	return render_template('override.html', **templateData)
   
@app.route('/camera')
def camera():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d, %H:%M")
   templateData = {
      'title' : 'Hornet Parking',
      'greeting' : 'Welcome to Hornet Parking',
      'csus' : 'California State University, Sacramento',
      'saying' : "Sac State's best parking",
      'time': timeString
   }
   return render_template('camera.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
