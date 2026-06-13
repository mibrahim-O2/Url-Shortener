# app.py
# This is the main Flask application file.
# It defines all the routes (pages and actions) of our URL shortener.

import random
import string

from flask import Flask, render_template, request, redirect, url_for, flash
from database import init_db, save_url, find_url

# Create the Flask app instance.
# Flask uses this to know where to look for templates and static files.
app = Flask(__name__)

# Secret key is required to use Flask's flash messaging system.
# Flash messages show alerts to the user (like "Invalid URL!").
app.secret_key = "your_secret_key_here"

# Initialize the database when the app starts.
# This creates the 'urls' table if it doesn't exist yet.
init_db()


# ─────────────────────────────────────────────
# HELPER FUNCTION: Generate Short Code
# ─────────────────────────────────────────────

def generate_short_code(length=6):
    """
    Generates a random short code made of letters and digits.
    Example output: "aB3kX9"

    length=6 means the code will be 6 characters long.
    """
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    return "".join(random.choices(characters, k=length))


# ─────────────────────────────────────────────
# ROUTE 1: Home Page
# ─────────────────────────────────────────────

@app.route("/")
def index():
    """
    GET /
    Shows the home page with the URL input form.
    """
    return render_template("index.html")


# ─────────────────────────────────────────────
# ROUTE 2: Shorten URL
# ─────────────────────────────────────────────

@app.route("/shorten", methods=["POST"])
def shorten():
    """
    POST /shorten
    Receives the long URL from the form.
    Validates it, generates a short code, saves to DB,
    then shows the result page with the short URL.
    """

    # Get the URL the user typed in the form.
    # "original_url" matches the name="" attribute in our HTML form input.
    original_url = request.form.get("original_url", "").strip()

    # ── Validation ──────────────────────────────
    # Make sure the user didn't submit an empty form.
    if not original_url:
        flash("Please enter a URL.", "danger")
        return redirect(url_for("index"))

    # Make sure the URL starts with http:// or https://
    # This prevents storing garbage like "abc" or "google"
    if not original_url.startswith(("http://", "https://")):
        flash("Invalid URL. Please include http:// or https://", "danger")
        return redirect(url_for("index"))

    # ── Generate Unique Short Code ───────────────
    # Keep generating until we get a code that isn't already in the DB.
    # This prevents duplicate short codes.
    short_code = generate_short_code()
    while find_url(short_code) is not None:
        short_code = generate_short_code()

    # ── Save to Database ─────────────────────────
    save_url(short_code, original_url)

    # ── Build the Full Short URL ─────────────────
    # url_for("redirect_url", short_code=short_code) builds: /aB3kX9
    # request.host_url gives us: http://localhost:5000/
    # Together: http://localhost:5000/aB3kX9
    short_url = request.host_url + short_code

    # Show the result page with the short URL
    return render_template("result.html", short_url=short_url, original_url=original_url)


# ─────────────────────────────────────────────
# ROUTE 3: Redirect Short URL
# ─────────────────────────────────────────────

@app.route("/<short_code>")
def redirect_url(short_code):
    """
    GET /<short_code>
    Looks up the short code in the database.
    If found → redirects the user to the original long URL.
    If not found → shows a 404 error page.
    """

    # Search the database for this short code
    row = find_url(short_code)

    if row is None:
        # Short code doesn't exist — show a friendly error
        return render_template("404.html"), 404

    # row["original_url"] gives us the original long URL
    # redirect() tells the browser to go to that URL
    return redirect(row["original_url"])


# ─────────────────────────────────────────────
# Run the App
# ─────────────────────────────────────────────

if __name__ == "__main__":
    # debug=True means Flask will auto-reload when you save changes.
    # Never use debug=True in a real production app.
    app.run(debug=True)