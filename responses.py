import requests

API_URL = 'http://API.aaronhernande26.repl.co'

def handle_response(message) -> str:
  message = message.lower()

  if message == 'hello':
    return 'shut up mate you are so annoying!'

  if message == 'help':
    return 'how am i supposed to help you dumbass i am just a bot in beta, btw i am in beta but i am an alpha.'

  if message == '/help':
    return '--Help section--\n\"/help\" Gives a general list of available commands.\n\"/topic\" Selects a random conversation topic from a list.\n\"/topic phil\" Selects a random philosophical conversation topic from a list.'
    
  if message == '/topic':
    URL = API_URL + "/general"
    print(URL)
    r = requests.get(url = URL)
    response = r.json()
    return response['topic']

  if message == '/topic phil':
    URL = API_URL + "/philosophical"
    print(URL)
    r = requests.get(url = URL)
    response = r.json()
    return response['topic']