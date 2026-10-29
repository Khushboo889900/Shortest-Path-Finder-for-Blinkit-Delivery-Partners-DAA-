# QuickRoute — Delivery Partner Shortest Path Finder

A DAA mini project showing Dijkstra's shortest-path algorithm in a Flask website. It is inspired by quick-commerce delivery workflows but is an independent educational demo, not affiliated with or connected to Blinkit.

## Run in VS Code on Windows
1. Extract the ZIP and open the `blinkit_shortest_path_finder` folder in VS Code.
2. Open Terminal → New Terminal.
3. Run `python -m pip install -r requirements.txt`
4. Run `python app.py`
5. Open **http://127.0.0.1:5000** in Chrome.
6. Keep the terminal running while using the website. Press Ctrl+C to stop the server.

If you prefer a virtual environment:
`python -m venv .venv`
`.venv\\Scripts\\activate`
`python -m pip install -r requirements.txt`

## Files
- `app.py`: Flask backend, weighted graph, Dijkstra algorithm and JSON API.
- `templates/index.html`: website structure and location dropdowns.
- `static/style.css`: responsive styling.
- `static/app.js`: interactive SVG graph, API request and result display.

## Algorithm
Graph nodes represent the store, neighborhood road junctions, and customer locations. Edge weights are illustrative distances in kilometres. Dijkstra computes the minimum-distance route. The ETA is only an example estimate (18 km/h plus 2 minutes handoff).

**Important:** This project uses sample data only. It does not use live GPS, real maps, live traffic, official Blinkit APIs, or real delivery partner data.
