import pytest

from turing.tape import Tape
from turing.transition import Transition
from turing.turing_machine import TuringMachine

class TestTuringMachine:
    def setup_method(self):
        """ setup any state tied to the execution of the given method in a
        class.  setup_method is invoked for every test method of a class.
        """
        states = ['q0', 'q1', 'q2', 'q3', 'q4']
        transitions = []
        transitions_description = [
            'q0 q0 a a R B a R B B S',
            'q0 q1 B B S B B L B B S',
            'q0 q2 b b R B B S B b R',
            'q1 q3 B B S B B S B B S',
            'q2 q2 b b R B B S B b R',
            'q2 q4 c c S B B L B B L',
            'q4 q4 c c R a a L b b L',
            'q4 q3 B B S B B S B B S'
        ]
        for description in transitions_description:
            splited_description = description.split()
            transition = Transition(splited_description[0], splited_description[1])
            for tape_part in zip(*(splited_description[2:][i::3] for i in range(3))):
                transition.add_tape_part(tape_part[0], tape_part[1], tape_part[2])
            transitions.append(transition)
        tapes = [
            Tape("B", ['a', 'b', 'c', 'B'], []),
            Tape("B", ['a', 'B'], []),
            Tape("B", ['b', 'B'], []),
        ]
        self.tm = TuringMachine(states, 'q0', ['q3'], 'B', transitions, tapes)
        
    
    def test_new_turing(self):
        assert self.tm.is_halted() == False
        assert self.tm.get_decision() == "Undefined"
    
    def test_restart(self):
        tapes = [
            Tape("B", ['a', 'b', 'c', 'B'], ['c', 'b', 'a']),
            Tape("B", ['a', 'B'], []),
            Tape("B", ['b', 'B'], []),
        ]
        self.tm.restart(tapes)
        assert len(self.tm.current_configurations) == 1
        assert self.tm.current_configurations[0].current_state == self.tm.initial_state
        assert self.tm.current_configurations[0].tapes == tapes
        assert self.tm.current_configurations[0].tapes[0].get_content() == 'c'
        assert self.tm.current_configurations[0].tapes[1].get_content() == 'B'
        assert self.tm.current_configurations[0].tapes[2].get_content() == 'B'
       
    def test_run_accept(self):
        tapes = [
            Tape("B", ['a', 'b', 'c', 'B'], ['a', 'b', 'c']),
            Tape("B", ['a', 'B'], []),
            Tape("B", ['b', 'B'], []),
        ]
        self.tm.restart(tapes)
        result = self.tm.run()
        assert result == True
        assert self.tm.get_decision() == "Accept"
        
    def test_run_reject(self):
        tapes = [
            Tape("B", ['a', 'b', 'c', 'B'], ['a', 'b']),
            Tape("B", ['a', 'B'], []),
            Tape("B", ['b', 'B'], []),
        ]
        self.tm.restart(tapes)
        result = self.tm.run()
        assert result == True
        assert self.tm.get_decision() == "Reject"
