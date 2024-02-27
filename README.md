# Welcome to Dockerized Service Function Chaining

## Getting Started
1. Clone the repository:
    ```bash
    git clone https://github.com/gara2000/opensource.git
    cd opensource/dockerized_ml
    ```

2. Build the Docker images:
    ```bash
    chmod +x build.sh # Run this once
    ./build.sh
    ```

3. Start the containers:
    ```bash
    chmod +x run.sh # Run this once
    ./run.sh
    ```

4. Access the user interface:

    Visit http://172.0.0.2:2400 to access the user interface, in which the user can upload the data
    The data uploaded by the user will be posted to the processing api

5. Stop the containers:
    ```bash
    chmod +x stop.sh # Run this once
    ./stop.sh
    ```

6. Cleaning Up:
    ```bash
    chmod +x clean.sh # Run this once
    ./clean.sh
    ```
