from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life
import alchemy.transmutation

def test_pathway_debate():
    try:
        print()
        print("=== Pathway Debate Mastery ===")
        print()

        print("Testing Absolute Imports (from basic.py):")
        print(f"lead_to_gold(): {lead_to_gold()}")
        print(f"stone_to_gem(): {stone_to_gem()}")
        print()

        print("Testing Relative Imports (from advanced.py):")
        print(f"philosophers_stone(): {philosophers_stone()}")
        print(f"elixir_of_life(): {elixir_of_life()}")
        print()

        print("Testing Package Access:")
        print(f"alchemy.transmutation.lead_to_gold(): {alchemy.transmutation.lead_to_gold()}")
        print(f"alchemy.transmutation.philosophers_stone(): {alchemy.transmutation.philosophers_stone()}")
        print()

        print("Both pathways work! Absolute: clear, Relative: concise")
    except AttributeError:
        print("Error: The element is not found")

if __name__ == "__main__":
    try:
        test_pathway_debate()
    except Exception as e:
        print(f"Error: {e}")
