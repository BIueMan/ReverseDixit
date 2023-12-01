from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mounting the static files (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates directory
templates = Jinja2Templates(directory="templates")


# Page 1: Login
@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
async def create_user(request: Request, username: str = Form(...)):
    # Check if user exists (in a real app, you would perform database queries here)
    if not user_exists(username):
        # Redirect to page 2
        return templates.TemplateResponse("page2.html", {"request": request, "username": username})
    else:
        # User already exists, handle accordingly (e.g., show an error message)
        return templates.TemplateResponse("login.html", {"request": request, "error_message": "User already exists"})


# Page 2: Send Text
@app.post("/send-text", response_class=HTMLResponse)
async def send_text(request: Request, text: str = Form(...)):
    # Process the text (in a real app, you might save it to a database, etc.)
    processed_text = process_text(text)

    # Display the processed text
    return templates.TemplateResponse("result.html", {"request": request, "processed_text": processed_text})


# Dummy functions for simulating database queries
def user_exists(username: str):
    # In a real app, you would check the database for user existence
    # This is just a dummy function
    return False


def process_text(text: str):
    # In a real app, you might perform some processing on the text
    # This is just a dummy function
    return f"Processed Text: {text}"
