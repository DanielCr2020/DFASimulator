import random,string

def randomString(length):
    return "".join(random.choices(string.ascii_lowercase[:8],k=length))

class DFASimulator:
    def __init__(self,DFA,inputString):
        self.DFA=DFA
        self.inputString=inputString

    def processDFA(self,DFA,inputString):
        curr=inputString[0]
        currState=list(DFA.keys())[0]
        for char in inputString:
            curr=DFA[currState][char]
            oldState=currState
            currState=curr
            print(f'{oldState}[{char}] -> {currState}')
        if DFA[currState].get('accept')==True:
            print("String was accepted")
        else:
            print("String was rejected")
        
if __name__=='__main__':
    machine = {
    'q1': {
        'a': 'q2',
        'b': 'q3',
        'c': 'q4',
        'd': 'q5',
        'e': 'q6',
        'f': 'q7',
        'g': 'q8',
        'h': 'q9'
    },
    'q2': {
        'a': 'q3',
        'b': 'q4',
        'c': 'q5',
        'd': 'q6',
        'e': 'q7',
        'f': 'q8',
        'g': 'q9',
        'h': 'q1'
    },
    'q3': {
        'a': 'q4',
        'b': 'q5',
        'c': 'q6',
        'd': 'q7',
        'e': 'q8',
        'f': 'q9',
        'g': 'q1',
        'h': 'q2'
    },
    'q4': {
        'a': 'q5',
        'b': 'q6',
        'c': 'q7',
        'd': 'q8',
        'e': 'q9',
        'f': 'q1',
        'g': 'q2',
        'h': 'q3'
    },
    'q5': {
        'a': 'q6',
        'b': 'q7',
        'c': 'q8',
        'd': 'q9',
        'e': 'q1',
        'f': 'q2',
        'g': 'q3',
        'h': 'q4'
    },
    'q6': {
        'a': 'q7',
        'b': 'q8',
        'c': 'q9',
        'd': 'q1',
        'e': 'q2',
        'f': 'q3',
        'g': 'q4',
        'h': 'q5'
    },
    'q7': {
        'a': 'q8',
        'b': 'q9',
        'c': 'q1',
        'd': 'q2',
        'e': 'q3',
        'f': 'q4',
        'g': 'q5',
        'h': 'q6'
    },
    'q8': {
        'a': 'q9',
        'b': 'q1',
        'c': 'q2',
        'd': 'q3',
        'e': 'q4',
        'f': 'q5',
        'g': 'q6',
        'h': 'q7',
        "accept":True
    },
    'q9': {
        'a': 'q1',
        'b': 'q2',
        'c': 'q3',
        'd': 'q4',
        'e': 'q5',
        'f': 'q6',
        'g': 'q7',
        'h': 'q8'
    }
    }
    inputString=input("Input a string:")
    print(inputString)
    dfa=DFASimulator(machine,inputString)
    dfa.processDFA(machine,inputString)
