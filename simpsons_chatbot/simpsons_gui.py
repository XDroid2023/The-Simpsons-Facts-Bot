import tkinter as tk
from tkinter import ttk, scrolledtext
import random
from PIL import Image, ImageTk
import os

class SimpsonsCharacter:
    def __init__(self, name, facts, catchphrases):
        self.name = name
        self.facts = facts
        self.catchphrases = catchphrases

    def get_random_fact(self):
        return random.choice(self.facts)

    def get_random_catchphrase(self):
        return random.choice(self.catchphrases)

class SimpsonsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("The Simpsons Chatbot")
        self.root.geometry("800x600")
        self.root.configure(bg='#FED41D')  # Simpsons yellow

        # Initialize characters
        self.setup_characters()
        
        # Create main frame
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Character selection
        self.char_frame = ttk.LabelFrame(self.main_frame, text="Select Character")
        self.char_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.char_buttons = {}
        for char_name in self.characters.keys():
            btn = ttk.Button(self.char_frame, text=char_name.title(),
                           command=lambda n=char_name: self.select_character(n))
            btn.pack(side=tk.LEFT, padx=5, pady=5)
            self.char_buttons[char_name] = btn

        # Chat display
        self.chat_display = scrolledtext.ScrolledText(self.main_frame, height=15, wrap=tk.WORD)
        self.chat_display.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        self.chat_display.configure(state='disabled')

        # Buttons frame
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(fill=tk.X, pady=(0, 10))

        self.fact_btn = ttk.Button(self.button_frame, text="Get Fact",
                                 command=self.show_fact)
        self.fact_btn.pack(side=tk.LEFT, padx=5)

        self.catchphrase_btn = ttk.Button(self.button_frame, text="Catchphrase",
                                        command=self.show_catchphrase)
        self.catchphrase_btn.pack(side=tk.LEFT, padx=5)

        self.clear_btn = ttk.Button(self.button_frame, text="Clear Chat",
                                  command=self.clear_chat)
        self.clear_btn.pack(side=tk.RIGHT, padx=5)

        # Initial state
        self.current_character = None
        self.update_buttons_state()
        
        # Welcome message
        self.add_message("System", "Welcome to the Simpsons Chatbot! Select a character to begin!")

    def setup_characters(self):
        self.characters = {
            "homer": SimpsonsCharacter(
                "Homer",
                [
                    "I work as a safety inspector at the Springfield Nuclear Power Plant",
                    "My favorite food is donuts, especially from the Kwik-E-Mart",
                    "I've won a Grammy Award for being part of a barbershop quartet",
                    "My middle name is Jay",
                    "I invented a drink called the Flaming Homer"
                ],
                ["D'oh!", "Mmm... donuts", "Why you little!", "Woo hoo!"]
            ),
            "marge": SimpsonsCharacter(
                "Marge",
                [
                    "My maiden name is Bouvier",
                    "I have naturally blue hair that stands 2 feet tall",
                    "I was a police officer once",
                    "I'm an excellent painter",
                    "I have a gambling addiction that I've overcome"
                ],
                ["Hmmmm...", "Oh, Homie!", "It's true, I don't approve"]
            ),
            "bart": SimpsonsCharacter(
                "Bart",
                [
                    "My full name is Bartholomew JoJo Simpson",
                    "I'm known for my skateboarding skills",
                    "I've been in the fourth grade for over 30 years",
                    "My catchphrase was once banned in some schools",
                    "I write different messages on the chalkboard in every opening sequence"
                ],
                ["Eat my shorts!", "¡Ay, caramba!", "Don't have a cow, man!"]
            ),
            "lisa": SimpsonsCharacter(
                "Lisa",
                [
                    "I became a vegetarian in season 7",
                    "I play the baritone saxophone",
                    "I'm a member of Mensa with an IQ of 159",
                    "I created a perpetual motion machine",
                    "I'm a Buddhist"
                ],
                ["If anyone wants me, I'll be in my room", "BAAAAART!", "Trust in yourself and you can achieve anything"]
            ),
            "maggie": SimpsonsCharacter(
                "Maggie",
                [
                    "I shot Mr. Burns",
                    "My first word was 'Daddy'",
                    "I'm usually seen with my red pacifier",
                    "I have the same IQ as Lisa",
                    "I've saved Homer's life multiple times"
                ],
                ["*pacifier sucking sound*", "*gun cocking sound*", "*falls down*"]
            )
        }

    def select_character(self, char_name):
        self.current_character = self.characters[char_name]
        self.add_message("System", f"Now talking to {char_name.title()}!")
        self.update_buttons_state()

    def show_fact(self):
        if self.current_character:
            fact = self.current_character.get_random_fact()
            self.add_message(self.current_character.name, fact)

    def show_catchphrase(self):
        if self.current_character:
            catchphrase = self.current_character.get_random_catchphrase()
            self.add_message(self.current_character.name, catchphrase)

    def clear_chat(self):
        self.chat_display.configure(state='normal')
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.configure(state='disabled')
        self.add_message("System", "Chat cleared! Select a character to continue.")

    def add_message(self, sender, message):
        self.chat_display.configure(state='normal')
        self.chat_display.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_display.see(tk.END)
        self.chat_display.configure(state='disabled')

    def update_buttons_state(self):
        state = 'normal' if self.current_character else 'disabled'
        self.fact_btn.configure(state=state)
        self.catchphrase_btn.configure(state=state)

def main():
    root = tk.Tk()
    app = SimpsonsGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
