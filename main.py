import requests

def guest_key():
    headers = {
        'authorization': '',
        }
    response = requests.post('https://api.twitter.com/1.1/guest/activate.json', headers=headers)
    guest_token = response.json()["guest_token"]
    return guest_token 
    
def favorite(tweet_id,token):
    ct0 = requests.get("https://twitter.com/i/release_notes").cookies.get_dict()["ct0"]
    api = "https://twitter.com/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet"
    payload = {
      "variables": {
        "tweet_id": tweet_id
      },
    }
    headers = {
        "cookie": f'auth_token={token}; ct0={ct0};',
        "authorization": "",
        "x-csrf-token": ct0,
              }
    r = requests.post(api, json = payload,headers = headers)
    return r.text

def retweet(tweet_id,token):
    ct0 = requests.get("https://twitter.com/i/release_notes").cookies.get_dict()["ct0"]
    api = "https://twitter.com/i/api/graphql/ojPdsZsimiJrUGLR1sjUtA/CreateRetweet"
    payload = {
      "variables": {
        "tweet_id": tweet_id
      }
    }
    headers = {
        "cookie": f'auth_token={token}; ct0={ct0};',
        "authorization": "",
        "x-csrf-token": ct0,
              }
    r = requests.post(api, json = payload,headers = headers)
    return r.text
