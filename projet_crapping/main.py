import collections
import json
from pprint import pprint
from textwrap import indent
from pathlib import Path

from bs4 import BeautifulSoup

import requests

path_dir = Path.home() / "Downloads"
path_dir.mkdir(exist_ok=True)
path_file = path_dir / "data_stromae.json"
path_file.touch(exist_ok=True)


def extracr_lyrics(url, word_lengh=5):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/91.0.4472.124 Safari/537.36"
        )
    }
    print(f"Fetching lyrics {url}...")
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print("❌ Erreur de requête HTTP:", r.status_code)
        return ""

    soup = BeautifulSoup(r.content, 'html.parser')

    # Récupérer tous les div avec l'attibut data-lyrics-container="true"
    lyrics_blocks = soup.find_all("div", attrs={"data-lyrics-container": "true"})

    # extraire le texte ligne par ligne
    lyrics = ""
    for block in lyrics_blocks:
        # supprimer tous les enfants à exclure
        for exclu in block.find_all(attrs={"data-exclude-from-selection": "true"}):
            exclu.decompose()  # supprime l'élément du DOM

        # Supprimer tous les boutons, spans, ou autres classes inutiles
        for tag in block.find_all(["button", "span", "svg"]):
            tag.decompose()

        all_words = []
        # Extraire les lignes de texte réelles
        for element in block.stripped_strings:
            element_words = [word for word in element.replace(",", "").replace(".", "").lower().split() if
                             len(word) > word_lengh and "[" not in word and "]" not in word]
            all_words.extend(element_words)

        return all_words


def get_all_songs_by_artist():
    page_number = 1
    links = []
    while page_number is not None:
        r = requests.get(f"https://genius.com/api/artists/9001/songs?page={page_number}&sort=popularity")
        if r.status_code == 200:
            print(f"Fetching page {page_number}")
            response = r.json().get("response", {})
            next_page = response.get("next_page")

            songs = response.get("songs")
            all_song_links = [song.get("url") for song in songs]
            links.extend(all_song_links)
            # pprint(links)
            # print(len(links))
            page_number += 1

            if not next_page:
                print("Il n y a plus de pages.")
                break

        if r.status_code != 200:
            print("Votre url a un souci.")
            break

    return links


def get_all_words():
    urls = get_all_songs_by_artist()
    print(urls)
    words = []
    for url in urls:
        lyrics = extracr_lyrics(url=url)
        if lyrics is not None:
            words.extend(lyrics)

    if path_file.exists():
        with open(path_file, "w", encoding="utf-8") as f:
            json.dump(words, f, indent=4)
    # with open(path_file, "r") as f:
    #     words = json.load(f)

    counter = collections.Counter(w for w in words if len(w) > 10)
    most_common_words = counter.most_common(20)
    pprint(most_common_words)


get_all_words()
