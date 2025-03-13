from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_path = "./fine_tuned_model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

def generate_response(query: str) -> str:
    """Generate a compliance response using the fine-tuned LLM."""
    inputs = tokenizer(query, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=200,
            num_return_sequences=1,
            temperature=0.7,
            do_sample=True
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)