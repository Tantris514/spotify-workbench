# Spotify Playlist Fetcher

This tool allows you to retrieve your Spotify playlists using your Spotify API credentials.

## Prerequisites

- Python 3.x installed on your machine
- Spotify Developer account

## Setup

### Step 1: Get Your Spotify API Credentials

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/login).
2. Log in or create a new account if you don’t have one.
3. Click on **Create an App**. Fill out the required information (app name and description).
4. After the app is created, you'll find the **Client ID** and **Client Secret** on the app's dashboard.
5. Copy the **Client ID** and **Client Secret**—you’ll need them in the next step.

### Step 2: Create a `config.yaml` File

In the project directory, create a file named `config.yaml`. Add your `Client ID` and `Client Secret` like this:

```yaml
spotify:
  client_id: "your-client-id-here"
  client_secret: "your-client-secret-here"

```


Then to run
python main.py -c config.yaml