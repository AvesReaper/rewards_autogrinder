from pynput.keyboard import Key, Controller
import time
import os
from utility import initialize_edge,terminate_edge


os_name = os.name

initialize_edge(os_name)

keyboard = Controller()
 
search_strings = [
    "Top rated hiking trails",
    "History of ancient civilizations",
    "Best workout routines"
    # "Advances in artificial organs",
    # "Tips for improving concentration",
    # "Popular online multiplayer games",
    # "How to build a smart home",
    # "Top investment strategies",
    # "Best smartphone apps 2024",
    # "Impact of virtual meetings",
    # "Autonomous vehicles technology",
    # "Mental health awareness campaigns",
    # "How to start a podcast",
    # "Tips for public speaking",
    # "3D printing innovations",
    # "Best coffee brewing techniques",
    # "Robotics in manufacturing",
    # "History of space missions",
    # "How to improve memory retention",
    # "The future of wearable technology",
    # "How to reduce carbon footprint",
    # "Latest virtual reality headsets",
    # "Top digital marketing tools",
    # "Cryptocurrency market analysis",
    # "Organic gardening techniques",
    # "How to start a YouTube channel",
    # "Mindfulness exercises for stress",
    # "Popular e-commerce platforms",
    # "History of world wars",
    # "Best machine learning tutorials"
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
