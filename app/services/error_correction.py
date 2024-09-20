class ErrorCorrectionService:
    def __init__(self):
        pass

    def correct_errors(self, extracted_text):
        corrected_text = extracted_text.replace('mistake', 'correction')
        return corrected_text
