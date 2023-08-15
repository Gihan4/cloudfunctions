import os
from google.cloud import secretmanager
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello there!')

def main(request):
    # Retrieve bot token from Secret Manager
    secret_client = secretmanager.SecretManagerServiceClient()
    secret_name = "projects/735741679605/secrets/bot_token/versions/1"
    secret_response = secret_client.access_secret_version(name=secret_name)
    bot_token = secret_response.payload.data.decode("UTF-8")

    updater = Updater(token=bot_token, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("hello", hello))

    update = Update.de_json(request.get_json(), updater.bot)
    dp.process_update(update)

    return "ok"

    // curl -F "url=https://us-central1-formidable-hold-392607.cloudfunctions.net/function-bot" "https://api.telegram.org/bot6410413468:AAG5s61kQFz-y0efwhh256MaOVGZrUUFCmY/setWebhook"

