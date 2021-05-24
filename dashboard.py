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
    sentence = sentences[randint(0, len(sentences) -1)]

    sentences["used"] = True
