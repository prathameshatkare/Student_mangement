
---

## 📚 Student Management System

A simple Flask web application to manage student information like **Name**, **Roll Number**, and **Course**. Built with Python, Flask, HTML, and deployed on [PythonAnywhere](https://www.pythonanywhere.com).

---

### 🌟 Features

- Add new students
- View a list of students
- Edit student details (optional)
- Delete student records (optional)
- Simple web interface
- Flask backend with templates
- Deployed and live on PythonAnywhere

---

### 🛠️ Tech Stack

- **Frontend:** HTML, CSS (optional JS)
- **Backend:** Python, Flask
- **Database:** SQLite (or any other Flask-supported DB)
- **Hosting:** PythonAnywhere

---

### 🗂️ Folder Structure

```
student-management/
├── app.py                # Main Flask app
├── templates/            # HTML files
│   └── index.html
├── static/               # CSS/JS files (optional)
│   ├── style.css
├── requirements.txt      # Python dependencies
├── README.md             # You're here!
```

---

### 🚀 Getting Started (Local)

1. **Clone the repo**:
   ```bash
   git clone https://github.com/yourusername/student-management.git
   cd student-management
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:
   ```bash
   python app.py
   ```

5. **Visit**: `http://127.0.0.1:5000` in your browser

---

### ☁️ Deploy on PythonAnywhere

1. Upload your project to `/home/yourusername/mysite/`
2. Go to the **Web** tab on PythonAnywhere
3. Set your **WSGI config file** to point to `app.py`
4. Reload the web app from the PythonAnywhere dashboard
5. Done!

---

### ✅ To Do (Optional)

- [ ] Add form validation
- [ ] Connect to MySQL or PostgreSQL
- [ ] Add login/authentication
- [ ] Pagination for large datasets

---

### 👨‍💻 Author

**Your Name**  
[GitHub](https://github.com/prathameshatkare) | [LinkedIn](https://www.linkedin.com/in/prathamesh-atkare-6223aa255/)

---

Let me know if you want to personalize this (e.g., add your GitHub link, live site URL, or screenshots). Want me to generate a `requirements.txt` too?
