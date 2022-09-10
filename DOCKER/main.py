from fastapi import FastAPI
import pickle
import numpy as np
import uvicorn

app = FastAPI()

model = None

def load_local_model():
	global model
	with open('RandomF_hongos.pickle', 'rb') as f:
	    # The protocol version used is detected automatically, so we do not
	    # have to specify it.
	    model = pickle.load(f)


@app.post("/predict/{x1}/{x2}/{x3}/{x4}/{x5}/{x6}/{x7}/{x8}/{x9}/{x10}/{x11}/{x12}/{x13}/{x14}/{x15}/{x16}/{x17}/{x18}/{x19}/{x20}/{x21}")
def predict(x1: int, x2: int, x3: int, x4: int,x5: int, x6: int, x7: int, x8: int,x9: int, x10: int, x11: int, x12: int, x13: int, x14: int, x15: int, x16: int, x17: int, x18: int, x19: int, x20: int, x21: int) -> int:

	#estandarizamos
	mean = np.load('mean.npy')
	std  = np.load('std.npy')

	X_test = np.array([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21])
	X_test = (X_test-mean)/std

	X_test = X_test.reshape(1,X_test.shape[0])
	y_pred = model.predict(X_test)
	return int(y_pred[0])

	
if __name__=="__main__":
	load_local_model()
	uvicorn.run(app, host='0.0.0.0',port=8500)
