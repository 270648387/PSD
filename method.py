class StringManipulator:
    def __init__(self,text):
        self.text = text

    def find_char(self,char):
        pos = self.text.find(char)
        return(f"Position: {pos}" if pos != -1 else "Character not found")
    
    def show_leng(self):
        return(f"Length:{len(self.text)}")

    def upper(self):
        return(f"Uppercase:{self.text.upper()}")
    
name = StringManipulator("example")

result = name.find_char('x')
leng = name.show_leng()
upper = name.upper()

print(result,leng,upper)

