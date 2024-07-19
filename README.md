# CBR Bot Task

This guide will help you to set up and run the project on your local machine.

## Prerequisites

- Python 3.8 or higher
- Redis server

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/shalmeo/sbr-bot-task.git
    ```
2. Navigate to the project directory:
    ```
    cd project
    ```
3. Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```

## Configuration

Before running the application, ensure that your Redis server is running and accessible. Export environment variables for the Redis URI and the Telegram Bot token:

```
export REDIS_URI=redis://localhost
export BOT_TOKEN=<your_bot_token>
```
    
## Running the Application

To run the application, use the following command:

```
python -m cbr.bot
python -m cbr.worker
```