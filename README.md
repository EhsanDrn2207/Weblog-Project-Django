
# Weblog Project

A **Django-based Weblog Application** designed for creating and managing blogs with an interactive web interface and robust API support. This project is built to be developer-friendly, responsive, and scalable, with seamless integration of modern tools like Docker and Django REST Framework.

---

## 🌟 Features

### Blog Management
- Create, read, update, and delete blog posts.
- Publish drafts or schedule posts.

### Comment System
- Allow users to leave comments on blog posts.
- Built-in comment moderation for admins.

### User Authentication
- Custom user model for flexibility.
- Secure login and logout functionality.

### API Endpoints
- Manage blogs and comments programmatically via RESTful API.
- Interactive API documentation powered by **Swagger** and **ReDoc**.

### Responsive Design
- Beautiful, mobile-friendly UI built with **Bootstrap 5** and **Crispy Forms**.

### Pagination
- Display blog posts and comments with smooth pagination.

### Containerized Deployment
- Ready-to-use **Docker** setup for local development and production.

---

## 🛠️ Technologies Used

| Stack                | Description                          |
|----------------------|--------------------------------------|
| **Backend**          | Django 5, Django REST Framework      |
| **Frontend**         | Bootstrap 5 (via Crispy Forms)       |
| **Database**         | PostgreSQL                          |
| **API Documentation**| drf-yasg (Swagger & ReDoc)           |
| **Environment Tools**| environs                            |
| **Containerization** | Docker, Docker Compose              |

---

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites
- Python 3.9+
- PostgreSQL
- Git
- Docker and Docker Compose

---

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Weblog-Project-Django.git
   cd blogs
   ```

2. **Set up environment variables**:
   Create a `.env` file in the project root and add:
   ```env
   DJANGO_SECRET_KEY=your_secret_key
   DJANGO_DEBUG=True
   DATABASE_NAME=your_db_name
   DATABASE_USER=your_db_user
   DATABASE_PASSWORD=your_db_password
   DATABASE_HOST=db
   DATABASE_PORT=5432
   ```

3. **Build and start Docker containers**:
   ```bash
   docker-compose up --build
   ```

4. **Access the application**:
   - Web interface: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
   - API documentation:
     - Swagger: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
     - ReDoc: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

5. **Stop the containers**:
   ```bash
   docker-compose down
   ```

---

## 📖 API Endpoints

| Endpoint              | HTTP Method      | Description                       |
|-----------------------|------------------|-----------------------------------|
| `/api/blogs/`         | GET, POST        | List all blogs or create a new one. |
| `/api/blogs/<id>/`    | GET, PUT, DELETE | Retrieve, update, or delete a blog post. |
| `/api/comments/`      | GET, POST        | List all comments or create a new one. |
| `/api/comments/<id>/` | GET, PUT, DELETE | Retrieve, update, or delete a comment. |

---

## 📂 Project Structure

```
weblog/
├── accounts/              # User authentication and management
├── blogs/                 # Blog and comment logic
├── config/                # Project configuration and settings
├── templates/             # HTML templates
├── static/                # Static files (CSS, JS, images)
├── docker-compose.yml     # Docker Compose configuration
├── Dockerfile             # Dockerfile for application containerization
└── manage.py              # Django management script
```

---

## 🌐 Deployment

You can deploy the project to any Docker-supported platform like **AWS**, **Azure**, or **Heroku**. For simpler setups, try platforms like **Render** or **PythonAnywhere** (if you remove Docker).

---

## 🧑‍💻 Author

Developed by **Ehsan Doroudian**.

Feel free to reach out for feedback, questions, or collaboration opportunities.

---

## 🤝 Contributing

At this time, this project is not open to external contributions. Suggestions and feedback are welcome! 

---

## 📜 License

Enjoy using **Weblog Project**! 🎉
