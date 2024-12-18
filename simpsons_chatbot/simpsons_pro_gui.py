import customtkinter as ctk
import tkinter as tk
from tkinter import scrolledtext
import random
from gtts import gTTS
import pygame
import os
import threading
import tempfile
import time

# Initialize pygame mixer
pygame.mixer.init()

class SimpsonsCharacter:
    def __init__(self, name, facts, catchphrases, voice_lang='en'):
        self.name = name
        self.facts = facts
        self.catchphrases = catchphrases
        self.voice_lang = voice_lang
        self.temp_dir = tempfile.mkdtemp()
        self.lock = threading.Lock()
        self.current_audio = None

    def get_random_fact(self):
        return random.choice(self.facts)

    def get_random_catchphrase(self):
        return random.choice(self.catchphrases)

    def speak(self, text):
        def speak_text():
            with self.lock:
                try:
                    # Create a unique filename for this text
                    filename = f"{abs(hash(text))}.mp3"
                    temp_file = os.path.join(self.temp_dir, filename)
                    
                    # Generate speech if file doesn't exist
                    if not os.path.exists(temp_file):
                        tts = gTTS(text=text, lang=self.voice_lang, slow=False)
                        tts.save(temp_file)
                    
                    # Stop any currently playing audio
                    pygame.mixer.music.stop()
                    
                    # Load and play the new audio
                    pygame.mixer.music.load(temp_file)
                    pygame.mixer.music.play()
                    
                    # Wait for the audio to finish
                    while pygame.mixer.music.get_busy():
                        time.sleep(0.1)
                        
                except Exception as e:
                    print(f"Speech error: {e}")

        # Run speech in a separate thread
        threading.Thread(target=speak_text, daemon=True).start()

