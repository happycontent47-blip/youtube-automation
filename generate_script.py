import random

topics = [
    "deep ocean mysteries",
    "peaceful coral reefs",
    "life of sea turtles",
    "deep sea creatures",
    "whales in the ocean"
    "wildlife animals"
]

def generate_script():
    topic = random.choice(topics)

    script = f"""
    0:00 Beneath the surface, the world of {topic} begins...

    2:00 The ocean is vast and full of quiet movement...

    5:00 Creatures move in harmony with the currents...

    10:00 In the deeper regions, life becomes more mysterious...

    20:00 Darkness surrounds the silent ocean floor...

    28:00 The ocean returns to stillness...
    """

    with open("script.txt", "w") as f:
        f.write(script)

generate_script()
