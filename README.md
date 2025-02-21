# Telegram Google Bot

This is a simple Telegram bot that responds to messages starting with the word "google" by providing a Let Me Google That For You (LMGTFY) link.

## Features
- Listens for messages that start with "google" (case-insensitive)
- Generates an LMGTFY link based on the user's query
- Uses `python-telegram-bot` v21
- Docker support for easy deployment
- Environment variable support for bot token

## Installation & Usage

### Prerequisites
- Python 3.9+
- A Telegram bot token from [BotFather](https://t.me/botfather)
- Docker (optional for containerized deployment)

### Running Locally
1. Clone the repository:
   ```sh
   git clone https://github.com/ApsiV11/LetMeGoogleThatForYouBot.git
   cd telegram-google-bot
   ```
2. Install dependencies:
   ```sh
   pip install python-telegram-bot
   ```
3. Set the environment variable:
   ```sh
   export TELEGRAM_BOT_TOKEN=your-bot-token
   ```
4. Run the bot:
   ```sh
   python bot.py
   ```

### Running with Docker
1. Build the Docker image:
   ```sh
   docker build -t telegram-google-bot .
   ```
2. Run the bot:
   ```sh
   docker run -e TELEGRAM_BOT_TOKEN=your-bot-token telegram-google-bot
   ```

### Running with Docker Compose
1. Create a `.env` file and add:
   ```sh
   TELEGRAM_BOT_TOKEN=your-bot-token
   ```
2. Run the bot:
   ```sh
   docker-compose up -d
   ```

## Usage
- Send a message like:
  ```
  google how to deploy a telegram bot
  ```
- The bot will reply with:
  ```
  Here you go: https://letmegooglethat.com/?q=how+to+deploy+a+telegram+bot
  ```

## License
This project is open-source and available under the MIT License.

