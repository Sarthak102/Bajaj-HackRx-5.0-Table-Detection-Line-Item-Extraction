import tensorflow as tf

class HandwrittenRecognitionModel:
    def __init__(self, model_path):  # Change model_path to your custom-trained model location
        self.model = tf.keras.models.load_model(model_path)

    def predict(self, image):
        img = tf.image.resize(image, [28, 28])
        img = tf.expand_dims(img, axis=0)
        prediction = self.model.predict(img)
        return prediction

def load_model():
    return HandwrittenRecognitionModel('C:\Users\G15-5511\Desktop\invoice_processing\app\models\handwriting_model.h5')  # Change this to your custom-trained model location
