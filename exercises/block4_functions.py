# Block 4 — Functions: turn the port classifier into reusable functions
# Run: python exercises/block4_functions.py
# You MAY look at block3_conditions.py — reusing your own code is the point.

# Your plan (3-5 lines in plain English) goes here FIRST:
#get code from block3_conditions.py
#define functions
#organize code within defined functions


def classify_port(text):
    port_text = text.strip()
    if not port_text.isdigit():
        return(f"Invalid: '{port_text}' is not a number")
    else:
        port = int(port_text)
    if port == 0 or port > 65535:
        return(f"Invalid: {port} is out of range")
    elif port >= 1 and port <=1023:
        return(f"Port {port}: well-known")
    elif port >= 1024 and port <= 49151:
        return(f"Port {port}: registered")
    else:
        return(f"Port {port}: dynamic")


def service_name(service):
    if service == 22:
        return(f"SSH")
    elif service == 80:
        return(f"HTTP")
    elif service == 443:
        return(f"HTTPS")
    elif service > 0 and service < 65536:
        return(f"unknown")
    else:
        return(f"Invalid: '{service}' is not a number")
            
print(classify_port("443"))
print(classify_port("8080"))
print(classify_port("65535"))
print(classify_port("0"))
print(classify_port("ssh"))
print(service_name(22))
print(service_name(443))
print(service_name(25))
print(classify_port("22").upper())