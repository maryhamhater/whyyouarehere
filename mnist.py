import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt 


mnist = tf.keras.datasets.mnist

(x_train,y_train),(x_test,y_test) = mnist.load_data() #0 to 9

x_test = x_test / 250.0
x_train = x_train / 250.0

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(128,"relu"))
model.add(tf.keras.layers.Dropout(0,2))
model.add(tf.keras.layers.Dense(10,  tf.nn.softmax))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=1)
model.evaluate(x_test, y_test)
model.evaluate(x_train, y_train)



model.save("model")

nmdl = tf.keras.models.load_model("model")

prediction = nmdl.predict([x_train])

print(np.argmax(prediction[1]))
print(x_train[0])


