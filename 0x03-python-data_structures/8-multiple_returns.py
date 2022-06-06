#!/usr/bin/python3
def multiple_returns(sentence):
    if type(sentence) is not str:
        return
    if sentence == '' or sentence == ' ':
        return (len(sentence), None)
    return (len(sentence), sentence[0])
