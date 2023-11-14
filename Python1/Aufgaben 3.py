def writeIntoFile(string):
    try:
        with open("strings.txt", "a") as file:
            file.write(string + "\n")
    except FileNotFoundError as e:
        print("Fehler: Datei 'strings.txt' nicht gefunden.")
        print(e)

def main():
    user_input = input("Geben Sie den zu schreibenden Text ein: ")
    writeIntoFile(user_input)

if __name__ == "__main__":
    main()
