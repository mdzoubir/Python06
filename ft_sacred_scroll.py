import alchemy
import alchemy.elements

def test_sacred_scroll():
    print()
    print("=== Sacred Scroll Mastery ===")
    print()
    
    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_water(): {alchemy.elements.create_water()}")
    print(f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")
    print()

    print("Testing package-level access (controlled by __init__.py):")
    for func_name in ["create_fire", "create_water", "create_earth", "create_air"]:
        try:
            func = getattr(alchemy, func_name)
            print(f"alchemy.{func_name}(): {func()}")
        except AttributeError:
            print(f"alchemy.{func_name}(): AttributeError - not exposed")
    print()

    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")

if __name__ == "__main__":
    try:
        test_sacred_scroll()
    except Exception as e:
        print(f"Error: {e}")
