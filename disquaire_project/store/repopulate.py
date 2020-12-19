
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'disquaire_project.settings'
import django
django.setup()

from store.models import Artist, Album


def show_albums():
    return Album.objects.all()


def show_artists():
    return Artist.objects.all()


def flush_albums():
    albums = Album.objects.all()
    for e in albums:
        e.delete()


def flush_artists():
    artists = Artist.objects.all()
    for e in artists:
        e.delete()


def repopulate():
    # flush 
    flush_artists()
    flush_albums()
    
    # artists
    artists = [
        Artist.objects.create(name='Miles Davis'),
        Artist.objects.create(name='Bill Evans'),
        Artist.objects.create(name='Herbie Hancock'),
    ]

    # albums
    albums = [
        Album.objects.create(title='Kind of Blue',
        picture='https://upload.wikimedia.org/wikipedia/en/9/9c/MilesDavisKindofBlue.jpg'),

        Album.objects.create(title='Sunday at The Village Vanguard',
        picture='https://upload.wikimedia.org/wikipedia/en/thumb/a/a1/Sunday_at_the_Village_Vanguard.jpg/220px-Sunday_at_the_Village_Vanguard.jpg'),
        
        Album.objects.create(title='On Green Dolphin Street',
        picture='https://upload.wikimedia.org/wikipedia/en/thumb/9/95/Green_Dolphin_Street_Evans.jpg/220px-Green_Dolphin_Street_Evans.jpg'),

        Album.objects.create(title='Maiden Voyage',
        picture='https://upload.wikimedia.org/wikipedia/en/thumb/7/7a/Maiden_Voyage_%28Hancock%29.jpg/220px-Maiden_Voyage_%28Hancock%29.jpg'),

        Album.objects.create(title='Head Hunters',
        picture='https://upload.wikimedia.org/wikipedia/en/thumb/5/54/Herbie-Hancock-Head-Hunters.png/220px-Herbie-Hancock-Head-Hunters.png'),
    ]

    # add artists
    albums[0].artists.add(artists[0])
    albums[1].artists.add(artists[1])
    albums[2].artists.add(artists[1])
    albums[3].artists.add(artists[2])
    albums[4].artists.add(artists[2])


if __name__ == "__main__":

    # repopulate()
    print(show_albums())
    print(show_artists())



