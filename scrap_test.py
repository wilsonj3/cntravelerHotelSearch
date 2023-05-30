import requests

URL = "https://www.cntraveler.com/category/hotel/tokyo?hierarchy=asia/japan"
page = requests.get(URL)

print(page.text)