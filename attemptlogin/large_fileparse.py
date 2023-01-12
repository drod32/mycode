#!/usr/bin/env python3

#fail counter
login_fail = 0

#parse keystone.common.wsgi and return number of failed logins
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

# loop over file
for line in keystone_file:

    # if this "fail pattern is seen on line
    if "- - - - -] Authorization failed" in line:
        login_fail += 1

print("The number of failed log in attempts is", login_fail)
keystone_file.close() # close the open file
