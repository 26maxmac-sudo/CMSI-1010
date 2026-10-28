import random

# Each template has words beginning with a colon that the player fills in.
templates = [
    {
        "text": "A :adjective ghost is behind you!",
        "author": "rtoal",
    },
    {
        "text": "Some :adjective :creature with a :weapon is eating :dessert.",
        "author": "rtoal",
    },
    {
        "text": "Look! There is a :adjective :animal :verb a :noun in :place.",
        "author": "rtoal",
    },
    {
        "text": "The :color :animal :action over the :adjective :plant.",
        "author": "rtoal",
    },
    {
        "text": "The :adjective :noun :verb the :adjective :noun.",
        "author": "rtoal",
    },
    {
        "text": "My :relative keeps a pet :animal named :name in the :room.",
        "author": "Max MacDonald",
    },
    {
        "text": "Never eat :food before :activity unless you want a :adjective :body_part.",
        "author": "Max MacDonald",
    },
    {
        "text": "Breaking news: a :adjective :occupation was caught :verb_ending_in_ing at :place.",
        "author": "Max MacDonald",
    },
    {
        "text": "To win the game you must collect :number :plural_noun and defeat the :adjective :creature.",
        "author": "Max MacDonald",
    },
    {
        "text": "Professor :name says that :plural_noun are :adjective and should be :verb_past_tense immediately.",
        "author": "Max MacDonald",
    },
    {
        "text": "On my vacation to :place I rode a :color :vehicle and lost my :clothing_item.",
        "author": "Max MacDonald",
    },
]

# Any of these answers means the player wants to go again.
yes_answers = {"yes", "y", "yeah", "yep", "sure", "ok", "okay",
               "sí", "si", "oui", "ja", "hai", "da"}


def ask_for_word(description):
    # Keep asking until the input is between 1 and 30 characters long.
    description = description.replace("_", " ")
    article = "an" if description[0] in "aeiou" else "a"
    while True:
        word = input(f"Enter {article} {description}: ").strip()
        if 1 <= len(word) <= 30:
            return word
        print("Your word must be between 1 and 30 characters long.")


def fill_in(text):
    filled_words = []
    for word in text.split():
        if word.startswith(":"):
            # Separate the placeholder from any trailing punctuation.
            placeholder = word[1:].rstrip(".,!?;:")
            punctuation = word[1 + len(placeholder):]
            filled_words.append(ask_for_word(placeholder) + punctuation)
        else:
            filled_words.append(word)
    return " ".join(filled_words)


def play():
    template = random.choice(templates)
    story = fill_in(template["text"])
    print()
    print(story)
    print()
    print(f"Template by {template['author']}")
    print()
    print()


while True:
    play()
    answer = input("Do you want to play again? ").strip().lower()
    if answer not in yes_answers:
        print("Thanks for playing!")
        break
