import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# write bot functions
def start(update: Update, callback:CallbackContext):
    user = update.effective_user
    update.message.reply_text("this is a numberguess bot. guess the number from 1 to 1000!")

def play(update:Update, callback:CallbackContext):
    num = update.message.from_user.id%1000 + 1
    if not update.message.text.isdigit():
        update.message.reply_text("please enter a number")
        return

    inputnum = int(update.message.text)
    if inputnum>num:
        update.message.reply_text("guess a lower number")
    if inputnum<num:
        update.message.reply_text("guess a higher number")
    if inputnum==num:
        update.message.reply_text("you won!")

def main():
    updater = Updater("Token")
    dispatcher = updater.dispatcher
    # add functions to dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, play))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
