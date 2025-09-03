"""Debugger exercise."""


def split_string(string):
    """Given a string, split it into a list of 'words'."""
    start_of_word = 0
    words = []
    for i in range(len(string)):
        if string[i] == " ":
            words.append(string[start_of_word:i])
            start_of_word = i
    return words


def count_words(words):
    """Count how often words occur in a list."""
    word_counts = dict()
    for i in words:
        if i in word_counts:
            word_counts[i] += 1
        else:
            word_counts[i] = 1
    return word_counts


def create_collective_count(word_counts1, word_counts2):
    """Take two word counters and combine them into one."""
    collective_count = dict()
    for i in word_counts1:
        if i in word_counts2:
            collective_count[i] = word_counts1[i] + word_counts2[i]
    return collective_count


def word_counter(string1, string2):
    """Find the word that occurs the most across the two strings."""
    string1_words = split_string(string1)
    string2_words = split_string(string2)
    word_counts1 = count_words(string1_words)
    word_counts2 = count_words(string2_words)
    collective_count = create_collective_count(word_counts1, word_counts2)
    curr_max = 0
    for i in collective_count:
        if collective_count[i] > curr_max:
            curr_max = collective_count[i]
            curr_word = i
    return curr_word


if __name__ == "__main__":

    # Test Case 0
    print("Test Case 0:")
    print("The result should be 'of'")

    string1 = (
        "Far out in the uncharted backwaters of the "
        "unfashionable end of the western spiral arm of "
        "the Galaxy lies a small unregarded yellow sun."
    )
    string2 = (
        "Orbiting this at a distance of roughly ninety-two million "
        "miles is an utterly insignificant little blue green "
        "planet whose ape-descended life forms are so amazingly "
        "primitive that they still think digital watches are a pretty neat idea."
    )

    print("Comparing:")
    print(f"Sentence 1: {string1}")
    print(f"Sentence 2: {string2}")

    test_word = word_counter(string1, string2)
    print(f"Result: {test_word}")

    # Test Case 1
    print("Test Case 1:")
    print("The result should be 'No matching words'")

    string1 = "I love Practical Data Science."
    string2 = "Who is Nick Eubank?"

    print("Comparing:")
    print(f"Sentence 1: {string1}")
    print(f"Sentence 2: {string2}")

    test_word = word_counter(string1, string2)
    print(f"Result: {test_word}")

    # Test Case 2
    print("Test Case 2:")
    print("The result should 'code'")

    string1 = "This is a test of my code."
    string2 = "I hope there's not bugs in this code."

    print("Comparing:")
    print(f"Sentence 1: {string1}")
    print(f"Sentence 2: {string2}")

    test_word = word_counter(string1, string2)
    print(f"Result: {test_word}")
