import tkinter as tk
import requests
import json

# Replace with your actual Hugging Face API key
API_KEY = "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"

# Function to get sentiment from Hugging Face model
def get_sentiment(text):
    url = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"inputs": text}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad responses

        result = response.json()
        
        # Check for possible errors in response
        if "error" in result:
            return f"API Error: {result['error']}"

        # Extract label and score
        results = []
        for prediction in result[0]:
                label = prediction["label"]
                score = prediction["score"]
                results.append(f"{label}: {score:.2f}")
        return "\n".join(results)
    except requests.exceptions.HTTPError as e:
        return f"HTTP Error: {e}"
    except requests.exceptions.ConnectionError:
        return "Error: Unable to connect to the Hugging Face API. Please check your internet connection."
    except requests.exceptions.Timeout:
        return "Error: The request timed out. Please try again."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    except KeyError:
        return "Unexpected response format. Please check the API response or try again later."

# Function to handle button click
def analyze_sentiment():
    user_input = entry.get()
    result = get_sentiment(user_input)
    result_label.config(text=result)

# Set up Tkinter window
root = tk.Tk()
root.title("Sentiment Analyzer")

# Input field
entry_label = tk.Label(root, text="Enter text for sentiment analysis:")
entry_label.pack()
entry = tk.Entry(root, width=50)
entry.pack()

# Analyze button
analyze_button = tk.Button(root, text="Analyze", command=analyze_sentiment)
analyze_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
