# Week HW

# Problem 7 in 6.9

def to_sec(hours, minutes, seconds):
    total_secs = (hours * 3600) + (minutes * 60) + (seconds)
    return(total_secs)

# TESTING
import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass :
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.". format(linenum))
    print(msg)

def test_suite():
    test(to_sec(2,30,10) == 9010)
    test(to_sec(2, 0, 0) == 7200)
    test(to_sec(0,2,0) == 120)
    test(to_sec(0,0,42)==42)
    test(to_sec(0, -10, 10) == -590)
test_suite()
