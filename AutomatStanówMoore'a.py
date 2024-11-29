# 5. Napisac obiektowo program, ktory realizuje automat stanow (np. Mealy'ego albo Moore'a),
# czyli nalezy stworzyc odpowiednie klasy z funkcjami, a nastepnie z nich
# utworzyc konkretna przykladowe instancje

# zalezny tylko od stanu
class MooreState:
    def __init__(self, name, output_value):
        self.name = name
        self.output_value = output_value  # Stałe wyjście dla tego stanu


class MooreMachine:
    def __init__(self):
        self.states = {}  # słownik stanów
        self.current_state = None
        self.transitions = {}  # przejscia

    def add_state(self, state):
        self.states[state.name] = state

    def add_transition(self, from_state, input_value, to_state):
        """ dodaje pzrzejscie z jednego stanu do drugiego """
        if from_state not in self.transitions:
            self.transitions[from_state] = {}
        self.transitions[from_state][input_value] = to_state

    def set_initial_state(self, state_name):
        """ ustawienie stanu poczatkowego automatu """
        self.current_state = self.states[state_name]

    def get_output(self):
        """ zwraca stan wyjscia jesli mamy jakis stan na wejsciu """
        if self.current_state:
            return self.current_state.output_value
        return None

    def transition(self, input_value):
        """ zmienia stan na podstawie tego co mamy na wejściu """
        if self.current_state and input_value in self.transitions[self.current_state.name]:
            next_state_name = self.transitions[self.current_state.name][input_value]
            self.current_state = self.states[next_state_name]

    # łatwe wypisanie funkcji
    def __str__(self):
        return f"Current State: {self.current_state.name}"


# przykładowy automat Moore'a

# tworzenie stanów
s1 = MooreState("S1", "A")
s2 = MooreState("S2", "B")
s3 = MooreState("S3", "C")

# tworzenie automatu
moore_machine = MooreMachine()
moore_machine.add_state(s1)
moore_machine.add_state(s2)
moore_machine.add_state(s3)
moore_machine.add_transition("S1", 0, "S3")
moore_machine.add_transition("S1", 1, "S2")
moore_machine.add_transition("S2", 0, "S1")
moore_machine.add_transition("S2", 1, "S3")
moore_machine.add_transition("S3", 0, "S1")
moore_machine.add_transition("S3", 1, "S2")


moore_machine.set_initial_state("S1")

# testowanie automatu moore'a
print(moore_machine)  # najpierw mamy S1
print(moore_machine.get_output())  # na wyjsciu A
moore_machine.transition(0)  # przejscie do S3
print(moore_machine)  # stan S3
print(moore_machine.get_output())  # na wyjsciu C
moore_machine.transition(1) # przejscie do S2
print(moore_machine) # stan S2
print(moore_machine.get_output()) # na wyjsciu B
