from random import randint

sentences = [
    {
        "name": "Czetry osiemnastki jeden",
        "category": "Music",
        "level": 1,
        "used": False
    },
    {
        "name": "Czetry osiemnastki dwa",
        "category": "Music",
        "level": 1,
        "used": False
    },
    {
        "name": "Czetry osiemnastki trzy",
        "category": "Music",
        "level": 1,
        "used": False
    },

]


def get_random_sentence():
    not_used_sentences = [sentence for sentence in sentences if not sentence["used"]]
    sentence = not_used_sentences[randint(0, len(sentences) - 1)]

    sentence["used"] = True
    return sentence


def check_letter(sentence, letter):
    counter = 0
    special_char = [" ", "?", "!", ",", "."]

    for char in sentence:
        if char.lower() == letter.lower() and letter not in special_char:
            counter += 1

    return counter


# s = get_random_sentence()["name"]
# print(check_letter(s, 'e'))


def show_sentence(sentence):
    converted_sentence = "".join([u"\u2593" if letter == " " else "_" for letter in sentence])
    print(converted_sentence)


s = get_random_sentence()["name"]
show_sentence(s)

