import pytest

from turing.transition import Transition

def test_new_transition():
    transition = Transition('A', 'B')
    transition.add_tape_part('x', 'y', 'L')
    transition.add_tape_part('y', 'x', 'R')
    assert transition.current_state == 'A'
    assert transition.new_state == 'B'
    assert len(transition.tape_data) == 2
    assert transition.tape_data[0].current_tape_symbol == 'x'
    assert transition.tape_data[0].new_tape_symbol == 'y'
    assert transition.tape_data[0].direction == 'L'
    assert transition.tape_data[1].current_tape_symbol == 'y'
    assert transition.tape_data[1].new_tape_symbol == 'x'
    assert transition.tape_data[1].direction == 'R'
    
def test_match_state_ok():
    transition = Transition('A', 'B')
    transition.add_tape_part('x', 'y', 'L')
    transition.add_tape_part('y', 'x', 'R')
    assert transition.match_state('A') == True

def test_match_state_err():
    transition = Transition('A', 'B')
    transition.add_tape_part('x', 'y', 'L')
    transition.add_tape_part('y', 'x', 'R')
    assert transition.match_state('B') == False

def test_match_tape_symbol_no_tape_number():
    transition = Transition('A', 'B')
    transition.add_tape_part('x', 'y', 'L')
    transition.add_tape_part('y', 'x', 'R')
    assert transition.match_tape_symbol('x') == True
    assert transition.match_tape_symbol('y') == False

def test_match_tape_symbol_with_tape_number():
    transition = Transition('A', 'B')
    transition.add_tape_part('x', 'y', 'L')
    transition.add_tape_part('y', 'x', 'R')
    assert transition.match_tape_symbol('x', 0) == True
    assert transition.match_tape_symbol('y', 0) == False
    assert transition.match_tape_symbol('x', 1) == False
    assert transition.match_tape_symbol('y', 1) == True
    
def test_match_valid():
    transition = Transition('A', 'B')
    transition.add_tape_part('x', 'y', 'L')
    transition.add_tape_part('y', 'x', 'R')
    assert transition.match('A', ['x', 'y']) == True
    
def test_match_valid_state_invalid_tape_symbols():
    transition = Transition('A', 'B')
    transition.add_tape_part('x', 'y', 'L')
    transition.add_tape_part('y', 'x', 'R')
    assert transition.match('A', ['y', 'x']) == False
    
def test_match_invalid_state_valid_tape_symbols():
    transition = Transition('A', 'B')
    transition.add_tape_part('x', 'y', 'L')
    transition.add_tape_part('y', 'x', 'R')
    assert transition.match('B', ['x', 'y']) == False
    
def test_match_invalid_state_invalid_tape_symbols():
    transition = Transition('A', 'B')
    transition.add_tape_part('x', 'y', 'L')
    transition.add_tape_part('y', 'x', 'R')
    assert transition.match('B', ['y', 'x']) == False
    
def test_get_new_tape_symbol():
    transition = Transition('A', 'B')
    transition.add_tape_part('x', 'y', 'L')
    transition.add_tape_part('y', 'x', 'R')
    assert transition.get_new_tape_symbol(0) == 'y'
    assert transition.get_new_tape_symbol(1) == 'x'

def test_get_direction():
    transition = Transition('A', 'B')
    transition.add_tape_part('x', 'y', 'L')
    transition.add_tape_part('y', 'x', 'R')
    assert transition.get_direction(0) == 'L'
    assert transition.get_direction(1) == 'R'    
    
def test_new_tape_data():
    transition = Transition('A', 'B')
    transition.add_tape_part('x', 'y', 'L')
    transition.add_tape_part('y', 'x', 'R')
    new_tape_data = transition.get_new_tape_data()
    assert new_tape_data[0][0] == 'y'
    assert new_tape_data[0][1] == 'L'
    assert new_tape_data[1][0] == 'x'
    assert new_tape_data[1][1] == 'R'
        
    
