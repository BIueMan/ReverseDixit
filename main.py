from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from python_print_color import *

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
    if not is_user_exists(username):
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


user_dict = {}
# Dummy functions for simulating database queries
def is_user_exists(username: str):
    username = username.strip()
    
    def append_user(username):
        user_dict[username] = ["", ""]
        print(f"***** User added - {print_colors['yellow']}{username}{print_colors['reset']} *****")
        return False
    
    def error_message(username):
        print(f"***** {print_colors['red']}MINOR-ERROR:{print_colors['reset']} User exists - {print_colors['yellow']}{username}{print_colors['reset']} *****")
        return True
    
    return append_user(username) if username not in user_dict else error_message(username)


def process_text(text: str):
    username = 'todo add user to function'
    print(f"***** {print_colors['yellow']}{username}{print_colors['reset']} added new prompt was given - {print_colors['yellow']}{text}{print_colors['reset']} *****")
    return f"Processed Text: {text}"
