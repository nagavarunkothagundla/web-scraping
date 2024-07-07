import requests
import pandas
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY")
#print(response)
soup=BeautifulSoup(response.content,"html.parser")
#print(soup)
#unstructured --> structured
names=soup.find_all('div',class_="KzDlHZ")
name=[]
for i in names[0:10]:
    name.append(i.get_text())
#print(name)

prices=soup.find_all('div',class_="Nx9bqj _4b5DiR")
price=[]
for i in prices[0:10]:
    price.append(i.get_text())
#print(price)

reviews=soup.find_all('div',class_="XQDdHH")
review=[]
for i in reviews[0:10]:
    review.append(float(i.get_text()))
#print(review)


ratings=soup.find_all('span',class_="Wphh3N")
rate=[]
for i in ratings[0:10]:
    rate.append(i.get_text())
#print(rate)


images=soup.find_all('img',class_="DByuf4")
image=[]
for i in images[0:10]:
    image.append(i['src'])
#print(image)

links=soup.find_all('a',class_="CGtC98")
link=[]
for i in links[0:10]:
    d='https://www.flipkart.com'+i['href']
    link.append(d)
#print(link)
#df=pandas.DataFrame() #2D array rows*columns
#print(df)
data={
    "Names":pandas.Series(name),
    "Ratings":pandas.Series(rate),
    "Prices":pandas.Series(price),
    "Reviews":pandas.Series(review),
    "Images":pandas.Series(image),
    "Links":pandas.Series(link),
}
#print(data)
df=pandas.DataFrame(data) #2D array rows*columns
print(df)

df.to_csv("mobiles.csv")