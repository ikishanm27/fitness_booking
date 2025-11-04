# 🏋️ Simple Fitness Booking API

A beginner-friendly **FastAPI** project that allows users to **sign up**, **log in**, **create fitness classes**, and **book slots** for available classes.
It includes **basic authentication**, **SQLite database**, and **CRUD API endpoints** — all in a single Python file for easy understanding.

---

## 📖 Project Overview

This API simulates a simple **Fitness Studio Booking System**, where:

* Users can sign up and log in.
* Authenticated users can:

  * Create new fitness classes (Yoga, HIIT, Zumba, etc.)
  * View all upcoming classes.
  * Book slots in a class.
  * View their personal bookings.

---

## ⚙️ Tech Stack

* **Language:** Python 3.10+
* **Framework:** FastAPI
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Authentication:** JWT (JSON Web Token)

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fitness-booking-api.git
cd fitness-booking-api
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] jwt
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

Server will start at:

👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🧠 How to Run Locally

1. Start the server (`uvicorn main:app --reload`)
2. Open your browser and go to **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**
3. You’ll see an interactive **Swagger UI** with all endpoints.
4. You can also test using **Postman** or **curl** commands (see below).

---

## 🧪 API Usage (Examples)

### 1️⃣ Sign Up

**Endpoint:** `POST /signup`

**Request Body:**

```json
{
  "name": "Alice",
  "email": "alice@example.com",
  "password": "password123"
}
```

**Response:**

```json
{
  "message": "Signup successful"
}
```

---

### 2️⃣ Log In

**Endpoint:** `POST /login`

**Request Body:**

```json
{
  "email": "alice@example.com",
  "password": "password123"
}
```

**Response:**

```json
{
  "access_token": "your_jwt_token_here",
  "token_type": "bearer"
}
```

💡 Copy the `access_token` and click the **Authorize** button in Swagger UI to use protected endpoints.

---

### 3️⃣ Create a Class (Authenticated)

**Endpoint:** `POST /classes`

**Request Body:**

```json
{
  "name": "Morning Yoga",
  "dateTime": "2025-11-06T07:00:00Z",
  "instructor": "John Doe",
  "availableSlots": 15
}
```

**Response:**

```json
{
  "message": "Class created successfully"
}
```

---

### 4️⃣ Get All Classes

**Endpoint:** `GET /classes`

**Response Example:**

```json
[
  {
    "id": 1,
    "name": "Morning Yoga",
    "dateTime": "2025-11-06T07:00:00",
    "instructor": "John Doe",
    "availableSlots": 15
  }
]
```

---

### 5️⃣ Book a Class (Authenticated)

**Endpoint:** `POST /book`

**Request Body:**

```json
{
  "class_id": 1,
  "client_name": "Alice",
  "client_email": "alice@example.com"
}
```

**Response:**

```json
{
  "message": "Class booked successfully"
}
```

---

### 6️⃣ View Your Bookings

**Endpoint:** `GET /bookings`

**Response:**

```json
[
  {
    "id": 1,
    "user_id": 1,
    "class_id": 1,
    "client_name": "Alice",
    "client_email": "alice@example.com",
    "booked_at": "2025-11-04T12:30:00"
  }
]
```

---

## 🧰 Useful Tools

* **FastAPI Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc UI:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
* **Database:** `fitness.db` (auto-created)

---

## 🏁 Next Steps

* Add role-based access (trainer vs user)
* Add email notifications after booking
* Deploy to Render / Railway / Vercel

---

**Author:** Your Name
**License:** MIT
**Version:** 1.0.0
