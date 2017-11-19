#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def is_balanced(text):
    """checking bracrers is correct"""
    brackets = ""
    opening, closing = "([{", ")]}"
    # keep track of opening brackets types
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
        print(is_balanced(text))
    except KeyboardInterrupt:
        print("Import data interrupted", file=sys.stderr)
 