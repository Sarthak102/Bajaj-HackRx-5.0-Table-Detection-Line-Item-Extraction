import os
import sys
from app.services.ocr_service import OCRService
from app.services.template_detection import TemplateDetectionService
from app.services.error_correction import ErrorCorrectionService
from app.models.transformer_model import TransformerModel

def process_folder(folder_path):
    ocr_service = OCRService()
    template_service = TemplateDetectionService()
    error_service = ErrorCorrectionService()
    transformer_model = TransformerModel()

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            print(f"Processing: {filename}")
            ocr_text = ocr_service.hybrid_ocr(file_path)
            lines = template_service.detect_template(file_path)
            classified_text = transformer_model.classify(ocr_text)
            corrected_text = error_service.correct_errors(classified_text)
            print(f"Processed text for {filename}: {corrected_text}")
        else:
            print(f"{filename} is not a file.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <folder_path>")
        sys.exit(1)
    folder_path = sys.argv[1]
    process_folder(folder_path)

if __name__ == "__main__":
    main()
