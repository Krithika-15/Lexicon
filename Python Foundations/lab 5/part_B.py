# 1
def add_all(*numbers):
# * only belongs in the parameter list,
# it tells python "Collect every positional argument the caller passes into a single tuple and call that tuple as numbers"
# Inside the function body, numbers is just a plain tuple and never use *
    total = 0
    for n in numbers:
    # notes here numbers is (1, 2, 3, 4, 5) a tuple
        total += n
    return total

print("Q-1")
result = add_all(1, 2, 3, 4, 5)
print(f"Sum of numbers : {result}\n")


# 2
def average(*numbers):
    total_nums = len(numbers)
    # when no arguments passed will have empty tuple numbers = ()
    if not total_nums:
        return "No Numbers were provided"
    else:
        total = 0
        for n in numbers:
            total += n
        average = total/total_nums
    return average


print("Q-2")
without_nums = average()
with_nums = average(1, 2, 3, 4, 5)
print(f"Without numbers : {without_nums}")
print(f"With numbers : {with_nums}\n")


# 3
def longest_word(*words):
    if not len(words):
        return "No values were provided", 0
    else :
        long_word = words[0]
        longest = len(words[0])
        for word in words:
            if len(word) > longest:
                long_word = word
                longest = len(word)
    return long_word, longest # returns tuple

print("Q-3")
empty_words, empty_size = longest_word()
print(f"Empty words : {empty_words}, {empty_size}")
# unpacking tuple to two variables
words_list, characters_size = longest_word("Harry Potter", "Hermione Granger", "Drace", "Ginny", "Ron Weasly", "Emma")
print(f"Longest word is {words_list} with {characters_size} characters.\n")


# 4
def build_sentence(separator, *words):
    sentence = separator.join(words)
    return sentence
print("Q-4")
sentence = build_sentence(" ", "Python", "is", "a", "dynamically", "typed", "language")
print(f"Sentence : {sentence}\n")


# 5
def describe_scores(student_name, *scores):
    name = student_name
    if len(scores):
        no_of_scores = len(scores)
        total = 0
        for score in scores:
            total += score
        average_score = total/no_of_scores
        return name, no_of_scores, average_score
    else:
        return "No scores were provided", 0, 0


print("Q-5")
name, num_of_scores, score_average = describe_scores("John", 50, 60, 70, 80, 90, 55)
print(f"Student Name : {name}\nNumber of scores : {num_of_scores}\nAverage Score : {score_average}")

