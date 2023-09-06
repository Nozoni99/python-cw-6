# write your code here
person={
    "name":"Noor",
    "age":17 ,
    "hobbies": ["Reading","Cooking","Watching TV","Writing"]

       }

print(person["name"])
print(person["age"])

################################################################

person["age"]=18
person["country"]="Egypt"

print(person)

print(len(person))

################################################################

person["hobbies"].append("Singing")

def check_hobbies(person):
    if len(person["hobbies"]) > 3:
        print("WOW your are amazing !!!")
    else:
        print("You better start new hobbies .")

check_hobbies(person) 
    





