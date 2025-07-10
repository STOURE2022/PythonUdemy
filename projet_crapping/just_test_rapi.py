from pprint import pprint
from bs4 import BeautifulSoup

import requests


def extracr_lyrics(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/91.0.4472.124 Safari/537.36"
        )
    }
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
            for word in element.split():
                if len(word) > 2 and word != "[Refrain]" and word != "Couplet":
                    print(word)

        counter = collections.Counter(all_words)
        print(counter.most_common(20))

print(extracr_lyrics(url="https://genius.com/Patrick-bruel-place-des-grands-hommes-lyrics"))

def get_all_songs_by_artist():
    page_number = 1
    links = []
    while page_number is not None:
        r = requests.get(f"https://genius.com/api/artists/29743/songs?page={page_number}&sort=popularity")
        if r.status_code == 200:
            response = r.json().get("response", {})
            next_page = response.get("next_page")

            songs = response.get("songs")
            all_song_links = [song.get("url") for song in songs]
            links.extend(all_song_links)
            pprint(links)
            print(len(links))
            page_number += 1

            if not next_page:
                print("Il n y a plus de pages.")
                break

        if r.status_code != 200:
            print("Votre url a un souci.")
            break



