"""An example of how to represent a group of acquaintances in Python."""

# 'name','age', 'job', 'connection'

my_group = [{"name":"Jill","age":"26","job":"biologist","connections":["Zalikas's friend", "John's partner"]},
             {"name":"Zalika","age":"28","job":"artist","connections":["Jill's friend"]},
                {"name":"John","age":"27","job":"writer","connections":["Jill's partner"]},
                    {"name":"Nash","age":"34","job":"chef","connections":["John's cousin", "Zalika's landlord"]}]
#  including name, age, job, connection inside the dict
#connections = [Partner={},
#                    Friend={},
 #                       Landlord={},
 #                           cousin={}]
#attempt to make a dict of connections


#1) It allows if they specifies that he has no job in the specific section

#2) similar to Q1

#3) no it does not


import json

with open('friend_group.json', 'w') as fg:
    json.dump(my_group,fg)