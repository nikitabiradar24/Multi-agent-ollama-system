# Multi-Agent AI System (Ollama आधारित)

## Overview
This project implements a multi-agent AI system:
- Search Agent (Google via SerpAPI)
- Summarizer Agent (Ollama LLM)
- Writer Agent (Ollama LLM)

## Tech Stack
- Python
- Ollama (LLaMA 3)
- SerpAPI

## Features
- Fully local LLM (no OpenAI dependency)
- Automated article generation
- Multi-agent pipeline

## Setup
1. Install dependencies:
   pip install requests python-dotenv

2. Add .env file:
   SERPAPI_KEY=your_key

3. Run Ollama:
   ollama serve

4. Run project:
   python app.py
