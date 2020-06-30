
"""
    @author Erika Leonor Basurto Munguia <iamdleonor@gmail.com>
    @version 1.0.0
"""
class Translate:
    def __init__(self):
        """
            Dictionary chars Heuroglon and Spanish
            {
                ...
                <charHeruglon>, <charSpanish>
                ...
            }
        """
        self.alphabetDictionary = {
                            's': 'a',
                            'x': 'b',
                            'o': 'c',
                            'c': 'd',
                            'q': 'f',
                            'n': 'g',
                            'm': 'h',
                            'w': 'i',
                            'p': 'j',
                            'f': 'k',
                            'y': 'l',
                            'h': 'm',
                            'e': 'n',
                            'l': 'o',
                            'j': 'p',
                            'r': 'q',
                            'd': 'r',
                            'g': 's',
                            'u': 't',
                            'i': 'v' 
                            }

    """
        Convert a Heruglon word to Spanish word
        
        @author Erika Leonor Basurto Munguia <iamdleonor@gmail.com>
        @version 1.0.0
    """
    def do(self, word):
        tokens = list(word)
        wordMyAlphabet = ""
        for character in tokens:
            wordMyAlphabet += self.alphabetDictionary[character]
        return wordMyAlphabet
