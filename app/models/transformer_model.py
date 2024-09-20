from transformers import BertTokenizer, BertForSequenceClassification
import torch

class TransformerModel:
    def __init__(self, model_name='bert-base-uncased'):  # You can change the model name here.
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertForSequenceClassification.from_pretrained(model_name)

    def classify(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        outputs = self.model(**inputs)
        logits = outputs.logits
        prediction = torch.argmax(logits, dim=1)
        return prediction.item()

def load_model():
    return TransformerModel()