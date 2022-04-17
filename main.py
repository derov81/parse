# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from bs4 import BeautifulSoup
from time import sleep
import requests

def parser():
    data = []




    url = f"https://www.onliner.by"
    r = requests.get(url)
    sleep(3)
    soup = BeautifulSoup(r.text,"lxml")


    links = soup.find(class_="project-navigation__part project-navigation__part_1").find("ul").find_all("a")
    # print(links)
    for item in links:
        item_url = item.get("href")
        print(f"{item.text}: {item_url}")



    # with open("https://www.onliner.by") as file:
    #     src = file.read()
    #     soup = BeautifulSoup(src,"lxml")
    #     print(src)

        # user_name = soup.find("div", {"class": "user"}).find("span").text
        # print(user_name)
        #
        # find_all_spans = soup.find_all(class_="city")
        # print(find_all_spans)
        # for item in find_all_spans:
        #     print(item.text)
        #
        # links = soup.find(class_="links").find("ul").find_all("a")
        # print(links)
        # for item in links:
        #     item_url = item.get("href")
        #     print(f"{item.text}: {item_url}")
        #
        # post_div = soup.find(class_="city_lebel").find_parent()
        # print(post_div)






def main():
    # Use a breakpoint in the code line below to debug your script.
   # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    parser()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
