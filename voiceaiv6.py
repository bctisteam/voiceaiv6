# voiceai version 5 consists of conversational ai with all command prompts
# key libraries are below

import os
import time
import playsound
import sounddevice #somehow hides alsa and jack errors
import speech_recognition as sr
from gtts import gTTS
import numpy
import pygame
import pygame_gui
from pygame.locals import *

#pygame gui initialization

pygame.init()
white = 255,255,255
screen_size= 880,600
pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode(screen_size,RESIZABLE)

background = pygame.Surface((800, 600))
background.fill(white)

manager = pygame_gui.UIManager((800, 600))

clock = pygame.time.Clock()




def get_audio(): #getting user input
        said = ""
        try:
            r = sr.Recognizer()
            print("Microphone Active.") #indicate mic active

            with sr.Microphone() as source:

                # timeout is the number of seconds it will wait for you to say something before it stops listening
                # phrase_time_limit is the maximum number of seconds that a phrase can be
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                said = r.recognize_google(audio)
        except sr.WaitTimeoutError:
            print("You did not say anything or I could not hear you.")
        except Exception as e:
            print(e)
        finally:
            # This block of code will run no matter what,
            # wether an exception is thrown or not.
            print(f"Speech recorded: '{said}' ")
        # return the text that was heard in lowercase
        # as there might be rare occasions where the text is not in lowercase
        # such as "3D printing" instead of "3d printing"
        return said.lower()


def speak(text): #saving user input in wav audio file
    tts = gTTS(text=text, lang="en")
    filename = "voice.wav"
    tts.save(filename)
    playsound.playsound(filename)


is_running = True

