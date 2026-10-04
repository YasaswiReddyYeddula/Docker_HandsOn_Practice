# Pullthe official MYSQL image from the Docker Hub 
FROM mysql:8.0

# Set the environment variables for MYSQL root password, database name
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=mydb

# Copy the initialization SQL script into the container
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the default MYSQL port
EXPOSE 3307