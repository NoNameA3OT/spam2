import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor



vk_session = vk_api.VkApi(token='0b930d0d0f5cc6af91656103d0d4f6f2eb33a74f2fe3423923a0448ef1bc10ac8f8a278b90a2bf2a79da8') #токен вашей группы
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session,193799294) #цифровой id вашей группы
def main():

	keyboard1 = VkKeyboard(one_time=False) # False - клавиатура после нажатия не будет закрываться. True - будет.

	keyboard1.add_button('Бан', color=VkKeyboardColor.POSITIVE)	
	
	while True: 
		try: 
			for event in longpoll.listen():

				if event.type == VkBotEventType.MESSAGE_NEW:
					print("успешно")
					while True:
						vk.messages.send(peer_id=event.object.peer_id, message="Тест",keyboard=keyboard1.get_keyboard(), random_id=1)	
					
			
		except Exception as e:
			print('') 

if __name__ == '__main__':
	main()
