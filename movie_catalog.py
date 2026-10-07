import json
try:
    with open('movie_catalog.json', mode = 'r') as file:
        raw_data = json.load(file)
except FileNotFoundError:
    print("This file does not exist!")

'''print(raw_data)'''

def clean_catalog(movie):
    try:
        movie['length_mins'] = int(movie['length_mins'])
        movie['rating'] = float(movie['rating'])
        movie['copies'] = int(movie['copies'])

        if movie['length_mins'] <= 0:
            return None
        if movie['rating'] <= 0:
            return None  
        if movie['copies'] <= 0:
            return None

        return movie      

    except Exception as e:
        print(e)
        return None

temp_movie_list = [clean_catalog(movie) for movie in raw_data]

movie_list = [movie for movie in temp_movie_list if movie is not None]

print(movie_list)

ranked_list = movie_list.sort(key = lambda movie: movie['rating'], reverse = True)

print(ranked_list)

total_copies_available = sum(movie['copies'] for movie in movie_list)

with open('inventory_report.txt', mode = 'w') as file:
    file.write("MOVIE INVENTORY REPORT\n")

    for movie in movie_list:
        file.write(f"Movie: {movie['title']}, Duration: {movie['length_mins']} minutes, Rating: {movie['rating']}, Available Copies: {movie['copies']}\n")

    file.write(f"The total number of copies available is {total_copies_available}\n")