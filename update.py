import os
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date

os.system('cmd /c "color a"')
os.system('cmd /c "cd Desktop"')
os.system('cmd /c "cd FitTest"')
os.system('cmd /c "git pull"')
os.system('cmd /c "conda env update --file environment.yml  --prune')
os.system('cmd /c "conda activate FitTest"')  # needed because Pyinstaller doesn't like to include itself as dependency
os.system('cmd /c "pyinstaller -n DynamicFitter --add-data source/images/*.png;./source/images/ driver.py --noconfirm"')
time.sleep(3)

print("\n\n\n ****** \n\n\nNow updating offline bike database from SlowTwitch.")

print("Versions of the database previous to today will remain archived.")

response = requests.get(
    'https://docs.google.com/spreadsheets/u/0/d/e/2PACX-1vRu5yNNvCe_v7A_bTWDZvVq-w9VfqmRKIyV8yXBWRrjXEC19hIqOKsZJjgCv_lm-LlUfN7-37WR58wJ/pubhtml/sheet?headers=false&gid=0&output=csv')
print(response.status_code, type(response.content))


data = []

# for getting the header from
# the HTML file
list_header = []
soup = BeautifulSoup(response.content, 'html.parser')
header = soup.find_all("table")[0].find("tr")

for items in header:
    try:
        list_header.append(items.get_text())
    except:
        continue

# for getting the data
HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue
    data.append(sub_data)

# Storing the data into Pandas
# DataFrame
dataFrame = pd.DataFrame(data=data, columns=list_header)

# Converting Pandas DataFrame
# into CSV file
new_file = 'slowtwitch_database/DB'+ str(date.today().strftime("%d%m%Y")) + '.csv'
dataFrame.to_csv(new_file)
print("Wrote new database to", new_file)
