# 🐳 Docker Hands-on Practice

A hands-on Docker learning repository containing practical exercises and small projects covering **Docker images, containers, Dockerfiles, port mapping, networking, volumes, and Docker Compose**.

This repository documents my practical learning and experimentation with Docker, including containerizing a Flask application, connecting Flask and MySQL containers through a Docker network, and managing a multi-container application using Docker Compose.

---

## 📌 About

I created this repository while learning Docker and practicing the core concepts through hands-on projects.

Instead of only learning Docker commands theoretically, I practiced how Docker components work together:

```text
Dockerfile
    ↓
Docker Image
    ↓
Docker Container
    ↓
Networking
    ↓
Multiple Containers
    ↓
Docker Compose
    ↓
Persistent Storage
```

The projects in this repository gradually build from a simple containerized application to a multi-container Flask + MySQL application.

---

## 🎯 Learning Objectives

Through these exercises, I practiced:

* Understanding Docker fundamentals
* Creating and managing Docker images
* Creating and managing containers
* Writing Dockerfiles
* Containerizing Python/Flask applications
* Installing Python dependencies inside containers
* Mapping container ports to host ports
* Understanding container networking
* Connecting multiple containers
* Connecting Flask with MySQL using Docker networking
* Understanding Docker volumes and persistent storage
* Using Docker Compose for multi-container applications
* Managing service dependencies
* Working with environment variables
* Inspecting containers, networks and volumes
* Viewing container logs and debugging applications

---

# 🧩 Docker Concepts Practiced

## 1. Docker Image

A Docker image is a packaged template used to create containers.

I practiced:

* Pulling images
* Building images from Dockerfiles
* Listing images
* Inspecting images
* Removing images
* Tagging images

Example:

```bash
docker build -t my-app .
docker images
docker image inspect my-app
```

---

## 2. Docker Container

A container is a running instance of a Docker image.

I practiced the basic container lifecycle:

```text
Create
  ↓
Run
  ↓
Inspect
  ↓
Stop
  ↓
Start
  ↓
Restart
  ↓
Remove
```

Common commands practiced:

```bash
docker run --name <container_name> <image>
docker ps
docker ps -a
docker stop <container>
docker start <container>
docker restart <container>
docker rm <container>
docker logs <container>
docker exec -it <container> bash
```

---

## 3. Dockerfile

I practiced creating Dockerfiles to package applications into Docker images.

Some of the Dockerfile instructions practiced include:

| Instruction | Purpose                                    |
| ----------- | ------------------------------------------ |
| `FROM`      | Selects the base image                     |
| `WORKDIR`   | Sets the working directory                 |
| `COPY`      | Copies files into the image                |
| `RUN`       | Executes commands while building the image |
| `EXPOSE`    | Documents the port used by the application |
| `CMD`       | Defines the default command to run         |

Typical workflow:

```text
Application Code
       ↓
   Dockerfile
       ↓
docker build
       ↓
   Docker Image
       ↓
docker run
       ↓
 Docker Container
```

---

## 4. Port Mapping

I practiced exposing applications running inside containers to the host machine.

Example:

```bash
docker run -p 5000:5000 <image>
```

The mapping is:

```text
Host Machine             Container
     │                       │
     │      Port 5000        │
     └──────────────────────>│
```

This allowed Flask applications running inside containers to be accessed through the host machine.

---

# 🌐 Docker Networking

One of the important concepts practiced in this repository is **communication between containers**.

In the networking project, a Flask container communicates with a MySQL container through a Docker network.

```text
                 Docker Network
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
   Flask Container          MySQL Container
       :5000                    :3306
          │                       │
          └────── Application ────┘
                 Communication
```

The Flask application can communicate with MySQL using the container/service name rather than treating `localhost` as the database host.

Commands practiced include:

```bash
docker network ls
docker network create <network>
docker network inspect <network>
```

### Key concept

Inside a container:

```text
localhost
```

refers to the **same container**, not another container.

Therefore, when two containers need to communicate, they can communicate through a Docker network using the appropriate container/service name.

---

# 💾 Docker Volumes

I also practiced the concept of persistent storage using Docker volumes.

Containers are temporary by nature, so database data should be stored outside the container's writable layer when persistence is required.

Basic volume commands practiced:

```bash
docker volume ls
docker volume create <volume-name>
docker volume inspect <volume-name>
docker volume rm <volume-name>
```

