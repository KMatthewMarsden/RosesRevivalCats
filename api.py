import requests

url = 'https://www.reddit.com/r/catpictures.json?limit=100'

response = requests.get(url, headers={'User-agent': 'KMM'})

if not response.ok:
    print("Error: ", response.status_code)
    exit()
data = response.json()['data']['children']

for i in range(0, 100):
    the_post = data[i]['data']
    image_url = the_post['url']
    image = requests.get(image_url)
    print(image_url)
    if(image.status_code == 200):
        fileHandler = open('img/cat' + str(i) + '.jpg',mode='bx')
        fileHandler.write(image.content)