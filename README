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

---

## 📌 Implemented APIs

### ✅ 1. `POST /api/forms/bogie-checksheet`
- **Description**: Submits bogie inspection data with component statuses.
- **Request**:
```json
{
  "adjusting_tube": "DAMAGED",
  "cylinder_body": "WORN OUT",
  "piston": "NEW",
  "piston_rod": "GOOD",
  "axle_box": "LOOSE",
  "anchor_link": "DAMAGED",
  "safety_loop": "OK"
}
```
- **Response**:
```json
{
  "id": 1,
  "inspector_name": "AutoFilled",
  "bogie_number": "AutoFilled",
  "remarks": "Saved successfully"
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
DB_NAME=kpa_db
DB_USER=postgres
DB_PASSWORD=Vaibhav@123
```

### 5️⃣ Run the Server

```bash
uvicorn app.main:app --reload
```

Open browser → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 Testing APIs

You can test using:
- ✅ Swagger UI → `/docs`
- ✅ Postman → import `kpa_postman_collection.json`

---

## 📂 Project Structure

```
kpa_backend/
│
├── app/
│   ├── main.py              # App entrypoint
│   ├── database.py          # DB connection setup
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # DB operations
│   └── routes/
│       ├── bogie_checksheet.py
│       └── wheel_specifications.py
│
├── .env                     # Environment variables
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 📥 Deliverables

| Item                 | File Name                             |
|----------------------|----------------------------------------|
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
