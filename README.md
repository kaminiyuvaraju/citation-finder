# Citation Finder

This project fetches data from an API, identifies citations in the responses, and displays them using a Flask web application.

## Features

- Fetches paginated data from a specified API endpoint.
- Identifies whether the response for each response-sources pair came from any of the sources.
- Lists the sources from which the response was formed.
- Displays the citations in a user-friendly web interface.

## Technologies Used

- Python
- Flask
- Requests

## Setup

### Prerequisites

- Python 3.6 or higher
- Git

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/kaminiyuvaraju/citation-finder
   cd citation_finder

### Create a virtual environment and activate it:

- python3 -m venv venv
- source venv/bin/activate  # On Windows use `venv\Scripts\activate`
### Install the dependencies:

- pip install -r requirements.txt
- Running the Application
- Run the Flask application:

- python app.py
Open your web browser and navigate to http://127.0.0.1:5000/ to view the citations.

### Project Structure
citation_finder/
├── app.py                # Main application file
├── fetch_data.py         # Module to fetch data from the API
├── find_citations.py     # Module to find citations in the fetched data
├── requirements.txt      # List of dependencies
├── templates/
│   └── index.html        # HTML template for displaying citations
└── README.md             # Project documentation
