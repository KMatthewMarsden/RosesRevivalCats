import requests

class Page:

    def __init__(self, url):
        response = requests.get(url, headers={'User-agent': 'KMM'})
        if not response.ok:
            print("Error: ", response.status_code)
            exit()
        data = response.json()['data']
        self.posts = data['children']
        self.after = data['after']
        self.before = data['before']

    def get_cat_pic(self, i):
        post = self.posts[i]['data']
        img_url = post['url']
        img_req = requests.get(img_url)
        if not img_req.ok:
            print("Failed to fetch cat img")
        return img_req.content

    def get_next_page(self):
        new_url = f"https://www.reddit.com/r/catpictures.json?limit=100&after={self.after}"
        return Page(new_url)

    def get_prev_page(self):
        new_url = f"https://www.reddit.com/r/catpictures.json?limit=100&before={self.after}"
        return Page(new_url)


def get_first_page():
    return Page("https://www.reddit.com/r/catpictures.json?limit=100")