Conceptually:

```text
          MySQL Container
                │
                │ database data
                ▼
          Docker Volume
                │
                ▼
        Persistent Storage
```

The purpose of a volume is to allow data to persist independently of the lifecycle of a container.

---

# 🧱 Docker Compose

I practiced Docker Compose for managing multiple containers as a single application.

Instead of manually creating and connecting each container, Docker Compose allows application services to be defined in a YAML configuration file.

The Compose project contains:

```text
docker-compose.yml
        │
        ├── Flask Service
        │
        └── MySQL Service
```

Concepts practiced include:

* Defining multiple services
* Building services
* Using existing images
* Port mappings
* Environment variables
* Service dependencies
* Health checks
* Container networking
* Volumes
* Starting and stopping multiple services together

Common commands practiced:

```bash
docker compose up
docker compose up -d
docker compose down
docker compose ps
docker compose logs
```

---

# 📂 Project Structure

```text
Docker_Tutorial/
│
└── Projects/
    │
    ├── 1_First_App/
    │   ├── app.py
    │   └── dockerfile
    │
    ├── 2_Flask_App/
    │   ├── app.py
    │   ├── Dockerfile
    │   └── requirements.txt
    │
    ├── 3_Docker_App_Network/
    │   │
    │   ├── Flask/
    │   │   ├── app.py
    │   │   ├── Dockerfile
    │   │   └── requirements.txt
    │   │
    │   └── MySQL/
    │       ├── Dockerfile
    │       └── init.sql
    │
    ├── 4_Docker_Compose/
    │   ├── docker-compose.yml
    │   │
    │   ├── Flask/
    │   │   ├── app.py
    │   │   ├── Dockerfile
    │   │   └── requirements.txt
    │   │
    │   └── MySQL/
    │       ├── Dockerfile
    │       └── init.sql
    │
    └── 5_Volume/
        └── MySQL/
            ├── Dockerfile
            └── init.sql
```

---

# 🚀 Hands-on Projects

## 1️⃣ First Docker Application

**Folder:** `Projects/1_First_App/`

This was my first hands-on Docker application.

### Concepts practiced

* Creating a simple application
* Creating a Dockerfile
* Selecting a base image
* Setting the working directory
* Copying application files
* Building a Docker image
* Running a container

### Workflow

```text
app.py
  ↓
Dockerfile
  ↓
Docker Build
  ↓
Docker Image
  ↓
Docker Run
  ↓
Container
```

---

## 2️⃣ Flask Application

**Folder:** `Projects/2_Flask_App/`

This project extends the basic Docker application by containerizing a Flask application.

### Concepts practiced

* Flask application
* Python dependencies
* `requirements.txt`
* Dockerfile
* Installing dependencies inside the image
* Port mapping
* Running a web application inside a container

### Technologies

* Python
* Flask
* Docker

### Workflow

```text
Flask Application
       ↓
requirements.txt
       ↓
Dockerfile
       ↓
Docker Image
       ↓
Docker Container
       ↓
Flask Application
```

---

## 3️⃣ Flask + MySQL Docker Networking

**Folder:** `Projects/3_Docker_App_Network/`

This project demonstrates communication between two separate containers.

### Architecture

```text
                 Docker Network
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
   Flask Container          MySQL Container
          │                       │
          │                       │
          └──── Database ─────────┘
              Communication
```

### Flask

The Flask application runs inside its own container.

### MySQL

MySQL runs inside a separate container.

### Networking

The containers communicate through a Docker network.

### Concepts practiced

* Multiple containers
* Custom Docker network
* Container-to-container communication
* Flask and MySQL integration
* MySQL initialization
* Database connection from a container

This project helped me understand why container networking is important when applications are split into separate services.

---

## 4️⃣ Flask + MySQL with Docker Compose

**Folder:** `Projects/4_Docker_Compose/`

This project combines the concepts learned previously and manages the Flask and MySQL services using Docker Compose.

### Architecture

```text
                  Docker Compose
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
       Flask Service       MySQL Service
             │                   │
             └────── Network ────┘
```

### Concepts practiced

* Docker Compose
* Multiple services
* Flask service
* MySQL service
* Service-to-service communication
* Port mapping
* Environment variables
* Service dependencies
* Health checks
* Volumes
* Starting and stopping the complete application using Compose

