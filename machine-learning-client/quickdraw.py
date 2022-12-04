from tensorflow.keras.models import load_model
import numpy as np
from random import choice
from PIL import Image
import base64
import io

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
	# print(image)
	for i in range(0, len(image)):
		for j in range(0, len(image[i])):
			for k in range(0, len(image[i][j])):
				if(image[i][j][k] > 0):
					image[i][j][k] += 2
	prediction = model.predict(np.expand_dims(image, axis=0))[0]
	print(max(prediction))
	if max(prediction) < 0.5:
		return 0
	ind = (-prediction).argsort()[:5]
	result = [ classes[x] for x in ind]
	print(result)
	print(result.index(category)+1)
	if (result.index(category)+1==1):
		score = 20
	elif (result.index(category)+1==2):
		score = 15
	elif (result.index(category)+1==3):
		score = 10
	elif (result.index(category)+1==4):
		score = 5
	else:
		score = 0
	

	try:
		return score, result.index(category)+1, category
	except ValueError:
		return 0

 