import random

OUTPUT_FILE = "script.txt"

hooks = [
    "Deep beneath the ocean surface, something massive is moving… and no one has fully explained it.",
    "In the darkest parts of the ocean, light disappears—but life doesn’t.",
    "Scientists discovered something in the deep sea that changed what we know about marine life.",
    "There is a place in the ocean where silence becomes terrifying.",
]

story_blocks = [
    "The ocean is not empty. It is a vast ecosystem filled with movement, pressure, and survival.",
    "Creatures in the deep ocean have adapted in ways that seem almost alien.",
    "Some species survive without sunlight, relying on chemical energy instead of the sun.",
    "The deeper you go, the stranger life becomes, and the more unknown it feels.",
    "Massive migrations happen daily beneath the surface, completely unseen from above.",
    "Whales communicate across thousands of kilometers using low-frequency sound waves.",
    "The ocean floor holds mysteries we are still trying to understand.",
]

outro = [
    "Even today, most of the ocean remains unexplored, leaving more questions than answers.",
    "What lies beneath is still one of Earth’s greatest mysteries.",
    "The ocean continues to hide secrets we may never fully uncover.",
]

def build_script(target_minutes=30):
    script = []

    # Hook (viral attention grab)
    script.append(random.choice(hooks))
    script.append("\n")

    # Expand content to simulate long-form retention script
    minutes_filled = 0
    while minutes_filled < target_minutes:
        block = random.choice(story_blocks)
        script.append(block)
        script.append("")
        minutes_filled += 2.5  # rough pacing estimate

    script.append(random.choice(outro))

    return "\n".join(script)

text = build_script()

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("VIRAL SCRIPT GENERATED: script.txt")
