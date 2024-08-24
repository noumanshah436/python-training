
def ReverseAlphabetsOfWordsInASentence(sen):
    single_word = ''
    result = ''
    for ch in sen:
        if ch == ' ':
            result = single_word[::-1] + result
            result += ' '
            single_word = ''
        else:
            single_word += ch
    result = single_word[::-1] + result  # reverse the last word
    print(result)
    return result


sen = "my name is ali"
ReverseAlphabetsOfWordsInASentence(sen)
