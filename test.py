#test = """Here we can find
#some text that
#can be anywhere"""

x = input("Enter the finding word : ")

if "text" in x:
    print("True")
elif "text" != x:
    print("Text is not present")

    GENRES = {
        'comedy': ['Meet the Parents', 'Anger Management'],
        'adventures': ['Mummy'],
        'romantic': ['Vanilla Sky', 'Meet Joe Black'],
        'drama': ['Meet Joe Black'],
        'thriller': ['Vanilla Sky'],
        'action': ['Mission Impossible']
    }

    ACTORS = {
        'Robert De Niro': ['Meet the Parents'],
        'Ben Stiller': ['Meet the Parents'],
        'Adam Sandler': ['Anger Management'],
        'Jack Nicholson': ['Anger Management'],
        'Brendan Fraser': ['Mummy'],
        'Rachel Weisz': ['Mummy'],
        'Tom Cruise': ['Vanilla Sky', 'Mission Impossible'],
        'Penelope Cruz': ['Vanilla Sky'],
        'Cameron Diaz': ['Vanilla Sky'],
        'Brad Pitt': ['Meet Joe Black'],
        'Anthony Hopkins': ['Meet Joe Black'],
        'Jeremy Renner': ['Mission Impossible']
    }


    x = input("Search by genre : ")

    if x in GENRES :
        print("This genre is present ")
    #else:
    #   print (list("Available Genres : ", {[0],[1]}))


    # Function to get every third element
    def get_every_third_element(sequence):
        # Using slicing to get every third element starting from index 2
        third_elements = sequence[2::3]
        print(f"List of every third element: {list(third_elements)}")


    # Main program
    def main():
        # Taking input from the user
        sequence = input("Enter a sequence of characters: ")

        # Get and print every third element
        get_every_third_element(sequence)


    # Run the program
    if __name__ == "__main__":
        main()