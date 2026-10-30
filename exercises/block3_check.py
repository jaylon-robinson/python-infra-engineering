# Block 3 cold check — how serious are these failed logins?
# Run: python exercises/block3_check.py
# Don't open block3_conditions.py while doing this.

raw_event = " user=Root failures=7 "

# Your plan (3-5 lines in plain English) goes here FIRST:
# Strip the text and split the text by " "
# Assign variable to list created through raw_event split
# Do another split on each variable assigned
# create some if states to get specfic printed text of severity by failures

event = raw_event.strip().split(" ")
user_txt = event[0].lower()
failures_txt = event[1]

user_split = user_txt.split("=")
failures_split = failures_txt.split("=")

user = user_split[1]
failures = failures_split[1]

if failures.isdigit():
    failures_int = int(failures)
    if failures_int == 0:
        print(f"OK: no failures for {user}")
    elif failures_int >= 1 and failures_int <= 4:
        print(f"Low: {failures_int} failures for {user}")
    elif failures_int >= 5 and failures_int <= 9:
        print(f"Medium: {failures_int} failures for {user}")
    else:
        print(f"High: {failures_int} failures for {user}")
    if (user == "root" or user == "admin") and failures_int >= 5:
        print(f"ALERT: privileged account {user}")
else:
    print(f"Invalid failure count: '{failures}'")
    


