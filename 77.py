"""

Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints: Use list[index] notation to get a element from a list.

"""
sub = ["I", "You"]
verb = ["Play", "Love"]
object = ["Hockey","Football"]
for s in sub:
    for v in verb:
        for o in object:
            print("%s %s %s" % (s,v,o))
