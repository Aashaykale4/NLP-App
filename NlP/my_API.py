import requests
import json

class API:
  def __init__(self):
      self.key="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"
 
  def get_sentiment(self,text):
        url = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
        headers = {"Authorization": f"Bearer {self.key}"}
        payload = {"inputs": text}

        try:
          response = requests.post(url, headers=headers, json=payload)
          response.raise_for_status()  # Raise an error for bad responses

          result = response.json()
        
        
          if "error" in result:
            return f"API Error: {result['error']}"

       
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


           

  def get_NER(self, text):
    url = "https://api-inference.huggingface.co/models/dbmdz/bert-large-cased-finetuned-conll03-english"
    headers = {"Authorization": f"Bearer {self.key}"}
    payload = {"inputs": text}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad responses

        result = response.json()
        return result[0]  # Log the raw API response

        

        
         

    except requests.exceptions.HTTPError as e:
        return f"HTTP Error: {e.response.status_code} - {e.response.text}"
    except requests.exceptions.ConnectionError:
        return "Error: Unable to connect to the Hugging Face API. Please check your internet connection."
    except requests.exceptions.Timeout:
        return "Error: The request timed out. Please try again."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    except KeyError:
        return "Unexpected response format. Please check the API response or try again later."
  

  def get_lang(self,text):
    url = "https://api-inference.huggingface.co/models/papluca/xlm-roberta-base-language-detection"
    headers = {"Authorization": f"Bearer {self.key}"}
    payload = {"inputs": text}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad responses

        result = response.json()
        return result[0]  # Log the raw API response

        

        
         

    except requests.exceptions.HTTPError as e:
        return f"HTTP Error: {e.response.status_code} - {e.response.text}"
    except requests.exceptions.ConnectionError:
        return "Error: Unable to connect to the Hugging Face API. Please check your internet connection."
    except requests.exceptions.Timeout:
        return "Error: The request timed out. Please try again."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    except KeyError:
        return "Unexpected response format. Please check the API response or try again later."
  
     