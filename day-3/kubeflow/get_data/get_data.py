import json

import argparse
from pathlib import Path

def _get_data(args):

    import tensorflow as tf
    # Gets and split dataset
    mnist = tf.keras.datasets.mnist
    (X_train, y_train),(X_test, y_test) = mnist.load_data()

    # Normalize the training set
    X_train = tf.keras.utils.normalize(X_train, axis=1)
    # Normalize the test set
    X_test = tf.keras.utils.normalize(X_test, axis=1)

    # Save the data into a json file 
    data = {'X_train' : X_train.tolist(), 'y_train' : y_train.tolist(),
            'X_test' : X_test.tolist(), 'y_test' : y_test.tolist()}

    # Creates a json object based on `data`
    data_json = json.dumps(data)

    # Saves the json object into a file
    with open(args.data, 'w') as f:
        json.dump(data_json, f)

if __name__ == '__main__':
    
    # This component does not receive any input
    # it only outpus one artifact which is `data`.
    parser = argparse.ArgumentParser(description='Get Data')
    parser.add_argument('--data', type=str)
    
    args = parser.parse_args()
    # Creating the directory where the data file will be stored 
    Path(args.data).parent.mkdir(parents=True, exist_ok=True)

    _get_data(args)