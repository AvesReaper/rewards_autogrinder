from pynput.keyboard import Key, Controller
import time
import os
from PC.utility import initialize_edge,terminate_edge


os_name = os.name

initialize_edge(os_name)

keyboard = Controller()
 
search_strings = [
    "how to design a user-friendly website",
    "best practices for remote work in 2024",
    "how to learn blockchain technology",
    "top 10 road trip destinations in 2024",
    "how to increase social media engagement",
    "best ways to save for retirement",
    "how to start a freelancing career",
    "most popular programming languages in 2024",
    "how to improve your leadership skills",
    "top 10 productivity tips for entrepreneurs",
    "how to start a healthy eating plan",
    "best strategies for risk management",
    "how to build passive income streams",
    "most famous castles in the world",
    "how to boost your immune system naturally",
    "top 10 online business ideas for 2024",
    "how to build a personal finance budget",
    "best ways to learn JavaScript in 2024",
    "how to improve your digital marketing skills",
    "most popular cloud storage services in 2024",
    "how to create a successful product launch",
    "best tools for project management in 2024",
    "how to reduce screen time and improve focus",
    "top 10 must-visit national parks in 2024",
    "how to develop a strong personal brand",
    "best ways to stay motivated while working from home",
    "how to create engaging video content",
    "most popular tourist destinations in South America",
    "how to improve your coding workflow",
    "best practices for customer relationship management"
]


time.sleep(1)

for i in search_strings:
	with keyboard.pressed(Key.ctrl):
		keyboard.press('t')
		keyboard.release('t')
	time.sleep(2)
	keyboard.type(i)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	time.sleep(5)
	with keyboard.pressed(Key.ctrl):
		keyboard.press('w')
		keyboard.release('w')
	time.sleep(1)

terminate_edge(os_name)
