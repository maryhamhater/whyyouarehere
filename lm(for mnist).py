import tensorflow as tf
import numpy as np

mnist = tf.keras.datasets.mnist

(x_train,y_train),(x_test,y_test) = mnist.load_data() #0 to 9 (28 x 28)

x_test = x_test / 250.0
x_train = x_train / 250.0


nmdl = tf.keras.models.load_model("model")

prediction = nmdl.predict([x_train])

print(np.argmax(prediction[0]))

