"""Debugger exercise."""


def split_string(string):
    """Given a string, split it into a list of 'words'."""
    start_of_word = 0
    words = []
    for i in range(len(string)):
        if string[i] == " ":
            word = string[start_of_word:i]

            # If starts with a space, drop that space.
            if word[0] == " ":
                word = word[1:]

            words.append(word)
            start_of_word = i
    return words


def get_list_of_unique_words(sentence_as_list):
    """Get a list that contains one copy of each word in sentence."""
    unique_words = []
    for word in sentence_as_list:
        if word not in unique_words:
            unique_words.append(word)
    return unique_words


def count_occurances_of_word(word_to_count, sentence_as_list):
    """
    Count the number of times a word appears in the list of words
    in the sentence.
    """
    counter = 0
    for word in sentence_as_list:
        if word == word_to_count:
            counter += 1
    return counter


def most_common_word(sentence):
    """Find the most common word in a list"""

    sentence_as_list = split_string(sentence)
    unique_words = get_list_of_unique_words(sentence_as_list)

    most_common_word = None
    most_common_word_count = 0
    for word in unique_words:
        count = count_occurances_of_word(word sentence_as_list)
        if most_common_word_count < count:
            most_common_word = word
            most_common_word_count = count

    return most_common_word


def main():

    # Test Case 0
    print("Test Case 0:")
    print("The result should be 'the'")

    sentence = (
        "Far out in the uncharted backwaters of the "
        "unfashionable end of the western spiral arm of "
        "the Galaxy lies a small unregarded yellow sun."
    )

    test_word = most_common_word(sentence)

    print(f"Result is: {test_word}")

    # Test Case 1
    print("Test Case 1:")
    print("The result should 'in'")

    sentence = "The ships hung in the sky in much the same way that bricks don't."

    test_word = most_common_word(sentence)
    print(f"Result is: {test_word}")

    # Test Case 2
    print("Test Case 2:")
    print("The result should 'code'")

    sentence = "Its hard to code but I hope there are no bugs in this code."

    test_word = most_common_word(sentence)
    print(f"Result is: {test_word}")


main()
