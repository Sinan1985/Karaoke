from django.shortcuts import render

from common.models import Song
def test(request):
    return render(request, 'user_app/test.html')
# Create your views here.

def enter_song_view(request):
    return render(request, 'user_app/enter_song.html')

def enter_song(request):
    user_name = None  # Initialize the variable
    sing_name = None  # Initialize the variable
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        sing_name = request.POST.get('sing_name')


    # Create and save a new Song entry in the database
    if user_name and sing_name:  # Ensure both fields are filled
        Song.objects.create(user_name=user_name, sing_name=sing_name)

    # Optionally, you can return a success message or redirect
    return render(request, 'user_app/enter_song.html', {'message': 'Song added successfully!'})

def songs_list(request):
    # Retrieve all songs from the database
    #songs = Song.objects.all()
    from django.utils.timezone import now
    from datetime import date
    # Get the current date
    today = now().date()

    songs = Song.objects.filter(timestamp__date=date.today())

    # Pass the songs to the template
    return render(request, r'user_app/songs_list.html', {'songs': songs})