# name = ""
# sender= ""
#
import os
# members_list = []

with open("..\\Members_list\\list.txt", mode="r") as data:
    members_list = data.readlines()

print(members_list)

for members in members_list:
    stripped_members = members.strip("\n")
    print(stripped_members)

def print_letter(name, sender):
    with open("..\\letter_body\\letter_content.py")


# def create_letter():
#     for members in members_list:
#         stripped_members = members.strip("\n")
#         with open(f"..\\result\\{stripped_members}.txt", mode="w") as invite:
#             invite.write(print_letter(stripped_members, "Vadivel"))
#
#
# create_letter()
