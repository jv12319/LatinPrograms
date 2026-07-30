import LatinData as ll
# animals = {
#     "Dog": {
#         "color": "Brown",
#         "legs": 4
#     },
#     "Cat": {
#         "color": "Black",
#         "legs": 4
#     }
# }

# for animal, attributes in animals.items():
#     print("Animal: "+str(animal))
#     for attribute, answer in attributes.items():
#         print(str(attribute)+": "+str(answer))
        
#print(ll.third_declension["VirtUs"])
#print(f"{ll.first_conjugation["LaudAre"]["Present"]}")

# name = "Joseph"
# print(name[-3:])

verbs = {"LaudAre" :{
                "Principal Parts":["laudO", "laudAre", "laudAvI", "laudAtum"],
                "Conjugation" :"1st",
                "English Meaning" :["to praise", "to approve", "to extol"]
}
}

conjugations = {"indicative active" :{
    "1st" :{
        "Present" :{
            "1st pers sg":"O",
            "2nd pers sg":"As",
            "3rd pers sg":"at",
            "1st pers pl":"Amus",
            "2nd pers pl":"Atis",
            "3rd pers pl":"ant",
        }
    }
}}

print(f"{verbs['LaudAre']['Principal Parts'][0][:-1]+conjugations['indicative active']['1st']['Present']['3rd pers sg']}")

#def test_conj(verb_dict, conjugations_dict):
