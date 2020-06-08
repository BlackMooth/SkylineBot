from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters

import os
import glob

from antlr4 import *
from antlr4.InputStream import InputStream
from cl.test.SkylineLexer import SkylineLexer
from cl.test.SkylineParser import SkylineParser
from MyVisitor import MyVisitor

from Skyline import Skyline

import pickle


def start(update, context):
    username = update.effective_chat.username
    message = "SkyLineBot!\nBenvingut %s" % (username)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def author(update, context):
    message = "SkylineBot!\n@DanielDonate\ndaniel.donate@est.fib.upc.edu"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def help(update, context):
    message = "Aquestes són les *comandes* que pots fer servir\n \
    /start inicia la conversa\n \
    /author mostra el nom i el correu de l'autor del projecte\n \
    /lst : mostra els identificadors dels skylines definits i la seva area\n \
    /clean : esborra tots els identificadors definits\n \
    /save id : guarda un skyline definit amb el nom id.sky\n \
    /load id : carrega un skyline de l'arxiu id.sky"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode='Markdown')


def lst(update, context):
    # Aquesta comanda llista tots els skylines que s.han guardat AMB la comanda
    # /save (no apareixen els skylines que s.han creat "durant la sessio")
    username = update.effective_chat.username
    list = ""
    try:
        for filename in glob.glob("./%s*" % (username)):
            ID = filename[(len(username)+3):]
            value = pickle.load(open(filename, "rb"))
            list += "identificador: %s, area: %s\n" % (ID, value.area)
        context.bot.send_message(chat_id=update.effective_chat.id, text=list)
    except (OSError, IOError) as e:
        message = "Error llistant els identificadors"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def save(update, context):
    ID = update.message.text[6:]
    if ID in context.user_data:
        value = context.user_data[ID]
        fitxer = update.effective_chat.username + "_" + ID + ".sky"
        pickle.dump(value, open(fitxer, "wb"))
        message = "El teu skyline amb identificador *%s* s'ha guardat exitosament" % (ID)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode='Markdown')
    else:
        message = "No tens cap skyline identificat per *%s*" % (ID)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode='Markdown')


def load(update, context):
    ID = update.message.text[6:]
    fitxer = update.effective_chat.username + "_" + ID + ".sky"
    try:
        value = pickle.load(open(fitxer, "rb"))
        context.user_data[ID] = value
        message = "L'skyline identificat per *%s* s'ha carregat exitosament" % (ID)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode='Markdown')
    except (OSError, IOError) as e:
        message = "No tens cap skyline guardat amb l'identificador *%s*" % (ID)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode='Markdown')


def clean(update, context):
    # Aquesta comanda esborra els skylines que ha guardat l.usuari en algunt moment amb /save
    username = update.effective_chat.username
    try:
        for filename in glob.glob("./%s*" % (username)):
            os.remove(filename)
        message = "Els teus identificadors s'han esborrat exitosament"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    except (OSError, IOError) as e:
        message = "S'ha produit un error eliminant els identificadors guardats"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def skyline(update, context):
    msg = update.message.text
    input_stream = InputStream(msg)
    lexer = SkylineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    tree = parser.prog()

    visitor = MyVisitor(context)
    value = visitor.visit(tree)  # Aixo es l.skyline generat
    fitxer = value.print_skyline()
    try:
        context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=open(fitxer, 'rb'))
        area = value.area
        altura = value.altura
        context.bot.send_message(chat_id=update.effective_chat.id, text="area: %s\nalçada: %s" % (area, altura))
    except (OSError, IOError) as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error")

    try:
        os.remove(fitxer)
    except (OSError, IOError) as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error")


# declara una constant amb el access-token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('lst', lst))
dispatcher.add_handler(CommandHandler('save', save))
dispatcher.add_handler(CommandHandler('load', load))
dispatcher.add_handler(CommandHandler('clean', clean))

dispatcher.add_handler(MessageHandler(Filters.text, skyline))

# engegem el bot
updater.start_polling()
