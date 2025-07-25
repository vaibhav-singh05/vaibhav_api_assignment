# 🚀 KPA Backend Assignment - Vaibhav Singh

This repository contains the solution to the **KPA Form API Assignment**, developed using **FastAPI** and **PostgreSQL**. The assignment demonstrates the implementation of two production-ready APIs — including full database integration, schema validation, environment-based config, and interactive API documentation.

---

## 🛠️ Tech Stack

| Technology         | Purpose                                |
|--------------------|----------------------------------------|
| **FastAPI**        | Web framework for building APIs        |
| **PostgreSQL**     | Relational database                    |
| **SQLAlchemy**     | ORM for DB operations                  |
| **Pydantic**       | Data validation and serialization      |
| **Uvicorn**        | ASGI server for FastAPI                |
| **python-dotenv**  | Load environment variables from `.env` |
| **HTML/CSS/JS**    | Simple interactive frontend            |

---

## 📌 Implemented APIs

### ✅ 1. `POST /api/forms/bogie-checksheet`
- **Description**: Submits bogie inspection data with component statuses.
- **Request**:
```json
{
  "inspector_name": "John Doe",
  "bogie_number": "BG123",
  "remarks": "All good"
}
```
- **Response**:
```json
{
  "id": 1,
  "inspector_name": "John Doe",
  "bogie_number": "BG123",
  "remarks": "All good"
}
```

---

### ✅ 2. `GET /api/forms/wheel-specifications`
- **Description**: Retrieves all available wheel specs.
- **Response**:
```json
[
  {
    "id": 1,
    "wheel_type": "Cast Iron",
    "diameter": "850mm",
    "material": "Steel Alloy"
  }
]
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone & Navigate

```bash
git clone https://github.com/your-username/kpa-backend-assignment.git
cd kpa-backend-assignment
```

### 2️⃣ Setup Virtual Environment

```bash
python -m venv env
env\Scripts\activate  # Windows
# or
source env/bin/activate  # Linux/macOS
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup PostgreSQL Database

Create a DB named `kpa_db` and ensure the `.env` file has:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=yourdatabasename
DB_USER=yourusername
DB_PASSWORD=yourpassword
```

### 5️⃣ One-Click Start (Backend + Frontend)

Run this command to start the backend and open the frontend automatically:

```bash
python start_project.py
```
- This will start the FastAPI backend and open the interactive frontend in your browser.
- Make sure your virtual environment is activated before running this command.

---

## 🌐 Frontend (HTML/CSS/JS)
- Located in the `frontend/` folder.
- Modern, interactive UI with notifications, loading states, and a warm color palette.
- **How to use manually:**
  1. Start the backend (`uvicorn app.main:app --reload`)
  2. Serve the frontend (optional, for best CORS support):
     ```bash
     cd frontend
     python -m http.server 8080
     ```
  3. Open [http://localhost:8080](http://localhost:8080) in your browser.

---

## 🔒 CORS Setup
- CORS middleware is enabled in `app/main.py` to allow frontend-backend communication.
- You can restrict allowed origins in the code for more security.

---

## 📂 Project Structure

```
vaibhav_api_assignment/
│
├── app/
│   ├── main.py              # App entrypoint (with CORS)
│   ├── database.py          # DB connection setup
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # DB operations
│   └── routes/
│       ├── bogie_checksheet.py
│       └── wheel_specifications.py
│
├── frontend/
│   ├── index.html           # Interactive frontend UI
│   ├── style.css            # Modern styles
│   └── script.js            # JS logic for API calls
│
├── start_project.py         # One-click start script
├── .env                     # Environment variables
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 🧪 Testing APIs

You can test using:
- ✅ Swagger UI → `/docs`
- ✅ Postman → import `kpa_postman_collection.json`
- ✅ The provided HTML frontend

---

## 📥 Deliverables

| Item                  | File Name                              |
|-----------------------|----------------------------------------|
| ✅ Source Code        | `vaibhav_kpa_backend_assignment.zip`   |
| ✅ Postman Collection | `vaibhav_postman_collection.json`      |
| ✅ README             | `vaibhav_kpa_readme.md`                |
| ✅ Video Demo         | `vaibhav_kpa_assignment_demo.mp4`      |

---

## 🙋‍♂️ About Me

**Vaibhav Singh**  
Backend Developer | Python Enthusiast | FastAPI & Django | PostgreSQL  
📍 Gorakhpur, Uttar Pradesh  
📫 Contact: vaibhavsingh273010@gmail.com

---

Thank you! 🙌
