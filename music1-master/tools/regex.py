def to_english(formatText):
    turkish_characters = ["ş",
                          "ç",
                          "ö",
                          "ğ",
                          "ü",
                          "ı",
                          "Ş",
                          "Ç",
                          "Ö",
                          "Ğ",
                          "Ü",
                          "İ"]

    english_characters = ["s",
                           "c",
                           "o",
                           "g",
                           "u",
                           "i",
                           "S",
                           "C",
                           "O",
                           "G",
                           "U",
                           "I"]
    text = formatText
    for i in range(12):
        text = text.replace(turkish_characters[i], english_characters[i])
    return text
