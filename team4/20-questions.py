#!c:\python33\python.exe
import os, sys
import unittest


class Node:
    thing = None
    question = None
    y = None
    n = None

    def __repr__(self):
        return '({},{},{})'.format(self.thing, self.question, self.y)

def get_what_thing_was_human():
    return input("What the thing was? ")

def get_new_question_human(thing):
    return input("Give us a question that is true for {}: ".format(thing))

def ask_human_yn(question):
    return input(question).upper().startswith('Y')

def iteration(root, ask_yn, get_what_thing_was, get_new_question):
    next = root
    while True:
        node = next
        print("N", root, node)
        if node.thing:
            if ask_yn("Is it a %s?" % node.thing):
                raise SystemExit("Winner")
            else:
                other_thing = get_what_thing_was()
                new_question = get_new_question(other_thing)

                new_yes_node = Node()
                new_no_node = Node()

                new_no_node.thing = node.thing
                new_yes_node.thing = other_thing
                node.question = new_question
                node.thing = None

                node.y = new_yes_node
                node.n = new_no_node
                next = root
        elif node.question:

            if ask_yn(node.question):
                next = node.y
            else:
                next = node.n
        else:
            node.thing = "Cat"

def run():
    root = Node()
    while True:
        next = root
        iteration(next, ask_human_yn, get_what_thing_was_human, get_new_question_human)

class TestIterations(unittest.TestCase):

    def test_one_iter(self):
        root = Node()
        iteration(root, lambda x: 'N', lambda x: 'Dog', lambda x: 'Does it bark?')

def main(type="run"):
    if type == "test":
        unittest.main ()
    else:
        run()

if __name__ == '__main__':
    #main(sys.argv[1])
    run()
    #unittest.main ()
