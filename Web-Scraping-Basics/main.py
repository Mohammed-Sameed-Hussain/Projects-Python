from bs4 import  BeautifulSoup


file_path = 'website.html'

with open(file_path) as web_file:
    contents  = web_file.read()


soup = BeautifulSoup(contents, "html.parser")

print(soup.title)
print(soup.title.name)
print(soup.title.string)   
print()
print()
print()
print(soup)
print()
print()
print()
print(soup.prettify())
print()
print()

# The below gives the first anchor tag of the website
print(soup.a)


# To get hold of all of the achor tags or all of some other tags to somehting like below
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

# To get the text of the above all anchor tags.
for tag in all_anchor_tags:
    print(tag.getText())


# To get the links of the acnhor tags aove
for tag in all_anchor_tags:
    print(tag.get("href"))


# To find things by their attributes
heading = soup.find(name='h1', id='name')
print(heading)
# In the above you can also use find_all() method to find all possible such things.!

# Another example
section_heading = soup.find(name='h3', class_='heading')
print(section_heading)
print(section_heading.name)  # To get the name of the type of tag
# In the above we used an underscore, because "class" is a reserved keyword in python to create classes


# You can also get hold of items using css elements
company_url = soup.select_one(selector="p a")
print(company_url)
# The above gets hold of an anchor tag inside a paragraph tag

# Another example to select by id
name = soup.select_one(selector='#name')
print(name)

# Another example to get hold by class
# We use select() method to get hold of all items 
heading = soup.select(".heading")
print(heading)