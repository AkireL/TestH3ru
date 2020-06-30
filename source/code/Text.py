"""
    
    
    @author Erika Leonor Basurto Munguia <iamdleonor@gmail.com>
    @version 1.0.0
"""
class Text:
        
    def getWords(self, text):   
        if(len(text) <= 0):
            raise Exception('Empty string!!')
        else:
            return text.split()
        


