import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.goodreads.com/list/show/6.Best_Books_of_the_20th_Century"
page = requests.get(url)
web_page = page.content

soup = BeautifulSoup(web_page, "html.parser")
titles_raw = [title.getText().strip() for title in soup.find_all(name="a", class_="bookTitle")]
authors_raw = [author.getText().strip() for author in soup.find_all(name="a", class_="authorName")]
data = {
    "authors": authors_raw,
    "titles": titles_raw
}
pd.set_option('display.max_rows', 100)
df = pd.DataFrame(data)
print(df)
with open("goodreads_recent_list.txt", mode="w", encoding="utf-8") as file:
    file.write(f'GoodReads Best Books of 20th Century: \n\n')
    file.write(f'{df}')
