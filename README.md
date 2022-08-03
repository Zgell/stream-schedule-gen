# Stream Schedule Generator (a.k.a. "Super Stream Scheduler Pro 9000")
A program I wrote for a friend to use in order to dynamically generate schedule images for his stream.
The program works by first taking in 3 games from the user (follows the stream schedule) and then does the following:
1. Fetches an access token from the Twitch API
2. Uses the access token to access the IGDB database for game metadata
3. Searches for games with the given titles, acquires their IDs
4. Searches for box art of the IDs, returns URLs to the box art
5. Downloads the box art
6. Creates a copy of the schedule template and begins inserting box art into it
7. Adds text to the schedule to show what game is played on each day
8. Produces a final image

## TO-DO (Project is still WIP)
- [x] Make a Twitch API access token retriever
- [x] Make an IGDB query function
- [x] Make a box art URL retriever using IGDB API
- [x] Make a box art downloader
- [x] Make a copier for the schedule template
- [x] Insert the box art into the template copy
- [x] Label the template copy
- [x] Produce final image
- [x] Add a default image for when box art cannot be scraped / "Let's Chat" on Twitch
- [x] Fix the template's Saturday/Sunday labels (they're swapped)
- [x] Add a name conflict resolver (ie. so you can generate more than 1 schedule per day)
- [x] Bundle project into distributable executable file (not included in repo)
- [ ] Update install instructions
### Bonus Things I Might Do (from highest to lowest priority)
- [ ] Add an alternate mode that fetches game screenshots instead of box art
- [ ] Decouple program from IGDB wrapper library (ie. write my own request headers)
- [ ] Create a UI (Qt?) to allow the user to enter in the games and select any settings????

## How to Install and Use
If you just want to use the program, download the pre-compiled binary and run the `main.exe` file (Windows only at the moment).
If you need a cross-platform copy or just want to run the main Python version

1. Install Python version 3.8 or newer.
2. Clone this repository.
3. Create a virtual environment using: `python -m venv env`
4. Open said virtual environment and install the following prerequisites:
```
pip install requests
pip install igdb-api-v4
pip install Pillow
```
5. In the Twitch developer console, create a new application. You'll need the **Client ID** as well as the **Client Secret** of the application. This is for accessing the IGDB API.
6. In `config/auth.json`, write the following:
```
{
    "CLIENT_ID": "paste your client id here",
    "CLIENT_SECRET": "paste your client secret here"
}
```
7. To run the program, open it through `main.py`.