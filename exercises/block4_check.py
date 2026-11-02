# Block 4 cold check — login checks as functions
# Run: python exercises/block4_check.py
# Don't open block3_check.py or block4_functions.py while doing this.

# Your plan (what each function does, step by step) goes here FIRST:
# severity function takes given severity level and compares runs it through if elif and else statement until it finds something true
# priviliged function will be used to say whether current user is priviliged or not

def severity(failures_text):
    failures_strip = failures_text.strip()
    if not failures_strip.isdigit():
        return f"invalid"
    else:
        failures = int(failures_strip)
        if failures == 0:
            return f"ok"
        elif failures >= 1 and failures <= 4:
            return f"low"
        elif failures >= 5 and failures <= 9:
            return f"medium"
        else:
            return f"high"

def is_privileged(user):
    user_strip = user.strip().lower()
    if user_strip == "root" or user_strip == "admin":
        return True
    else:
        return False


print(severity("7"))
print(severity(" 12 "))
print(severity("0"))
print(severity("abc"))
print(is_privileged("Root"))
print(is_privileged(" admin "))
print(is_privileged("alice"))
level = severity("4")
print(f"Level: {level.upper()}")
if is_privileged("ADMIN") and severity("9") == "medium":
    print("ALERT")