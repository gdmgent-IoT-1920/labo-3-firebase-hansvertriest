from sense_hat import SenseHat
import firebase_admin
from firebase_admin import credentials, firestore
import time

# constants
COLLECTION = 'data'
DOCUMENT = 'metrics'
NEIGHBOURS_NEEDED = 3

# firebase
cred = credentials.Certificate("./config.json")
firebase_admin.initialize_app(cred)


# connect firestore
db = firestore.client()
pi_ref = db.collection(COLLECTION).document(DOCUMENT)

# sensehat 
sense = SenseHat()
sense.set_imu_config(False, False, False)
sense.clear()

def getData():
	return {
		# u'date' : datetime.now,
		u'temp' : sense.get_temperature(),
		u'pressure' : sense.get_pressure(),
		u'humidity' : sense.get_humidity(),
	}



# app
while True:
	pi_ref.set(getData())
	time.sleep(60)
