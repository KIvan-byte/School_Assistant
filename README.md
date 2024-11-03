# School Assistant

School Assistant is a Python-based reference application designed for students in grades 8-11. It provides a comprehensive database of terms and definitions from educational manuals in Society, Biology, and History, including both Belarusian and World History. 

## Features

- Educational Database: Access definitions and historical events from a local SQLite database.
- Wikipedia Integration: If no local results are found, the app queries the Wikipedia API for relevant information.
- User-Friendly Interface: Intuitive design for easy navigation and search capabilities.
- Electronic Diary: Track assignments and notes efficiently.

## Tech Stack

- Programming Language: Python
- Framework: kivy
- Database: SQLite
- APIs: Wikipedia API for external data retrieval

## How to Use

1. Input a term or date in the search field.
2. The app displays relevant definitions or historical events.
3. If local results are unavailable, the app retrieves data from Wikipedia.

## Installation

Clone the repository and run the application in your Python environment. Make sure to install the required dependencies.

`bash
pip install -r requirements.txt
