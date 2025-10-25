class StringReverser:
    def __init__(self, text):
        self.__text = text   # private variable

    def get_reversed(self):
        # reverse the string word by word
        return " ".join(self.__text.split()[::-1])#split string whitespace


# Example
reverser = StringReverser("Hello World from Python")
print(reverser.get_reversed())   # Output: Python from World Hello
# take an input from use you can reverse it by this [::-1]