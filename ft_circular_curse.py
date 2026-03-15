from alchemy.grimoire import record_spell, validate_ingredients

def test_circular_curse():
    try:
        print()
        print("=== Circular Curse Breaking ===")
        print()

        print("Testing ingredient validation:")
        print(f'validate_ingredients("fire air"): {validate_ingredients("fire air")}')
        print(f'validate_ingredients("dragon scales"): {validate_ingredients("dragon scales")}')
        print()

        print("Testing spell recording with validation:")
        print(f'record_spell("Fireball", "fire air"): {record_spell("Fireball", "fire air")}')
        print(f'record_spell("Dark Magic", "shadow"): {record_spell("Dark Magic", "shadow")}')
        print()

        print("Testing late import technique:")
        print(f'record_spell("Lightning", "air"): {record_spell("Lightning", "air")}')
        print()

        print("Circular dependency curse avoided using late imports!")
        print("All spells processed safely!")
    except AttributeError:
        print("Error: The element is not found")

if __name__ == "__main__":
    try:
        test_circular_curse()
    except Exception as e:
        print(f"Error: {e}")
