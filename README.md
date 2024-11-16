
# Weblog Project

A **Django-based Weblog application** that allows users to create, read, update, and delete blog posts and comments. It includes API endpoints powered by **Django REST Framework (DRF)** with **drf-yasg** for API documentation.

---

## Features

- **Blog Management**: 
  - Create, Read, Update, and Delete blog posts.
  - Support for drafts and published posts.
- **Comment System**: 
  - Add comments to blog posts.
  - Admin moderation of comments.
- **Authentication**: 
  - Custom user model.
  - Secure login and logout functionality.
- **Pagination**: Blogs are displayed with pagination support.
- **API Endpoints**: 
  - Blog and Comment management through a RESTful API.
  - API documentation available via Swagger and ReDoc.
- **Responsive Design**: 
  - Integration with **Crispy Forms** using Bootstrap 5.
- **Docker Support**: Simplified setup with Docker Compose for development and production.

---

## Technologies Used

- **Backend**: Django 5, Django REST Framework
- **Frontend**: Bootstrap 5 (via Crispy Forms)
- **Database**: PostgreSQL
- **API Documentation**: drf-yasg (Swagger & ReDoc)
- **Environment Management**: environs
- **Containerization**: Docker, Docker Compose

---

## Installation

### Prerequisites
- Python 3.9+
- PostgreSQL
- Git
- A virtual environment tool (e.g., venv or virtualenv)
- Docker and Docker Compose installed on your system.

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/WEBLOG_PROJECT_DJANGO.git
   cd blogs
   ```

2. **Set up environment variables**:
   Create a `.env` file in the project root with the following:
   ```env
   DJANGO_SECRET_KEY=your_secret_key
   DJANGO_DEBUG=True
   ```

3. **Build and start the containers**:
   ```bash
   docker-compose up --build
   ```

4. **Access the application**:
   - Web interface: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`
   - API documentation:
     - Swagger: `http://127.0.0.1:8000/swagger/`
     - ReDoc: `http://127.0.0.1:8000/redoc/`

5. **Stop the containers**:
   ```bash
   docker-compose down
   ```

---

## API Endpoints

| Endpoint              | HTTP Method | Description                       |
|-----------------------|-------------|-----------------------------------|
| `/api/blogs/`         | GET, POST   | List or create blog posts.        |
| `/api/blogs/<id>/`    | GET, PUT, DELETE | Retrieve, update, or delete a blog. |
| `/api/comments/`      | GET, POST   | List or create comments.          |
| `/api/comments/<id>/` | GET, PUT, DELETE | Retrieve, update, or delete a comment. |

---

## Project Structure

```
weblog/
├── accounts/              # Custom user model and authentication
├── blogs/                 # Blog and Comment models, views, and APIs
├── config/                # Project configuration
├── templates/             # HTML templates for the web interface
├── static/                # Static files (CSS, JS, images)
├── docker-compose.yml     # Docker Compose configuration
├── Dockerfile             # Dockerfile for containerizing the application
└── manage.py              # Django management script
```

---

## Screenshots

### Home Page
![Home Page](https://via.placeholder.com/800x400.png?text=Screenshot+Home+Page)

### Swagger Documentation
![Swagger](https://via.placeholder.com/800x400.png?text=Swagger+Documentation)

---

## Author

This project was developed by **Your Name**. Feel free to reach out with any questions or feedback.

---

## Contributing

At the moment, this project does not accept contributions as it is solely developed and maintained by the author.
