# Block 5 — Exceptions: parse values safely with try / except
# Run: python exercises/block5_exceptions.py
# Rule for this one: no .isdigit() — use try / except instead.

# Your plan (what each function does, step by step) goes here FIRST.
# Then tell your mentor "check plan" BEFORE writing any code.
# parse_latenncy should 

def parse_latency(text):
    try:
        return float(text.strip(" "))
    except ValueError:
        return None

def parse_prefix(text):
    try:
        address= (text.strip(" "))
        textblock = (address.split("/")[1])
        block = int(textblock)
        if block >= 0 and block <= 32:
            return block
        else:
            return None
    except (ValueError, IndexError):
        return None

print(parse_latency("12.5"))
print(parse_latency(" 8 "))
print(parse_latency("fast"))
print(parse_latency(""))
print(parse_prefix("10.0.0.1/24"))
print(parse_prefix(" 192.168.1.0/16 "))
print(parse_prefix("10.0.0.1"))
print(parse_prefix("10.0.0.1/abc"))
print(parse_prefix("10.0.0.1/33"))
print(parse_prefix("10.0.0.1/0"))
p = parse_prefix("10.0.0.1/8")
if p is None:
    print("bad")
else:
    print(f"Host bits: {32 - p}")
