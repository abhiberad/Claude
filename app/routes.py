from flask import render_template

from app import app

# Apps shown on the home screen. Each opens the service's website in the
# TV browser. Edit this list to add, remove or reorder tiles.
APPS = [
    {"name": "JioHotstar", "url": "https://www.hotstar.com/in", "color": "#0f1c4d"},
    {"name": "Netflix", "url": "https://www.netflix.com/in/", "color": "#141414"},
    {"name": "Prime Video", "url": "https://www.primevideo.com", "color": "#0f2a3d"},
    {"name": "YouTube", "url": "https://www.youtube.com/tv", "color": "#3a0d0d"},
    {"name": "SonyLIV", "url": "https://www.sonyliv.com", "color": "#2b1a3d"},
    {"name": "ZEE5", "url": "https://www.zee5.com", "color": "#2d0f3a"},
    {"name": "JioSaavn", "url": "https://www.jiosaavn.com", "color": "#0d3330"},
    {"name": "Spotify", "url": "https://open.spotify.com", "color": "#0f2a17"},
]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", apps=APPS)
