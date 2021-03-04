

def collect_text():
    sentences = []
    entry = input("Insert some text with correct punctuation.")

    while entry is not "":       # loop for entering text until the user press Intro without characters
        entry = entry.strip()    # remove spaces before and after the text

        for character in entry:     # analyze letter by letter
            if character is "." or character is "?" or character is "!":   # main punctuation signs
                i = entry.index(character)                           # find the character's index
                sentences.append(entry[:i + 1].strip())                   # append the sentence to the list
                entry = entry[i + 1:]                             # remove appended sentence from the text

        entry = input("Do you wish to add more text? If not just press Intro")      # option to add another paragraph
        entry = entry.strip()

    return sentences          # return sentences' list


def collect_censored_words():

    censored_words = []
    print("Insert the words you want to censor.")       # instructions
    print("After each word press Intro. To finish press it leaving the entry empty. Max. 10 words.")

    for word in range(10):      # loop 10 times or until the user says so

        entry = input()         # new entry each time
        entry = entry.strip()

        if entry is "":         # break the loop when the entry is empty
            break

        censored_words.append(entry)    # gather forbidden words in a list

    return censored_words


def cut_sentence():
    sentences = collect_text()                  # collect text and list of censored words separately
    censored_words = collect_censored_words()

    for sentence in sentences:                  # analyze each sentence to check if contains a forbidden word
        for word in censored_words:
            if word in sentence:
                idx_sentence = sentences.index(sentence)    # if it does, find sentence index in the list
                sentences.remove(sentences[idx_sentence])   # and remove it

    complete_text = " ".join(sentences)         # join remaining sentences

    return complete_text


def display_text():
    full_text = cut_sentence()          # get the resulting text
    lines = []                          # the text will be split in lines, stored in a list
    new_line = False                    # says when it's time to break line

    for char_idx, character in enumerate(full_text):    # loop over the characters and their indexes

        if char_idx % 40 == 0 and char_idx != 0:        # every 40 characters, activate new line warning
            new_line = True

        if new_line and character == " ":          # it can't be done until a space it's found, though
            lines.append(full_text[:char_idx])     # append the new line to the list
            full_text = full_text[char_idx+1:]     # and remove it from the text
            new_line = False

        if len(full_text) < 40:                    # when the remaining text is les than 40 characters
            lines.append(full_text)                # append it as a new line, the last one
            break

    for line in lines:          # print it
        print(line)


display_text()
