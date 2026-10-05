# 1
def min_max(num, min_v, max_v):
    for n in num:
        if n < min_v:
            min_v = n
        elif n > max_v:
            max_v = n
    return min_v, max_v


# 2
def is_palindrome(word):
    return word.lower().strip() == word[::-1].lower().strip()


# 3
def character_frequency(word):
    characters = {}
    for ch in word:
        if ch not in characters:
            characters[ch] = 1
        else:
            characters[ch] += 1
    return characters

# 4
def pos_neg_zero(nums):
    classify = {
        "positive" : 0,
        "negative" : 0,
        "zero" : 0
        }
    for n in nums:
        if n == 0:
            classify["zero"] += 1
        elif n > 0:
            classify["positive"] += 1
        else:
            classify["negative"] += 1
    return classify



# 5
def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b

def is_even(num: int) -> bool:
    """Return True if num is even, otherwise False."""
    return num % 2 == 0

def classify(celsius: float) -> str:
    """Classify a Celsius temperature as cold, warm, or hot."""
    if celsius < 10:
        return "cold"
    elif celsius <= 25:
        return "warm"
    else:
        return "hot"

def calculate_area(width: int, height: int) -> int:
    """Calculates area which is product of width and height"""
    return width * height

def calculate_cost(area: int, price_per_sqm: int) -> int:
    """Calculates cost by performing product of area and price per sqm."""
    return area * price_per_sqm

def report_area_cost(width: int, height: int, price_per_sqm: int) -> int:
    """Calculates cost by calling calculate area and calculate cost functions"""
    area = calculate_area(width, height)
    cost = calculate_cost(area, price_per_sqm)
    return cost

if __name__ == "__main__":
    print("Q-1")
    numbers = [1, 2, 3, 4, 55, 40, 33, 20, 0]
    min_value, max_value = min_max(numbers, numbers[0], numbers[0])
    print(f"Minimum num : {min_value}, Maximum num : {max_value}")
    print()

    print("Q-2")
    words = ["Madam", "level", "Mom", "Dad", "Harry", "Test"]
    for word in words:
        result = "Palindrome" if is_palindrome(word) else "Not a Palindrome"
        print(f"{word} is {result}")
    print()

    print("Q-3")
    print(character_frequency("hello"))
    print()

    print("Q-4")
    numbers = [0, 1, 2, 3, 4, 0, 55, 40, 33, 20, 0]
    print(pos_neg_zero(numbers))
    print()
