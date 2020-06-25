class Text:
        
    def wordInText(self, text):   
        if(len(text) <= 0):
            raise Exception('spam')
        else:
            return text.split()
        

t = Text()
try:
    print(t.wordInText("gola"))
except Exception as error:
    print(error)

