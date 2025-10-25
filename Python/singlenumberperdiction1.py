# MNIST classification with a simple Dense neural network (TensorFlow / Keras)
import numpy as np# array
import tensorflow as tf# deep learning
from tensorflow.keras import layers, models#framework
import matplotlib.pyplot as plt#  visualization

# Optional: make results reproducible
np.random.seed(42)
tf.random.set_seed(42)

# 1) Load the MNIST dataset (handwritten digits)
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 2) Normalize pixel values from [0,255] -> [0.0, 1.0]
x_train = x_train.astype("float32") / 255.0
x_test  = x_test.astype("float32")  / 255.0

# 3) Build the model
model = models.Sequential([#sequeatial
    layers.Flatten(input_shape=(28, 28)),     # convert 2D 28x28 images to 1D vector (784,)
    layers.Dense(128, activation='relu'),     # hidden dense layer with ReLU
    layers.Dense(10, activation='softmax')    # output layer: 10 classes (0-9), softmax yields probabilities
])

# Show model architecture
model.summary()

# 4) Compile the model (choose optimizer, loss, and metrics)
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',   # use sparse when labels are integers (not one-hot)
    metrics=['accuracy']
)

# 5) Train the model
history = model.fit(
    x_train, y_train,
    epochs=5,                 # try increasing to 10-20 for better accuracy
    batch_size=64,
    validation_split=0.1      # keep 10% of training data for validation during training
)

# 6) Evaluate on test set
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"Test accuracy: {test_acc:.4f}, Test loss: {test_loss:.4f}")

# 7) Make predictions (probability vectors) and show the first example
predictions = model.predict(x_test)                # shape: (10000, 10)
predicted_label = np.argmax(predictions[0])        # pick the class with highest probability

# 8) Visualize the first test image with predicted & actual labels
plt.imshow(x_test[0], cmap='gray')
plt.title(f"Predicted: {predicted_label}   Actual: {y_test[0]}")
plt.axis('off')
plt.show()
