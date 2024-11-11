
# Task Management Microservices Project

## Overview

This project is a microservice-based **Task Management System** built with Django REST Framework (DRF). 
The system provides functionalities to manage tasks, handle user roles, and send notifications. 
Key features include user and task management, automated notifications for task events, and 
a dashboard API to view assigned tasks and relevant notifications.

## Deployment in Cloud Service(Render)

The project is deployed in a live environment(Render Cloud) as a API Services with PostgreSQL DB.

Deployed URL: [https://task-mgr-services.onrender.com/]

Please check out the above URL which covers all use cases defined in the practical test document.

## API Documentation
The complete API documentation of this project has been provided and uploaded in the current Github repository having filename as 
API Documentation Filename in github: <h3>Task_Management_API_Documentation.docx</h3>

---

### Main Components

- **Task Service**: Manages tasks and their assignments. Provides CRUD operations, status updates, 
  and due date management.
- **User Service**: Handles user registration, authentication, and user roles. Integrates JWT-based 
  authentication for securing endpoints.
- **Notification Service**: Sends notifications on task-related events, such as task assignments, 
  reassignments, and approaching due dates. Uses Django Signals for event-driven notifications.

---

## Project Architecture

This microservice-based architecture separates core functionalities across services, allowing 
each component to operate independently. The services communicate via shared databases and 
Django signals.

- **Task Management Service**: Handles tasks with fields like title, description, status, 
  due date, and assigned user.
- **User Management Service**: Manages users with roles like admin and regular users. Admins 
  can manage tasks, while regular users can only view tasks assigned to them.
- **Notification Service**: Stores and serves notifications for task events using a centralized 
  model and provides a dashboard API that consolidates task and notification data.

---

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd task_management_microservices
   ```

2. **Create and Activate Virtual Environment**:

   ```bash
   python -m venv env
   source env/bin/activate    # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up PostgreSQL Database**:

   - Create a PostgreSQL database for the project.
   - Add database credentials in `settings.py`:

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your_database_name',
             'USER': 'your_database_user',
             'PASSWORD': 'your_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser**:

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

8. **Access Swagger Documentation** (for API testing and documentation):

   - **Swagger UI**: [http://127.0.0.1:8000/api/docs/swagger/](http://127.0.0.1:8000/api/docs/swagger/)
   - **ReDoc**: [http://127.0.0.1:8000/api/docs/redoc/](http://127.0.0.1:8000/api/docs/redoc/)

---

## API Endpoints

### User Service

- **POST** `/api/users/register/`: Register a new user.
- **POST** `/api/users/login/`: Login to obtain JWT tokens.
- **GET** `/api/users/dashboard/`: Retrieve the user dashboard with tasks and notifications.

### Task Service

- **POST** `/api/tasks/`: Create a new task (admin only).
- **GET** `/api/tasks/`: List all tasks (admin) or assigned tasks (regular users).
- **PUT** `/api/tasks/{id}/`: Update a task for Task id, including reassignment and status changes.
- **DELETE** `/api/tasks/{id}/`: Deletes a task based on Task id.

### Notification Service

- **GET** `/api/notifications/`: List all unread notifications for the user.

---

## Key Features

1. **Role-Based Access Control**: Only admins can create and manage tasks, while regular users 
   can only view their assigned tasks.

2. **Notifications**: Users receive notifications when:
   - A task is assigned to them.
   - A task is reassigned.
   - A task's due date is within the next 24 hours.
   - Notifications are viewable in the user dashboard.

3. **Dashboard API**: Provides a consolidated view of tasks and notifications for each user.

---

## Technologies Used

- **Django REST Framework**: For building APIs.
- **drf-spectacular**: For generating OpenAPI 3.0 documentation.
- **PostgreSQL**: Database for storing user, task, and notification data.
- **JWT Authentication**: For secure access to API endpoints.

---

## Additional Notes

- **Environment Variables**: Store sensitive information like database credentials, secret keys, 
  and email configurations in environment variables or a `.env` file (if using `django-environ`).
- **Email Notifications**: Configure email settings in `settings.py` to enable email notifications 
  (e.g., SMTP setup for task status change alerts).

---

## License

This project is licensed under the MIT License.

---

## Contact

For support or inquiries, please contact [support@taskmanagement.com](mailto:support@taskmanagement.com).

