import cv2

class TemplateDetectionService:
    def __init__(self):
        pass

    def detect_template(self, image_path):
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150, apertureSize=3)
        lines = cv2.HoughLinesP(edges, 1, cv2.pi/180, 100)
        return lines
