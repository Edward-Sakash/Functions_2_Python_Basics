"""Task 1
Define a global variable named settings as a dictionary with a key title that contains a string of your choice, then create a function named change_site_title that takes one argument of type String and assigns it to the key title in the global variable settings.

Use this test case:

print(settings)
change_site_title("A new fancy title")
print(settings)
Your result should look like this:
{'title': 'My original title'}
{'title': 'A new fancy title'}"""

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
print(settings)

# Call the function to change the site title
change_site_title("A new fancy title")

# Print the updated value of `settings`
print(settings)

print("___________________________________________________")

# Solution 2
def change_site_title(settings, new_title):
    # Create a new dictionary based on the input settings with the updated title
    updated_settings = dict(settings)
    updated_settings['title'] = new_title
    return updated_settings

# Define the initial settings dictionary
settings = {'title': 'My original title'}

# Print the initial value of `settings`
print(settings)

# Call the function to change the site title and update `settings`
settings = change_site_title(settings, "A new fancy title")

# Print the updated value of `settings`
print(settings)
