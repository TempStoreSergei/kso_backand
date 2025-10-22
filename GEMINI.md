# Project Overview

This project is a modular FastAPI application designed to serve as a backend for a kiosk system. It follows a microservices-like architecture, with different functionalities encapsulated in separate modules. The application uses a variety of technologies, including:

*   **FastAPI:** A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
*   **SQLAlchemy:** A SQL toolkit and Object-Relational Mapper (ORM) for Python.
*   **PostgreSQL:** A powerful, open-source object-relational database system.
*   **Redis:** An in-memory data structure store, used as a database, cache, and message broker.
*   **Minio:** A high-performance, distributed object storage system.
*   **Docker Compose:** A tool for defining and running multi-container Docker applications.
*   **Loki, Promtail, Grafana:** A stack for collecting, storing, and visualizing logs.

The application is structured into a core `api` directory and a `modules` directory. The `api` directory contains the main application logic, including authentication, configuration, and the router factory. The `modules` directory contains the different modules of the application, such as the cash system, scanner, and hotel modules. Each module has its own routers, endpoints, and DTOs.

## Building and Running

The project is containerized using Docker Compose. To build and run the application, you will need to have Docker and Docker Compose installed.

1.  **Start the services:**

    ```bash
    docker-compose up -d
    ```

2.  **Run the API:**

    The API can be run directly using `uvicorn`:

    ```bash
    uvicorn api.main:app --host 0.0.0.0 --port 8005 --reload
    ```

    Alternatively, you can run the `run_api.py` script:

    ```bash
    python run_api.py
    ```

## Development Conventions

*   **Modular Architecture:** The project is divided into modules, each with its own set of routes, endpoints, and DTOs. When adding new functionality, it should be encapsulated in a new module.
*   **Router Factory:** A `RouterFactory` is used to dynamically load routes from the different modules. This makes it easy to add or remove modules without having to modify the main application file.
*   **DTOs:** Data Transfer Objects (DTOs) are used to define the structure of the data that is sent and received by the API. This helps to ensure that the data is consistent and that it can be easily validated.
*   **Dependency Injection:** FastAPI's dependency injection system is used to manage dependencies, such as database connections and authentication.
*   **Configuration:** The application is configured using environment variables and Pydantic settings.
*   **Logging:** The application uses the `loguru` library for logging, and the logs are collected and stored using Loki, Promtail, and Grafana.
