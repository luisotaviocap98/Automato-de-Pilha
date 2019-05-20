import pytest

from turing.instance import Instance
from turing.tape import Tape
from turing.transition import Transition

def test_new_instance():
    tape1 = Tape("B", ['a', 'b'], ['b', 'b'])
    tape2 = Tape("B", ['x', 'y', 'z'], ['x', 'x'])
    tapes = [tape1, tape2]
    instance = Instance('A', tapes)
    assert instance.current_state == 'A'
    assert instance.tapes is not tapes 

def test_is_transition_valid_with_valid_transition():
    transition = Transition('A', 'B')
    transition.add_tape_part('x', 'y', 'L')
    transition.add_tape_part('y', 'x', 'R')
    tape1 = Tape("B", ['x', 'y'], ['x', 'y'])
    tape2 = Tape("B", ['x', 'y'], ['y', 'x'])
    tapes = [tape1, tape2]
    instance = Instance('A', tapes)
    assert instance.is_transition_valid(transition)

def test_is_transition_valid_with_invalid_transition():
    transition = Transition('A', 'B')
    transition.add_tape_part('x', 'y', 'L')
    transition.add_tape_part('y', 'x', 'R')
    tape1 = Tape("B", ['x', 'y'], ['x', 'y'])
    tape2 = Tape("B", ['x', 'y'], ['x', 'x'])
    tapes = [tape1, tape2]
    instance = Instance('A', tapes)
    assert not instance.is_transition_valid(transition)
            
def test_get_valid_transitions():
    transition1 = Transition('A', 'B')
    transition1.add_tape_part('x', 'y', 'L')
    transition1.add_tape_part('y', 'x', 'R')
    transition2 = Transition('A', 'B')
    transition2.add_tape_part('x', 'y', 'L')
    transition2.add_tape_part('x', 'x', 'R')
    transitions = [transition1, transition2]
    tape1 = Tape("B", ['x', 'y'], ['x', 'y'])
    tape2 = Tape("B", ['x', 'y'], ['y', 'x'])
    tapes = [tape1, tape2]
    instance = Instance('A', tapes)
    valid_transitions = instance.get_valid_transitions(transitions)
    assert transition1 in valid_transitions
    assert transition2 not in valid_transitions
    
def test_apply_transition_valid_transition():
    transition = Transition('A', 'B')
    transition.add_tape_part('a', 'b', 'L')
    transition.add_tape_part('x', 'y', 'R')
    tape1 = Tape("B", ['a', 'b', 'c'], ['a', 'c'])
    tape2 = Tape("B", ['x', 'y', 'z'], ['x', 'z'])
    tapes = [tape1, tape2]
    instance = Instance('A', tapes)
    new_instance = instance.apply_transition(transition)
    assert new_instance.current_state == 'B'
    assert new_instance.tapes[0].content == ['B', 'b', 'c']
    assert new_instance.tapes[0].get_content() == 'B'
    assert new_instance.tapes[1].content == ['y', 'z']
    assert new_instance.tapes[1].get_content() == 'z'
    
def test_apply_transition_invalid_transition():
    transition = Transition('A', 'B')
    transition.add_tape_part('a', 'b', 'L')
    transition.add_tape_part('x', 'y', 'R')
    tape1 = Tape("B", ['a', 'b', 'c'], ['a', 'c'])
    tape2 = Tape("B", ['x', 'y', 'z'], ['z', 'z'])
    tapes = [tape1, tape2]
    instance = Instance('A', tapes)
    new_instance = instance.apply_transition(transition)
    assert new_instance == None
