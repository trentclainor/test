#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def is_balanced(text):
    """checking brackets is correct"""
    opening, closing = "([{", ")]}"
    stack = []
    for character in text:
        if character in opening:
            # if opening bracket add to stack
            stack.append(opening.index(character))
        elif character in closing:
            if stack and stack[-1] == closing.index(character):
                # if last bracket in stack closing remove last item from stack
                stack.pop()
            else:
                # unbalanced (no corresponding opening bracket) or
                # unmatched (different type) closing bracket
                return False
    # no unbalanced brackets
    return (not stack)


if __name__ == '__main__':
    try:
        text = input("Please input something: ")
        print("Input is {0}".format(
            "valid" if is_balanced(text) else "invalid"))
    except KeyboardInterrupt:
        print("Import data interrupted", file=sys.stderr)
 