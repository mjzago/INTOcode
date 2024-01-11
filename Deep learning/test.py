import tensorflow as tf
import keras
from keras import layers


import tensorflow as tf

# Get the list of available GPUs
gpus = tf.config.experimental.list_physical_devices('GPU')

if gpus:
    # TensorFlow is using GPU
    print("TensorFlow is running on GPU.")
    for gpu in gpus:
        print(f"Device name: {gpu.name}")
else:
    # TensorFlow is using CPU
    print("TensorFlow is running on CPU.")
