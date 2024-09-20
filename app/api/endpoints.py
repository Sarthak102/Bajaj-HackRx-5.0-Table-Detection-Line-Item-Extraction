from fastapi import FastAPI, UploadFile, File
from services.ocr_service import OCRService
from services.template_detection import TemplateDetectionService
from services.error_correction import ErrorCorrectionService
from models.transformer_model import TransformerModel

app = FastAPI()

ocr_service = OCRService()
template_service = TemplateDetectionService()
error_service = ErrorCorrectionService()
transformer_model = TransformerModel()

@app.post("/upload-invoice/")
async def process_invoice(file: UploadFile = File(...)):
    file_location = f"/tmp/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

    ocr_text = ocr_service.hybrid_ocr(file_location)
    lines = template_service.detect_template(file_location)
    classified_text = transformer_model.classify(ocr_text)
    corrected_text = error_service.correct_errors(classified_text)

    return {"processed_text": corrected_text}
