import numpy as np
import tensorflow.keras
from PIL import Image, ImageOps

def skin_cancer_classifier(image):
    
    np.set_printoptions(suppress=True)
    # Load the model
    model = tensorflow.keras.models.load_model('model/skin-cancer-detection/skin_cancer_detection_mobilenet_4.h5')
    # Determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    # Turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array
    labels = {0: "Bowen's disease", 1: "basal cell carcinoma", 2: "benign keratosis-like lesions ",3: "dermatofibroma", 4: "melanoma", 5: "melanocytic nevi",6:" vascular lesions "}
    # Run the inference
    predictions = model.predict(data).tolist()
    best_outcome = predictions[0].index(max(predictions[0]))
    print(labels[best_outcome])
    return labels[best_outcome]