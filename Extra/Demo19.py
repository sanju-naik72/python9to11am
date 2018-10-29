

from firebase import firebase as fab

fb = fab.FirebaseApplication("https://mynewprojectclass.firebaseio.com/student_details",None)
d = fb.get("student_details",None)
for x in d:
    print(x,d[x])