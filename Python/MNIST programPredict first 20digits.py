import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# STEP 0: seeds
np.random.seed(42)
tf.random.set_seed(42)

# STEP 1: Load data
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
print("STEP 1:", x_train.shape, y_train.shape)

# STEP 2: pixel range before normalize
print("STEP 2:", x_train.min(), x_train.max())

# STEP 3: normalize
x_train = x_train.astype("float32") / 255.0
x_test  = x_test.astype("float32")  / 255.0
print("STEP 3:", x_train.min(), x_train.max())

# STEP 4: model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])
model.summary()

# STEP 5: compile
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# STEP 6: train
history = model.fit(
    x_train, y_train,
    epochs=5,
    batch_size=64,
    validation_split=0.1
)

# STEP 7: evaluate
loss, acc = model.evaluate(x_test, y_test, verbose=0)
print(f"Test Acc = {acc:.4f}")

# ----------------------------
# STEP 8: Predict MULTIPLE digits
# ----------------------------
N = 20   # number of images to predict
pred = model.predict(x_test[:N])   # shape (N, 10)
pred_labels = np.argmax(pred, axis=1)

print("\nPredicted labels:", pred_labels)
print("Actual labels:    ", y_test[:N].tolist())

# ----------------------------
# STEP 9: Display first 20 images with predictions
# ----------------------------
plt.figure(figsize=(12, 6))
for i in range(N):
    plt.subplot(4, 5, i+1)    # 4 rows × 5 columns
    plt.imshow(x_test[i], cmap='gray')
    plt.title(f"P:{pred_labels[i]} / A:{y_test[i]}")
    plt.axis('off')
plt.tight_layout()
plt.show()
