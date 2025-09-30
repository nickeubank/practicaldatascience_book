"""Debugger exercise."""


def split_string(string):
    """Given a string, split it into a list of 'words'."""
    # Remove last period
    string = string[:-1]

    # Split
    words = string.split()
    return words


def get_repeats(sentence_as_list):
    unique_words = []
    repeated_words = []
    for i in range(1, len(sentence_as_list)):
        # If we haven't see it before, put in
        # unique words list.
        word = sentence_as_list[i]
        if word not in unique_words:
            unique_words.append(word)

        # If we have seen it before (it's in
        # the unique words list),
        # it is a repeat and we put it in
        # repeated words if it isn't already there.
        elif word in unique_words and word not in repeated_words:
            repeated_words.append(word)
    return repeated_words


def get_repeated_words(sentence):
    """Get a list that contains one copy of each repeated word in sentence."""

    # Separate words in sentence
    sentence_as_list = split_string(sentence)

    # Figure out what is repeated
    repeated_words = get_repeats(sentence_as_list)
    return repeated_words


def main():

    # Test Case 0
    print("Test Case 0:")

    sentence = (
        "you should always be yourself unless you can "
        "be Batman then you should always be Batman."
    )

    print(f"The sentence is: {sentence}")
    print("The result should be  ['be', 'you', 'should', 'always', 'Batman']")

    test_word = get_repeated_words(sentence)
    print(f"Result is: {test_word}")

    # Test Case 1
    print("Test Case 1:")

    sentence = (
        "far out in the uncharted backwaters of the "
        "unfashionable far end of the western spiral arm of "
        "the Galaxy lies a small unregarded yellow sun."
    )

    print(f"The sentence is: {sentence}")
    print("The result should be  ['the', 'far', 'of']")

    test_words = get_repeated_words(sentence)

    print(f"Result is: {test_words}")


main()
