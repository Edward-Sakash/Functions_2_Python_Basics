"""Task 4:
Create a new function named print_user_profile that will take 4 parameters:

gender: a String indicating the gender of the user. The values available should be male and female. The default value should be female.
first: a String with the first name of the user. The default value should be John if the gender is male but it should be Jane if the gender is female.
last: a String with the last name of the user. The default value should be Doe.
pictures: a List of strings with the name of the picture files. The default value should be an empty list.
This function will add a common header picture to all profiles and then it will print on screen the name of the person and its list of pictures (including the common header). Example:

The user {first} {last} has the following pictures:
common_header.png
{user_picture1.png}
{user_picture2.png}
If the user has no pictures it should print only the common_header.png file name.

Use this test cases:

test_data1 = {
    "gender": "male",
    "last": "Brown",
    "pictures": ["holidays1.png", "easter_grandma.png"]
}
test_data2 = {
    "first": "Alicia",
    "last": "Schmidt"
}
test_data3 = {
    "last": "Korkov",
    "pictures": ["sunset.png"]
}
print_user_profile(**test_data1)
print_user_profile(**test_data2)
print_user_profile(**test_data3)
print_user_profile(**test_data2)

Your result should look like this:
The user John Brown has the following pictures:
common_header.png
holidays1.png
easter_grandma.png
The user Alicia Schmidt has the following pictures:
common_header.png
The user Jane Korkov has the following pictures:
common_header.png
sunset.png
The user Alicia Schmidt has the following pictures:
common_header.png"""

# Solution
def print_user_profile(gender="female", first=None, last="Doe", pictures=[]):
    # Determine the first name based on gender and default value
    if first is None:
        first = "John" if gender == "male" else "Jane"

    # Add the common header picture to the pictures list
    pictures = ["common_header.png"] + pictures

    # Print the user's name and pictures
    print(f"The user {first} {last} has the following pictures:")
    for picture in pictures:
        print(picture)

# Test data
test_data1 = {
    "gender": "male",
    "last": "Brown",
    "pictures": ["holidays1.png", "easter_grandma.png"]
}
test_data2 = {
    "first": "Alicia",
    "last": "Schmidt"
}
test_data3 = {
    "last": "Korkov",
    "pictures": ["sunset.png"]
}

# Test cases
print_user_profile(**test_data1)
print_user_profile(**test_data2)
print_user_profile(**test_data3)
print_user_profile(**test_data2)
