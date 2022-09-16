from bs4 import BeautifulSoup

#soup = BeautifulSoup(html, "html.parser")

# print(soup)

# print(type(soup)) #class bs4.BeautifulSoup

# print(soup.body) #prints body

# print(soup.body.div) #prints the first div

# print(soup.find("div")) #print the first div

# print(soup.find_all("div")) #returns a list

# print(soup.find(id = "first")) #find using id

# print(soup.find_all(class_ = "special")) #list of item with the same class

# print(soup.find_all(attrs = {"data-example": "yes"})) #search using an attribute

# ---------------------------------------------------------------------------------

# css style selectors

# id - #foo

# class - .bar

# children : div > p

# descendent : div p

# print(soup.select("#first")) #selects with id of first - it always gives a list back

# print(soup.select(".special")) # selects with class of "special"

# print(soup.select("[data-example]")) #select using an attribute

# ---------------------------------------------------------------------------------

# Accessing data

#el = soup.select(".special")

# text = el.getText()  # this returns the inner text.

# print(text)

# for el in soup.select(".special"):
