# Block 3 — Conditions: what kind of port is this?
# Run: python exercises/block3_conditions.py

raw_port = "  8080 "

port_text = raw_port.strip()

if port_text.isdigit():
    port = int(port_text)
    if port == 0 or port > 65535:
        print(f"Invalid: {port} is out of range")
    elif port >= 1 and port <=1023:
        print(f"Port {port}: well-known")
    elif port >= 1024 and port <= 49151:
        print(f"Port {port}: registered")
    else:
        print(f"Port {port}: dynamic")
    if port == 22:
        print(f"Service: SSH")
    elif port == 80:
        print(f"Service: HTTP")
    elif port == 443:
        print(f"Service: HTTPS")
    elif port > 0 and port < 65536:
        print(f"Service: unknown")
else:
    print(f"Invalid: '{port_text}' is not a number")


# ===== STEP 2 of 4: two small fixes =====
#
# Step 1 works. Fix these two things, then run it again:
#
# 1. Rename porttxt to port_text. Python names put an underscore
#    between words. Tip: click on porttxt and press F2 to rename it
#    everywhere at once.
#
# 2. Put single quotes around the value in the Invalid message:
#      Invalid: 'ssh' is not a number
#
# Try it twice:
#   raw_port = "  443 "   ->  Valid number: 443
#   raw_port = "ssh"      ->  Invalid: 'ssh' is not a number
# Then set raw_port back to "  443 ".
