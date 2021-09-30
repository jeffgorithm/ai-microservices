import requests
import tensorflow as tf
# Gets and split dataset
mnist = tf.keras.datasets.mnist
(X_train, y_train),(X_test, y_test) = mnist.load_data()
image_idx = 20
image = X_test[image_idx]
# Rescale the image as we did before training the NN
image = image / 255
label = y_test[image_idx]
# Convert the Tensor to a batch of Tensors and then to a list
image_tensor = tf.expand_dims(image, 0)
image_tensor = image_tensor.numpy().tolist()
# Define the endpoint with the format: http://localhost:8501/v1/models/MODEL_NAME:predict
endpoint = "http://localhost:8501/v1/models/model:predict"
# Prepare the data that is going to be sent in the POST request
  
json_data = {
"instances": image_tensor
}
# Send the request to the Prediction API
response = requests.post(endpoint, json=json_data)
# Retrieve the highest probablity index of the Tensor (actual prediction)
prediction = tf.argmax(response.json()['predictions'][0])
print(f"Prediction: {prediction} vs True Label: {label}")