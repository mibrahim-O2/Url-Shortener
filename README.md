# ✂️ URL Shortener

A simple URL shortener web application built with Python and Flask.
Convert long, hard-to-share URLs into short, clean links instantly.

Built as part of the **CodeAlpha Backend Development Internship**.

---

## 🚀 Features

- Paste any long URL and get a short link instantly
- Click the short link to be redirected to the original URL
- Input validation (rejects empty or malformed URLs)
- Friendly error page for invalid short codes
- Clean, responsive UI built with Bootstrap 5
- Lightweight SQLite database — no setup required

---

## 🛠 Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Flask | Web framework (routing, rendering) |
| SQLite | Database (stores URL mappings) |
| Jinja2 | HTML templating engine |
| Bootstrap 5 | Frontend styling and layout |

---

## 📁 Folder Structure

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

## ⚙️ Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/codealpha-url-shortener.git
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

## ▶️ How To Run

```powershell
python app.py
```

Then open your browser and visit:
http://localhost:5000

---

## 📸 Screenshots

### Home Page — URL Input Form
[Screenshot 1 Here]

### Result Page — Short URL Generated
[Screenshot 2 Here]

### Redirect — Browser Goes to Original URL
[Screenshot 3 Here]

### 404 Page — Invalid Short Code
[Screenshot 4 Here]

---

## 👨‍💻 Author

**Ibrahim** — BS Computer Science Final Year Student
CodeAlpha Backend Development Internship

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).