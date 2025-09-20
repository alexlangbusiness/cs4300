from task6 import countWords

def test_word_count_file():

    filename = "task6_read_me.txt"  
    word_count = countWords(filename)  
    assert word_count == 127
