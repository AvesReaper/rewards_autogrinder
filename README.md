MOTIVATION:

    - So ever heard of rewards program ?
    - If yes then you know you have to use edge browser in order to earn points.
    - But you dont prefer to use edge like me ? But still want to grind those points to claim those sweet giftcards?
    - WELL I GOT YOU BRO :)

WHAT IT DOES?

    - Simple we use keystroke automation!!! i.e. Programmatically we send in keyboard inputs.
    - So each for each search we do we gain points. I just want the points but dont prefer to use this browser.
    - So at a stretch im just gonna claim all the point I can gain per day.

HOW TO USE:

    PREREQUISITES:
        - Need a Microsoft account signed up for rewards program.
        - Microsoft edge installed.
    STEPS:
        - Go to chatgpt/ any AI of your choice. Type in the following: 
            "GIVE ME A PYTHON LIST OF STRING. THESE SEARCH PHRASES(STRINGS) MUSTN'T BE OF SAME TOPIC.THESE STRINGS MUST ATLEAST HAVE 3 WORDS. NUMBER OF SUCH STRINGS MUST BE 30."
        - Copy that list and replace "search_strings" in code.
        - Close all other window/application in foreground. Have edge alone open.
        - Open a shell and run this .py file.
        - Wait till the program ends.

+================================[DEV NOTES]=================================+

ITERATION 1:

    - My naive approach, involved just taking a list of strings, which needs to be replaced on a daily basis.
    - Used pynput library to mimic the required keystrokes.
    - Had to introduce a time delay between each search, cause sometimes edge doesnt award you points if you do quick searches.

+=========================================================================+

