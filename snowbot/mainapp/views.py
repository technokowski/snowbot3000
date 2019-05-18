from django.shortcuts import render
import os,random,mainapp.lists
from speaker import Speaker
from django.http import JsonResponse,HttpResponse
from mainapp.models import Jokes,Sing,Wisdom

"""

Every view that creates a db instance uses a comparitive operator
to determine if the length of the db has changed, and if so,
it plays the new entry first, then all entries (jokes, wisdom, songs)
return to random. The more that are added, the more 'random' the selections
will be, so create away!

"""

# Used to indicate how many entries are in the db
# Must commented out if starting a new db from scratch
jokes_num = len(Jokes.objects.all())
songs_num = len(Sing.objects.all())
wisdom_num = len(Wisdom.objects.all())

# Instance of custom Speaker class
speak = Speaker()

# Main view that displays the 6 panel content to visitors.
def index(request):
    # os.system('afplay static/audio/56k.wav')
    speak.say('Welcome, I am ready.')
    return render(request, 'mainapp/index.html')

# Secondary "secret" page that allows input without the premade name responses
def support(request):
    # speak.speak("support")
    return render(request, 'mainapp/support.html')

# Second panel on index.html that allows for visitor name input and
# and adds random stock phrases to the greeting
def text_input(request):
    human_words = request.GET.get('human_words', None)
    data = {'words': human_words}
    speak.speak(str(random.choice(mainapp.lists.namehello)) + str(human_words))
    speak.speak(str(random.choice(mainapp.lists.namecompliment))
    + str(random.choice(mainapp.lists.namegreets)) + str(human_words))
    return JsonResponse(data)

# Returns an entry from the jokes db
def jokes(request):
    global jokes_num
    my_jokes_local = Jokes.objects.all()
    length_of_jokes = len(my_jokes_local)
    if length_of_jokes != jokes_num:
        print("Jokes must have been changed")
        jokes_num = length_of_jokes
        speak.speak(str(my_jokes_local[length_of_jokes -1]))
        os.system('afplay static/audio/comic008.wav')
    else:
        speak.speak(str(random.choice(my_jokes_local)))
        os.system('afplay static/audio/comic008.wav')
    return HttpResponse('joke granted')

# Returns a random song entry from the song db
def songs(request):
    global songs_num
    my_songs_local = Sing.objects.all()
    length_of_songs = len(my_songs_local)
    if length_of_songs != songs_num:
        print('Songs must have changed')
        songs_num = length_of_songs
        rand = str(my_songs_local[length_of_songs - 1])
        for i in rand.split():
            speak.singer(i)
        os.system('afplay static/audio/applause.wav')
    else:
        rand = str(random.choice(my_songs_local))
        # for vals, words in zip(pitch_vals, words_for_song):
        #     speak.singer(vals, words)
        #     print(vals)
        for i in rand.split():
            speak.singer(i)
        os.system('afplay static/audio/applause.wav')

    return HttpResponse('song sung')

def wisdom(request):
    global wisdom_num
    my_wisdom_local = Wisdom.objects.all()
    length_of_wisdom = len(my_wisdom_local)
    if length_of_wisdom != wisdom_num:
        print('Wisdom list must have changed')
        wisdom_num = length_of_wisdom
        speak.speak(str(my_wisdom_local[length_of_wisdom - 1]))
        os.system('afplay static/audio/youknow.wav')
    else:
        speak.speak(str(random.choice(my_wisdom_local)))
        os.system('afplay static/audio/youknow.wav')
    return HttpResponse('wisdom given')

def dareyou(request):
    speak.speak(random.choice(mainapp.lists.dareyou_list))
    os.system('afplay -v 4 static/audio/snowbot_song.wav')
    return HttpResponse('I dared you')

def voice(request):
    speak.change_voice(random.choice(mainapp.lists.voices_names))
    speak.speak(random.choice(mainapp.lists.voice_list))
    return HttpResponse('Voice changed')

def support_input(request):
    human_words = request.GET.get('human_words', None)
    data = {'words': human_words}
    speak.speak(human_words)
    return JsonResponse(data)
