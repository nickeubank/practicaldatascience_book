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


def get_repeated_words(sentence):
    """Get a list that contains one copy of each repeated word in sentence."""

    # Separate words in sentence
    sentence_as_list = split_string(sentence)

    # Figure out what is repeated
    unique_words = []
    repeated_words = []
    for word in sentence_as_list:
        # If we haven't see it before, put in
        # unique words list.
        if word not in unique_words:
            unique_words.append(word)

        # If we have seen it before (it's in
        # the unique words list),
        # it is a repeat and we put it in
        # repeated words if it isn't already there.
        elif word in unique_words word not in repeated_words:
            repeated_words.append(word)

    return repeated_words


def main():

    # Test Case 0
    print("Test Case 0:")

    sentence = (
        "Far out in the uncharted backwaters of the "
        "unfashionable end of the western spiral arm of "
        "the Galaxy lies a small unregarded yellow sun."
    )

    print(f"The sentence is: {sentence}")
    print("The result should be  ['the', 'of']")

    test_words = get_repeated_words(sentence)

    print(f"Result is: {test_words}")

    # Test Case 1
    print("Test Case 1:")

    sentence = (
        "You should always be yourself unless you can "
        "be Batman then you should always be Batman."
    )

    print(f"The sentence is: {sentence}")
    print("The result should be  ['be', 'you', 'should', 'always', 'Batman']")

    test_word = get_repeated_words(sentence)
    print(f"Result is: {test_word}")


main()