class SimpsonsProGUI:
    def __init__(self):
        self.setup_window()
        self.setup_characters()
        self.setup_gui_elements()

    def setup_window(self):
        self.root = ctk.CTk()
        self.root.title("The Simpsons Chatbot Pro")
        self.root.geometry("800x600")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

    def setup_characters(self):
        self.characters = {
            "homer": SimpsonsCharacter(
                "Homer",
                [
                    "I work as a safety inspector at the Springfield Nuclear Power Plant",
                    "My favorite food is donuts, especially from the Kwik-E-Mart",
                    "I've won a Grammy Award for being part of a barbershop quartet",
                    "My middle name is Jay",
                    "I invented a drink called the Flaming Homer",
                    "I once went to space as an astronaut",
                    "I was the mascot for Mr. Plow, my snow plowing business",
                    "I once owned the Denver Broncos",
                    "I've been to every state in America (except Montana)",
                    "I was briefly a monorail conductor",
                    "I was the leader of a secret society called the Stonecutters",
                    "I once had a crayon removed from my brain and became a genius",
                    "I designed my own car called 'The Homer'",
                    "I was once the voice of Poochie on The Itchy & Scratchy Show",
                    "I've worked as a food critic for the Springfield newspaper",
                    "I once climbed the tallest mountain in Springfield",
                    "I was temporarily banned from Moe's Tavern",
                    "I once became a professional boxer",
                    "I founded my own religion called 'Movementarianism'",
                    "I once became the sanitation commissioner of Springfield",
                    "I was briefly the mayor of New Springfield",
                    "I once worked as Mr. Burns' personal assistant",
                    "I've been to Japan, Australia, and Brazil",
                    "I once owned a pet lobster named Pinchy",
                    "I was briefly a blackjack dealer at Mr. Burns' casino",
                    "I once became the mascot of a baseball team called the Isotopes",
                    "I discovered a new element that nearly destroyed Springfield",
                    "I was once the leader of a motorcycle gang",
                    "I became a professional food critic and gained 60 pounds",
                    "I invented the 'Everything's OK Alarm'",
                    "I once joined the Naval Reserve",
                    "I was briefly a missionary in the South Pacific",
                    "I once became a renowned artist with my Mr. Plow painting",
                    "I worked as a technical director for a country music star",
                    "I was temporarily the CEO of the Power Plant",
                    "I once became a professional arm wrestler",
                    "I invented the 'Makeup Gun' for women",
                    "I was briefly a professional baseball mascot",
                    "I once worked as a truck driver hauling hazardous materials",
                    "I became the king of Mardi Gras in New Orleans",
                    "I was a substitute teacher at Springfield Elementary",
                    "I once became a successful YouTube star",
                    "I invented a chair with a built-in toilet",
                    "I was briefly the owner of a successful sugar business",
                    "I once became a professional football coach",
                    "I worked as a bounty hunter for a week",
                    "I was temporarily the head of Springfield's mob",
                    "I once became a professional opera singer",
                    "I invented a drink mixing robot that started a bar fight",
                    "I was briefly a professional bull rider",
                    "I once became a professional wine taster",
                    "I invented a special hammock that rocks itself",
                    "I was briefly a professional sumo wrestler",
                    "I started my own energy drink company",
                    "I once became a professional food sculptor",
                    "I worked as a voice actor for GPS navigation",
                    "I was temporarily a professional mattress tester",
                    "I created a successful hot sauce brand",
                    "I once became a professional competitive eater",
                    "I started my own donut delivery service",
                    "I was briefly a professional sleep study participant",
                    "I invented a bacon-scented air freshener",
                    "I once became a professional beer critic",
                    "I worked as a professional couch tester",
                    "I was temporarily a professional nap consultant",
                    "I created a successful burger recipe blog",
                    "I once became a professional TV marathon watcher",
                    "I started my own lazy lifestyle coaching business",
                    "I was briefly a professional hammock reviewer",
                    "I invented a remote control finder device",
                    "I once became a professional snack food taster",
                    "I worked as a professional pillow fort architect",
                    "I was temporarily a professional comfort food chef",
                    "I created a successful lazy man's workout program",
                    "I once became a professional donut hole inspector",
                    "I invented a sandwich that cures hiccups",
                    "I became a professional couch surfing champion",
                    "I started a successful napping Olympics",
                    "I created a donut-flavored energy drink",
                    "I was briefly a professional food combination inventor",
                    "I worked as a professional laziness consultant",
                    "I invented a remote-controlled sandwich maker",
                    "I once became a professional food dream interpreter",
                    "I started a successful snack food review channel",
                    "I was temporarily a professional comfort food therapist",
                    "I created a donut-scented cologne line",
                    "I once became a professional food nap coordinator",
                    "I worked as a professional snack food architect",
                    "I was briefly a professional food meditation guru",
                    "I invented a pizza-summoning device",
                    "I once became a professional couch comfort consultant",
                    "I started my own food-based relaxation therapy",
                    "I was temporarily a professional snoring analyst",
                    "I created a successful lazy cooking show",
                    "I once became a professional food-coma researcher",
                    "I worked as a professional nap environment designer",
                    "I was briefly a professional food dream therapist",
                    "I invented a burger-based meditation technique",
                    "I once became a professional food relaxation expert",
                    "I started a successful lazy gourmet movement"
                ],
                ["D'oh!", "Mmm... donuts", "Why you little!", "Woo hoo!", "Stupid Flanders!", "Save me, Jebus!", "Mmm... beer"],
                'en'
            ),
            "marge": SimpsonsCharacter(
                "Marge",
                [
                    "My maiden name is Bouvier",
                    "I have naturally blue hair that stands 2 feet tall",
                    "I was a police officer once",
                    "I'm an excellent painter",
                    "I have a gambling addiction that I've overcome",
                    "I once owned a pretzel franchise business",
                    "I wrote a novel called 'The Harpooned Heart'",
                    "I was once a real estate agent",
                    "I graduated from Springfield Community College",
                    "I was briefly a competitive bodybuilder",
                    "I once worked at the Nuclear Power Plant",
                    "I've been part of a women's investment group",
                    "I was the director of 'Streetcar!' the musical",
                    "I once owned the Leftorium with Ned Flanders",
                    "I have a fear of flying that I overcame",
                    "I was once a food blogger",
                    "I've been in a women's bowling league",
                    "I worked as an art teacher at Springfield Elementary",
                    "I once ran a successful bed & breakfast",
                    "I was briefly a marijuana activist",
                    "I competed in a demolition derby",
                    "I once worked as a church organist",
                    "I started my own sandwich shop",
                    "I was the voice of reason in the Springfield Militia",
                    "I once worked as a professional carpenter",
                    "I was briefly a successful fashion designer",
                    "I once became a professional ice skater",
                    "I started a successful organic food business",
                    "I was temporarily a professional photographer",
                    "I invented a special cleaning solution that became popular",
                    "I once worked as a substitute teacher",
                    "I became a successful lifestyle blogger",
                    "I was briefly a radio talk show host",
                    "I started a neighborhood watch program",
                    "I once became a professional chess player",
                    "I worked as a voice actor for commercials",
                    "I invented a special hair care product",
                    "I was briefly a professional theater critic",
                    "I started a successful home organizing business",
                    "I once became a yoga instructor",
                    "I worked as a professional party planner",
                    "I was temporarily a professional matchmaker",
                    "I started a successful catering business",
                    "I once became a professional life coach",
                    "I worked as an environmental activist",
                    "I was briefly a professional mediator",
                    "I started a successful book club",
                    "I once became a professional gardener",
                    "I worked as a marriage counselor",
                    "I was temporarily a professional etiquette teacher",
                    "I once started a successful home bakery business",
                    "I became a professional family counselor",
                    "I invented a natural cleaning product line",
                    "I started a neighborhood cooking class",
                    "I was briefly a professional interior decorator",
                    "I worked as a children's book illustrator",
                    "I created a successful parenting podcast",
                    "I once became a professional organization consultant",
                    "I started a family-friendly recipe blog",
                    "I was temporarily a professional stress management coach",
                    "I invented a special hair care routine",
                    "I once became a professional family photographer",
                    "I worked as a professional meal planner",
                    "I was briefly a professional home economics teacher",
                    "I created a successful family budgeting app",
                    "I once became a professional decluttering expert",
                    "I started my own family counseling practice",
                    "I was temporarily a professional family portrait artist",
                    "I invented a special recipe organization system",
                    "I once became a professional family event planner",
                    "I worked as a professional home safety consultant",
                    "I was briefly a professional family tradition consultant",
                    "I created a successful family memory book business",
                    "I once became a professional family vacation planner",
                    "I started a successful family wellness program",
                    "I created a successful family harmony program",
                    "I invented a natural home aromatherapy system",
                    "I started a mindful parenting movement",
                    "I became a professional family meditation guide",
                    "I was briefly a professional home harmony consultant",
                    "I worked as a family wellness coordinator",
                    "I created a successful family bonding app",
                    "I once became a professional family historian",
                    "I started a family tradition preservation society",
                    "I was temporarily a professional family chef",
                    "I invented a special family communication method",
                    "I once became a professional home peace keeper",
                    "I worked as a professional family balance coach",
                    "I was briefly a professional household zen master",
                    "I created a successful family mindfulness program",
                    "I once became a professional family unity consultant",
                    "I started my own family healing practice",
                    "I was temporarily a professional home energy balancer",
                    "I invented a special family bonding ritual",
                    "I once became a professional family memory keeper",
                    "I worked as a professional home harmony designer",
                    "I was briefly a professional family joy consultant",
                    "I created a successful family peace program",
                    "I once became a professional home blessing coordinator",
                    "I started a successful family enlightenment movement"
                ],
                ["Hmmmm...", "Oh, Homie!", "It's true, I don't approve", "Now it's Marge's time to shine!", "I just think they're neat!"],
                'en'
            ),
            "bart": SimpsonsCharacter(
                "Bart",
                [
                    "My full name is Bartholomew JoJo Simpson",
                    "I'm known for my skateboarding skills",
                    "I've been in the fourth grade for over 30 years",
                    "My catchphrase was once banned in some schools",
                    "I write different messages on the chalkboard in every opening sequence",
                    "I was Springfield Elementary's hall monitor",
                    "I discovered the comet 'Bart's Comet'",
                    "I was Krusty the Clown's assistant",
                    "I once owned a factory in China",
                    "I was the 'I Didn't Do It' boy",
                    "I've won a Grammy for my 'Do the Bartman' song",
                    "I was briefly the owner of Milhouse's soul",
                    "I worked as Radioactive Man's sidekick Fallout Boy",
                    "I once became a faith healer",
                    "I was the leader of the Pre-Teen Braves",
                    "I created the comic character Angry Dad based on Homer",
                    "I once worked at the Kwik-E-Mart",
                    "I've been to Australia and got in trouble with their government",
                    "I was a member of the Junior Campers",
                    "I once had a hit radio show as 'El Barto'",
                    "I discovered a three-eyed fish named Blinky",
                    "I was briefly famous for saying 'I didn't do it'",
                    "I once owned a race horse named Duncan",
                    "I was the star of the Spiderman musical",
                    "I created a fake soul mate for Mrs. Krabappel",
                    "I once became a professional stand-up comedian",
                    "I started my own underground newspaper",
                    "I was briefly a professional magician",
                    "I created a successful prank call app",
                    "I once became a graffiti artist in New York",
                    "I worked as a professional video game tester",
                    "I was temporarily a professional skateboarder",
                    "I started my own detective agency",
                    "I once became a successful child actor",
                    "I worked as a professional party clown",
                    "I was briefly a professional baseball player",
                    "I created a popular web series",
                    "I once became a successful DJ",
                    "I worked as a professional prankster",
                    "I was temporarily a professional rapper",
                    "I started my own YouTube gaming channel",
                    "I once became a successful street artist",
                    "I worked as a professional stunt double",
                    "I was briefly a professional snowboarder",
                    "I created a popular meme",
                    "I once became a successful cartoon voice actor",
                    "I worked as a professional BMX rider",
                    "I was temporarily a professional film critic",
                    "I started my own social media platform",
                    "I once became a successful child entrepreneur",
                    "I once became a professional skateboard designer",
                    "I started my own prank supply company",
                    "I invented a homework-doing robot",
                    "I created a successful school excuse generator app",
                    "I was briefly a professional extreme sports athlete",
                    "I worked as a professional comic book critic",
                    "I started my own animation YouTube channel",
                    "I once became a professional graffiti consultant",
                    "I created a successful prank call compilation album",
                    "I was temporarily a professional stunt coordinator",
                    "I invented a special skateboard with rockets",
                    "I once became a professional video game streamer",
                    "I worked as a professional mischief consultant",
                    "I was briefly a professional rebel fashion designer",
                    "I created a successful school survival guide",
                    "I once became a professional detention escape artist",
                    "I started my own extreme sports league",
                    "I was temporarily a professional chaos coordinator",
                    "I invented a special teacher prank detector avoider",
                    "I once became a professional rebellion consultant",
                    "I worked as a professional troublemaking advisor",
                    "I was briefly a professional school protest organizer",
                    "I created a successful rebel lifestyle brand",
                    "I once became a professional mischief mathematician",
                    "I started a successful rebel radio show",
                    "I invented an automatic homework excuser",
                    "I created a teacher-proof prank system",
                    "I started a professional troublemaker academy",
                    "I became a master of digital pranking",
                    "I was briefly a professional chaos theorist",
                    "I worked as a rebellion strategy consultant",
                    "I created a successful prankster network",
                    "I once became a professional mayhem coordinator",
                    "I started a digital mischief movement",
                    "I was temporarily a professional anarchy artist",
                    "I invented a special prank prediction algorithm",
                    "I once became a professional rebellion forecaster",
                    "I worked as a professional chaos mathematician",
                    "I was briefly a professional disorder scientist",
                    "I created a successful troublemaker's handbook",
                    "I once became a professional rebellion theorist",
                    "I started my own chaos research institute",
                    "I was temporarily a professional mischief physicist",
                    "I invented a special trouble-making formula",
                    "I once became a professional anarchy analyst",
                    "I worked as a professional mayhem theorist",
                    "I was briefly a professional chaos philosopher",
                    "I created a successful rebellion science program",
                    "I once became a professional disorder consultant",
                    "I started a successful mischief theory movement"
                ],
                ["Eat my shorts!", "¡Ay, caramba!", "Don't have a cow, man!", "I'm Bart Simpson, who the hell are you?", "Cowabunga!"],
                'en'
            ),
            "lisa": SimpsonsCharacter(
                "Lisa",
                [
                    "I became a vegetarian in season 7",
                    "I play the baritone saxophone",
                    "I'm a member of Mensa with an IQ of 159",
                    "I created a perpetual motion machine",
                    "I'm a Buddhist",
                    "I was briefly Springfield Elementary's student body president",
                    "I won the Springfield Spelling Bee",
                    "I created Little Lisa's Recycling Plant",
                    "I discovered a new species of angel fossil",
                    "I was the first female member of the Junior Skeptics Club",
                    "I've written for the school newspaper",
                    "I once joined Mensa",
                    "I created an artificial intelligence system",
                    "I was a jazz musician at Jazz Hole",
                    "I won the Springfield Marathon",
                    "I solved the Springfield Mystery",
                    "I was briefly a professional ice hockey player",
                    "I created a social networking platform",
                    "I won the Science Fair with my steamed hams experiment",
                    "I was the conductor of the Springfield Youth Orchestra",
                    "I started a successful microlending business",
                    "I discovered corruption in the Springfield politics",
                    "I was a guest curator at the Springfield Museum",
                    "I created an app that predicts train arrivals",
                    "I once ran for Springfield's Board of Education",
                    "I invented a renewable energy source for Springfield",
                    "I once became a professional chess champion",
                    "I started an environmental protection movement",
                    "I created a successful educational podcast",
                    "I was briefly a professional debate champion",
                    "I worked as a research assistant at a university",
                    "I created a new mathematical theorem",
                    "I once became a successful documentary filmmaker",
                    "I started a girls' coding club at school",
                    "I was temporarily a professional music critic",
                    "I invented a universal translation device",
                    "I once became a successful political blogger",
                    "I created a sustainable farming initiative",
                    "I was briefly a professional climate scientist",
                    "I started a successful youth orchestra",
                    "I worked as a professional book reviewer",
                    "I was temporarily a professional ethicist",
                    "I created a successful meditation app",
                    "I once became a professional civil rights activist",
                    "I started a successful science magazine",
                    "I was briefly a professional philosopher",
                    "I created a successful educational software",
                    "I once became a professional environmental lawyer",
                    "I started a successful youth mentoring program",
                    "I was temporarily a professional peace negotiator",
                    "I created an artificial intelligence ethics council",
                    "I started a quantum physics study group",
                    "I invented a new form of sustainable energy",
                    "I wrote a thesis on advanced string theory",
                    "I was briefly a professional quantum computer programmer",
                    "I worked as a professional climate change researcher",
                    "I created a successful science education platform",
                    "I once became a professional ethics consultant",
                    "I started a successful quantum mechanics journal",
                    "I was temporarily a professional particle physicist",
                    "I invented a universal consciousness translator",
                    "I once became a professional philosophy writer",
                    "I worked as a professional quantum ethics researcher",
                    "I was briefly a professional dark matter theorist",
                    "I created a successful quantum meditation app",
                    "I once became a professional space-time theorist",
                    "I started my own quantum research institute",
                    "I was temporarily a professional multiverse explorer",
                    "I invented a special quantum consciousness detector",
                    "I once became a professional entropy researcher",
                    "I worked as a professional quantum archaeologist",
                    "I was briefly a professional time paradox consultant",
                    "I created a successful quantum poetry movement",
                    "I once became a professional dimension theorist",
                    "I started a successful quantum art gallery",
                    "I discovered a new quantum consciousness theory",
                    "I created a universal empathy algorithm",
                    "I started a quantum environmental movement",
                    "I became a quantum sociology pioneer",
                    "I was briefly a professional reality architect",
                    "I worked as a quantum consciousness researcher",
                    "I created a successful dimension bridging theory",
                    "I once became a professional universe designer",
                    "I started a quantum enlightenment program",
                    "I was temporarily a professional reality theorist",
                    "I invented a special consciousness expansion device",
                    "I once became a professional dimension theorist",
                    "I worked as a professional reality mathematician",
                    "I was briefly a professional quantum philosopher",
                    "I created a successful universe mapping system",
                    "I once became a professional reality engineer",
                    "I started my own quantum consciousness institute",
                    "I was temporarily a professional dimension architect",
                    "I invented a special reality harmonization method",
                    "I once became a professional universe consultant",
                    "I worked as a professional quantum poet",
                    "I was briefly a professional reality artist",
                    "I created a successful quantum healing program",
                    "I once became a professional dimension healer",
                    "I started a successful quantum enlightenment movement"
                ],
                ["If anyone wants me, I'll be in my room", "BAAAAART!", "Trust in yourself and you can achieve anything", "I'm going to my room", "Quit it, Bart!"],
                'en'
            ),
            "maggie": SimpsonsCharacter(
                "Maggie",
                [
                    "I shot Mr. Burns",
                    "My first word was 'Daddy'",
                    "I'm usually seen with my red pacifier",
                    "I have the same IQ as Lisa",
                    "I've saved Homer's life multiple times",
                    "I was briefly the leader of a daycare gang",
                    "I can communicate through saxophone playing",
                    "I once escaped from the Ayn Rand School for Tots",
                    "I've demonstrated exceptional marksmanship skills",
                    "I was temporarily adopted by Mr. Burns",
                    "I saved Springfield from a bear attack",
                    "I can understand sign language",
                    "I once led a baby revolution",
                    "I have perfect pitch in music",
                    "I solved the mystery of the missing pacifier",
                    "I was briefly a professional ice skater",
                    "I can drive better than Homer",
                    "I once won a baby beauty pageant",
                    "I've shown skills in martial arts",
                    "I helped capture Snake the criminal",
                    "I can play the saxophone like Lisa",
                    "I once saved the family from a house fire",
                    "I have a collection of hidden weapons",
                    "I've demonstrated advanced computer skills",
                    "I once became the mascot for a baseball team",
                    "I secretly learned multiple languages",
                    "I once became a professional baby food tester",
                    "I started a successful baby revolution movement",
                    "I created a secret baby communication network",
                    "I was briefly a professional baby model",
                    "I worked as a secret agent for the FBI",
                    "I created a successful baby sign language system",
                    "I once became a professional baby gymnast",
                    "I started a successful baby yoga class",
                    "I was temporarily a professional baby critic",
                    "I invented a new type of baby toy",
                    "I once became a successful baby influencer",
                    "I created a baby security system",
                    "I was briefly a professional baby chess player",
                    "I started a successful baby music band",
                    "I worked as a professional baby stunt double",
                    "I was temporarily a professional baby photographer",
                    "I created a successful baby fashion line",
                    "I once became a successful baby food critic",
                    "I started a successful baby detective agency",
                    "I was briefly a professional baby martial artist",
                    "I created a successful baby meditation program",
                    "I once became a professional baby artist",
                    "I started a successful baby book club",
                    "I was temporarily a professional baby archaeologist",
                    "I secretly solved advanced quantum equations",
                    "I created a baby quantum teleporter",
                    "I invented a pacifier-powered spaceship",
                    "I started a secret baby space program",
                    "I was briefly a professional baby quantum physicist",
                    "I worked as a professional baby time traveler",
                    "I created a successful baby telekinesis program",
                    "I once became a professional baby mind reader",
                    "I started a successful baby telepathy network",
                    "I was temporarily a professional baby astronaut",
                    "I invented a special baby quantum computer",
                    "I once became a successful baby dimension hopper",
                    "I created a baby parallel universe detector",
                    "I was briefly a professional baby alien communicator",
                    "I started a successful baby space exploration program",
                    "I worked as a professional baby quantum mechanic",
                    "I was temporarily a professional baby universe creator",
                    "I created a successful baby time machine",
                    "I once became a professional baby reality bender",
                    "I started a successful baby quantum research lab",
                    "I was briefly a professional baby multiverse navigator",
                    "I created a successful baby quantum portal",
                    "I once became a professional baby space-time architect",
                    "I started a successful baby quantum energy company",
                    "I was temporarily a professional baby universe explorer",
                    "I discovered baby quantum entanglement",
                    "I created a pacifier-based quantum computer",
                    "I started a baby universe exploration program",
                    "I became a baby quantum reality engineer",
                    "I was briefly a professional baby dimension walker",
                    "I worked as a baby quantum consciousness guide",
                    "I created a successful baby universe mapping system",
                    "I once became a professional baby reality architect",
                    "I started a baby quantum enlightenment program",
                    "I was temporarily a professional baby universe designer",
                    "I invented a special baby quantum teleportation device",
                    "I once became a professional baby dimension consultant",
                    "I worked as a professional baby reality mathematician",
                    "I was briefly a professional baby quantum philosopher",
                    "I created a successful baby universe harmonization system",
                    "I once became a professional baby reality engineer",
                    "I started my own baby quantum consciousness institute",
                    "I was temporarily a professional baby dimension architect",
                    "I invented a special baby reality stabilization method",
                    "I once became a professional baby universe consultant",
                    "I worked as a professional baby quantum poet",
                    "I was briefly a professional baby reality artist",
                    "I created a successful baby quantum healing program",
                    "I once became a professional baby dimension healer",
                    "I started a successful baby quantum enlightenment movement"
                ],
                ["*pacifier sucking sound*", "*gun cocking sound*", "*falls down*", "*happy baby noises*", "*determined grunt*"],
                'en'
            )
        }

    def setup_gui_elements(self):
        # Title
        self.title_label = ctk.CTkLabel(
            self.root,
            text="The Simpsons Chatbot",
            font=("Arial Black", 24, "bold"),
            text_color="#FED41D"
        )
        self.title_label.pack(pady=20)

        # Character selection frame
        self.char_frame = ctk.CTkFrame(self.root)
        self.char_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        # Character buttons
        self.char_buttons = {}
        for char_name in self.characters.keys():
            btn = ctk.CTkButton(
                self.char_frame,
                text=char_name.title(),
                command=lambda n=char_name: self.select_character(n),
                fg_color="#3498db",
                hover_color="#2980b9",
                width=120
            )
            btn.pack(side=tk.LEFT, padx=10, pady=10)
            self.char_buttons[char_name] = btn

        # Chat display
        self.chat_display = scrolledtext.ScrolledText(
            self.root,
            height=15,
            wrap=tk.WORD,
            font=("Arial", 12),
            bg="#FFFFFF",
            fg="#000000"
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        self.chat_display.configure(state='disabled')

        # Button frame
        self.button_frame = ctk.CTkFrame(self.root)
        self.button_frame.pack(fill=tk.X, padx=20, pady=20)

        # Action buttons
        self.fact_btn = ctk.CTkButton(
            self.button_frame,
            text="Get Fact",
            command=self.show_fact,
            fg_color="#2ecc71",
            hover_color="#27ae60",
            state="disabled"
        )
        self.fact_btn.pack(side=tk.LEFT, padx=5)

        self.catchphrase_btn = ctk.CTkButton(
            self.button_frame,
            text="Catchphrase",
            command=self.show_catchphrase,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            state="disabled"
        )
        self.catchphrase_btn.pack(side=tk.LEFT, padx=5)

        self.clear_btn = ctk.CTkButton(
            self.button_frame,
            text="Clear Chat",
            command=self.clear_chat,
            fg_color="#95a5a6",
            hover_color="#7f8c8d"
        )
        self.clear_btn.pack(side=tk.RIGHT, padx=5)

        # Speech toggle
        self.speech_var = tk.BooleanVar(value=True)
        self.speech_cb = ctk.CTkCheckBox(
            self.button_frame,
            text="Enable Speech",
            variable=self.speech_var,
            fg_color="#3498db",
            hover_color="#2980b9"
        )
        self.speech_cb.pack(side=tk.RIGHT, padx=20)

        self.current_character = None
        self.add_message("System", "Welcome to the Simpsons Chatbot Pro! Select a character to begin!")

    def select_character(self, char_name):
        self.current_character = self.characters[char_name]
        message = f"Now talking to {char_name.title()}!"
        self.add_message("System", message)
        self.current_character.speak(message)
        self.update_buttons_state()

    def show_fact(self):
        if self.current_character:
            fact = self.current_character.get_random_fact()
            self.add_message(self.current_character.name, fact)
            self.current_character.speak(fact)

    def show_catchphrase(self):
        if self.current_character:
            catchphrase = self.current_character.get_random_catchphrase()
            self.add_message(self.current_character.name, catchphrase)
            self.current_character.speak(catchphrase)

    def clear_chat(self):
        self.chat_display.configure(state='normal')
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.configure(state='disabled')
        message = "Chat cleared! Select a character to continue."
        self.add_message("System", message)
        if self.current_character:
            self.current_character.speak(message)

    def add_message(self, sender, message):
        self.chat_display.configure(state='normal')
        full_message = f"{sender}: {message}\n\n"
        self.chat_display.insert(tk.END, full_message)
        self.chat_display.see(tk.END)
        self.chat_display.configure(state='disabled')

    def update_buttons_state(self):
        state = "normal" if self.current_character else "disabled"
        self.fact_btn.configure(state=state)
        self.catchphrase_btn.configure(state=state)

    def run(self):
        self.root.mainloop()

def main():
    app = SimpsonsProGUI()
    app.run()

if __name__ == "__main__":
    main()
