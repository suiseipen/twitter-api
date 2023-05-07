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
    
def follow(user_id,token):
    ct0 = requests.get("https://twitter.com/i/release_notes").cookies.get_dict()["ct0"]
    api = "https://twitter.com/i/api/1.1/friendships/create.json"
    data = {
        "include_profile_interstitial_type": "1",
        "include_blocking": "1",
        "include_blocked_by": "1",
        "include_followed_by": "1",
        "include_want_retweets": "1",
        "include_mute_edge": "1",
        "include_can_dm": "1",
        "include_can_media_tag": "1",
        "include_ext_has_nft_avatar": "1",
        "skip_status": "1",
        "id": user_id,
        }
    headers = {
        "cookie": f'auth_token={token}; ct0={ct0};',
        "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        "x-csrf-token": ct0,
    }
    cookie = {"auth_token": token,"ct0": ct0}
    r = requests.post(api, cookies=cookie, data = data,headers= headers)
    return r.text
    
def unfollow(user_id,token):
    ct0 = requests.get("https://twitter.com/i/release_notes").cookies.get_dict()["ct0"]
    api = "https://twitter.com/i/api/1.1/friendships/destroy.json"
    data = {
        "include_profile_interstitial_type": "1",
        "include_blocking": "1",
        "include_blocked_by": "1",
        "include_followed_by": "1",
        "include_want_retweets": "1",
        "include_mute_edge": "1",
        "include_can_dm": "1",
        "include_can_media_tag": "1",
        "include_ext_has_nft_avatar": "1",
        "skip_status": "1",
        "id": user_id,
        }
    headers = {
        "cookie": f'auth_token={token}; ct0={ct0};',
        "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        "x-csrf-token": ct0,
    }
    cookie = {"auth_token": token,"ct0": ct0}

    r = requests.post(api, cookies=cookie, data = data,headers= headers)
    return r.text
