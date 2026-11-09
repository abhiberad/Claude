# Flask Docker Demo – TV Home Screen

A clean, dark, full-screen home page built for viewing on an LG TV's web browser.
It is set up for India: the clock runs on IST, it greets you with "Namaste", and
the tiles open Indian streaming services.

To build run: `docker build -t flasktest .`

To run: `docker run -p 8888:5000 flasktest`

## Open it on your LG TV

1. Run the container on a computer that is on the same Wi-Fi as the TV.
2. Find that computer's local IP address (for example `192.168.1.20`).
3. On the TV, open the **Web Browser** app and go to `http://192.168.1.20:8888`.
4. Use the arrow keys on the remote to move between tiles and **OK** to open one.
   The Magic Remote pointer works too.

To change the apps, edit the `APPS` list in `app/routes.py`.
