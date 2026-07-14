# Installation Guide

This guide explains how to install and configure the **Recommendation Pipeline** project on a new machine.

---

# Prerequisites

Ensure the following software is installed:

- Python 3.12+
- Git
- Docker Desktop
- (Optional) pgAdmin or DBeaver for viewing the PostgreSQL database

---

# 1. Clone the Repository

Clone the repository.

```bash
git clone <repository-url>
```

Navigate to the project directory.

```bash
cd RecommendationPipeline
```

---

# 2. Create a Virtual Environment

Create a Python virtual environment.

```bash
python -m venv .venv
```

---

# 3. Activate the Virtual Environment

### Windows Command Prompt (CMD)

```cmd
.venv\Scripts\activate
```

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation your terminal should look similar to:

```text
(.venv) D:\RecommendationPipeline>
```

---

# 4. Install Python Dependencies

Install all required packages.

```bash
pip install -r requirements.txt
```

---

# 5. Configure Environment Variables

Copy the example environment file.

```text
.env.example
```

Rename (or copy) it as:

```text
.env
```

Update the PostgreSQL configuration according to your environment.

Example:

```ini
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=recommendation_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

LOG_LEVEL=INFO
```

---

# 6. Start PostgreSQL using Docker

The project includes a Docker Compose configuration for PostgreSQL.

Ensure Docker Desktop is running.

Navigate to the project root.

```bash
cd RecommendationPipeline
```

Start PostgreSQL.

```bash
docker compose up -d
```

Docker will automatically:

- Pull the PostgreSQL 16 image (first run only)
- Create the PostgreSQL container
- Create the database
- Create a persistent Docker volume

The database container will be created as:

```text
recommendation_postgres
```

---

# 7. Verify the Container

Check that PostgreSQL is running.

```bash
docker ps
```

You should see a container similar to:

```text
recommendation_postgres
```

with status:

```text
Up
```

---

# 8. Verify Database Connectivity (Optional)

Open a PostgreSQL client such as pgAdmin or DBeaver.

Use the following connection details:

| Property | Value |
|----------|-------|
| Host | localhost |
| Port | 5432 |
| Database | recommendation_db |
| Username | postgres |
| Password | postgres |

If the connection succeeds, PostgreSQL has been configured correctly.

---

# Installation Complete

The project has now been installed successfully.

Continue with the **Execution Guide** to:

- Start the Prefect Server
- Start the MLflow UI
- Execute the Recommendation Pipeline