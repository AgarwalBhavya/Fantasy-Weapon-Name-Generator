from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import time
import logging

app = FastAPI()
start_time = time.time()

# Configure logging
logging.basicConfig(filename="requests.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Load fine-tuned model and tokenizer
model_path = "./fine-tuned-model"  # Adjust if model is in a different location
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Pydantic model for input validation
class PromptRequest(BaseModel):
    prompt: str
    max_length: int = 30

@app.get("/status")
def get_status():
    uptime = time.time() - start_time
    return {
        "status": "Model is running",
        "uptime_seconds": int(uptime),
        "model": "Fine-tuned DistilGPT2"
    }

@app.post("/generate")
def generate_text(req: PromptRequest):
    try:
        logging.info(f"Prompt received: {req.prompt}")
        result = generator(req.prompt, max_length=req.max_length, num_return_sequences=1)
        return {"output": result[0]['generated_text']}
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return {"error": str(e)}
