import os
import subprocess
import shutil

# Define the Docker image and paths
docker_image = "debian:stable-slim"
download_dir = "/tmp"
docker_containers_dir = "/var/lib/docker/containers"

def check_docker_installed():
    """Check if Docker is installed; if not, install it."""
    if shutil.which("docker") is None:
        print("Docker is not installed. Installing Docker...")
        subprocess.run(["sudo", "apt", "install", "-y", "docker.io"], check=True)
        print("Docker has been installed successfully.")

def start_docker_service():
    """Start the Docker service if it's not running."""
    print("Checking if Docker service is running...")
    try:
        # Check if the Docker service is active
        subprocess.run(["sudo", "systemctl", "start", "docker"], check=True)
        subprocess.run(["sudo", "systemctl", "enable", "docker"], check=True)
        print("Docker service started successfully.")
    except subprocess.CalledProcessError:
        print("Failed to start Docker service. Please check your Docker installation.")
        exit(1)

def pull_docker_image(image):
    """Pull the Docker image."""
    print(f"Pulling Docker image: {image}")
    subprocess.run(["docker", "pull", image], check=True)

def run_docker_container(image):
    """Run the Docker container in the current terminal with cleanup on exit."""
    print(f"Running Docker image: {image}")

    # Create a shell command that traps the EXIT signal to ensure cleanup
    shell_command = f"""
    trap 'echo Cleaning up...; docker container prune -f; sudo rm -rf {docker_containers_dir}/*' EXIT;
    docker run -it --rm {image}
    """
    
    # Run the command in the same terminal
    subprocess.run(["bash", "-c", shell_command], check=True)

if __name__ == "__main__":
    # Check if Docker is installed and install if necessary
    check_docker_installed()

    # Start the Docker service
    start_docker_service()

    # Pull the minimal Debian Docker image
    pull_docker_image(docker_image)

    # Run the Docker container interactively in the current terminal
    run_docker_container(docker_image)
