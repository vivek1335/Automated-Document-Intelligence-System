# intellidoc.py

import pdfplumber
import pandas as pd
from transformers import LayoutLMv3Processor, LayoutLMv3ForTokenClassification
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# ----------------------------
# 1. Load Document
# ----------------------------
def load_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

file_path = input("Enter PDF file path: ")
document_text = load_pdf(file_path)

# ----------------------------
# 2. Initialize LayoutLMv3 Processor (for layout-aware NLP)
# ----------------------------
processor = LayoutLMv3Processor.from_pretrained("microsoft/layoutlmv3-base")
model = LayoutLMv3ForTokenClassification.from_pretrained("microsoft/layoutlmv3-base")

# For demonstration, we will tokenize text blocks (for real use, layout + images can be used)
inputs = processor(text=document_text, return_tensors="pt", truncation=True)

# Dummy forward pass (actual token classification requires labels)
with torch.no_grad():
    outputs = model(**inputs)

# ----------------------------
# 3. Sentiment Analysis using Transformer
# ----------------------------
sentiment_model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(sentiment_model_name)
sentiment_model = AutoModelForSequenceClassification.from_pretrained(sentiment_model_name)

inputs = tokenizer(document_text, return_tensors="pt", truncation=True, max_length=512)
with torch.no_grad():
    logits = sentiment_model(**inputs).logits
predicted_class_id = logits.argmax().item()
sentiment = ["NEGATIVE", "POSITIVE"][predicted_class_id]

# ----------------------------
# 4. Save Insights
# ----------------------------
df = pd.DataFrame({
    "Document": [file_path],
    "Sentiment": [sentiment],
    "Text_Excerpt": [document_text[:500]]  # first 500 characters
})
output_file = "intellidoc_insights.csv"
df.to_csv(output_file, index=False)

print(f"\nDocument processed. Sentiment: {sentiment}")
print(f"Insights saved to {output_file}")
