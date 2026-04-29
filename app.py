import os
import requests
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

if not SERPAPI_KEY:
    raise ValueError("Missing SERPAPI_KEY in .env file")

# =========================
# 🔎 TOOL: GOOGLE SEARCH
# =========================
def google_search(query):
    url = "https://serpapi.com/search"

    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "engine": "google"
    }

    response = requests.get(url, params=params)
    data = response.json()

    results = []

    for item in data.get("organic_results", [])[:5]:
        results.append({
            "title": item.get("title"),
            "snippet": item.get("snippet"),
            "link": item.get("link")
        })

    return results


# =========================
# 🤖 LOCAL LLM (OLLAMA)
# =========================
def call_llama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:1b",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


# =========================
# 🤖 AGENT 1: SEARCH
# =========================
def search_agent(question):
    return google_search(question)


# =========================
# 🤖 AGENT 2: SUMMARIZER
# =========================
def summarizer_agent(search_result):
    prompt = f"""
You are a summarization expert.

Summarize the following research data into key bullet points:

{search_result}
"""
    return call_llama(prompt)


# =========================
# 🤖 AGENT 3: WRITER
# =========================
def writer_agent(summary):
    prompt = f"""
You are a professional content writer.

Write a well-structured article using this summary:

{summary}

Format:
Title
Introduction
Main Body
Conclusion
"""
    return call_llama(prompt)


# =========================
# 🚀 PIPELINE FUNCTION
# =========================
def run_pipeline(question):

    # STEP 1: SEARCH
    search_result = search_agent(question)

    # STEP 2: SUMMARIZE (LLM)
    summary = summarizer_agent(search_result)

    # STEP 3: WRITE ARTICLE (LLM)
    article = writer_agent(summary)

    return article


# =========================
# 🔁 USER LOOP
# =========================
if __name__ == "__main__":

    print("\n🤖 Local Multi-Agent System (Ollama) Started")
    print("Ask a question or type 'exit' to stop\n")

    while True:

        question = input("User: ")

        if question.lower() == "exit":
            print("\n👋 System stopped.")
            break

        print("\n🚀 Processing through Multi-Agent Pipeline...\n")

        result = run_pipeline(question)

        print("\n================ FINAL ARTICLE ================\n")
        print(result)
        print("\n==============================================\n")