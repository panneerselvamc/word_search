from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import permissions
from blog.models import Words
from django.db.models import Q
import json
import logging
logging.basicConfig(filename='test.log',level=logging.DEBUG)

@api_view(['POST'])
def word_search(request):
    #loading json data
    received_request=json.loads(request.body)
    #getting the value passed by UI
    userData=received_request["value"]
    #Assigning variables
    dataDictionary={}
    required_word=""
    repeated_value_of_the_word=""
    count=0
    #Quering to get objects name starts with user data
    startWithQueried_objects=Words.objects.filter(Q(name__startswith=userData))

    #if no objects then checking names in inbetween
    if len(startWithQueried_objects)==0:
        all_entries = Words.objects.all()
        for eachEntry in all_entries:
            if (userData) in (str(eachEntry.name)):
                dataDictionary[str(eachEntry.repeatedValue)]=eachEntry.name
    else:
        for eachEntry in startWithQueried_objects:
            dataDictionary[str(eachEntry.repeatedValue)]=eachEntry.name

    #calculating the word with smallest length
    for key,value in dataDictionary.items():
        if count==0:
            required_word=value
            repeated_value_of_the_word=key
            count=1
        else:
            if len(value) < len(required_word):
                required_word=value
                repeated_value_of_the_word=key
            elif len(value) == len(required_word):
                if int(key) > int(repeated_value_of_the_word):
                    required_word=value
                    repeated_value_of_the_word=key
            else:
                continue
    print required_word
    return Response({"requiredWord":required_word})
