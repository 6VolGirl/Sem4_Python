def head (file_name: str):
    """
    Выводит первые три строчки текстового файла.
    """
    with open(file_name + '.txt', 'r', encoding='utf-8') as file:
        for x in range(3):
            line = file.readline()
            if not len(line):
                print ("Less than 3 lines in file.")
                return
            print(line.rstrip())

def tail (file_name: str):
      """
      Выводит последние три строчки текстового файла.
      """
      with open(file_name + '.txt', 'r', encoding='utf-8') as file:
          buffer = []
          for line in file:
              buffer.append(line)
              if len(buffer) > 3:  # max размер 3, если больше, то удаляем первую строчку
                  buffer.pop(0)
          if len(buffer) < 3:
              print ("Less than 3 lines in file.")
          for line in buffer:
              print(line.rstrip())






file_name1 ='Томас_Манн'
file_name2 = 'коротыш'

head(file_name1)
tail(file_name1)