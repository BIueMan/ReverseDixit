# FastAPI Login App

This is a simple FastAPI login app with two pages. It allows users to create a username on the login page and proceed to a second page where they can input text and send it to the server.

## Installation

1. Install FastAPI and Uvicorn:

   ```bash
   pip install fastapi uvicorn
   ```

## Running the App

1. Run the FastAPI app using Uvicorn:

   ```bash
   uvicorn main:app --reload
   ```

2. Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000) to access the login page.

3. Follow the instructions on the pages to create a user, navigate to the second page, and send text to the server.

## Project Structure

- `main.py`: The main FastAPI application file.
- `templates/`: Folder containing HTML templates.
- `static/`: Folder containing static files such as stylesheets.
- `style.css`: Basic stylesheet for styling the HTML pages.

Feel free to customize the app, styles, and templates according to your requirements.

```

Make sure to customize the README file with relevant information for your specific project. Include any additional steps or dependencies that might be necessary for your application.