from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
import azure.cognitiveservices.speech as speechsdk

from voices.models import Voice, Region_lan

# Set up the subscription info for the Speech Service:

speech_key, service_region = "e1a022e65fba43b58b865d11802bac0d", "eastus"

def speech_synthesis_with_voice(region='en-US',person='JennyNeural', text="This is sample"):
    #"""performs speech synthesis to the default speaker with specified voice"""
    # Creates an instance of a speech config with specified subscription key and service region.
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    # Sets the synthesis voice name.
    # e.g. "Microsoft Server Speech Text to Speech Voice (en-US, JennyNeural)".
    # The full list of supported voices can be found here:
    # https://aka.ms/csspeech/voicenames
    # And, you can try get_voices_async method to get all available voices (see speech_synthesis_get_available_voices() sample below).
    voice = "Microsoft Server Speech Text to Speech Voice ({}, {})".format(region,person)
    print(voice)
    speech_config.speech_synthesis_voice_name = voice
    # Creates a speech synthesizer for the specified voice,
    # using the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    # Receives a text from console input and synthesizes it to speaker.
    result = speech_synthesizer.speak_text_async(text).get()
        

# Create your views here.

#Texty_TalkieForm=modelform_factory(Region_lan, exclude=[])
    

def welcome(request):
    text2 =''
    if request.method=="POST":
        #user has chosen voice, process data
       # form=request.POST
        #if form.is_valid():
            region=request.POST.get("region") #This line pass the actual region as it gets an integer for the order of the region in Voice region.
            person=request.POST.get("voice_person")
            text=request.POST.get("sample")            
            print(region)
            print(person)
            print(text)
            speech_synthesis_with_voice(region,person, text)
            return render(request,"website/welcome.html",
                {"message": "Below2 are all available voices for you to choose from",
                 "text": text
                  })
    
    else:
        return render(request,"website/welcome.html",
                  {"message": "Below are all available voices for you to choose from",
                   "text": text2
                   })

def about(request):
    return HttpResponse("This is a project created during the Fix, Hack, Learn week long event at E+D") 