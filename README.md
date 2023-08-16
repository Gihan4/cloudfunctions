# cloudfunctions

- User sends a message to the bot in a chat.
- Telegram's servers send a webhook POST request to your server.
- Your server processes the incoming request using the webhook function.
- The webhook function extracts the chat ID from the update.
- The bot instance sends a message back to the same chat with the content "hey there!".
- The webhook function returns "OK" to acknowledge the successful processing of the request.
