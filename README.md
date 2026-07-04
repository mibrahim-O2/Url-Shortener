<div align="center">
  
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightblue?logo=sqlite)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)
</br>

# URL Shortener
A simple URL shortener web application built with **Python** and **Flask**.  
Convert long, hard-to-share URLs into short, clean links instantly.
> Built as part of the **Backend Development**

</div>

---

## Features

- Paste any long URL and get a short link instantly
- Click the short link to be redirected to the original URL
- Input validation — rejects empty or malformed URLs
- Friendly 404 error page for invalid short codes
- Clean, responsive UI built with Bootstrap 5
- Lightweight SQLite database — no setup required

---

## Tech Stack

| Technology  | Purpose                            |
|-------------|------------------------------------|
| Python 3    | Core programming language          |
| Flask       | Web framework (routing, rendering) |
| SQLite      | Database (stores URL mappings)     |
| Jinja2      | HTML templating engine             |
| Bootstrap 5 | Frontend styling and layout        |

---

## Folder Structure

```text
codealpha-url-shortener/
│
├── app.py            → Main Flask app (routes and logic)
├── database.py       → Database setup and query functions
├── requirements.txt  → Python dependencies
├── README.md         → Project documentation
│
├── templates/
│   ├── base.html     → Shared layout (navbar, Bootstrap)
│   ├── index.html    → Home page (URL input form)
│   ├── result.html   → Result page (shows short URL)
│   └── 404.html      → Error page (invalid short code)
│
└── urls.db           → SQLite database (auto-created on first run)
```

---

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/mibrahim-O2/codealpha-url-shortener.git
cd codealpha-url-shortener
```

### 2. Create a Virtual Environment

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

---

## How To Run

```powershell
python app.py
```

Then open your browser and visit:

```
http://localhost:5000
```

---

## Screenshots

### Home Page — URL Input Form
![Home Page](https://github.com/mibrahim-O2/codealpha-url-shortener/blob/main/ScreenShoots/screenshot-1-home.png?raw=true)

### Result Page — Short URL Generated
![Result Page](https://github.com/mibrahim-O2/codealpha-url-shortener/blob/main/ScreenShoots/screenshot-2-result.png?raw=true)

### Redirect — Browser Goes to Original URL
![Redirect](https://github.com/mibrahim-O2/codealpha-url-shortener/blob/main/ScreenShoots/screenshot-3-redirect.png?raw=true)

### 404 Page — Invalid Short Code
![404 Page](https://github.com/mibrahim-O2/codealpha-url-shortener/blob/main/ScreenShoots/screenshot-4-404.png?raw=true)

---
<div align="center">

## Author
**Muhammad Ibrahim**
BS Computer Science (Student)

[![LinkedIn](https://img.shields.io/badge/Connect%20on%20LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/muhammad-ibrahim-o2)

</div>

---
<div align="center">
    
## License

This project is developed for self learning and educational purposes.
&copy; 2026 Muhammad Ibrahim. All rights reserved.

<div align="center">

Built with Python · Flask · SQLite · Bootstrap 5

</div>
