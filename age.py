import streamlit as st
import datetime
import random
import calendar

compliments_facts = [
    "You're doing great! 😄",
    "That's a lovely choice!",
    "Fun fact: Honey never spoils!",
    "Nice taste! 💯",
    "You have good vibes!",
    "Did you know octopuses have three hearts?",
    "You seem like someone who makes the world better!",
    "Fun fact: Bananas are berries, but strawberries aren’t!",
    "You're awesome. Don't forget it!",
    "You light up the room!",
    "Fun fact: Wombat poop is cube-shaped!",
    "You're as sharp as a tack!",
    "People like you make coding fun!",
]

ascii_art = {
    "dog": r"""
     / \__
    (    @\___
    /         O
   /   (_____/
  /_____/ U
""",
    "cat": r"""
 /\_/\ 
( o.o )
 > ^ <
""",
    "rabbit": r"""
 (\_/)
 ( •_•)
 / >🥕
""",
    "fox": r"""
 /\   /\
( o^.^o )
 (")___(")
""",
}

animal_sounds = {
    "dog": "🐶 Bark bark!",
    "cat": "🐱 Meow~",
    "parrot": "Squawk! I'm clever!",
    "cow": "🐮 Moo!",
    "lion": "Roar!",
    "snake": "Hisssss!",
    "duck": "Quack!",
    "chicken": "Bawk bawk!",
    "horse": "Neighhh!",
    "rabbit": "Boing boing!",
    "owl": "Hoo hoo!",
    "fox": "🦊 What does the fox say?",
}

def is_valid_date(year, month, day):
    try:
        datetime.datetime(year, month, day)
        return True
    except ValueError:
        return False

def print_highlighted_calendar(year, month, day):
    cal = calendar.TextCalendar()
    cal_str = cal.formatmonth(year, month)
    day_str = f"{day}".rjust(2)
    highlighted = cal_str.replace(f"{day_str} ", f"[{day_str}] ") \
                         .replace(f"{day_str}\n", f"[{day_str}]\n")
    st.text("Here's the calendar with your entered date highlighted:\n")
    st.text(highlighted)

def age_and_message(birth_year, birth_month, birth_day, today_month, today_day):
    current_year = datetime.datetime.now().year
    if not is_valid_date(birth_year, birth_month, birth_day):
        return "Invalid birth date!"
    if not is_valid_date(current_year, today_month, today_day):
        return "Invalid today's date!"
    birth_date = datetime.datetime(birth_year, birth_month, birth_day)
    today_date = datetime.datetime(current_year, today_month, today_day)
    age = today_date.year - birth_date.year
    if (today_month, today_day) < (birth_month, birth_day):
        age -= 1

    messages = []
    messages.append(f"You are {age} years old.")

    if age < 18:
        messages.append("You are a minor. No drinking yet (:")
    elif 18 <= age < 20:
        messages.append("You are a young adult.")
    elif age == 21:
        messages.append("Please do not drink and drive :)")
    elif 20 <= age < 30:
        messages.append("You are in your twenties.")
    elif 30 <= age < 50:
        messages.append("You are an adult.")
    elif 50 <= age < 100:
        messages.append("You are experienced!")
    elif age >= 100:
        messages.append("How are you not dead yet?")
    elif age == 16:
        messages.append("You just got your driver's license, don't break any laws (; *cough Jake *cough")

    messages.append(random.choice(compliments_facts))
    return "\n".join(messages)

def color_animal_interaction(favorite_color, favorite_animal):
    color_messages = {
        "red": "Red is the color of passion and power!",
        "blue": "Blue is calming like the ocean.",
        "green": "Green? Grass eater.",
        "yellow": "Yellow is bright and cheerful like the sun!",
        "pink": "This is the most girly answer ever",
        "black": "Boring person.",
        "white": "White is clean, calm, and classic.",
        "purple": "You look like a blueberry.",
        "orange": "Orange is energetic and fun like a sunset!",
        "brown": "Brown is warm and earthy.",
        "gray": "Gray is sophisticated and mysterious.",
        "gold": "Gold means you shine bright like royalty!",
        "silver": "Silver is sleek and futuristic.",
        "cyan": "Cyan is bright and cool like tropical waters.",
        "magenta": "Magenta is bold and artsy.",
        "beige": "Beige is subtle, stylish, and soothing.",
        "teal": "Teal is deep and unique — just like you.",
        "maroon": "Maroon is rich and refined.",
        "turquoise": "Turquoise gives strong beach day vibes."
    }
    messages = []
    color_msg = color_messages.get(favorite_color.lower(), f"{favorite_color.capitalize()} is a great choice — very original!")
    messages.append(color_msg)
    messages.append(random.choice(compliments_facts))

    animal = favorite_animal.lower()
    if animal in animal_sounds:
        messages.append(animal_sounds[animal])
    else:
        messages.append(f"{animal.capitalize()}s are awesome!")

    if animal in ascii_art:
        messages.append(ascii_art[animal])

    if animal == "fox":
        messages.append("""
Ring-ding-ding-ding-dingeringeding!
Wa-pa-pa-pa-pa-pa-pow! -Ylvis
""")

    messages.append(random.choice(compliments_facts))
    return "\n".join(messages)

def favorite_food_message(food):
    food = food.lower()
    if food == "cheese":
        return "You are basically eating flavored expired milk."
    elif food == "hot dogs":
        return "Your answer tells me that you like grilling."
    elif food == "mac and cheese":
        return "You are eating noodles covered in flavored expired milk."
    elif food == "strawberry":
        return "You like straws that taste like berries?"
    else:
        return f"Yum! {food.capitalize()} sounds delicious!"

# Streamlit UI
st.title("Age & Personality Program")

name = st.text_input("What is your name?").strip()
if name:
    st.write(f"Hello, {name}!")
    birth_year = st.number_input("Enter your birth year:", 1900, datetime.datetime.now().year, 2000)
    birth_month = st.number_input("Enter your birth month (1-12):", 1, 12, 1)
    birth_day = st.number_input("Enter your birth day (1-31):", 1, 31, 1)
    today_month = st.number_input("Enter today's month (1-12):", 1, 12, datetime.datetime.now().month)
    today_day = st.number_input("Enter today's day (1-31):", 1, 31, datetime.datetime.now().day)

    if st.button("Calculate Age & Show Message"):
        msg = age_and_message(birth_year, birth_month, birth_day, today_month, today_day)
        st.text(msg)
        if is_valid_date(birth_year, birth_month, birth_day):
            print_highlighted_calendar(birth_year, birth_month, birth_day)

    favorite_color = st.text_input("What is your favorite color? (e.g. red, blue, green)")
    favorite_animal = st.text_input("What is your favorite animal?")
    if st.button("Show Color & Animal Messages"):
        msg = color_animal_interaction(favorite_color, favorite_animal)
        st.text(msg)

    favorite_food = st.text_input("What is your favorite food?")
    if st.button("Show Food Message"):
        msg = favorite_food_message(favorite_food)
        st.text(msg)
