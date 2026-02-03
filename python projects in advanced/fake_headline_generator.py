# import the random module
import random

# create subjects
subjects = [
    "shahrukh khan",
    "virat kohli",
    "nirmala sitharaman",
    "a mumbai cat",
    "a group of monkeys",
    "prime minister modi",
    "an auto rickshaw driver from delhi"
]

# create actions
actions = [
    "launches",
    "cancels",
    "dances with",
    "declares war on",
    "orders",
    "celebrates",
    "announces",
    "gives away free mobiles"
]

# create places or things
places_or_things = [
    "at red fort",
    "in mumbai local train",
    "a plate of samosas",
    "inside parliament",
    "at ganga ghat",
    "during IPL match",
    "at india gate"
]

# start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place}!"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        break

# print goodbye message
print("\nThanks for using this Fake News Headline Generator tool. Have a fun day!")