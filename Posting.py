import json
class Posting:
    def __init__(self, inputDocID = None, freq = 0) -> None:
        self.docID = inputDocID
        self.freq = freq
        
    def get_docID(self):
        return self.docID
    
    def get_freq(self):
        return self.freq
        
    def increment_freq(self):
        self.freq += 1
    
    def set_docID(self, newDocID):
        self.docID = newDocID
        
    def __str__(self) -> str:
        return f"Posting(docID: {self.docID}, freq: {self.freq})"
    
    def __repr__(self) -> str:
        return f"(docID: {self.docID}, freq: {self.freq})"
    
    def to_json(self):
        # return json.dumps(dict(self), ensure_ascii=False)
        return json.dumps(self, default=lambda o: o.__dict__)