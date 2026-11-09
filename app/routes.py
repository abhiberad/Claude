from flask import render_template

from app import app

# Apps shown on the home screen. Each opens the service's website in the
# TV browser. Edit this list to add, remove or reorder tiles.
#   color   - icon background
#   glow    - colour of the featured banner when the app is highlighted
#   tagline - text shown in the featured banner
APPS = [
    {"name": "JioHotstar", "url": "https://www.hotstar.com/in", "color": "#1a2a7a",
     "glow": "#2f4bd6", "tagline": "Live cricket, Indian originals and Disney favourites"},
    {"name": "Netflix", "url": "https://www.netflix.com/in/", "color": "#1c1c1c",
     "glow": "#b3121c", "tagline": "Series, films and Indian originals"},
    {"name": "Prime Video", "url": "https://www.primevideo.com", "color": "#0f3550",
     "glow": "#1a8fd6", "tagline": "Movies, shows and live sport"},
    {"name": "YouTube", "url": "https://www.youtube.com/tv", "color": "#4a1010",
     "glow": "#e02424", "tagline": "Videos, music and creators you follow"},
    {"name": "SonyLIV", "url": "https://www.sonyliv.com", "color": "#33204d",
     "glow": "#7a4be0", "tagline": "Sports, shows and Sony originals"},
    {"name": "ZEE5", "url": "https://www.zee5.com", "color": "#3a1248",
     "glow": "#b23ad6", "tagline": "Movies and shows in 12 languages"},
    {"name": "JioSaavn", "url": "https://www.jiosaavn.com", "color": "#0d3d39",
     "glow": "#1fb5a5", "tagline": "Bollywood, regional and global music"},
    {"name": "Spotify", "url": "https://open.spotify.com", "color": "#0f3319",
     "glow": "#1fb954", "tagline": "Music and podcasts"},
]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", apps=APPS)
