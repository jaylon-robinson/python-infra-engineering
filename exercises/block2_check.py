# Block 2 cold check — Strings: parse a failed-login log line
# Don't look at block2_strings.py while doing this.
#
# OBJECTIVE: Pull clean values out of one messy auth-log line.
#
# The raw line is already written for you below:
#   raw_line = "  FAILED user=Admin src=203.0.113.45 port=2222  \n"
#
# REQUIREMENTS (build every value FROM raw_line — no typing answers in):
# 1. line      = raw_line with the outer spaces/newline removed
# 2. Split line on " " (one space) into its 4 words
# 3. status    = the 1st word, lowercased                      -> failed
# 4. user      = the text AFTER "=" in the 2nd word, lowercased -> admin
# 5. src_ip    = the text AFTER "=" in the 3rd word            -> 203.0.113.45
# 6. port_text = the text AFTER "=" in the 4th word; port = it as an int
# 7. Print the report below with f-strings
#
# Hint: "user=Admin" is a string too. How did you get the prefix out of "10.0.0.1/24"?
#
# EXPECTED OUTPUT:
# Status: failed
# User: admin
# Source IP: 203.0.113.45
# Source last octet: 45
# Port: 2222
# Port is digits: True
#
# TEST CASE 2: change ONLY raw_line to "FAILED user=ROOT src=10.9.8.7 port=22"
# Expected: failed / root / 10.9.8.7 / 7 / 22 / True
#
# COMPLETION: both test cases correct, 6 output lines, no traceback,
# nothing edited except raw_line.
#
# Run: python exercises/block2_check.py

raw_line = "  FAILED user=Admin src=203.0.113.45 port=2222  \n"

