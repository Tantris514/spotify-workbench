import requests
import argparse
import yaml


parser = argparse.ArgumentParser(description="Okta Client Configuration")
parser.add_argument("-c", "--config", help="Path to the configuration YAML file", required=True)
args = parser.parse_args()
loadConfig = lambda config_file: yaml.safe_load(open(config_file, 'r'))
yamlConfig = loadConfig(args.config)

CLIEND_ID = yamlConfig["spotify_app"]["client_id"]
CLIENT_SECRET = yamlConfig["spotify_app"]["client_secret"]

def get_spotify_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception("Failed to get token")



if __name__ == "__main__":
    print(get_spotify_token(CLIEND_ID, CLIENT_SECRET))



