from pymongo import MongoClient

def main():
    # Connect to MongoDB (change the URI as needed)
    client = MongoClient('mongodb://host.docker.internal:27017/')
    db = client['name_database']  # Replace with your database name
    collection = db['names']  # Replace with your collection name

    while True:
        print("\nMenu:")
        print("1) Enter Name")
        print("2) Show All Names")
        print("3) Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            # Insert the name into the MongoDB collection
            collection.insert_one({'name': name})
            print(f"Name '{name}' saved to database.")

        elif choice == '2':
            # Fetch all names from the MongoDB collection
            names = collection.find()
            print("All entered names:")
            for entry in names:
                print(entry['name'])

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
