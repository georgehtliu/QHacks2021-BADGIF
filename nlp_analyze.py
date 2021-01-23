# Imports the Google Cloud client library
from google.cloud import language_v1

# The text to analyze
testing_text = u"I am so happy! This is a very happy sounding text!! :)"

def get_sentiment_score(text):
  # Instantiates a client
  client = language_v1.LanguageServiceClient.from_service_account_json("./cred.json")
  document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
  # Detects the sentiment of the text
  sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
  return sentiment.score


def get_sentiment_magnitude(text):
  client = language_v1.LanguageServiceClient.from_service_account_json("./cred.json")
  document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
  # Detects the sentiment of the text
  sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
  return sentiment.magnitude
  

print("SENTIMENT SCORE:")
print(get_sentiment_score(testing_text))
print("SENTIMENT MAGNITUDE:")
print(get_sentiment_magnitude(testing_text))