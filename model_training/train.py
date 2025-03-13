from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from datasets import load_dataset
import yaml
import torch
import os

def load_config(config_file="model_training/config.yaml"):
    """Load training configuration from YAML."""
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)

def train_model():
    """Fine-tune the LLM on regulatory data."""
    config = load_config()
    model_name = config['model_name']
    data_file = config['data_file']

    # Ensure data directory exists
    os.makedirs(os.path.dirname(data_file), exist_ok=True)
    if not os.path.exists(data_file):
        raise FileNotFoundError(f"Data file {data_file} not found. Run data ingestion first.")

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(model_name)

    dataset = load_dataset("json", data_files=data_file)
    def tokenize_function(examples):
        return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=512)

    tokenized_dataset = dataset.map(tokenize_function, batched=True)
    train_dataset = tokenized_dataset["train"]

    training_args = TrainingArguments(
        output_dir=config['output_dir'],
        evaluation_strategy="no",
        learning_rate=config['learning_rate'],
        per_device_train_batch_size=config['batch_size'],
        num_train_epochs=config['epochs'],
        save_steps=500,
        save_total_limit=2,
        fp16=torch.cuda.is_available(),  # GPU acceleration if available
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
    )
    trainer.train()
    model.save_pretrained("./fine_tuned_model")
    tokenizer.save_pretrained("./fine_tuned_model")

if __name__ == "__main__":
    train_model()