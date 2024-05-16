def str_upper(word):
    '''Функция принимает строку и возвращает исходною строку преобразованную в заглавные буквы'''
    return word.upper()

def words_str(words):
    '''Функция принимает строку и возвращает исходнуб строку,
       в которой все слова с заглавной буквы'''
    return ' '.join([word.title() for word in words.split()])