# StormSignal

StormSignal is a mobile-first prototype for the TravelTech problem statement: **Real-Time Crisis Communication for Tourists During Extreme Weather Events**. It helps travellers across India find their district's current official weather warning, understand practical safety steps, and reach nationwide emergency help.

## Live demo

- [Open StormSignal](https://venuveerapaneni.github.io/StormSignal/)
- [Public source repository](https://github.com/VenuVeerapaneni/StormSignal)
- [Open the official IMD district warning map](https://mausam.imd.gov.in/responsive/districtWiseWarningGIS.php)
- [View current alerts on NDMA's SACHET portal](https://sachet.ndma.gov.in/)

StormSignal links to the India Meteorological Department's interactive district map. Select a forecast date and district on the official IMD page to see the published warning. It also links to NDMA's SACHET portal for its current CAP alerts. This prototype does not mirror either source's live alerts; the issuing authority's page remains the source of truth. The interface and practical travel guidance are available in 18 languages: English, Hindi, Bengali, Telugu, Marathi, Tamil, Gujarati, Kannada, Malayalam, Punjabi, Odia, Assamese, Urdu, French, Spanish, German, Simplified Chinese, and Japanese. The IMD's original warning wording is preserved on its source page.

## What it includes

- India-wide entry point to official district warnings and forecast dates.
- Direct links to official IMD district warnings and NDMA SACHET's current alerts.
- IMD warning-level legend: No Warning, Watch, Alert, and Warning.
- Three concise travel-safety steps and clear limitations.
- A language selector with 18 languages and saved preference, covering Indian travellers and visitors from several major international language groups.
- A call link to India's nationwide 112 emergency response number.
- Share support on browsers that provide the Web Share or clipboard API.
- An installable Progressive Web App (PWA) with a cached app shell for offline access to the guidance and emergency call link.

## Run locally

Open `index.html` in a modern browser. No build step, package installation, or backend is required. For installation and offline app-shell support, serve the site over HTTPS (GitHub Pages already does this). The official IMD district map opens in a separate tab because the source does not allow embedding. An Android APK has not been packaged; this repo is currently a web app/PWA.

## Data and safety

IMD's public [district-wise warning map](https://mausam.imd.gov.in/responsive/districtWiseWarningGIS.php) provides district warnings and forecast dates. [NDMA's SACHET portal](https://sachet.ndma.gov.in/) provides its current CAP alerts. StormSignal links to these official sources without mirroring their alerts. Official warning language is kept at its source; StormSignal's translated guidance is a concise aid, not an official translation of the warning.

StormSignal does not provide automatic location tracking, street-level flood status, road closures, verified shelters, evacuation routes, or rescue dispatch. It is not an emergency service. For emergencies, call [112](https://112.gov.in/) and follow current instructions from local authorities.

## Submission materials

- [Copy-ready project description](SUBMISSION_DESCRIPTION.md)
- [Timed narration and recording notes](DEMO_SCRIPT.md)
- [Browser-tab-only recording helper](demo/recorder.html)
- [AI narration audio](demo/stormsignal-narration-16k.mp3)
- [Timed English captions](demo/stormsignal-demo.srt)
- [Submission checklist](SUBMISSION_CHECKLIST.md)

The final 2–5 minute video still needs to be recorded and added to the repository before submission.

## Libraries and services

- Frontend: plain HTML, CSS, JavaScript, and browser Web APIs; no JavaScript libraries.
- Google Fonts is used for typography, with system-font fallbacks.
- Warning source: India Meteorological Department public district map.
- Emergency number source: Government of India's Emergency Response Support System.
- Hosting: GitHub Pages.

## Problem and solution

The problem statement describes the difficulty travellers face when weather warnings are fragmented, unfamiliar, or hard to understand. StormSignal gives travellers an India-wide starting point to the official district warnings and forecast dates, concise safety guidance in 18 languages, and a nationwide emergency contact. It deliberately sends district/date selection to the authoritative IMD map instead of presenting an unverified local alert as live data.

