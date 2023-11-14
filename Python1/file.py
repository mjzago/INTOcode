import mysql.connector

# Function to get all information about a person based on their name
def get_person_by_name(name):
    conn = mysql.connector.connect(
        host='localhost',
        user='admin',
        password='Mjones00',
        database='people.db'
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM people WHERE name = %s", (name,))
    person_data = cursor.fetchone()

    conn.close()

    return person_data

# Function to add a new person to the database
def add_person_to_db(name, age, city, email):
    conn = mysql.connector.connect(
        host='localhost',
        user='admin',
        password='Mjones00',
        database='people.db'
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO people (name, age, city, email) VALUES (%s, %s, %s, %s)",
                   (name, age, city, email))
    conn.commit()
    conn.close()

    print("Person added successfully to the database!")

# Function to add multiple people to the database
def add_multiple_people_to_db():
    while True:
        name = input("Enter the name of the person: ")
        age = int(input("Enter the age of the person: "))
        city = input("Enter the city of the person: ")
        email = input("Enter the email of the person: ")

        add_person_to_db(name, age, city, email)

        choice = input("Do you want to add another person? (yes/no): ")
        if choice.lower() != "yes":
            break

# Function to ask the user whether they want to insert a person or select an existing person
def ask_user_operation():
    while True:
        choice = input("Do you want to (I)nsert a new person or (S)elect an existing person? (I/S): ").lower()

        if choice == 'i':
            add_multiple_people_to_db()
        elif choice == 's':
            search_name = input("Enter the name of the person you want to search: ")
            person_data = get_person_by_name(search_name)

            if person_data:
                print("Name:", person_data[0])
                print("Age:", person_data[1])
                print("City:", person_data[2])
                print("Email:", person_data[3])
            else:
                print("Person not found in the database.")
        else:
            print("Invalid choice. Please enter 'I' or 'S'.")

        another_operation = input("Do you want to perform another operation? (yes/no): ")
        if another_operation.lower() != "yes":
            break

# Call the function to ask the user for the operation they want to perform
ask_user_operation()
