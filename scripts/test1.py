from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
#bot1 = ListTrainer(bot)
#bot1.train()
#bot.set_trainer(ListTrainer)


trainer = ListTrainer(bot)


for files in os.listdir('C:/Users/nkandasamy\Documents\Fun\chatterbot-corpus-master\chatterbot_corpus\data\english'):
	data = open('C:/Users/nkandasamy\Documents\Fun\chatterbot-corpus-master\chatterbot_corpus\data\english/' + files , 'r').readlines()
	trainer.train(data)

while True:
	msg = input('You :')
	if msg.strip() != 'Bye':
		reply = bot.get_response(msg)
		print('ChatBot :',reply)
	if msg.strip() == 'Bye':
		print('ChatBot : Bye')
		break
