songs = [
    {'title': 'song1', 'artist': 'artist1', 'genre': 'pop', 'favourite': False},
    {'title': 'song2', 'artist': 'artist2', 'genre': 'rock', 'favourite': False},
    {'title': 'song3', 'artist': 'artist1', 'genre': 'hip hop', 'favourite': False},
    {'title': 'song4', 'artist': 'artist3', 'genre': 'country', 'favourite': False},
    {'title': 'song5', 'artist': 'artist2', 'genre': 'jazz', 'favourite': False},
]

favourites = []

def display_data(data):
    for i, song in enumerate(data):
        print(f"{i+1}. {song['title']} by {song['artist']} ({song['genre']})")

def search_data(data, search_term):
    search_results = []
    for song in data:
        if search_term.lower() in song['title'].lower() or search_term.lower() in song['artist'].lower() or search_term.lower() in song['genre'].lower():
            search_results.append(song)
    return search_results

def sort_data(data, sort_key):
    return sorted(data, key=lambda x: x[sort_key])

def add_to_favourites(data, favourites, index):
    favourites.append(data[index])
    data[index]['favourite'] = True
    print(f"{data[index]['title']} added to favourites")

def remove_from_favourites(data, favourites, index):
    favourites.remove(data[index])
    data[index]['favourite'] = False
    print(f"{data[index]['title']} removed from favourites")

def display_favourites(favourites):
    for i, song in enumerate(favourites):
        print(f"{i+1}. {song['title']} by {song['artist']} ({song['genre']})")
        
while True:
    print("1. Display all data")
    print("2. Search/Filter data")
    print("3. Sort data")
    print("4. Add to favourites")
    print("5. Remove from favourites")
    print("6. Display favourites")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_data(songs)

    elif choice == "2":
        search_term = input("Enter search term: ")
        search_results = search_data(songs, search_term)
        display_data(search_results)

    elif choice == "3":
        sort_key = input("Enter sort key (title, artist, genre): ")
        songs = sort_data(songs, sort_key)
        display_data(songs)

    elif choice == "4":
        display_data(songs)
        index = int(input("Enter index of song to add to favourites: ")) - 1
        add_to_favourites(songs, favourites, index)

    elif choice == "5":
        display_favourites(favourites)
        index = int(input("Enter index of song to remove from favourites: ")) - 1
        remove_from_favourites(songs, favourites, index)

    elif choice == "6":
        display_favourites(favourites)
        
    elif choice == "7":
        break
