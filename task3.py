"""Task 3: Default and non default arguments combined
Add a key pages to your previous settings and default_settings dictionaries.

Now, define two functions named get_pages and add_page. They will both have a parameter settings that will default to default_settings.

The function get_pages will simply return the list stored in the key pages of the given settings dictionary.

The function add_page will have an additional positional argument that will be the page as a dictionary. The function will append this argument to the pages key of the given settings dictionary.

Use this test case:

home = {"title": "Home", "path": "/"}
add_page(home)
print(get_pages())
print(get_pages(settings))
about = {"title": "About", "path": "/about/"}
add_page(about, settings)
print(get_pages())
print(get_pages(settings))
Your result should look like this:
[{'title': 'Home', 'path': '/'}]
[]
[{'title': 'Home', 'path': '/'}]
[{'title': 'About', 'path': '/about/'}]"""

# Solution
# Solution 1
# Define the global variable `settings` as a dictionary with the initial title and pages
settings = {'title': 'My original title', 'pages': []}

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
# Define the global variable `default_settings` as a dictionary with a key 'title' and 'pages'
default_settings = {'title': 'My original title', 'pages': []}

# Function to get the title from a given dictionary
def get_title(settings=default_settings):
    # Retrieve the value of the 'title' key from the provided dictionary
    return settings['title']

# Print the title from the `settings` dictionary
#print(get_title(settings))

# Print the title using the `default_settings` dictionary
#print(get_title())

# Change the site title
change_site_title("A new fancy title")

# Print the updated title from the `settings` dictionary
#print(get_title(settings))

# Print the title using the `default_settings` dictionary
#print(get_title())


# Task 3
# Function to get the pages from a given dictionary
def get_pages(settings=default_settings):
    # Retrieve the value of the 'pages' key from the provided dictionary
    return settings['pages']

# Function to add a page to the 'pages' key of a given dictionary
def add_page(page, settings=default_settings):
    # Access the 'pages' key in the provided dictionary and append the new page
    settings['pages'].append(page)

# Create the 'home' page dictionary
home = {"title": "Home", "path": "/"}

# Add the 'home' page to the 'pages' key using default_settings
add_page(home)

# Print the pages using default_settings
print(get_pages())

# Print the pages using the `settings` dictionary
print(get_pages(settings))

# Create the 'about' page dictionary
about = {"title": "About", "path": "/about/"}

# Add the 'about' page to the 'pages' key using `settings`
add_page(about, settings)

# Print the pages using default_settings
print(get_pages())

# Print the pages using the `settings` dictionary
print(get_pages(settings))
