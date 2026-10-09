# StormSignal

StormSignal is a mobile-first hackathon prototype for the TravelTech problem: helping tourists understand extreme-weather alerts and practical safety guidance.

## Current prototype

- View a Chennai-area sample weather alert with area and update time.
- Read short safety steps and use official Chennai help contacts.
- Switch between English, Tamil, and Hindi.
- See clear labels explaining that the alert is demonstration data, not a live emergency feed.
- Open a brief explanation of the data source, and share the demo with a sample-data note.

## Run locally

Open `index.html` in a modern web browser. No package installation or backend is needed for this static prototype.

## Live demo

The current public demo is hosted on GitHub Pages:

[Open StormSignal](https://venuveerapaneni.github.io/StormSignal/) · [View the source repository](https://github.com/VenuVeerapaneni/StormSignal)

The site publishes from the `main` branch at the repository root. It is a static page with no build step, backend, or secrets. After changing files on `main`, GitHub Pages rebuilds the site automatically.

The page links to official external sources and uses the Web Share API when supported. It does not need secrets or a server.

## Data and safety

The heavy-rain scenario and affected-area claim are illustrative sample content. Chennai is the prototype's demo area, not a user-detected location. The app is not an emergency service and must not be treated as a source of live warnings. A real deployment should use verified local authority sources, show attribution and freshness for each item, and explain what to do when information is stale or unavailable.

The prototype links directly to the India Meteorological Department's Chennai city warning page and the Chennai District Administration's helpline page. IMD documents district warning and nowcast APIs, but API access returned an authorization error during preparation, so this version does not pretend to ingest live data. The official helpline page lists Disaster Helpline 1077 and Chennai Corporation Complaints 1913. No evacuation shelter is listed because the Greater Chennai Corporation page located during research lists urban homeless shelters, not confirmed emergency evacuation centres.

## Sources

- IMD Chennai city warnings: https://mausam.imd.gov.in/chennaiums/district_warning_chnums.php
- IMD API reference: https://api.imd.gov.in/public/api_reference.html
- Chennai District helplines: https://chennai.nic.in/helpline/

## Libraries and services

- No JavaScript libraries or APIs are currently used.
- Google Fonts is referenced for typography; the page falls back to system sans-serif fonts if unavailable.

## Problem and solution

Tourists may not understand local warning systems, languages, or geography during a severe weather event. StormSignal explores a simple way to present an alert, explain immediate safety steps in a selected language, and identify nearby help while making the source and freshness of information visible.

