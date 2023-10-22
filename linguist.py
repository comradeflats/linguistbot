import pyfiglet
import colorama
import time
import webbrowser
import os
import subprocess
import threading
import pygame
import random

# Variable to control the beep audio loop.
beep_audio_playing = True

# Function to loop a 1-second .mp3 audio file.
def loop_beep_audio():
    audio_path = os.path.expanduser("~/Desktop/beep.mp3")  # Provide the full path to the audio file
    try:
        while beep_audio_playing:  # Loop while the flag is True
            subprocess.Popen(["afplay", audio_path])
            time.sleep(1)
    except Exception as e:
        print("Error playing audio:", e)

# Function to play background music in a separate thread.
def play_background_music():
    pygame.mixer.init()
    background_music_path = os.path.expanduser("~/Desktop/back.mp3")  # Provide the path to your background music
    pygame.mixer.music.load(background_music_path)
    pygame.mixer.music.set_volume(0.8)  # Adjust the volume as needed (0.0 to 1.0)
    pygame.mixer.music.play(-1)

# Function to display a loading animation for 2 seconds.
def loading_animation():
    for _ in range(2):
        for i in range(4):
            chars = ["/", "-", "\\", "|"]
            print(f"{colorama.Fore.GREEN}Thinking... {chars[i]}{colorama.Fore.RESET}", end="\r")
            time.sleep(0.5)
    print(" " * 15)  # Clear loading message

# Function to display a loading bar with "Starting..." in yellow and the bar in green.
def display_loading_bar():
    loading_text = f"{colorama.Fore.YELLOW}Starting...{colorama.Fore.RESET}"
    total_time = 8  # 8 seconds
    num_steps = 40  # Number of steps (40 steps * 0.2 seconds per step = 8 seconds)
    increment = 100 / num_steps

    for i in range(num_steps + 1):
        progress = i * increment
        bar = f"[{'#'*i}{' '*(num_steps - i)}]"
        print(f"\r{loading_text} {colorama.Fore.GREEN}{bar}{colorama.Fore.RESET} [{progress:.1f}%", end="", flush=True)
        time.sleep(total_time / num_steps)

# Function to get a valid user input (either 'y'/'n' or a number within a range).
def get_valid_input(prompt, valid_values):
    while True:
        user_input = input(prompt)
        if user_input in valid_values:
            return user_input
        else:
            print("Sorry, I don't understand. Please try again")

# Function to play the "blip.mp3" audio file.
def play_blip_audio():
    audio_path = os.path.expanduser("~/Desktop/blip.mp3")  # Provide the full path to the audio file
    try:
        subprocess.Popen(["afplay", audio_path])
    except Exception as e:
        print("Error playing audio:", e)

# Function to display the question and answer with optional example in the specified color.
def display_question_and_answer(question, answer, example=None, question_color=colorama.Fore.WHITE, answer_color=colorama.Fore.GREEN, example_color=colorama.Fore.YELLOW):
    print(f"{question_color}{question}{colorama.Fore.RESET}")
    print(f"{answer_color}{answer}{colorama.Fore.RESET}")
    if example:
        print(f"{example_color if 'buttercup' in example else answer_color}{example}{colorama.Fore.RESET}")

# Function to display a welcome message.
def display_welcome_message():
    welcome_text = "-- Ryan's Project --"
    welcome_art = pyfiglet.Figlet(font='small').renderText(welcome_text)
    print("\n" + f"{colorama.Fore.YELLOW}{welcome_art}{colorama.Fore.RESET}\n")

# Function to create a new word by combining two random words from the database.
def create_new_word():
    database = [
        ("neuro", "eco"),
        ("robo", "fusion"),
        ("nano", "cloud"),
        ("space", "hub"),
        ("data", "plex"),
        ("bio", "gen"),
        ("med", "net"),
        ("info", "wave"),
        ("tech", "minds"),
        ("cyber", "works"),
        ("smart", "ex"),
        ("eco", "gen"),
        ("robo", "tech"),
        ("neuro", "cloud"),
        ("info", "fusion"),
        ("bio", "hub"),
        ("med", "gen"),
        ("robo", "data"),
        ("smart", "net"),
        ("space", "plex"),
    ]
    # Select two random words from the database.
    new_word_pair = random.choice(database)

    # Combine the two words with a hyphen.
    new_word = "-".join(new_word_pair)

    # Get the meaning of the new word from the database.
    new_word_meaning = get_word_meaning(new_word_pair)

    # Display the new word in different colors.
    print(f"\n{colorama.Fore.CYAN}Your new word:{colorama.Fore.RESET} {colorama.Fore.YELLOW}{new_word}{colorama.Fore.RESET}\n")
    print(f"{colorama.Fore.MAGENTA}Meaning:{colorama.Fore.RESET} {colorama.Fore.GREEN}{new_word_meaning}{colorama.Fore.RESET}")

    # Display the new word in ASCII style art with a different color.
    art_color = colorama.Fore.RED if 'buttercup' in new_word else colorama.Fore.YELLOW
    print(art_color + pyfiglet.Figlet(font='small').renderText(new_word) + colorama.Fore.RESET)

