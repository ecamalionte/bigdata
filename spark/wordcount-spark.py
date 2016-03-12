#Mapper A
# input_example: line = "able,999"
def split_fileA(line):
    word, count = line.split(',')
    return (word,int(count))

def test_splitA():
    pair = split_fileA("able, 999")
    return pair == ("able", 999)


#Mapper B
# input_example: line = "Jan-01 able,5"
def split_fileB(line):
    date_word, count_string = line.split(',')
    date, word = date_word.split()
    return (word, date + " " + count_string)

def test_splitB():
    pair = split_fileB("Jan-01 able,5")
    return pair == ("able", "Jan-01 5")
