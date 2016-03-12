fileA = sc.textFile("input/join1_FileA.txt")
fileA.collect()

# Out[]: [u'able,991', u'about,11', u'burger,15', u'actor,22']

fileB = sc.textFile("input/join1_FileB.txt")
fileB.collect()

#Out[29]:
#[u'Jan-01 able,5',
# u'Feb-02 about,3',
# u'Mar-03 about,8',
# u'Apr-04 able,13',
# u'Feb-22 actor,3',
# u'Feb-23 burger,5',
# u'Mar-08 burger,2',
# u'Dec-15 able,100']


#Mapper A
# input_example: line = "able,999"
def split_fileA(line):
    word, count = line.strip().split(',')
    return (word,int(count))

def test_splitA():
    pair = split_fileA("able, 999")
    pair == ("able", 999)

fileA_data = fileA.map(split_fileA)
fileA_data.collect()


#Mapper B
# input_example: line = "Jan-01 able,5"
def split_fileB(line):
    date_word, count_string = line.split(',')
    date, word = date_word.split()
    return (word, date + " " + count_string)

def test_splitB():
    pair = split_fileB("Jan-01 able,5")
    pair == ("able", "Jan-01 5")

fileB_data = fileB.map(split_fileB)
fileB_data.collect()


#Join
fileB_joined_fileA = fileB_data.join(fileA_data)
fileB_joined_fileA.collect()
