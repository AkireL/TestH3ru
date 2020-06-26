from Translate import Translate

"""
    
    
    @author Erika Leonor Basurto Munguia <iamdleonor@gmail.com>
    @version 1.0.0
""" 
class Order:
    def __init__(self):
        self.t = Translate()
        
    def prepare(self, listWord):
        arraydictWord = []
        for word in listWord: 
            translate_w = self.t.do(word)
            arraydictWord.append({'tw':translate_w,'w': word})
        return arraydictWord
    
    def do(self, arrayWords):
        sorted_activities = sorted(arrayWords, key=lambda x: x['tw'])
        result = list(map(lambda x: x['w'], sorted_activities))
        return (result)
