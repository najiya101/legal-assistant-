from transformers import BertTokenizer, BertForMaskedLM

# Load fine-tuned model
model_path = "./indian-legal-bert"
tokenizer = BertTokenizer.from_pretrained(model_path)
model = BertForMaskedLM.from_pretrained(model_path)

# Example legal text
text = "The accused was convicted under [MASK] section of the IPC."
inputs = tokenizer(text, return_tensors="pt")

# Get predictions
with torch.no_grad():
    outputs = model(**inputs)

print(outputs)
