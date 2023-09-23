import random
import json
import os
class vocabulary:
    def __init__(self):
        self.vocabulary = self._vocabulary()
        if os.name == 'nt':
            self.clear = "cls"
        else:
            self.clear = "clear"
        
    def _vocabulary(self):
        with open("vokabel.json", "r") as f:
            return json.loads(f.read())
    
    def start(self):
        while True:
            vocabulary = list(self.vocabulary)
            random.shuffle(vocabulary)
            mistakes = 0
            while len(vocabulary) != 0:
                vocable = random.choice(vocabulary)
                os.system(self.clear)
                if input(f"""Total vocabularies: {len(self.vocabulary)}\nVocabulary left: {len(vocabulary)}\nTotal mistakes: {mistakes}\n\nCurrent: {vocable[0]}\ninput: """) == vocable[-1]:
                    print(f"Correct answer: {vocable[-1]}")
                    vocabulary.remove(vocable)
                    input()
                    if len(vocabulary) == 0: break
                else:
                    print(f"Wrong answer. Correct answer: {vocable[-1]}")
                    mistakes += 1
                    input()
                
vocabulary().start()