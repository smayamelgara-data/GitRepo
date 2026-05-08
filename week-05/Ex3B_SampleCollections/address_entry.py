#Exercise 3B Address Entry 
#Lab 3

#Create dictionary 
contact_info = {
    "name": "Smaya",
    "address": "123 Branch St",
    "city": "Charlotte",
    "state": "NC",
    "zip": "28227"
}

#print formatted address 
print(f"""{contact_info["name"]}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}""")

#Remove name 
contact_info.pop("name")

#Create a full_name dictionary 
full_name = {
    "first name": "Smaya",
    "last name": "Melgara"
}

#Adding honorific using update()
full_name.update({"honorific":"Ms"})

#Using update() to add it to contact_info 
contact_info.update({"full_name": full_name})

#Printing updated information 
print(f"""{contact_info["full_name"]["honorific"]}. {contact_info["full_name"]["first name"]} {contact_info["full_name"]["last name"]}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}""")