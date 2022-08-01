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
- [ ] Add a default image for when box art cannot be scraped / "Let's Chat" on Twitch
- [ ] Fix the template's Saturday/Sunday labels (they're swapped)
- [ ] Add install and run scripts for easy usage
- [ ] Update install instructions
### Bonus Things I Might Do (from highest to lowest priority)
- [ ] Add an alternate mode that fetches game screenshots instead of box art
- [ ] Decouple program from IGDB wrapper library (ie. write my own request headers)
- [ ] Create a UI (Qt?) to allow the user to enter in the games and select any settings????

## How to Use
To run, create a virtual environment and install the following:
```
pip install requests
pip install igdb-api-v4
pip install Pillow
```