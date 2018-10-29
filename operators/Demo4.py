
def sleep_in(weekday,vacation):
    if not weekday or vacation:
        return "You Can Sleep"
    else:
        return "Don't Sleep"

print(sleep_in(False,False))
print(sleep_in(True,False))
print(sleep_in(False,True))
print(sleep_in(True,True))
