from telegram.ext import Updater, CommandHandler


def main():
    # Instanciamos updater
    updater = Updater(token="1201526847:AAGJ4Nh5kxxqGBgFuTDnCf-nwOZa2LZMB1k", use_context=True)

    # Añadiedno un manejador al comando /start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # Manejador para el comando /repite
    updater.dispatcher.add_handler(CommandHandler("repite", repite))

    # Manejador para el comando /suma
    updater.dispatcher.add_handler(CommandHandler("suma", suma))

    # Empezamos a pedir notificaciones a Telegram
    updater.start_polling()

    # Capturamos señales de parada
    updater.idle()

def start(update, context):
    update.message.reply_text("Hola, soy un bot")
    
def repite(update, context):
    update.message.reply_text(update.message.text)

def suma(update, context):
    resultado = int(context.args[0]) + int(context.args [1])
    update.message.reply_text("El resultado es " + str(resultado)) # Lo pasamos a string para que así pueda sacer el número en el mensaje.


main()