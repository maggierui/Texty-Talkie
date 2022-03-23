import json
import ntpath
import requests

#get a list of supported voices
def get_voices():
    region = 'eastus'
    key = 'e1a022e65fba43b58b865d11802bac0d'
    url = 'https://{}.customvoice.api.speech.microsoft.com/api/texttospeech/v3.0/longaudiosynthesis/voices'.format(region)
    header = {
        'Ocp-Apim-Subscription-Key': key
    }

    response = requests.get(url, headers=header)
    print(response.text)

get_voices()