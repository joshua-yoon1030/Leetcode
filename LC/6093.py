class TextEditor(object):

    def __init__(self):
        self.left = []
        self.right = []
        

    def addText(self, text):
        """
        :type text: str
        :rtype: None
        """
        self.left += list(text)
      

    def deleteText(self, k):
        """
        :type k: int
        :rtype: int
        """
        if len(self.left) < k:
            length = len(self.left)
            self.left = []
            return length
        else:
            self.left = self.left[:len(self.left) - k]
            return k
        

    def cursorLeft(self, k):
        """
        :type k: int
        :rtype: str
        """
        if len(self.left) < k:
            self.right = self.left + self.right
            self.left = []
            return ""
        else:
            self.right = self.left[len(self.left) - k:] + self.right
            self.left = self.left[:len(self.left) - k]
            if len(self.left) <= 10:
                return "".join(str(e) for e in self.left)
            else:
                return "".join(str(e) for e in self.left[len(self.left) - 10:])
        

    def cursorRight(self, k):
        """
        :type k: int
        :rtype: str
        """
        if(len(self.right))< k:
            self.left = self.left + self.right
            self.right = []
        else:
            self.left = self.left + self.right[:k]
            self.right = self.right[k:]
        if len(self.left) <= 10:
                return "".join(str(e) for e in self.left)
        else:
            return "".join(str(e) for e in self.left[len(self.left) - 10:])
        
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
print(str(list("abade")))