# Function to get the meaning of a new word based on the word pair.
def get_word_meaning(word_pair):
    meanings = {
        ("neuro", "eco"): "A new word representing the combination of neurology and ecology, often related to sustainable technology.",
        ("robo", "fusion"): "A new word representing the fusion of robotics and technology.",
        ("nano", "cloud"): "A new word describing technology related to nanotechnology and cloud computing.",
        ("space", "hub"): "A new word representing a central hub for space-related activities.",
        ("data", "plex"): "A new word related to complex data processing and analysis.",
        ("bio", "gen"): "A new word describing the combination of biology and genetics.",
        ("med", "net"): "A new word representing the networked world of medical technology and healthcare.",
        ("info", "wave"): "A new word describing the wave of information technology.",
        ("tech", "minds"): "A new word referring to the collective intelligence of technological minds.",
        ("cyber", "works"): "A new word describing collaborative cyber technology initiatives.",
        ("smart", "ex"): "A new word representing the excellence of smart technology.",
        ("eco", "gen"): "A new word related to ecological genetics or environmentally friendly genetics.",
        ("robo", "tech"): "A new word representing the combination of robotics and technology.",
        ("neuro", "cloud"): "A new word describing cloud technology related to neurology.",
        ("info", "fusion"): "A new word representing the fusion of information technology and data analysis.",
        ("bio", "hub"): "A new word representing a central hub for biology-related research and development.",
        ("med", "gen"): "A new word related to medical genetics.",
        ("robo", "data"): "A new word describing data related to robotics and automation.",
        ("smart", "net"): "A new word describing the intelligent networking of devices and systems.",
        ("space", "plex"): "A new word representing a complex space-related structure or network."
    }

    return meanings.get(word_pair, "This new word combines two concepts or technologies.")

