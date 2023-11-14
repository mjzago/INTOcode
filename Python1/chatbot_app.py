import random
import re
import tkinter as tk

# Define the patterns and responses for the chatbot
pairs = [
    {
        "patterns": [r"hi|hello|hey"],
        "responses": ["Hello!", "Hi there!", "How can I assist you?"]
    },
    {
        "patterns": [r"why are you gay"],
        "responses": ["Who says I'm gay?"]
    },
    {
        "patterns": [r"you are gay"],
        "responses": ["Okay"]
    },
    {
        "question": ["How can I install Python?"],
        "answer": ["You can install Python by downloading the installer from the official Python website (python.org) and following the installation instructions for your operating system."]
    },
    {
        "question": ["What are the advantages of using Python?"],
        "answer": ["Python offers simplicity, readability, and a large standard library. It is widely used for web development, data analysis, machine learning, and automation. Python's extensive community support and vast ecosystem of libraries make it a popular choice among developers."]
    },
    {
        "question": ["How do I write a 'Hello, World!' program in Python?"],
        "answer": ["To write a 'Hello, World!' program in Python, you can use the following code:\n\nprint('Hello, World!')"]
    },
    {
        "question": ["What are Python packages and modules?"],
        "answer": ["In Python, packages are directories that contain multiple modules, while modules are files containing Python code. Packages and modules allow you to organize and reuse code across different projects."]
    },
    {
        "question": ["How do I install external libraries or packages in Python?"],
        "answer": ["You can use the pip package manager, which comes bundled with Python, to install external libraries. For example, to install the 'requests' library, you can run 'pip install requests' in your command-line interface."]
    },
    {
        "question": ["How can I handle exceptions or errors in Python?"],
        "answer": ["Python provides a 'try-except' block to handle exceptions. You can place the code that might raise an exception inside the 'try' block and use 'except' to catch and handle specific exceptions or provide a generic exception handler."]
    },
    {
        "question": ["What is the difference between Python 2 and Python 3?"],
        "answer": ["Python 2 and Python 3 are different versions of the Python programming language. Python 3 introduced several improvements and changes, including better Unicode support, syntax enhancements, and the removal of deprecated features. Python 2 is no longer actively maintained, and it is recommended to use Python 3 for new projects."]
    },
    {
        "question": ["How can I read and write files in Python?"],
        "answer": ["You can use the built-in 'open()' function to read or write files in Python. The 'open()' function returns a file object, and you can use methods like 'read()', 'write()', 'readline()', and 'writelines()' to perform file operations."]
    },
    {
        "question": ["Can Python be used for web development?"],
        "answer": ["Yes, Python is widely used for web development. Frameworks such as Django and Flask provide a structured way to build web applications, while libraries like BeautifulSoup help with web scraping and parsing HTML."]
    },
    {
        "question": ["How can I perform data analysis in Python?"],
        "answer": ["Python offers various libraries for data analysis, such as NumPy, pandas, and matplotlib. NumPy provides support for mathematical operations on arrays, pandas offers data manipulation and analysis tools, and matplotlib enables data visualization."]
    },
    {
        "patterns": [r"what is your name", r"who are you"],
        "responses": ["I am a chatbot.", "You can call me ChatBot."]
    },
    {
        "patterns": [r"how are you"],
        "responses": ["I'm good. How about you?", "I'm doing well. Thank you!"]
    },
    {
        "patterns": [r"omae wa mou shindeiro"],
        "responses": ["NANIIIIIIIIII"]
    },
    {
        "patterns": [r"sorry|apologies"],
        "responses": ["No problem.", "That's alright.", "Don't worry about it."]
    },
    {
        "patterns": [r"exit|quit"],
        "responses": ["Goodbye!", "See you later!", "Take care!"]
    }
]

# Define a function to select a random response from a list
def get_random_response(responses):
    return random.choice(responses)

# Define a function to handle user input and generate responses
def handle_user_input():
    user_input = user_input_entry.get()
    user_input_entry.delete(0, tk.END)

    if user_input in ["exit", "quit"]:
        response = get_random_response(pairs[-1]["responses"])
    else:
        matched_patterns = []
        for pair in pairs:
            if "patterns" in pair:
                for pattern in pair["patterns"]:
                    if re.search(pattern, user_input):
                        matched_patterns.append(pair)
                        break

        if matched_patterns:
            response = get_random_response(random.choice(matched_patterns)["responses"])
        else:
            response = "Sorry, I didn't understand. Can you please rephrase?"

    chat_log_text.config(state=tk.NORMAL)
    chat_log_text.insert(tk.END, "You: " + user_input + "\n")
    chat_log_text.insert(tk.END, "ChatBot: " + response + "\n")
    chat_log_text.config(state=tk.DISABLED)
    chat_log_text.see(tk.END)

# Create the main chatbot app window
root = tk.Tk()
root.title("ChatBot App")

# Create a text widget to display the chat log
chat_log_text = tk.Text(root, width=50, height=20, state=tk.DISABLED)
chat_log_text.pack()

# Create an entry widget for user input
user_input_entry = tk.Entry(root, width=50)
user_input_entry.pack()

# Create a button to handle user input
submit_button = tk.Button(root, text="Submit", command=handle_user_input)
submit_button.pack()

# Start the main event loop
root.mainloop()
