a = int ((input ('Сколько сейчас время? : ')))
while a >= 0 and a <= 24:
	if a >= 0 and a < 6 :
		print ("уже ночь! быстро туши компуктер и ложись спать!")
	elif a >= 6 and a < 12 :
		print ('уже утро! собирайся на пары хулиган!')
	elif a >= 12 and a < 18 :
		print ('уже день! ты почему не на парах, бунтарь?!')
	elif a >= 18 and a < 0 :
		print ('уже вечер! учи уроки, а то мамке расскажу!')
else :
	print('такого времени суток не существует')