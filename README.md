docker.py

# Docker Manager Script

This is a Python script designed to simplify the management of Docker containers. It automatically checks if Docker is installed, installs it if necessary, pulls a minimal Debian Docker image, and runs it in the terminal. The script also ensures cleanup of stopped containers and the Docker containers directory upon exit.

## Features

- Automatically installs Docker if not already installed.
- Pulls the minimal Debian Docker image (`debian:stable-slim`).
- Runs the Docker container interactively in the same terminal.
- Cleans up stopped containers and the Docker containers directory when exiting.

## Prerequisites

- Python 3.x
- `apt` package manager (for Debian-based systems)
- `sudo` privileges

## Usage

1. Clone the repository or download the `docker.py` script.
2. Make the script executable:

   ```bash
   chmod +x docker.py

run:

sudo python3 docker.py

Happy Docking!
