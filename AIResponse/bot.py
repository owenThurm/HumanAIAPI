from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer
import nltk
import sys
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

Hugo = ChatBot(name="Hugo",
                      read_only = False,
                      logic_adapters = ["chatterbot.logic.BestMatch"],
                      storage_adapter = "chatterbot.storage.SQLStorageAdapter")

message = sys.argv[1]
print(Hugo.get_response('message'));
