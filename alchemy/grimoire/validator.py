def validate_ingredients(ingredients: str) -> str:
    valid = {"fire", "water", "earth", "air"}
    words = ingredients.lower().split()
    if any(word in valid for word in words):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
