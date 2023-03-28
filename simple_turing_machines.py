class TuringMachine:
    def __init__(self, transitions, input_string=' '):
        self.transitions = transitions
        self.position = 0
        self.tape = list(input_string)
        self.state = 's'

        if len(self.tape) == 0 : self.tape.append(' ')


    def step(self):
        symbolRead = self.tape[self.position]

        try:
            symbolWrite, move, self.state = self.transitions[(self.state, symbolRead)]
        except:
            return False
        self.tape[self.position] = symbolWrite

        if move == 'R':
            self.position += 1
            if len(self.tape) <= self.position:
                self.tape.append(' ')
        else:
            self.position -= 1
        return True


    def run(self, show=False):
        while self.step():
            if show: 
                print(self)    
        return "".join(self.tape).rstrip()


    def __str__(self):

       def head2str(i):
           if self.state and self.position == i:
               return self.state
           else:
               return ' '

       return ''.join([f'{self.tape[i]}, {head2str(i)}' for i in range(len(self.tape))])