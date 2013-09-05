#c:\python33\python.exe
import os, sys
import unittest

class Node:
    thing = None
    question = None
    y = None
    n = None

def get_what_thing_was_human():
    return input("What the thing was?")

def get_new_question_human(thing):
    return input("Give us a question that is true for {}".format(thing))

def ask_human_yn(question):
    return input(question)

def iteration(next, ask_yn, get_what_thing_was, get_new_question):
    while True:
        node = next

        if node.thing:
            if thing_correct(node.thing):
                break
            else:
                other_thing = get_what_thing_was()
                new_question = get_new_question(other_thing)

                new_yes_node = Node()
                new_no_node = Node()

                new_yes_node.thing = node.thing
                new_no_node.thing = other_thing
                node.question = new_question
                node.thing = None

                node.y = new_yes_node
                node.n = new_no_node

        elif node.question:

            answer = ask_yn(root.question)
            if answer == "Y":
                next = node.y
            else:
                next = node.n
        else:
            root.thing = "Cat"

def run():
    root = Node()
    while True:
        next = root
        iteration(next, ask_human_yn, get_what_thing_was, get_new_question)

class Test(unittest.TestCase):

    def test_one_iter(self):
        root = Node()
        iteration(root, lambda: 'N', lambda x: 'Dog', lambda x: 'Does it bark?')

def test():
  unittest.main ()

def main(type="run"):
    if type == "test":
        test()
    else:
        run()

if __name__ == '__main__':
    main(*sys.argv[1:])
