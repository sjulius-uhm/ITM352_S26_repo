emotions = ("happy", "sad", "fear", "surprise")

#  Write code that uses a conditional expression 
# do not use an if-statement or ternary expression
# print “true” if the last element is “happy” and there are more than 3 elements
# or “false” if it is not.
result = "true" if emotions[-1] == "happy" and len(emotions) > 3 else "false"
print(result)

# Rewrite the code using an if-statement
if emotions[-1] == "happy" and len(emotions) > 3:
    print("true")
else:
    print("false")