# 📝 Demo Comment Web App

This is a lightweight full-stack demo application showcasing a **FastAPI backend**, **MongoDB database**, and a **Next.js frontend**.
It provides a simple comment system where users can:

* View all comments
* Add a new comment
* Edit a comment’s text
* Delete a specific comment

The backend exposes CRUD APIs, and the frontend renders a clean UI with a navbar/footer and interactive comment widgets.

---

## 🚀 Tech Stack

### **Backend**

* [FastAPI](https://fastapi.tiangolo.com/)
* [MongoDB](https://www.mongodb.com/)
* [Docker](https://www.docker.com/)

### **Frontend**

* [Next.js (React)](https://nextjs.org/)

### **Log Viewer**

* [Dozzle](https://dozzle.dev/)

---

## 🧰 Prerequisites

Please ensure the following are installed on your machine:

* **Docker** & **Docker Compose**
    [install](https://docs.docker.com/engine/install/)
* **Node.js** & **npm**
    [install](https://nodejs.org/en/download)

---

## 📦 Project Structure

```
root/
├─ docker/                 # Docker compose setup for backend + MongoDB
├─ server/                 # FastAPI backend
│   ├─ .env                # Contains the Mongo URI
│   └─ ...                 # CRUD logic for comments
├─ client/                 # Next.js frontend
│   └─ ...                 # UI + comment widget
├─ data/                   # Example comment JSON data
└─ README.md
```

---

## 🐳 Running the Backend (Docker)

1. Navigate to the **docker** folder:

```bash
cd docker
```

2. Start all services:

```bash
docker compose up --build
```

This starts:

* **MongoDB**
* **FastAPI server** (default mapped to `http://localhost:8020`)

---

## 🗄️ Initial Database Setup

The MongoDB instance starts **empty**.
To test the API, you must manually insert some comment data.

### You can initialize data in two ways:

#### **Option 1 — Use Swagger UI**

Open:

```
http://localhost:8020/docs
```

Use the available CRUD endpoints to **POST** some comment data.

#### **Option 2 — Use MongoDB GUI**

Use tools like **MongoDB Compass** and connect with the URI found in:

```
server/.env
```

Insert comment documents directly into the `comment` collection.

---

#### **Option 3 — Use UI**

Start the client UI, and add the comment data from the UI.

## 🖥️ Running the Frontend (Next.js)

1. Navigate to the **client** folder:

```bash
cd client
```

2. Install dependencies:

```bash
npm install
```

3. Start the development server:

```bash
npm run dev
```

The app will be available at:

```
http://localhost:3000
```

---

## 🔧 Backend Features (FastAPI)

The backend provides basic CRUD operations for comments:

* **GET /comment** — Retrieve all comments
* **Get /comment/{id}** - Retrieve a comment
* **POST /comment** — Add a new comment
* **PUT /comment/{id}** — Edit a comment
* **DELETE /comment/{id}** — Delete a comment

Swagger documentation available at:

```
http://localhost:8020/docs
```

---

## 🎨 Frontend Features (Next.js)

The frontend demonstrates:

* A simple **navbar** and **footer**
* A central **comment widget** section
* Ability for users to:

  * View all comments
  * Add comments
  * Edit comment text
  * Delete comments

---

## 📂 Sample Data

The `data/` folder contains example comment JSON files you may use to seed the database manually.

---

## ✔️ Summary

This demo app is intended as a quick showcase of:

* Docker-orchestrated backend services
* FastAPI CRUD design
* MongoDB integration
* A minimal Next.js frontend consuming the API
