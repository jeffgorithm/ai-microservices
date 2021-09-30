import tensorflow as tf

# Gets and split dataset
mnist = tf.keras.datasets.mnist
(X_train, y_train),(X_test, y_test) = mnist.load_data()
# Normalize the training set
X_train = tf.keras.utils.normalize(X_train, axis=1)
# Normalize the test set
X_test = tf.keras.utils.normalize(X_test, axis=1)
#Build the model object
model = tf.keras.models.Sequential()
# Add the Flatten Layer (Input Layer)
model.add(tf.keras.layers.Flatten())
# Build 2 hidden layers
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
# Build the output layer
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
# Compile the model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
# Train the compiled model
model.fit(x=X_train, y=y_train, epochs=5)
# Evaluate the model performance
_, accuracy = model.evaluate(x=X_test, y=y_test)
# Export the model to be deployed in Tensorflow Serving 
import os
save_path = os.path.join("./models/model/1/")
tf.saved_model.save(model, save_path)
