import requests

user_agent = "KMM"

fact_url = "https://meowfacts.herokuapp.com"
bio_url = "https://www.twitterbiogenerator.com/generate"


def get_cat_fact():
    response = requests.get(fact_url, user_agent=user_agent)
    if not response.ok:
        return None
    fact = response.json()["data"][0]
    return fact


def get_bio():
    response = requests.get(bio_url, user_agent=user_agent)
    if not response.ok:
        return "Didn't know what to put in my bio :)"
    bio = response.content
    return bio
