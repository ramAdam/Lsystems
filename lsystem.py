class Grammar:
    def __init__(self, axiom, rules):
        self.axiom = axiom
        self.rules = rules
        self.allstrs = []        
        self.initstr = self._applyrules(self.axiom, self.rules)
        self.allstrs.append(self.initstr)

    def _applyrules(self, txt, rules):
        text = txt
        for k, v in rules.items():
            text = text.replace(k, v)
            # print(text)
        return text


    def produce(self, num=2):
        """produce number of strings"""
        mstr = self.initstr
        for i in range(num -1):
            mstr = self._applyrules(mstr, self.rules)
            self.allstrs.append(mstr)
        return self.allstrs
    
