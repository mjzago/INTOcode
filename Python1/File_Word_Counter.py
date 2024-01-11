class FileWordCounter:
    def __init__(self, input_filename, output_filename="word_count.txt"):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.word_count = 0

    def count_words(self):
        try:
            with open(self.input_filename, 'r') as file:
                for line in file:
                    words = line.split()
                    self.word_count += len(words)
        except FileNotFoundError:
            print(f"Error: The file '{self.input_filename}' was not found.")
        except IOError:
            print(f"Error: Unable to read the file '{self.input_filename}'.")

    def display_word_count(self):
        print(f"Total number of words: {self.word_count}")

    def write_word_count_to_file(self):
        try:
            with open(self.output_filename, 'w') as file:
                file.write(str(self.word_count))
            print(f"Word count written to '{self.output_filename}' successfully.")
        except IOError:
            print(f"Error: Unable to write to the file '{self.output_filename}'.")


if __name__ == "__main__":
    input_filename = "input.txt"
    word_counter = FileWordCounter(input_filename)

    # Step 1: Count words from the input file
    word_counter.count_words()

    # Step 2: Display the word count on the screen
    word_counter.display_word_count()

    # Step 3: Write the word count to a new file named "word_count.txt"
    word_counter.write_word_count_to_file()
