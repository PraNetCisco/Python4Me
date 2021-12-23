# This program uses list of dictionaries "students"

contacts = {
    "number" : 4,
    "students" :
    [
        {"name":"Pradeep Sharma", "email":"psharma@test.com"},
        {"name":"Abhimanyu Sharma", "email":"asharma@test.com"},
        {"name":"Saroj Sharma", "email":"ssharma@test.com"},
        {"name":"Gia Sharma", "email":"gsharma@test.com"}
    ]
}

for student in contacts["students"]:
    print (student["email"])