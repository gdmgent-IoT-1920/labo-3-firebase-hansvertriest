from sense_hat import SenseHat
import firebase_admin
from firebase_admin import credentials, firestore

# constants
COLLECTION = 'matrix'
DOCUMENT = 'matrix'
NEIGHBOURS_NEEDED = 3

# firebase
cred = credentials.Certificate("./pidashboard-866ea-firebase-adminsdk-6h13v-78b029c611.json")
firebase_admin.initialize_app(cred)

# sensehat 
sense = SenseHat()
sense.set_imu_config(False, False, False)
sense.clear()

# def convertDictToPixels(pixel_dict):
# 	off = [0,0,0]
# 	array = [
# 		off, off, off, off, off, off, off, off,
# 		off, off, off, off, off, off, off, off,
# 		off, off, off, off, off, off, off, off,
# 		off, off, off, off, off, off, off, off,
# 		off, off, off, off, off, off, off, off,
# 		off, off, off, off, off, off, off, off,
# 		off, off, off, off, off, off, off, off,
# 		off, off, off, off, off, off, off, off,
# 	]

# 	for key in pixel_dict:
# 		column  = key[6:7]
# 		row  = key[8:9]
# 		number = (8 * int(row)) + int(column)
# 		print(pixel_dict[key])
# 		array[number] = pixel_dict[key]
# 	return array

def setPixels(pixels_dict):
	for key in pixels_dict:
		if key != "dummy":
			column  = int(key[6:7])
			row  = int(key[8:9])
			sense.set_pixel(row, column, pixels_dict[key][0], pixels_dict[key][1], pixels_dict[key][2])

def update_sensehat(col_snapshot, changes, read_time):
	sense.clear()
	for doc in col_snapshot:
		doc_readable = doc.to_dict()
		setPixels(doc_readable)


# connect firestore
db = firestore.client()
pi_ref = db.collection(COLLECTION)
pi_watch = pi_ref.on_snapshot(update_sensehat)

# app
while True:
    pass
