import string

def statistic_text (file_name: str):
    """
    Высчитывает статистику текстового файла: число строк,
    число слов, число символов, число символов без пробелов, число символов без знаков препинания.
    """
    num_line = 0
    num_words = 0
    num_symbols = 0
    num_symbols_no_spaces = 0
    num_symbols_no_punctuation = 0
    num_sentences = 0
    punctuation = string.punctuation + "«»"

    with open(file_name + '.txt', "r", encoding="utf-8") as file:
        for line in file:
            num_line += 1

            words = line.split()
            num_words += len(words)

            num_symbols += len(line)
            num_symbols_no_spaces += len(line.replace(" ", ""))

            num_symbols_no_punctuation += len(line.translate(str.maketrans('', '', string.punctuation)))

            for char in line:
                if char in ".!?":
                    num_sentences += 1

    print(f"Число строк: {num_line}")
    print(f"Число слов: {num_words}")
    print(f"Число символов: {num_symbols}")
    print(f"Число символов без пробелов: {num_symbols_no_spaces}")
    print(f"Число символов без знаков препинания: {num_symbols_no_punctuation}")
    print(f"Число предложений: {num_sentences}")




file_name1 ='Томас_Манн'
file_name2 = 'коротыш'
statistic_text (file_name1)
