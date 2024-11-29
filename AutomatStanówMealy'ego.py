# 5. Napisac obiektowo program, ktory realizuje automat stanow (np. Mealy'ego albo Moore'a),
# czyli nalezy stworzyc odpowiednie klasy z funkcjami, a nastepnie z nich
# utworzyc konkretna przykladowe instancje

# automat mealy'ego - zalezny od stanu i wejscia
class MealyState:
    def __init__(self, name, output_function):
        self.name = name
        self.output_function = output_function  # funkcja wyjscia

class MealyMachine:
    def __init__(self):
        self.states = {}  # słownik stanów
        self.current_state = None  # bieżący stan
        self.transitions = {}  # przejście z jednego stanu do drugiego

    # dodaje stan
    def add_state(self, state):
        self.states[state.name] = state


    def add_transition(self, from_state, input_value, to_state):
        """dodaje przejscie miedzy stanami"""
        if from_state not in self.transitions: # jelsi nie ma przejscia dla tego from_state
            self.transitions[from_state] = {} # to je tworzymy
        self.transitions[from_state][input_value] = to_state
        # towrzymy klucz:wartosc ktory bedzie przechowywal przejscie dla danej wartosci


    def set_initial_state(self, state_name):
        """ustawia stan początkowy automatu"""
        self.current_state = self.states[state_name]


    def get_output(self, input_value):
        """ zwraca wyjście na podstawie bieżącego stanu oraz wejscia """
        if self.current_state:
            # zwraca wyjscie z uzyciem funkcji wejscia
            output = self.current_state.output_function(input_value)
            return output
        return None

    def transition(self, input_value):
        """ zmienia stan na podstawie wejścia """
        if self.current_state and input_value in self.transitions[self.current_state.name]:
            next_state_name = self.transitions[self.current_state.name][input_value]
            self.current_state = self.states[next_state_name]

    def __str__(self):
        return f"Current State: {self.current_state.name}"


# przykladowy automat mealy'ego

# funkcja wyjscia dla S1, przy 0 "A" przy 1 "B"
def s1_output(input_value):
    return "A" if input_value == 0 else "B"


# funkcja wyjscia dla stanu S2, przy 0 "C", przy 1 "D"
def s2_output(input_value):
    return "C" if input_value == 0 else "D"

# funckaj wyjscia dla stanu S3, przy 0 "B", przy 1 "C"
def s3_output(input_value):
    return "B" if input_value == 0 else "C"

# tworzymy stany z funkcjami wyjscia
s1 = MealyState("S1", s1_output)
s2 = MealyState("S2", s2_output)
s3 = MealyState("S3", s3_output)

# tworzymy automat z przejsciami
mealy_machine = MealyMachine()
mealy_machine.add_state(s1)
mealy_machine.add_state(s2)
mealy_machine.add_state(s3)
mealy_machine.add_transition("S1", 0, "S2")
mealy_machine.add_transition("S1", 1, "S1")
mealy_machine.add_transition("S2", 0, "S1")
mealy_machine.add_transition("S2", 1, "S3")
mealy_machine.add_transition("S3", 0, "S1")
mealy_machine.add_transition("S3", 1, "S2")

# stan inicjalizujacy na S1
mealy_machine.set_initial_state("S1")

# testowanie automatu
print(mealy_machine)  # stan S1
print(mealy_machine.get_output(0))  # wyjscie A
mealy_machine.transition(0)  # przechodzimy do S2
print(mealy_machine)  # stan S2
print(mealy_machine.get_output(1))  # wyjscie D
mealy_machine.transition(1) # przechodzimy do S3
print(mealy_machine) # stan S3
print(mealy_machine.get_output(1)) # wyjscie C
print(mealy_machine.get_output(0)) # wyjscie B
mealy_machine.transition(0) # przechoidzmy do S1
print(mealy_machine) # stan S1
