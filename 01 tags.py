import requests
from bs4 import BeautifulSoup

with open("sample.html","r")as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())

# print(soup.title.string,type(soup.title.string))

# print(soup.find_all("div"))

# for links in soup.find_all("a"):
#     print(links.get("href"))
#     print(links.get_text())

# a = soup.find(id="link3")
# print(a.get("href"))

# print(soup.find(id="italic"))

# for chil in soup.find(class_="container").children:
#     print(chil)
    
# for parent in soup.find(class_ = "box").parents:
#     print(parent)
    
    
# cont = soup.find(class_ = "container")
# cont.name = "span"
# cont["class"] = "myclass1 myclass2"
# cont.string = "hey!! i'm shubham"
# print(cont)

# # First we have to prepare the tag 
# ulTag = soup.new_tag("ul")

# liTag = soup.new_tag("li")
# liTag.string = "Home"
# ulTag.append(liTag)

# liTag = soup.new_tag("li")
# liTag.string = "About"
# ulTag.append(liTag)


# soup.html.body.insert(0,ulTag)

# with open("modified.html","w")as f:
#     f.write(str(soup))
    
# con = soup.find(class_ = "container")
# print(con.has_attr("contenteditable"))


# def has_class_but_not_id(tag):
#     return tag.has_attr("class") and not tag.has_attr(id)

# result = soup.find_all(has_class_but_not_id)
# print(result)
    
#     def has_content(tag):
#     return tag.has_attr("content")
# result = soup.find_all(has_content)
# for i in result:
#     print(i, "n/,n/")