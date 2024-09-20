import io
from google.cloud import vision
from PIL import Image
import pytesseract
from models.handwritten_recognition import HandwrittenRecognitionModel

class OCRService:
    def __init__(self):
        self.client = vision.ImageAnnotatorClient()  # Ensure your GCP credentials are set up correctly.
        self.handwriting_model = HandwrittenRecognitionModel('handwriting_model.h5')  # Update the model path if required.

    def google_vision_ocr(self, image_path):
        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()
        image = vision.Image(content=content)
        response = self.client.text_detection(image=image)
        return response.text_annotations[0].description if response.text_annotations else ''

    def hybrid_ocr(self, image_path):
        img = Image.open(image_path)
        ocr_text = pytesseract.image_to_string(img)
        handwritten_text = self.handwriting_model.predict(img)
        return ocr_text + handwritten_text

def load_service():
    return OCRService()