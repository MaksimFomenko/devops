# Pet and Owner Manager

Small Spring Boot REST application for managing owners and their pets.

## Run with Docker Compose

Run this from the project directory **inside the VM**:

```bash
docker compose up --build
```

The app and PostgreSQL both run inside the VM. To open the app in a browser on the VM, visit [http://localhost:8080](http://localhost:8080). To open it from the host computer, use `http://<VM-IP>:8080` (get the VM address with `hostname -I` on Linux). The VM network must allow access to port 8080. With VirtualBox NAT, add a port forwarding rule from host port `8080` to guest port `8080`, then use `http://localhost:8080` on the host. The browser interface lets you create, edit, list, and delete owners and pets. The API is also available at `/api/users` and `/api/pets`.

Compose starts the Spring Boot app and PostgreSQL in separate containers. PostgreSQL data is stored in the `postgres_data` named volume.

Stop the containers with `Ctrl+C`, or run `docker compose down` in another terminal. To also delete the database volume and its data, run `docker compose down -v`.

## Run the app without Docker

You need Java 17+, Maven, and a PostgreSQL server. Create a database named `pet_base`, then set `SPRING_DATASOURCE_URL`, `SPRING_DATASOURCE_USERNAME`, and `SPRING_DATASOURCE_PASSWORD` if your local PostgreSQL credentials differ from the defaults (`postgres` / `postgres`). Start the application with:

```bash
mvn spring-boot:run
```

The browser interface is served by Spring Boot at `http://localhost:8080`.

## Build the app image only

```bash
docker build -t pet-owner-manager .
```

The app needs PostgreSQL, so use Compose to run the complete setup.
