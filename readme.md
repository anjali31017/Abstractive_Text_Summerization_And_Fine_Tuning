# Text Summarizer

This project performs abstractive text summarization using a fine-tuned DistilBART model with LoRA.  
It includes a FastAPI backend for generating summaries and a simple HTML interface for user input.

## Features
- Fine-tuned DistilBART model for summarizing long news articles.
- LoRA optimization for lightweight and CPU-friendly training.
- Uses a reduced CNN/DailyMail dataset to ensure smooth training on CPU.
- FastAPI endpoint (`/summarize`) for serving summaries.
- Clean and responsive HTML UI for easy text input and output.
