from django.shortcuts import render

# Create your views here.

from bs4 import BeautifulSoup
import requests
def scrape(username, base_url):
    _full_url = base_url.format(username)
    req = requests.get(_full_url)
    soup = BeautifulSoup(req.text, "html.parser")
    u = soup.find("meta", property="og:description")
    img = soup.find("meta", property={"og:image"})
    profile_url = soup.find("meta",  property="al:android:url")
    username = soup.find("meta", property="al:ios:url")
    posts = soup.findAll("meta")
    scrape_object = {
        "followers":  u.attrs["content"].split("s,")[0].split(" ")[0],
        "following": u.attrs["content"].split("s,")[1].split("g,")[0].split(" ")[1],
        "post":  u.attrs["content"].split("s,")[1].split("-")[0].split(',')[-1].split(" ")[1],
        "img": img.attrs["content"],
        "profile_url": profile_url.attrs["content"],
        "username": username["content"].split("=")[-1],
    }
    return scrape_object
def main(req):
    username = "crispen_gari_"
    if req.method == "GET" or req.method == "POST":
        try:
            username = str(req.GET["search_term"]).strip().lower() or str(
                req.POST["search_term"]).strip().lower()
            print(username)
        except Exception as e:
            pass
    url = "https://www.instagram.com/{}/"
    # print(str(scrape("crispen_gari_", url)))
    data = data = scrape("crispen_gari_", url)
    if username:
        data = scrape(username, url)
    else:
        data = data
    # dowload the profile
    if req.method == "GET":
        try:
            print(req.GET["profile"])
        except Exception:
            pass
    else:
        print("another form is fired!!")
    return render(req, 'index.html', {"data": data})
