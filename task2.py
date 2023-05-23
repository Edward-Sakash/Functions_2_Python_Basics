"""Task 2
Keep the previous code and define now a global variable named default_settings as a dictionary with a key title, then create a function named get_title that takes one argument as a dictionary that defaults to default_settings and returns the content of the key title in the given dictionary.

Use this test case:

print(get_title(settings))
print(get_title())
change_site_title("A new fancy title")
print(get_title(settings))
print(get_title())
Your result should look like this:
My original title
My original title
A new fancy title
My original title"""


# Solution 1
# Define the global variable `settings` as a dictionary with the initial title
settings = {'title': 'My original title'}

# Function to change the site title
def change_site_title(new_title):
    # Access the global variable `settings`
    global settings
    # Update the value of the 'title' key in `settings` with the new title
    settings['title'] = new_title

# Print the initial value of `settings`
#print(settings)

# Call the function to change the site title
change_site_title("A new fancy title")

# Print the updated value of `settings`
#print(settings)


# Task 2
# Define the global variable `default_settings` as a dictionary with a key 'title'
default_settings = {'title': 'My original title'}

# Function to get the title from a given dictionary
def get_title(settings=default_settings):
    # Retrieve the value of the 'title' key from the provided dictionary
    return settings['title']

# Print the title from the `settings` dictionary
print(get_title(settings))

# Print the title using the `default_settings` dictionary
print(get_title())

# Change the site title
change_site_title("A new fancy title")

# Print the updated title from the `settings` dictionary
print(get_title(settings))

# Print the title using the `default_settings` dictionary
print(get_title())
