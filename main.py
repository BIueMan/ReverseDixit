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


@app.post("/waiting-room", response_class=HTMLResponse)
async def create_user(request: Request, username: str = Form(...)):
    # Check if user exists
    if not is_user_exists(username):
        # Redirect to waiting lobby
        return templates.TemplateResponse("waiting_lobby.html", {"request": request, "username": username, "users": [key for key in USER_DICT.keys()]})
    else:
        # User already exists, handle accordingly
        return templates.TemplateResponse("login.html", {"request": request, "error_message": "User already exists"})

@app.post("/enter-prompt-init", response_class=HTMLResponse)
async def enter_prompt_init(request: Request, username: str = Form(...)):
    return templates.TemplateResponse("enter_prompt_init.html", {"request": request, "username": username})


# Page 2: Send Text
@app.post("/waiting_ai", response_class=HTMLResponse)
async def send_text(request: Request, username: str = Form(...), text: str = Form(...)):
    # Process the text (in a real app, you might save it to a database, etc.)
    processed_text = process_text(username, text)

    # Display the processed text along with the username
    return templates.TemplateResponse("waiting_ai.html", {"request": request, "username": username, "processed_text": processed_text})


USER_DICT = {}
# Dummy functions for simulating database queries
def is_user_exists(username: str):
    username = username.strip()
    
    def append_user(username):
        USER_DICT[username] = {"global_prompt": "", "current_prompt": ""}
        print(f"***** User added - {print_colors['yellow']}{username}{print_colors['reset']} *****")
        return False
    
    def error_message(username):
        print(f"***** {print_colors['red']}MINOR-ERROR:{print_colors['reset']} User exists - {print_colors['yellow']}{username}{print_colors['reset']} *****")
        return True
    
    return append_user(username) if username not in USER_DICT else error_message(username)


def process_text(username: str, text: str):
    USER_DICT[username]["global_prompt"] = text
    print(f"***** {print_colors['yellow']}{username}{print_colors['reset']} added new prompt was given - {print_colors['yellow']}{text}{print_colors['reset']} *****")
    return f"Processed Text: {text}"
