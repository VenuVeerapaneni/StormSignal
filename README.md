# StormSignal

StormSignal is a mobile-first hackathon prototype for the TravelTech problem: helping tourists understand extreme-weather alerts and practical safety guidance.

## Current prototype

- View the latest published IMD district warning for Chennai, with the district and source update date shown.
- Read short safety steps and use official Chennai help contacts.
- Switch between English, Tamil, and Hindi.
- See a clear warning when the source data is old or unavailable; outdated warning text is not presented as current.
- Open the official source, read the exact IMD wording, and share the app with a scope note.

## Run locally

Open `index.html` in a modern web browser. No package installation or backend is needed for this static prototype.

## Live demo

The current public demo is hosted on GitHub Pages:

[Open StormSignal](https://venuveerapaneni.github.io/StormSignal/) · [View the source repository](https://github.com/VenuVeerapaneni/StormSignal)

The site publishes from the main branch at the repository root. The page itself is static and has no backend or secrets. A GitHub Actions workflow checks the public IMD Chennai district-warning page every 30 minutes and publishes a small JSON snapshot only when the source data changes. GitHub Pages then rebuilds the site from main.

The page links to official external sources and uses the Web Share API when supported. It does not need secrets or a server.

## Submission materials

- [Copy-ready project description](SUBMISSION_DESCRIPTION.md)
- [Timed 2:23 AI-narrated demo guide](DEMO_SCRIPT.md)
- [Browser-tab-only recording helper](demo/recorder.html)
- [AI narration audio track](demo/stormsignal-narration.mp3)
- [Timed English captions](demo/stormsignal-demo.srt)
- [Submission checklist](SUBMISSION_CHECKLIST.md)

## Data and safety

Chennai is the prototype's fixed demo district, not a user-detected location. IMD's district warning is district-level forecast information; it does not confirm street-level flooding, open shelters, safe routes, or current road conditions. StormSignal is not an emergency service. The app shows the exact source wording and its update date, and treats records from a previous day as unverified.

The warning snapshot is collected from the public [IMD Regional Meteorological Centre Chennai district-warning page](https://mausam.imd.gov.in/imd_latest/contents/districtwise-warning_mc.php?id=26&day=Day_1). The official [IMD API reference](https://api.imd.gov.in/public/api_reference.html) documents warning APIs, but API access requires authorization, so this prototype reads the public warning page instead. The official Chennai helpline page lists Disaster Helpline 1077 and Chennai Corporation Complaints 1913. No evacuation shelter is listed because the Greater Chennai Corporation page located during research lists urban homeless shelters, not confirmed emergency evacuation centres.

## Sources

- IMD Chennai city warnings: https://mausam.imd.gov.in/chennaiums/district_warning_chnums.php
- IMD API reference: https://api.imd.gov.in/public/api_reference.html
- Chennai District helplines: https://chennai.nic.in/helpline/

## Libraries and services

- The frontend uses plain JavaScript and the browser Fetch API; no JavaScript libraries are used.
- scripts/update_imd_warnings.py uses only Python's standard library.
- The refresh workflow uses the official GitHub Actions checkout and setup-python actions.
- Google Fonts is referenced for typography; the page falls back to system sans-serif fonts if unavailable.

## Problem and solution

**Selected problem statement: TravelTech - Real-Time Crisis Communication for Tourists During Extreme Weather Events.** The challenge describes fragmented local weather warnings, language barriers, limited knowledge of local geography, and travelers relying on unverified reports during floods and cyclones.

StormSignal presents the official Chennai district warning, practical safety steps, and official help contacts in English, Tamil, and Hindi. It makes the district, exact source wording, source update date, and data freshness visible. It does not claim street-level hazard detection, verified safe-zone declarations, rescue dispatch, or route guidance.



