from tensorflow.keras.models import load_model
import numpy as np
from random import choice
from PIL import Image
import base64
import io
import pymongo

def initialize():
	model = load_model('keras10objects.h5')
	f = open("categories.txt","r")
	classes = f.read().split('\n')[:-1]
	f.close()
	return model, classes

def getObject(classes):
	return choice(classes)
	
def predict(model, classes, image, category):
	image = base64.b64decode(image)
	image = Image.open(io.BytesIO(image)).convert('L').resize((28, 28))
	image = np.array(image).reshape(28,28,1).astype('float32')/255.0
	prediction = model.predict(np.expand_dims(image, axis=0))[0]
	ind = (-prediction).argsort()[:5]
	predictions = [prediction[x] for x in ind]
	print(predictions)
	result = [ classes[x] for x in ind]
	print(result)
	try:
		return result.index(category)+1
	except ValueError:
		return 0

 