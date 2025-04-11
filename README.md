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

   - [ ] Implement SQLAlchemy models
   - [ ] Configure relationships between entities
   - [ ] Create Pydantic schemas for validation

4. **Basic API:**

   - [ ] Implement CRUD endpoints for vehicles
   - [ ] Configure FastAPI routers organized by domain
   - [ ] Document API with Swagger/OpenAPI

5. **Authentication and Authorization:**

   - [ ] Implement user registration and login
   - [ ] Configure JWT system with refresh tokens
   - [ ] Define access levels (buyers, sellers, admin)

6. **Business Features:**

   - [ ] Implement search system and filters for vehicles
   - [ ] Create endpoints for listing management
   - [ ] Develop favorites system and viewing history

7. **Asynchronous Processing:**

   - [ ] Configure background tasks with Celery or FastAPI background tasks
   - [ ] Implement notifications and alerts (RabbitMQ)
   - [ ] Develop periodic report generation

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

    - [ ] Dockerize the application
    - [ ] Configure Docker Compose for development
      - [ ] Configure the database
      - [ ] Configure the application
    - [ ] Prepare for deployment in production environments

## Structure of Project:

This repository follows a modular and scalable architecture to ensure ease of development and maintainability. Below is an overview of the purpose of each folder and file:

```
WheelsAPI/
├── .venv
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── items.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── logging.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── sales.py
│   │   ├── users.py
│   │   └── vehicles.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── item.py
│   ├── crud/
│   │   ├── __init__.py
│   │   └── item.py
│   └── db/
│       ├── __init__.py
│       └── session.py
├── tests/
│       ├── __init__.py
│       └── test.py
├── .env
├── .gitignore
├── .python-version
├── docker-compose.yaml
├── Dockerfile
├── README.md
└── requirements.txt
```

### Folders

- **`.venv/`**  
  Contains the virtual environment for the project, including all installed dependencies.

- **`app/`**  
  The core of the application, containing all the business logic, API routes, database models, schemas, and more. It is structured into subdirectories for clarity:

  - **`api/`**: Handles API routing and controller logic.
  - **`core/`**: Includes configuration and core application setup.
  - **`models/`**: Defines the database models.
  - **`schemas/`**: Contains Pydantic schemas for request validation and response formatting.
  - **`crud/`**: Implements Create, Read, Update, and Delete (CRUD) operations for the models.
  - **`db/`**: Manages the database connection and session handling.

- **`tests/`**  
  Contains unit and integration tests for the application to ensure functionality and reliability.

### Files

- **`.env`**  
  Stores environment variables for the application, such as database connection strings and secret keys.

- **`.gitignore`**  
  Specifies files and directories that should be ignored by Git to prevent sensitive or unnecessary files from being tracked.

- **`.python-version`**  
  Defines for the Pyenv version used in the project to maintain consistency across environments.

- **`docker-compose.yaml`**  
  Used to define and manage multi-container Docker applications, including the API and any associated services like databases.

- **`Dockerfile`**  
  Contains the instructions for building the Docker image for the application.

- **`README.md`**  
  Provides an overview of the project, including its purpose, usage, and structure (this file).

- **`requirements.txt`**  
  Lists all Python dependencies required by the project.
