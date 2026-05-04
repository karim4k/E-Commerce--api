# E-Commerce--api
# Cloud-Based E-commerce REST API

## 📌 Overview

This project is a cloud-based e-commerce REST API built using FastAPI. It provides a simple product catalogue and allows users to create and manage orders.

The application is designed to be **cloud-ready**, with:

* Global error handling
* Secure environment variable usage
* Public documentation hosted on AWS S3

---

## 🚀 Features

* View all products
* Create new orders
* Retrieve all orders
* Global error handling system
* Environment-based configuration
* Deployed documentation website (AWS S3)

---

## 🛠️ Technologies Used

* Python (FastAPI)
* AWS S3 (Static Website Hosting)
* Postman (API testing)

---

## 📡 API Endpoints

| Method | Endpoint  | Description           |
| ------ | --------- | --------------------- |
| GET    | /         | Check API status      |
| GET    | /products | Retrieve all products |
| POST   | /orders   | Create a new order    |
| GET    | /orders   | Retrieve all orders   |

---

## 📘 API Documentation

Interactive API docs (Swagger UI) available at:

```
/docs
```

---

## 🧪 Example Request

### Create Order

POST /orders

```json
{
  "items": ["Laptop", "Phone"]
}
```

---

## 🌐 Live Links

* API (CodeSandbox): https://w2f7hl-8000.csb.app/
* AWS S3 Website: http://karim-s5-final-exam-max5.s3-website.eu-north-1.amazonaws.com

---

## ⚙️ How to Run Locally

1. Clone the repository:

```
git clone https://github.com/yourusername/ecommerce-api.git
```

2. Navigate into the project:

```
cd ecommerce-api
```

3. Install dependencies:

```
pip install fastapi uvicorn
```

4. Run the server:

```
uvicorn main:app --reload
```

5. Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 🔐 Environment Variables

The project uses environment variables for security:

```
MY_SECRET_KEY=your_secret_key
```

---

## 👨‍💻 Author

Karim Kallel

---
