# Dockerfile
FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && \
    apt-get install -y fortune cowsay netcat-openbsd && \
    apt-get clean && \
    ln -s /usr/games/fortune /usr/bin/fortune && \
    ln -s /usr/games/cowsay /usr/bin/cowsay

# Set working directory
WORKDIR /app

# Copy the wisecow script into the container
COPY wisecow.sh .

# Make it executable
RUN chmod +x wisecow.sh

# Expose port 4499
EXPOSE 4499

# Start the application
CMD ["./wisecow.sh"]




