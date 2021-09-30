import json

import argparse
from pathlib import Path

def _convolutional_nn(args):
    import tensorflow as tf

    # Open and reads file "data"
    with open(args.data) as data_file:
        data = json.load(data_file)
    
    # Load the data from the json file
    data = json.loads(data)

    X_train = data['X_train']
    y_train = data['y_train']
    X_test = data['X_test']
    y_test = data['y_test']

    #Build the model object
    model = tf.keras.models.Sequential()
    # Add a convolution layer
    model.add(tf.keras.models.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
    # Apply Max Pooling
    model.add(tf.keras.models.MaxPooling2D((2, 2)))
    # Add the Flatten Layer (Input Layer)
    model.add(tf.keras.models.Flatten())
    # Build 1 hidden layers
    model.add(tf.keras.models.Dense(100, activation='relu'))
    # Build the output layer
    model.add(tf.keras.models.Dense(10, activation='softmax'))
    # compile model
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy",
    metrics=["accuracy"])

    # Train the compiled model
    model.fit(x=X_train, y=y_train, epochs=10)

    # Evaluate the model performance
    _, accuracy = model.evaluate(x=X_test, y=y_test)

    # Save output into file
    with open(args.accuracy, 'w') as f:
        f.write(str(accuracy))

if __name__ == '__main__':

    # Defining and parsing the command-line arguments
    parser = argparse.ArgumentParser(description='Convolutional Neural Network model')
    parser.add_argument('--data', type=str)
    parser.add_argument('--accuracy', type=str)

    args = parser.parse_args()

    # Creating the directory where the output file will be created (the directory may or may not exist).
    Path(args.accuracy).parent.mkdir(parents=True, exist_ok=True)
    
    _convolutional_nn(args)