# Block 2 — Strings: parse a messy interface config line
#
# OBJECTIVE: Turn messy user input into clean values and print a report.
#
# Start with these two lines (already written for you below):
#   raw_address  = "   10.0.0.1/24  \n"
#   raw_hostname = "  Core-SW-01 "
#
# REQUIREMENTS (build every value FROM the raw variables — no typing answers in):
# 1. hostname    = raw_hostname cleaned of spaces AND lowercased
# 2. address     = raw_address cleaned of spaces/newline
# 3. Split address at "/" into ip_text (left piece) and prefix_text (right piece)
# 4. prefix      = prefix_text converted to an int
# 5. host_bits   = 32 minus prefix
# 6. first_octet = the first number of ip_text  (hint: split again, on ".")
# 7. Print this report using f-strings:
#
# EXPECTED OUTPUT:
# Host: core-sw-01
# IP: 10.0.0.1
# Prefix: /24
# Host bits: 8
# First octet: 10
# IP length: 8
# Prefix is digits: True
#
# TEST CASE 2: change ONLY raw_address to "  192.168.50.7/16 " and run again.
# Expected: IP: 192.168.50.7 / Prefix: /16 / Host bits: 16 / First octet: 192 / IP length: 12
# Then change it back.
#
# COMPLETION: both test cases correct without editing anything but raw_address.
#
# Run: python exercises/block2_strings.py

raw_address = "   10.0.0.1/24  \n"
raw_hostname = "  Core-SW-01 "

hostname = raw_hostname.strip().lower()
address = raw_address.strip()
prefix_text = address[1].split("/")
ip_text = prefix_text[0]
prefix = int(prefix_text)
host_bits = 32 - prefix
octet = ip_text.split(".")
first_octet = octet[0]
last_octet = octet[3]



print(f"Host: {hostname}")
print(f"IP: {prefix_text[0]}")
print(f"Prefix: /{prefix}")
print(f"Host bits: {host_bits}")
print(f"First octet: {first_octet}")
print(f"IP length: {len(prefix_text[0])}")
print(f"Prefix is digits: {prefix_text[1].isdigit()}")






