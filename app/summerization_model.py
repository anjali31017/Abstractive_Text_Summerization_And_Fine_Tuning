from transformers import BartTokenizer, BartForConditionalGeneration
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the fine-tuned model
tokenizer = BartTokenizer.from_pretrained('../bart_lora')
model = BartForConditionalGeneration.from_pretrained('../bart_lora').to(device)

def summarize(text):
    try:
        inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
        inputs = {k: v.to(device) for k, v in inputs.items()}

        summary_ids = model.generate(
            inputs['input_ids'],
            # max_length=50,
            # min_length=60,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )

        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
    except Exception as e:
        str(e)
        
