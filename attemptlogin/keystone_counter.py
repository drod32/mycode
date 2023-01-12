#!/usr/bin/env python3

#parse keystone.common.wsgi and return number of failed logins

login_fail = 0  #counter for fails

#open file for reading
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r")

# return th file to a list of lines in memory
keystone_file_lines = keystone_file.readlines()

#loop over the list of lines
for line in keystone_file_lines:
    #if this "fail pattern" appears in line...
    if "- - - - -] Authorization failed" in line:
        login_fail += 1 
print("The number of failed log in attempts is", login_fail)
keystone_file.close()
