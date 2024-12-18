import random

class SimpsonsCharacter:
    def __init__(self, name, facts, catchphrases):
        self.name = name
        self.facts = facts
        self.catchphrases = catchphrases

    def get_random_fact(self):
        return random.choice(self.facts)

    def get_random_catchphrase(self):
        return random.choice(self.catchphrases)

# Character definitions with facts and catchphrases
homer = SimpsonsCharacter(
    "Homer",
    [
        "I work as a safety inspector at the Springfield Nuclear Power Plant",
        "My favorite food is donuts, especially from the Kwik-E-Mart",
        "I've won a Grammy Award for being part of a barbershop quartet",
        "My middle name is Jay",
        "I invented a drink called the Flaming Homer"
    ],
    ["D'oh!", "Mmm... donuts", "Why you little!", "Woo hoo!"]
)

marge = SimpsonsCharacter(
    "Marge",
    [
        "My maiden name is Bouvier",
        "I have naturally blue hair that stands 2 feet tall",
        "I was a police officer once",
        "I'm an excellent painter",
        "I have a gambling addiction that I've overcome"
    ],
    ["Hmmmm...", "Oh, Homie!", "It's true, I don't approve"]
)

bart = SimpsonsCharacter(
    "Bart",
    [
        "My full name is Bartholomew JoJo Simpson",
        "I'm known for my skateboarding skills",
        "I've been in the fourth grade for over 30 years",
        "My catchphrase was once banned in some schools",
        "I write different messages on the chalkboard in every opening sequence"
    ],
    ["Eat my shorts!", "¡Ay, caramba!", "Don't have a cow, man!"]
)

lisa = SimpsonsCharacter(
    "Lisa",
    [
        "I became a vegetarian in season 7",
        "I play the baritone saxophone",
        "I'm a member of Mensa with an IQ of 159",
        "I created a perpetual motion machine",
        "I'm a Buddhist"
    ],
    ["If anyone wants me, I'll be in my room", "BAAAAART!", "Trust in yourself and you can achieve anything"]
)

maggie = SimpsonsCharacter(
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

characters = {
    "homer": homer,
    "marge": marge,
    "bart": bart,
    "lisa": lisa,
    "maggie": maggie
}

def main():
    print("Welcome to the Simpsons Chatbot!")
    print("Available characters: Homer, Marge, Bart, Lisa, Maggie")
    print("Type 'exit' to quit, 'list' to see characters, or 'help' for commands")
    
    while True:
        user_input = input("\nWho would you like to talk to? ").lower().strip()
        
        if user_input == "exit":
            print("D'oh! Goodbye!")
            break
        elif user_input == "list":
            print("Available characters: Homer, Marge, Bart, Lisa, Maggie")
            continue
        elif user_input == "help":
            print("Commands:")
            print("- Enter character name to talk to them")
            print("- 'fact' to get a random fact")
            print("- 'catchphrase' to hear their catchphrase")
            print("- 'list' to see all characters")
            print("- 'exit' to quit")
            continue
            
        if user_input in characters:
            character = characters[user_input]
            print(f"\nTalking to {character.name}!")
            
            while True:
                action = input(f"What would you like {character.name} to do? (fact/catchphrase/back): ").lower().strip()
                
                if action == "fact":
                    print(f"{character.name}: {character.get_random_fact()}")
                elif action == "catchphrase":
                    print(f"{character.name}: {character.get_random_catchphrase()}")
                elif action == "back":
                    break
                else:
                    print("Please choose 'fact', 'catchphrase', or 'back'")
        else:
            print("D'oh! Character not found. Type 'list' to see available characters.")

if __name__ == "__main__":
    main()
