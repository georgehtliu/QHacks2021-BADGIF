# Imports the Google Cloud client library
from google.cloud import language_v1

# The text to analyze
# testing_text = u"I am so happy! This is a very happy sounding text!! :)"

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
  

def get_entity_link(text):
  client = language_v1.LanguageServiceClient.from_service_account_json("./cred.json")
  # Available types are PLAN_TEXT and HTML
  type_ = language_v1.Document.Type.PLAIN_TEXT
  language = "en"
  document = {"content": text, "type_": type_, "language": language}
  encoding_type = language_v1.EncodingType.UTF8
  response = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type})
  entity = response.entities[0]
  link = ""
  for metadata_name, metadata_value in entity.metadata.items():
    if(metadata_name == "wikipedia_url"):
      link = metadata_value
  if(link == ""):
    link = "http://en.wikipedia.org/wiki/"
  return link

# print(get_entity_link("Google, headquartered in Mountain View (1600 Amphitheatre Pkwy, Mountain View, CA 940430), unveiled the new Android phone for $799 at the Consumer Electronic Show. Sundar Pichai said in his keynote that users love their new Android phones."))
print(get_entity_link("My iPhone just dided"))