# Block 1 cold check — values, types & variables
# Don't look at server_inventory.py while doing this.
#
# 1. vlan_text = "10"   (a string, as if typed by a user)
# 2. Make next_vlan equal to 11 as an int, built from vlan_text.
# 3. Print next_vlan and its type.
# 4. Make vlan_label equal to "VLAN10" by joining "VLAN" with vlan_text. Print it.
# 5. Create switch_up = True, then reassign it to False and print it.
#
# Expected output:
# 11
# <class 'int'>
# VLAN10
# False
#
# Run: python exercises/block1_check.py


vlan_text = "10"

next_vlan = int(vlan_text) + 1
vlan = "VLAN"
vlan_label = vlan + vlan_text
switch_up = True

print(next_vlan)
print(type(next_vlan))
print(vlan_label)

switch_up = False
print(switch_up)