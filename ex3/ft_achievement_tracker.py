import random


achievements = [
    "First Steps",
    "Boss Slayer",
    "Master Explorer",
    "Collector Supreme",
    "Strategist",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "World Savior",
    "Untouchable",
    "Crafting Genius",
    "Unstoppable",
    "Sharp Mind",
    "Hidden Path Finder"
]


def gen_player_achievement():
    count = random.randint(5, 9)
    selected = random.sample(achievements, count)
    return set(selected)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievement()
    bob = gen_player_achievement()
    charlie = gen_player_achievement()
    dylan = gen_player_achievement()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_achievements = alice.union(bob, charlie, dylan)
    print(f"\nAll distinct achievements: {all_achievements}")

    common_achievement = alice.intersection(bob, charlie, dylan)
    print(f"\nCommon achievements: {common_achievement}\n")

    only_alice = alice.difference(bob, charlie, dylan)
    only_bob = bob.difference(alice, charlie, dylan)
    only_charlie = charlie.difference(bob, alice, dylan)
    only_dylan = dylan.difference(bob, charlie, alice)

    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")

    all_possible = set(achievements)
    alice_missing = all_possible.difference(alice)
    bob_missing = all_possible.difference(bob)
    charlie_missing = all_possible.difference(charlie)
    dylan_missing = all_possible.difference(dylan)

    print("\n")
    print(f"Alice is missing: {alice_missing}")
    print(f"Bob is missing: {bob_missing}")
    print(f"Charlie is missing: {charlie_missing}")
    print(f"Dylan is missing: {dylan_missing}")
