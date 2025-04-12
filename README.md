# Web Services and Applications – Weekly Assignments

This repository contains a collection of weekly assignments completed for the **Web Services and Applications** course. Each assignment focuses on a specific concept such as APIs, AJAX, HTTP requests, and Flask-based routing.

---

## Assignment 1 – Card Draw using Deck of Cards API

### Description
This Python script interacts with the public **Deck of Cards API** to simulate drawing 5 cards from a shuffled deck. It performs the following steps:
- Shuffles a new deck via API.
- Draws 5 cards using the deck ID.
- Prints the value and suit of each card.

**Filename:** [Assignment2-carddraw.py](https://github.com/FrancescaRuberto/WSAA-coursework/blob/main/Assignments/assignment2-carddraw.py)

---

### How to Run

1. Make sure you have Python installed.
2. Install the `requests` package
3. Clone or download the repository
4. Run the script as python assignment2-carddraw.py

Expected Outcome:
- The script will shuffle a new deck of cards. 
- It will draw 5 cards and display their value and suit.

### Resources Used

- [Making HTTP Requests in Python – DataCamp](https://www.datacamp.com/tutorial/making-http-requests-in-python)
- [Stack Overflow – Print multiple entries from a JSON response to a GET request](https://stackoverflow.com/questions/63542770/print-multiple-entries-from-a-json-response-to-e-get-request)
- [Shuffle Deck of Cards Example – Vultr](https://docs.vultr.com/python/examples/shuffle-deck-of-cards)
- [Python Requests Documentation – Real Python](https://realpython.com/python-requests/)

---

## Assignment 2 – Retrieve Exchequer Account Data from CSO API

### Description
This Python script retrieves the dataset for the "Exchequer account (historical series)" from the **CSO (Central Statistics Office)** API and stores it into a file called **`cso.json`**. The program doesn't analyze or format the data; it simply fetches and saves it.

**Filename:** [Assignment03-cso.py](https://github.com/FrancescaRuberto/WSAA-coursework/blob/main/Assignments/assignment03-cso.py)

---

### How to Run

1. Make sure you have Python istalled.
2. Install the request package.
3. Clone or dowload the repository.
4. Run the script as python assignment03-cso.py

Expected outcome: 
- The script will retrieve the "Exchequer account (historical series") dataset from the CSO API
- The data will be saved into a file named [cso.json](https://github.com/FrancescaRuberto/WSAA-coursework/blob/main/Assignments/cso.json)(Check [Assignements folder](https://github.com/FrancescaRuberto/WSAA-coursework/tree/main/Assignments) for reference)

### Resources Used

- [CSO Ireland API Documentation](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-cso-api?utm_source=chatgpt.com)
- [CSO Ireland GitHub Repository](https://github.com/CSOIreland?utm_source=chatgpt.com)
- [Python Requests Documentation – Real Python](https://realpython.com/python-requests/?utm_source=chatgpt.com)
- [Requests Quickstart Guide](https://docs.python-requests.org/en/latest/user/quickstart/?utm_source=chatgpt.com)
- [Stack Overflow – Check for 200 OK](https://stackoverflow.com/questions/54087303/python-requests-how-to-check-for-200-ok)
- [W3Schools Python Requests POST](https://www.w3schools.com/PYTHON/ref_requests_post.asp?)

---
## Assignment 3 – Replace Text in File and Push Changes to GitHub Repository

### Description
This Python script reads a file from a GitHub repository, replaces all instances of the text **"Andrew"** with your name, commits the changes, and then pushes the modified file back to the repository.

**Filename:** `assignment04-replace-text.py`

The program uses the **`PyGithub`** library to interact with the GitHub API, and the **API key** is securely stored in a separate **`config.py`** file to avoid exposing sensitive information.

---

### How to Run

1. Make sure you have Python installed.
2. Install the required libraries:
    ```bash
    pip install pygithub
    ```
3. Clone or download the repository that contains the script.
4. Create a **`config.py`** file to store your **GitHub API key** (this file should not be committed to the repository; it should be added to `.gitignore`):
    ```python
    apiKey = "your-github-api-key-here"
    ```
5. Run the script as:
    ```bash
    python assignment04-replace-text.py
    ```

---

### Expected Outcome

- The script will retrieve the content of **`test.txt`** from the repository.
- It will replace all instances of the text **"Andrew"** with your name (in this case, **"Francesca"**).
- The modified file will be committed and pushed back to the repository.
- The file **`test.txt`** will now contain your name instead of "Andrew".

---

### File Modified in the Repository

You can find the modified file here: [Link to `test.txt`](https://github.com/FrancescaRuberto/Miscellaneous/blob/main/test.txt).

---

### Resources Used

- [Making HTTP Requests in Python – DataCamp](https://www.datacamp.com/tutorial/making-http-requests-in-python)
- [Stack Overflow – Print multiple entries from a JSON response to a GET request](https://stackoverflow.com/questions/63542770/print-multiple-entries-from-a-json-response-to-e-get-request)
- [GitHub API Documentation](https://developer.github.com/v3/)
- [PyGithub Documentation](https://pygithub.readthedocs.io/en/latest/)
- [Python Requests Documentation – Real Python](https://realpython.com/python-requests/)

---

## Assignment 3 – Replace Text in File and Push Changes to GitHub Repository

### Description
This Python script reads a file from a GitHub repository, replaces all instances of the text **"Andrew"** with your name, commits the changes, and then pushes the modified file back to the repository.

**Filename:** `assignment04-replace-text.py`

The program uses the **`PyGithub`** library to interact with the GitHub API, and the **API key** is securely stored in a separate **`config.py`** file to avoid exposing sensitive information.

---

### How to Run

1. Make sure you have Python installed.
2. Install the required libraries:
    ```bash
    pip install pygithub
    ```
3. Clone or download the repository that contains the script.
4. Create a **`config.py`** file to store your **GitHub API key** (this file should not be committed to the repository; it should be added to `.gitignore`):
    ```python
    apiKey = "your-github-api-key-here"
    ```
5. Run the script as:
    ```bash
    python assignment04-replace-text.py
    ```

---

### Expected Outcome

- The script will retrieve the content of **`test.txt`** from the repository.
- It will replace all instances of the text **"Andrew"** with your name (in this case, **"Francesca"**).
- The modified file will be committed and pushed back to the repository.
- The file **`test.txt`** will now contain your name instead of "Andrew".

---

### File Modified in the Repository

You can find the modified file here: [Link to `test.txt`](https://github.com/FrancescaRuberto/Miscellaneous/blob/main/test.txt).

---

### Resources Used

- [Making HTTP Requests in Python – DataCamp](https://www.datacamp.com/tutorial/making-http-requests-in-python)
- [Stack Overflow – Print multiple entries from a JSON response to a GET request](https://stackoverflow.com/questions/63542770/print-multiple-entries-from-a-json-response-to-e-get-request)
- [GitHub API Documentation](https://developer.github.com/v3/)
- [PyGithub Documentation](https://pygithub.readthedocs.io/en/latest/)
- [Python Requests Documentation – Real Python](https://realpython.com/python-requests/)

---

## Assignment 3 – Replace Text in File and Push Changes to GitHub Repository

### Description
This Python script reads a file from a GitHub repository, replaces all instances of the text **"Andrew"** with your name, commits the changes, and then pushes the modified file back to the repository.

**Filename:** `assignment04-replace-text.py`

The program uses the **`PyGithub`** library to interact with the GitHub API, and the **API key** is securely stored in a separate **`config.py`** file to avoid exposing sensitive information.

---

### How to Run

1. Make sure you have Python installed.
2. Install the required libraries:
    ```bash
    pip install pygithub
    ```
3. Clone or download the repository that contains the script.
4. Create a **`config.py`** file to store your **GitHub API key** (this file should not be committed to the repository; it should be added to `.gitignore`):
    ```python
    apiKey = "your-github-api-key-here"
    ```
5. Run the script as:
    ```bash
    python assignment04-replace-text.py
    ```

---

### Expected Outcome

- The script will retrieve the content of **`test.txt`** from the repository.
- It will replace all instances of the text **"Andrew"** with your name (in this case, **"Francesca"**).
- The modified file will be committed and pushed back to the repository.
- The file **`test.txt`** will now contain your name instead of "Andrew".

---

### File Modified in the Repository

You can find the modified file here: [Link to `test.txt`](https://github.com/FrancescaRuberto/Miscellaneous/blob/main/test.txt).

---

### Resources Used

- [Making HTTP Requests in Python – DataCamp](https://www.datacamp.com/tutorial/making-http-requests-in-python)
- [Stack Overflow – Print multiple entries from a JSON response to a GET request](https://stackoverflow.com/questions/63542770/print-multiple-entries-from-a-json-response-to-e-get-request)
- [GitHub API Documentation](https://developer.github.com/v3/)
- [PyGithub Documentation](https://pygithub.readthedocs.io/en/latest/)
- [Python Requests Documentation – Real Python](https://realpython.com/python-requests/)

---

## Assignment 3 – Replace Text in File and Push Changes to GitHub Repository

### Description
This Python script reads a file from a GitHub repository, replaces all instances of the text **"Andrew"** with your name, commits the changes, and then pushes the modified file back to the repository.

**Filename:** [Assignment04-github.py](https://github.com/FrancescaRuberto/WSAA-coursework/blob/main/Assignments/assignment04-github.py)

The program uses the **`PyGithub`** library to interact with the GitHub API, and the **API key** is securely stored in a separate **`config.py`** file to avoid exposing sensitive information.

---

### How to Run

1. Make sure you have Python installed.
2. Install the required libraries:
    pip install pygithub
3. Clone or download the repository that contains the script.
4. Create a **`config.py`** file to store your **GitHub API key** (this file should not be committed to the repository; it should be added to `.gitignore`):
    apiKey = "your-github-api-key-here"
5. Run the script as:
    python assignment04-replace-text.py
    
---

### Expected Outcome

- The script will retrieve the content of **`test.txt`** from the repository.
- It will replace all instances of the text **"Andrew"** with your name (in this case, **"Francesca"**).
- The modified file will be committed and pushed back to the repository.
- The file **`test.txt`** will now contain your name instead of "Andrew".

---

### File Modified in the Repository

I created a new public repository to store the file I modified. You can find the modified file here: [Test.txt`](https://github.com/FrancescaRuberto/Miscellaneous/blob/main/test.txt).

---

### Resources Used

- [Making HTTP Requests in Python – DataCamp](https://www.datacamp.com/tutorial/making-http-requests-in-python)
- [Stack Overflow – Print multiple entries from a JSON response to a GET request](https://stackoverflow.com/questions/63542770/print-multiple-entries-from-a-json-response-to-e-get-request)
- [GitHub API Documentation](https://developer.github.com/v3/)
- [PyGithub Documentation](https://pygithub.readthedocs.io/en/latest/)
- [Python Requests Documentation – Real Python](https://realpython.com/python-requests/)

---

