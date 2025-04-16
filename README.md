<h1 align="center">WheelsAPI</h1>

## Technologies used:

- [Python](https://www.python.org/)
  - Libraries:
    - **Environment Configuration:**
      - [FastAPI](https://fastapi.tiangolo.com/)
      - [Uvicorn](https://www.uvicorn.org/)
      - [Loguru](https://github.com/Delgan/loguru)
    - **Database:**
      - [Psycopg2-binary](https://www.psycopg.org/)
      - [SQLAlchemy](https://www.sqlalchemy.org/)
      - [Alembic](https://alembic.sqlalchemy.org/en/latest/)
    - **ORM Configuration:**
      - [Pydantic](https://docs.pydantic.dev/latest/)
    - **Extern Requests:**
      - [HTTPX](https://www.python-httpx.org/)
    - **Autentication and Authorization:**
      - [PyJWT](https://github.com/jpadilla/pyjwt)
      - [Bcrypt](https://github.com/pyca/bcrypt/)
    - **Asynchronous Processing:**
      - [Pika](https://pika.readthedocs.io/en/stable/)
    - **Cache and Optimization:**
      - [Redis-py](https://github.com/redis/redis-py)
    - **Monitoring and Observability:**
      - [Prometheus](https://prometheus.io/)
      - [OpenTelemetry](https://opentelemetry.io/)
      - [Grafana](https://grafana.com/)
    - **Templates and Emails:**
      - [Jinja2](https://jinja.palletsprojects.com/en/stable/)
      - [fastapi-mail](https://pypi.org/project/fastapi-mail/)
    - **Tests:**
      - [Pytest](https://docs.pytest.org/en/stable/)
      - [Pytest-asyncio](https://pypi.org/project/pytest-asyncio/)
      - [Freezegun](https://github.com/spulec/freezegun)
      - [Factory-boy](https://factoryboy.readthedocs.io/en/stable/)
      - [Testcontainers](https://testcontainers.com/)
    - **Security and Validation:**
      - [Slowapi](https://github.com/laurents/slowapi)
      - [FastAPI Secirity](https://fastapi.tiangolo.com/tutorial/security/#openid-not-openid-connect)
- [PostgreSQL](https://www.postgresql.org/)
- [RabbitMQ](https://www.rabbitmq.com/)
- [Docker](https://www.docker.com/)

## Features:

1. **Environment Setup**:

   - [x] Configure Python, virtual environment, and initial dependencie
   - [x] Structure the FastAPI project with appropriate folders
   - [x] Set up logging system

2. **Database Design:**

   - [x] Design entity-relationship model for vehicles, users and sales
     - [x] Save images as Base64
   - [x] Implement migrations with Alembic
   - [x] Configure the PostgreSQL Docker image

3. **ORM Configuration:**

   - [x] Implement SQLAlchemy models
   - [x] Configure relationships between entities
   - [x] Create Pydantic schemas for validation

4. **Basic API:**

   - [x] Upgrade database to add type of vehicles
   - [x] Implement CRUD endpoints for vehicles, users and sales
     - **Users:**
       - [x] Create user
       - [x] Update user
       - [x] Delete user
       - [x] Get user by ID
     - **Vehicles:**
       - [x] Create vehicle
       - [x] Update vehicle
       - [x] Delete vehicle
       - [x] Get vehicle by id
       - [x] Get vehicles by user
       - [x] Get vehicles by type
       - [x] Get vehicles by year
     - **Sales:**
       - [x] Create ad
       - [x] Update info about ad
       - [x] Delete ad
       - [x] Get ad
       - [x] Get sales vehicles
   - [x] Document API with Swagger/OpenAPI
   - [x] Fild email in user will be validate
   - [x] Update user not do hash in password

5. **Authentication and Authorization:**

   - [x] Implement JWT
   - [x] Implement endpoints for auth
   - [x] Configure JWT system with refresh tokens
   - [x] Implement JWT in others endpoints
   - [x] Update errors
   - [ ] Update README.md

6. **Business Features:**

   - [ ] Add paging in sales endpoint
   - [ ] Implement search system and filters for vehicles
   - [ ] Create endpoints for listing management
   - [ ] Develop favorites system and viewing history

7. **Asynchronous Processing:**

   - [ ] Configure background tasks with Celery or FastAPI background tasks
   - [ ] Implement notifications and alerts (RabbitMQ)
   - [ ] Develop periodic report generation
   - [ ] Configure RabbitMQ in Docker

8. **Events and Lifecycle Integration:**

   - [ ] Implement application events (new listings, completed sales)
   - [ ] Configure FastAPI lifecycle events
   - [ ] Create webhooks system for integrations

9. **Cache and Optimization:**

   - [ ] Implement Redis for caching frequent queries
   - [ ] Optimize queries with SQLAlchemy
   - [ ] Configure appropriate TTL for different data types

10. **Monitoring and Observability:**

    - [ ] Configure metrics system (Prometheus)
    - [ ] Implement request tracing (OpenTelemetry)
    - [ ] Create monitoring dashboards

11. **Templates and Emails:**

    - [ ] Configure template system (Jinja2)
    - [ ] Implement email sending for notifications
    - [ ] Create templates for different types of communication

12. **Tests:**

    - [ ] Write unit tests
    - [ ] Implement integration tests
    - [ ] Configure CI/CD for automated test execution

13. **Documentation:**

    - [ ] Document system architecture
    - [ ] Create usage examples and tutorials
    - [ ] Develop documentation for developers

14. **Security and Validation:**

    - [ ] Implement rate limiting
    - [ ] Configure advanced input validation
    - [ ] Audit and reinforce API security

15. **Deployment and Containerization:**

    - [x] Dockerize the application
    - [x] Configure Docker Compose for development
      - [x] Configure the database
      - [x] Configure the application
      - [ ] Configure the Nginx
    - [ ] Prepare for deployment in production environments

## How to Run:

1. Clone the repository.

2. Create a `.env` file with the required variables.

   - `DATABASE_URL`
   - `PRIVATE_KEY`
   - `EXPIRE_TIME_JWT`

3. Build and start the application using Docker:

```bash
docker compose up --build
```

4. Access the API documentation at `http://localhost:8000/docs`.

## Structure of Project:

This repository follows a modular and scalable architecture to ensure ease of development and maintainability. Below is an overview of the purpose of each folder and file:

```
WheelsAPI/
├── .venv
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── auth.py
│   │   ├── sales.py
│   │   ├── users.py
│   │   └── vehicles.py
│   ├── core/
│   │   ├── errors/
│   │   │   ├── sales_errors.py
│   │   │   ├── users_errors.py
│   │   │   └── vahicles_errors.py
│   │   ├── securrity.py
│   │   └── logging.py
│   ├── models/
│   │   ├── sales.py
│   │   ├── users.py
│   │   └── vehicles.py
│   ├── schemas/
│   │   ├── auth.py
│   │   ├── generic.py
│   │   ├── sales.py
│   │   ├── users.py
│   │   └── vehicles.py
│   ├── crud/
│   │   ├── sales.py
│   │   ├── users.py
│   │   └── vehicles.py
│   └── db/
│       └── session.py
├── tests/
│       └── test.py
├── logs/
│       └── file_log.log
├── migrations/
│       ├── versions/
│       ├── env.py
│       └── README
├── .env
├── .gitignore
├── .python-version
├── .dockerignore
├── docker-compose.yaml
├── Dockerfile
├── entrypoint.sh
├── alembic.ini
├── README.md
└── requirements.txt
```

### Folder and File Overview

#### **Core Folders:**

- `app/`: The application folder, structured into modular components for easy development and scaling.

  - `api/`: API routes and controllers.

  - `core/`: Configuration and core setup files.

  - `models/`: Database models defined with SQLAlchemy.

  - `schemas/`: Pydantic schemas for data validation.

  - `crud/`: Handles Create, Read, Update, Delete operations.

  - `db/`: Database session and connection management.

- `logs/`: Contains runtime log files for monitoring and debugging.

- `migrations/`: Database migration scripts and configurations.

- `tests/`: Unit and integration test cases for the application.

#### **Core Files:**

- `.env`: Stores environment variables.

- `.gitignore`: Specifies files to ignore in Git.

- `.dockerignore`: Optimizes the Docker build process by excluding unnecessary files.

- `entrypoint.sh`: Docker container initialization script.

- `alembic.ini`: Alembic configuration file.

- `README.md`: Project overview and documentation.

- `requirements.txt`: Python dependencies.