### Main Compose commands

```bash
docker compose up
docker compose up -d
docker compose ps
docker compose logs
docker compose down
```

### Why Docker Compose?

Without Compose, multiple containers need to be created and configured separately.

With Compose:

```text
docker-compose.yml
        ↓
docker compose up
        ↓
Flask + MySQL
        ↓
Complete Application
```

This makes running a multi-container application easier and more reproducible.

---

## 5️⃣ Docker Volume Practice

**Folder:** `Projects/5_Volume/`

This project focuses on persistent storage for a MySQL container.

### Concepts practiced

* Docker volumes
* Database storage
* Container storage vs persistent storage
* Keeping database data independent of the container lifecycle

### Concept

```text
MySQL Container
      │
      ▼
Docker Volume
      │
      ▼
Persistent Database Data
```

---

# 🛠️ Docker Commands Practiced

## Images

```bash
docker images
docker pull <image>
docker build -t <image-name> .
docker image inspect <image>
docker rmi <image>
```

## Containers

```bash
docker run <image>
docker ps
docker ps -a
docker start <container>
docker stop <container>
docker restart <container>
docker rm <container>
docker logs <container>
docker exec -it <container> bash
```

## Port Mapping

```bash
docker run -p <host-port>:<container-port> <image>
```

## Networks

```bash
docker network ls
docker network create <network>
docker network inspect <network>
docker network rm <network>
```

## Volumes

```bash
docker volume ls
docker volume create <volume>
docker volume inspect <volume>
docker volume rm <volume>
```

## Docker Compose

```bash
docker compose up
docker compose up -d
docker compose ps
docker compose logs
docker compose down
```

---

# 🧠 Key Concepts I Practiced

### Image vs Container

```text
Docker Image
     │
     │ docker run
     ▼
Docker Container
```

An **image** is the packaged template, while a **container** is a running instance created from that image.

---

### Dockerfile → Image → Container

```text
Dockerfile
    │
    │ docker build
    ▼
Docker Image
    │
    │ docker run
    ▼
Docker Container
```

---

### Container Networking

```text
Container A
     │
     │ Docker Network
     │
Container B
```

Containers connected to the same Docker network can communicate with each other using the appropriate service/container name.

---

### Persistent Storage

```text
Container
    │
    ▼
Volume
    │
    ▼
Persistent Data
```

Volumes allow important data, such as database data, to persist beyond the lifecycle of an individual container.

---

### Multi-container Application

```text
                Application
                     │
          ┌──────────┴──────────┐
          │                     │
       Flask                  MySQL
      Container              Container
          │                     │
          └──── Docker Network ─┘
```

Docker Compose can be used to manage these services together.

---

# 🔧 Technologies Used

* **Docker**
* **Docker Compose**
* **Python**
* **Flask**
* **MySQL**
* **YAML**
* **SQL**

---

# 📚 Learning Resource

This repository was created as part of my hands-on Docker learning and practice based on:

**Ansh Lamba — Docker Tutorial for Beginners (Data Domain Edition)**

The tutorial helped me practice Docker fundamentals including images, containers, Dockerfiles, networking, volumes, Docker Compose and related concepts.

---

# 🎓 Learning Outcome

After completing these exercises, I gained hands-on experience with the fundamental Docker workflow:

```text
Write Application
       ↓
Create Dockerfile
       ↓
Build Image
       ↓
Run Container
       ↓
Map Ports
       ↓
Create Networks
       ↓
Connect Multiple Containers
       ↓
Use Volumes
       ↓
Manage Services with Docker Compose
```

I also gained practical understanding of how a simple application can be broken into multiple containerized services and connected using Docker networking.

---

# 🚧 Future Practice

I plan to extend this Docker knowledge by practicing Docker in more realistic data and application workflows, including:

* Dockerizing data engineering projects
* Dockerizing machine learning applications
* Dockerizing FastAPI/Flask APIs
* Using PostgreSQL with Docker
* Integrating Docker with Airflow
* Using Docker in data pipelines
* CI/CD with Docker
* Container deployment and cloud environments
* Exploring Kubernetes after strengthening Docker fundamentals

---

## ⭐ Repository Purpose

This repository is primarily a **hands-on learning and practice repository**. It documents the Docker concepts I practiced and the small applications I built while learning containerization and multi-container application development.
