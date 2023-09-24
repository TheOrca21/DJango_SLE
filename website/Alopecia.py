import os
import random
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Define the path to your dataset directory
dataset_dir = 'D:\\work\\sem-7\\Data\\ALO'

# List of class labels (subdirectory names in your dataset directory)
class_labels = os.listdir(dataset_dir)

# Initialize lists to store data and labels
data = []
labels = []

# Load and preprocess images
for label in class_labels:
    label_dir = os.path.join(dataset_dir, label)
    for image_filename in os.listdir(label_dir):
        image_path = os.path.join(label_dir, image_filename)

        # Load image, resize, and convert to numpy array
        img = load_img(image_path, target_size=(224, 224))  # Adjust target size as needed
        img_array = img_to_array(img) / 255.0  # Normalize pixel values

        data.append(img_array)
        labels.append(label)

# Split the data into training, validation, and test sets
train_data, temp_data, train_labels, temp_labels = train_test_split(data, labels, test_size=0.3, random_state=42)
val_data, test_data, val_labels, test_labels = train_test_split(temp_data, temp_labels, test_size=0.5, random_state=42)

# Convert labels to one-hot encoded format (assuming you have multiple classes)
label_binarizer = LabelBinarizer()
train_labels = label_binarizer.fit_transform(train_labels)
val_labels = label_binarizer.transform(val_labels)
test_labels = label_binarizer.transform(test_labels)

# Convert data and labels to NumPy arrays for better performance
train_data = np.array(train_data)
val_data = np.array(val_data)
test_data = np.array(test_data)

# Define the CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(len(class_labels), activation='softmax')  # Output layer with one neuron per class
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Print a summary of the model architecture
from tensorflow.keras.utils import to_categorical

# Assuming train_labels, val_labels, and test_labels are your original labels
num_classes = len(class_labels)  # Number of classes in your dataset
train_labels = to_categorical(train_labels, num_classes=2)
val_labels = to_categorical(val_labels, num_classes=2)
test_labels = to_categorical(test_labels, num_classes=2)

# Train the model
history = model.fit(train_data, train_labels,
                    validation_data=(val_data, val_labels),
                    epochs=10,  # Adjust the number of training epochs
                    batch_size=32)  # Adjust batch size as needed