#import task1 script
import task1

#Verify expected output
#Reads what was printed during function call, and verifies outout
def test(capsys):
    
    task1.main()

    capturedOutput = capsys.readouterr()

    assert capturedOutput.out.strip() == "Hello World"

