#Task 6 test file
#Double checks to make sure that the expected number of words in the file is there 
from task6 import countWords

def test_word_count_file():

    filename = "task6_read_me.txt"  
    word_count = countWords(filename)  
    assert word_count == 127
