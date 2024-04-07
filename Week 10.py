# Week 10 Homeword

# Problem 10 in Section 11.22

# Replace Function
def replace(s, old, new):
    old_string = s.split(old)
    new_string = new.join(old_string)
    return print(new_string)

# Testing
replace("Mississippi", "i", "I")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
replace(s, "om", "am")
    
replace(s, "o", "a")
    
 


