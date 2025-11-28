student1 = {
    "Name":"Rahul",
    "Age":16,
    "Grade":9,
    "Country":"India"
}
#Access Data
print(student1)
print(student1["Name"])

#Add Data
student1["Religion"] = "Hindu"

#Update Data
student1["Grade"] = 6
print(student1)

#Remove
student1.pop("Name")
print(student1)