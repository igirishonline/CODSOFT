# Data for books and songs
books_data = {
    "True To Their Salt: The British Indian Army and an Alternative History of Decolonization":{"author":"Ravindra Rathee","genre":"Fiction"},
    "Dreamers : How Young Indians Are Changing Their World": {"author": "Snigda Poonam", "genre": "Contemporary Fiction"},
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "genre": "Fiction"},
    "To Kill a Mockingbird": {"author": "Harper Lee", "genre": "Fiction"},
    "1984": {"author": "George Orwell", "genre": "Science Fiction"},
    "Pride and Prejudice": {"author": "Jane Austen", "genre": "Romance"},
    "Harry Potter and the Sorcerer's Stone": {"author": "J.K. Rowling", "genre": "Fantasy"}
}

songs_data = {
    "Aaradhya": {"artist": "Bheems Ceciroleo", "genre": "Melody"},
    "Nijamene Chebutunna": {"artist": "Sid Sriram", "genre": "Melody"},
    "Bohemian Rhapsody": {"artist": "Queen", "genre": "Rock"},
    "Like a Rolling Stone": {"artist": "Bob Dylan", "genre": "Rock"},
    "I Will Always Love You": {"artist": "Whitney Houston", "genre": "Pop"},
    "Hotel California": {"artist": "Eagles", "genre": "Rock"},
    "Billie Jean": {"artist": "Michael Jackson", "genre": "Pop"}
}

# Function to recommend books and songs based on user preferences
def recommend_items(preferences):
    recommended_items = []
    for item, details in books_data.items():
        if (details["genre"] in preferences or details["author"] in preferences or item in preferences) and item not in recommended_items:
            recommended_items.append(item)
    for item, details in songs_data.items():
        if (details["genre"] in preferences or details["artist"] in preferences or item in preferences) and item not in recommended_items:
            recommended_items.append(item)
    return recommended_items

# Example usage
def main():
    print("Welcome to the Recommendation System!")
    print("Please enter your preferences. You can enter genres, authors, artists, or specific titles.")
    preferences = input("Enter your preferences (separated by commas): ").split(",")
    recommended_items = recommend_items(preferences)
    if recommended_items:
        print("\nRecommended items based on your preferences:")
        for item in recommended_items:
            print(item)
    else:
        print("Sorry, no items match your preferences.")

if __name__ == "__main__":
    main()