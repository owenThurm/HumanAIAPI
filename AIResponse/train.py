from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

#initializes the trainer bot
trainer_bot = ChatBot(name="trainer")

#Make a new trainer to train the trainer bot
trainer = ChatterBotCorpusTrainer(trainer_bot)

#Trains the chatbot on the english corpus
trainer.train("chatterbot.corpus.english")