while is_running:
    user_text = get_audio()

    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0,0))
    manager.draw_ui(window_surface)
    
    user_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 275), (400, 500)),text=user_text, manager=manager)

    

    #command prompts
    #user input must be written in full lower case

    #GREETINGS
    if "" in user_text:
        robot_response='can you repeat that?'

    if "hello" in user_text:
        robot_response="Hello there human. How may I help you?"

    if ("introduce yourself" in user_text) or ("who are you" in user_text) or ("what are you" in user_text):
        robot_response="Hello, my name is Chatbot. I am an AI robot created by STEAM members in 2024. You can ask me questions about the BCTI. "
    

    if ("bye" in user_text) or ("they are leaving" in user_text):
        robot_response="Good-bye human. It was nice talking to you"

    
    #IMPORTANT LOCATIONS WITH DESCRIPTIONS 
        def location_description(text):
            locations = {
                "steam lab" or "stem": "The steam Lab islocated on the second floor at CTI 215. There are other projects there like PuzzleBot, DrawBot, BuzzMe, and the MPS station",
                "3d printing" or "additive" or "javelin": "the javelin additive manufacturing lab is located on the second floor at cti 216. you can see that there are 3d printed models, 3d printers, and a laser cutting machine.",
                "c p factory" or "festo":"the cp factory is located on the first floor at cti 117. there, automated guided vehicles are occasionally driving across the room to aid .",
                "magna" or "skills" or "mechatronics":"the magna mechatronics skills training room is located on the second floor at cti 210. here students are able to learn to program and build small scale versions of industrial factories.",
                "atrium" or "demonstration" or "event": "the Main Atrium is located on the first floor at CTI 107 and the demonstration room is located CTI 108. Many event are held in these areas.",
                "prototyping": "The Product Prototyping Facility is located in the machine shop at CTI 110. This facility contains specialized and traditional machining equipment that will enable users to bring ideas and concepts to life by transforming digital files into tangible models, prototypes and proof-of-concepts.",
                "gaming": "The Gaming zone is located on the second floor at CTI 209. here the humber esports team train",
                "indigenous": "The Indigenous Cultural Marker is located on the second floor. This sculpture is a representation of our entire life and the central piece that links this life is symbolic of the spirit.",
                "kuka" or "automation": "The Kuka Advanced Automation Lab is located in the fourth floor at CTI 409. This lab is equipped with robotics technology dedicated to the collaboration of industry, faculty members and students on robotics systems integration applications.",
                "s e w" or "eurodrive": "The S E W-Eurodrive Innovation Lab is located in the second floor at CTI 221 where it demonstrates how humans, technology, and machines collaborate on the production line. The laboratory focuses on Automated Guided Vehicles for assembly, production and distribution logistics.",
                "capstone" or "projects":"the capstone projects room is located on the fourth floor at CTI 215 and CTI 216. these rooms are for students to complete their industrial capstone projects.",
                "sick": "The SICK sensor lab is located on the third floor at CTI 316 A. this lab is used to deliver training on SICK Vison Sensor Technologies. ",
                "cisco" or "digital": "The Cisco Digital Transformation Zone is located on the fourth floor at CTI 410. The data centre provides critical services to support a wide range of projects and innovation activities in the capacity of Internet of Things (IoT), and digital transformation. It allows for end-user project connectivity for capstone projects, applied research, and industry activities.",

            }

            for keyword, description in locations.items():
                if keyword in text:
                    return description
            
            return " I'm sorry, I cannot find information to your question."
        
















    # if "steam lab" in user_text: 
    #          robot_response="The STEAM Lab is located on the second floor at CTI 215. There are other projects there like PuzzleBot, DrawBot, BuzzMe, and the MPS station"

    # if ("3d printing" in user_text) or ("additive" in user_text) or ("javelin" in user_text): 
    #          robot_response="the javelin additive manufacturing lab is located on the second floor at cti 216. you can see that there are 3d printed models, 3d printers, and a laser cutting machine."

    # if ("c p factory" in user_text) or ("festo" in user_text): 
    #          robot_response="the cp factory is located on the first floor at cti 117. there, automated guided vehicles are occasionally driving across the room to aid ."

    # if ("magna" in user_text) or ("skills" in user_text) or ("mechatronics" in user_text): 
    #          robot_response="the magna mechatronics skills training room is located on the second floor at cti 210. here students are able to learn to program and build small scale versions of industrial factories."

    # if ("atrium" in user_text) or ("demonstration" in user_text) or ("event" in user_text): 
    #          robot_response="the Main Atrium is located on the first floor at CTI 107 and the demonstration room is located CTI 108. Many event are held in these areas."

    # if "prototyping" in user_text: 
    #          robot_response="The Product Prototyping Facility is located in the machine shop at CTI 110. This facility contains specialized and traditional machining equipment that will enable users to bring ideas and concepts to life by transforming digital files into tangible models, prototypes and proof-of-concepts."

    # if "gaming" in user_text: 
    #          robot_response="The Gaming zone is located on the second floor at CTI 209. here the humber esports team train" 

    # if "indigenous" in user_text: 
    #          robot_response="The Indigenous Cultural Marker is located on the second floor. This sculpture is a representation of our entire life and the central piece that links this life is symbolic of the spirit."

    # if ("kuka" in user_text) or ("automation" in user_text): 
    #          robot_response="The Kuka Advanced Automation Lab is located in the fourth floor at CTI 409. This lab is equipped with robotics technology dedicated to the collaboration of industry, faculty members and students on robotics systems integration applications."

    # if ("S E W" in user_text) or ("eurodrive" in user_text): 
    #          robot_response="The S E W-Eurodrive Innovation Lab is located in the second floor at CTI 221 where it demonstrates how humans, technology, and machines collaborate on the production line. The laboratory focuses on Automated Guided Vehicles for assembly, production and distribution logistics. " 

    # if ("capstone" in user_text) or ("projects" in user_text): 
    #          robot_response="the capstone projects room is located on the fourth floor at CTI 215 and CTI 216. these rooms are for students to complete their industrial capstone projects."

    # if "sick" in user_text: 
    #          robot_response="the Sick sensor lab is located on the third floor at CTI 316 A. this lab is used to deliver training on SICK Vison Sensor Technologies. "

    # if ("cisco" in user_text) or ("digital" in user_text): 
    #          robot_response="The Cisco Digital Transformation Zone is located on the fourth floor at CTI 410. The data centre provides critical services to support a wide range of projects and innovation activities in the capacity of Internet of Things (IoT), and digital transformation. It allows for end-user project connectivity for capstone projects, applied research, and industry activities."
    #JOKES 
    if "tell me a joke" in user_text:
        jokes = [
                    "Why was Cinderella so bad at soccer? She kept running away from the ball!",
                    "What do you call a well-balanced horse? Stable.",
                    "Why did the bicycle fall over? Because it was two-tired!",
                    "What did the triangle say to the circle? You are pointless.",
                    "Why are balloons so expensive? Inflation!",
                    "What did the ocean say to the beach? Nothing, it just waved.",
                    "Why did the programmer quit their job? Because they didn't get arrays",
                    "Why do programmers prefer dark mode? Because light attracts bugs.",
                    "How does the moon cut its hair? Eclipse it.",
                    "Why can't you trust an atom? Because they make everything up.",
                    "What did one wall say to the other? I'll meet you at the corner.",
                    "What do you call a poor Santa Claus? Saint Nickel-less",
                    "What is the most used language in programming? Profanity.",
                    "Why did the robot go to the shoe shop? To get re-booted.",
                    "Binary: It's as easy as 01, 10, 11",

                #Add more jokes here (don't forget the comma at the end of each joke! )
        ]
        joke_choice = numpy.random.randint(0, len(jokes))
        robot_response=jokes[joke_choice] 

#FUN FACTS
    if ("fact" in user_text) or ("tell me a fact" in user_text) or ("fun fact" in user_text):

        facts =  [
            "A single ant can carry fifty time its own body weight.",
            "The Earth's core is as hot as the surface of the Sun.",
            "Dolphins sleep with one eye open.",
            "The shortest war in history lasted only 38 minutes.",
            "The human brain takes in 11 million bits of information every second but is aware only of 40.",
             #Add more fun facts here (don't forget the comma at the end of each fun fact! )
        ]

        fact_choice = numpy.random.randint(0, len(facts))
        robot_response=facts[fact_choice]

    robot_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 275), (600, 500)),text=robot_response, manager=manager)
    speak(robot_response)
    pygame.display.update()

#PUT ALL CODE ABOVE THIS LINE
pygame.quit()