if __name__ == "__main__":
    # Create a separate thread to loop the 1-second beep audio.
    beep_thread = threading.Thread(target=loop_beep_audio)
    beep_thread.daemon = True
    beep_thread.start()

    # Display loading animation and loading bar.
    display_loading_bar()

    # Stop the beep audio when switching to background music.
    beep_audio_playing = False

    # Play background music in a separate thread.
    play_background_music()

    # Display welcome message.
    display_welcome_message()

    while True:
        # List the topics with different colors.
        print(f"{colorama.Fore.RED}1. Phonetics{colorama.Fore.RESET}")
        print(f"{colorama.Fore.GREEN}2. Phonology{colorama.Fore.RESET}")
        print(f"{colorama.Fore.BLUE}3. Morphology{colorama.Fore.RESET}")
        print("4. Quit")

        # Select a topic.
        valid_topic_numbers = ["1", "2", "3", "4"]
        topic_number = get_valid_input("Enter the number of the topic you want to explore (or '4' to quit): ", valid_topic_numbers)
        if topic_number == '4':
            break

        # Display questions from the selected topic.
        if topic_number == "1":
            # List the questions for Phonetics.
            phonetics_questions = [
                (
                    f"{colorama.Fore.CYAN}What is the International Phonetic Alphabet (IPA)?{colorama.Fore.RESET}",
                    "The International Phonetic Alphabet (IPA) is an alphabetic system of phonetic notation based on the Latin alphabet. It is used to represent the sounds of spoken language.",
                    f"{colorama.Fore.YELLOW}{pyfiglet.Figlet(font='small').renderText('IPA')}{colorama.Fore.RESET}",
                    "https://www.cambridge.org/features/IPAchart/"
                ),
                (
                    f"{colorama.Fore.CYAN}What are two examples of phonemes that exist in English but do not exist in the Russian language?{colorama.Fore.RESET}",
                    "[θ] - The Voiceless Interdental Fricative: This sound is represented by the symbol [θ] and is found in English words like thick and math. To produce the voiceless interdental fricative [θ] sound, place your tongue against your upper front teeth, create a small gap, and exhale air without vibrating your vocal cords."
                    "[ð] - The Voiced Interdental Fricative: This sound is represented by the symbol [ð] and is heard in words like this and brother. To produce this sound, it's similar to [θ], but it's voiced. Place the tip of your tongue against your upper front teeth and let your vocal cords vibrate.",
                    pyfiglet.Figlet(font='small').renderText("th-ick\nbro-th-er"),
                    "https://www.lispeech.com/lets-learn-a-little-more-about-russian-influenced-english/"
                ),
                (
                    f"{colorama.Fore.CYAN}What three parameters classify English consonants?{colorama.Fore.RESET}",
                    "Consonants are characterized by voicing, place of articulation, and manner of articulation. These features determine how consoants are articulated. We can further explore them in categories known as Plosives, Nasals, Fricatives, Affricates and Approximants.",
                    pyfiglet.Figlet(font='small').renderText("Plosives\nNasals\nFricatives"),
                    "https://literaryenglish.com/wp-content/uploads/2022/04/manner-of-articulation-copy.jpg"
                ),
                # Add more questions for phonetics.
                # ...
            ]

            # List the questions within the selected topic with individual colors.
            print(f"\nQuestions about {colorama.Fore.CYAN}Phonetics{colorama.Fore.RESET}:")

            for i in range(len(phonetics_questions)):
                question, _, _, _ = phonetics_questions[i]
                print(f"{i + 1}. {colorama.Fore.CYAN}{question}{colorama.Fore.RESET}")

            while True:
                # Select a question within the topic.
                valid_question_numbers = [str(i) for i in range(1, len(phonetics_questions) + 1)]
                question_number = get_valid_input(
                    f"Enter the number of the question you want to learn about ( or 'b' for back): ",
                    valid_question_numbers + ['b']
                )

                if question_number == 'b':
                    break

                question_number = int(question_number) - 1

                # Play the "blip.mp3" audio when the user presses Enter.
                play_blip_audio()

                # Display a loading animation.
                loading_animation()

                # Get the question, answer, example, and URL for the selected question.
                question, answer, example, url = phonetics_questions[question_number]

                # Display the question and answer, including the description and example with individual colors for questions.
                display_question_and_answer(question, answer, example, colorama.Fore.CYAN)

                # Ask the user if they want to open a web browser for further examples.
                open_browser = get_valid_input(
                    "Would you like to open a web-browser to see a further example with visuals? (y/n): ",
                    ["y", "n"]
                )
                if open_browser == "y":
                    webbrowser.open(url)  # Open the URL for the selected question

        elif topic_number == "2":
            # List the questions for Phonology.
            phonology_questions = [
                (
                    f"{colorama.Fore.MAGENTA}What is the difference between phonetics and phonology?{colorama.Fore.RESET}",
                    "Phonetics deals with the study of the articulatory and acoustic properties of sounds, while phonology deals with the structure and systematic patterning of sounds.",
                    pyfiglet.Figlet(font='small').renderText("Phonetics\nPhonology"),
                    "https://static.wixstatic.com/media/e0d2e0_c8599824747b41d0a0014c812b15c4cc.jpg/v1/fill/w_415,h_311,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/e0d2e0_c8599824747b41d0a0014c812b15c4cc.jpg"
                ),
                (
                    f"{colorama.Fore.MAGENTA}What is a minimal pair in phonology?{colorama.Fore.RESET}",
                    "A minimal pair is a pair of words in a language that only differ in one phoneme. Minimal pairs are used to demonstrate that two sounds are separate phonemes in a language. For example, in English, 'pat' and 'bat' are a minimal pair because the only difference is the initial sound, /p/ and /b/.",
                    pyfiglet.Figlet(font='small').renderText("pat\nbat"),
                    "https://pbs.twimg.com/media/FTxo1arUsAAbwdx.jpg:large"
                ),
                (
                    f"{colorama.Fore.MAGENTA}What is an allophone in phonology?{colorama.Fore.RESET}",
                    "Allophones are phonetic variations - different pronunciations - of the same phoneme. Using a different allophone does not change meaning. The /l/ sound is pronounced differently in 'love' and in 'wool'.",
                    pyfiglet.Figlet(font='small').renderText("love\nwool"),
                    "https://upload.wikimedia.org/wikipedia/commons/5/5a/Phoneme-allophone-determination-chart.svg"
                ),
                # Add more questions for phonology.
                # ...
            ]

            # List the questions within the selected topic with individual colors.
            print(f"\nQuestions about {colorama.Fore.CYAN}Phonology{colorama.Fore.RESET}:")

            for i in range(len(phonology_questions)):
                question, _, _, _ = phonology_questions[i]
                print(f"{i + 1}. {colorama.Fore.CYAN}{question}{colorama.Fore.RESET}")

            while True:
                # Select a question within the topic.
                valid_question_numbers = [str(i) for i in range(1, len(phonology_questions) + 1)]
                question_number = get_valid_input(
                    f"Enter the number of the question you want to learn about ( or 'b' for back): ",
                    valid_question_numbers + ['b']
                )

                if question_number == 'b':
                    break

                question_number = int(question_number) - 1

                # Play the "blip.mp3" audio when the user presses Enter.
                play_blip_audio()

                # Display a loading animation.
                loading_animation()

                # Get the question, answer, example, and URL for the selected question.
                question, answer, example, url = phonology_questions[question_number]

                # Display the question and answer, including the description and example with individual colors for questions.
                display_question_and_answer(question, answer, example, colorama.Fore.CYAN)

                # Ask the user if they want to open a web browser for further examples.
                open_browser = get_valid_input(
                    "Would you like to open a web-browser to see a further example with visuals? (y/n): ",
                    ["y", "n"]
                )
                if open_browser == "y":
                    webbrowser.open(url)  # Open the URL for the selected question

        elif topic_number == "3":
            # List the questions for Morphology.
            morphology_questions = [
                (
                    f"{colorama.Fore.YELLOW}What is morphology in linguistics?{colorama.Fore.RESET}",
                    "Morphology is the study of the internal structure of words and the rules governing how words are formed from their basic units called morphemes.",
                    pyfiglet.Figlet(font='small').renderText("Morphology"),
                    "https://www.sheffield.ac.uk/linguistics/home/all-about-linguistics/about-website/branches-linguistics/morphology/what-morphology"
                ),
                (
                    f"{colorama.Fore.YELLOW}What are morphemes and their variations??{colorama.Fore.RESET}",
                    "A morpheme is the most diminutive linguistic unit of langage with a meaning. A word might consist of more than one morpheme, but we can not break a morpheme into any unit.",
                    pyfiglet.Figlet(font='small').renderText("Beauty\nful\n=\nBeautiful"),
                    "https://sastrainggris-fib.ub.ac.id/wp-content/uploads/2022/01/Alya-Fadhilla-1-410x1024.png"
                ),
                (
                    f"{colorama.Fore.YELLOW}Create a new word in morphology!{colorama.Fore.RESET}",
                    "Combine two random words to create a new word.",
                    "",
                    ""
                ),
                # Add more questions for morphology.
                # ...
            ]

            # List the questions within the selected topic with individual colors.
            print(f"\nQuestions about {colorama.Fore.CYAN}Morphology{colorama.Fore.RESET}:")

            for i in range(len(morphology_questions)):
                question, _, _, _ = morphology_questions[i]
                print(f"{i + 1}. {colorama.Fore.CYAN}{question}{colorama.Fore.RESET}")

            while True:
                # Select a question within the topic.
                valid_question_numbers = [str(i) for i in range(1, len(morphology_questions) + 1)]
                question_number = get_valid_input(
                    f"Enter the number of the question you want to learn about ( or 'b' for back): ",
                    valid_question_numbers + ['b']
                )

                if question_number == 'b':
                    break

                question_number = int(question_number) - 1

                if question_number == len(morphology_questions) - 1:
                    # Create a new word in morphology.
                    # Play the "blip.mp3" audio when the user presses Enter.
                    play_blip_audio()

                    # Display a loading animation.
                    loading_animation()

                    # Generate a new word in morphology and display it.
                    create_new_word()
                else:
                    # Play the "blip.mp3" audio when the user presses Enter.
                    play_blip_audio()

                    # Display a loading animation.
                    loading_animation()

                    # Get the question, answer, example, and URL for the selected question.
                    question, answer, example, url = morphology_questions[question_number]

                    # Display the question and answer, including the description and example with individual colors for questions.
                    display_question_and_answer(question, answer, example, colorama.Fore.CYAN)

                    # Ask the user if they want to open a web browser for further examples.
                    open_browser = get_valid_input(
                        "Would you like to open a web-browser to see a further example with visuals? (y/n): ",
                        ["y", "n"]
                    )
                    if open_browser == "y":
                        webbrowser.open(url)  # Open the URL for the selected question

    # Exit the program with a goodbye message.
    print("\nGoodbye!")
