import numpy as np #array
import matplotlib.pyplot as plt# display
import tensorflow as tf# deep learning 
from tensorflow.keras.datasets import mnist# mnist
from tensorflow.keras.models import Sequential# step wise step
from tensorflow.keras.layers import Dense, Flatten#neural network
from tensorflow.keras.utils import to_categorical#
from sklearn.metrics import classification_report#

# Step 1: Load and Preprocess Data
(x_train, y_train), (x_test, y_test) = mnist.load_data()#
x_train = x_train / 255.0  # Normalize
x_test = x_test / 255.0

# Step 2: Build a simple model
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')  # 10 digits: 0-9
])

model.compile(optimizer='adam',# compile optimization optimization algorithm
              loss='sparse_categorical_crossentropy',#
              metrics=['accuracy'])

# Step 3: Train the model
print("Training model...")
model.fit(x_train, y_train, epochs=5, validation_split=0.1)# ecochs number of pass 5

# Step 4: Evaluate model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"\nTest Accuracy: {test_acc * 100:.2f}%")

# Step 5: Predict a single digit
def predict_digit(index):
    img = x_test[index]
    prediction = model.predict(img.reshape(1, 28, 28))
    predicted_label = np.argmax(prediction)
    confidence = prediction[0][predicted_label]

    plt.imshow(img, cmap='gray')
    plt.title(f"Predicted: {predicted_label} (Confidence: {confidence:.2f})")
    plt.axis('off')
    plt.show()

    # AI Recommendation system
    sorted_probs = np.argsort(-prediction[0])  # sort from highest to lowest
    print("\nTop 3 Predictions:")
    for i in range(3):
        print(f"Digit {sorted_probs[i]} with confidence {prediction[0][sorted_probs[i]]:.2f}")

    suggested_next = sorted_probs[1]
    print(f"\n🤖 Try testing with digit '{suggested_next}' next. The model is somewhat confused between '{predicted_label}' and '{suggested_next}'.")

# Try prediction on some test sample (e.g., index = 102)
predict_digit(index=102)
