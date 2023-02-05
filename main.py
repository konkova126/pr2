# Importing the required libraries
import xml.etree.ElementTree as Xet
import pandas as pd

cols = ["название", "автор", "страниц", "цена", "жанр", "количество", "издательство", "вес", "тираж", "публикация"]
rows = []

# Parsing the XML file
xmlparse = Xet.parse('books.xml')
root = xmlparse.getroot()
for книга in root:
    name = книга.find("название").text
    author = книга.find("автор").text
    page = книга.find("страниц").text
    price = книга.find("цена").text
    genre= книга.find("жанр").text
    amount = книга.find("количество").text
    house = книга.find("издательство").text
    weight = книга.find("вес").text
    circulation = книга.find("тираж").text
    year = книга.find("публикация").text

    rows.append({"название": name,
                 "автор": author,
                 "страниц": page,
                 "жанр": genre,
                 "количество": amount,
                 "издательство": house,
                 "вес": weight,
                 "тираж": circulation,
                 "публикация": year})

df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
df.to_csv('books.csv')