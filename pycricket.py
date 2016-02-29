import requests
import json
from datetime import datetime
from pycricket_storagehandler import *


class RcaApp():
  """The RcaApp class will be containg various funtion to access
     the defferent CricketAPI API's.


  """
  def __init__(self, access_key, secret_key, app_id, store_handler, device_id=None):
    """ initialzing user Cricket API app details.


    Arg:
        access_key : Cricket API APP access_key
        secret_key : Cricket API APP secret_key
        store_handler : RcaStorageHandler/RcaFileStorageHandler object name
        device_id : User device_id

    """
    self.access_key = access_key
    self.secret_key = secret_key
    self.app_id = app_id
    self.store_handler = store_handler
    self.api_path = "https://rest.cricketapi.com/rest/v2/"
    if device_id:
      new_id = device_id
    else:
      new_id = store_handler.new_device_id()
    store_handler.set_value("device_id", new_id)
    self.device_id = new_id

  def auth(self):
    """Auth is used to call the AUTH API of CricketAPI.
       
       Aceestoken required for every request call to CricketAPI.
       Auth fuctional will post user Cricket API app details to server
       and return the access token.


    Return:
       Aceestoken    


    """
    if(self.store_handler.has_value('access_token')):
      self.access_token = self.store_handler.get_value('access_token')
      # print "get_access_token", self.access_token  #Debugger
      return True
    else:
      params = {}
      params["access_key"] = self.access_key
      params["secret_key"] = self.secret_key
      params["app_id"] = self.app_id
      params["device_id"] = self.device_id
      auth_url = self.api_path + "auth/"
      response = self.get_response(auth_url, params, "post")

      if 'auth' in response:
        self.store_handler.set_value("access_token", response['auth']['access_token'])
        self.store_handler.set_value("expires", response['auth']['expires'])
        self.access_token = response['auth']['access_token']
        # print "set_token" #Debugger
        return True
      else:
        raise Exception("Auth Failed, please check your access details")
        return False

  def get_response(self, url, params="", method="get"):
    """It will return json response based on given url, params and methods.
    

    Arg:    
       params: 'dictionary'
       url: 'url' formate
       method: default 'get', support method 'post' 
    Return:
       json data   


    """
    if(method == "post"):
      return json.loads(requests.post(url, params=params).text)
    else:
      return json.loads(requests.get(url, params=params).text)

  def check_token_active(self):
    """Checking the access token validity.

       Access token expires every 24 hours, It will expires then it will
       generate a new token.
    Return:
       True (always) 


    """
    expire_time = self.store_handler.has_value("expires")
    access_token = self.store_handler.has_value("access_token")
    if expire_time and access_token:
      expire_time = self.store_handler.get_value("expires")
      if not datetime.now() < datetime.fromtimestamp(float(expire_time)):
        self.store_handler.delete_value("access_token")
        self.store_handler.delete_value("expires")
        self.auth()
      else:
        expire_time = self.store_handler.get_value("expires")
        self.access_token = self.store_handler.get_value("access_token")
        # print "access_token not expired", self.access_token  #Debugger
    else:
      self.auth()
    return True

  def get_match(self, match_key, card_type="full_card"):
    """Calling the Match API.
    

    Arg:
       match_key: key of the match
       card_type: optional, default to full_card. Accepted values are 
       micro_card, summary_card & full_card.
    Return:
       json data   


    """
    self.check_token_active()
    match_url = self.api_path + "match/" + match_key + "/"
    params = {}
    params["access_token"] = self.access_token, 
    params["card_type"] = card_type
    response = self.get_response(match_url, params)
    return response

  def get_recent_matches(self, card_type="micro_card"):
    """Calling the Recent Matches API.

    Arg:
       card_type: optional, default to micro_card. Accepted values are
       micro_card & summary_card.
    Return:
       json data

    
    """
    self.check_token_active()
    recent_matches_url = self.api_path + "recent_matches/"
    params = {}
    params["access_token"] = self.access_token, 
    params["card_type"] = card_type
    response = self.get_response(recent_matches_url, params)
    return response  

  def get_recent_season_matches(self, season_key):
    """Calling specific season recent matches.

    Arg:
       season_key: key of the season.
    Return:
       json date


    """
    self.check_token_active()
    season_recent_matches_url = self.api_path + "season/" + season_key + "/recent_matches/"
    params = {}
    params["access_token"] = self.access_token, 
    response = self.get_response(season_recent_matches_url, params)
    return response      

  def get_recent_seasons(self):
    """Calling the Recent Season API.

    Return:
       json data


    """
    self.check_token_active()
    recent_seasons_url = self.api_path + "recent_seasons/"
    params = {}
    params["access_token"] = self.access_token
    response = self.get_response(recent_seasons_url, params)
    return response

  def get_schedule(self, date=None):
    """Calling the Schedule API.

    Return:
       json data


    """
    self.check_token_active()
    schedule_url = self.api_path + "schedule/"
    params = {}
    params["access_token"] = self.access_token
    if date:
      params['date'] = date
    response = self.get_response(schedule_url, params)
    return response

  def get_season_schedule(self, season_key):
    """Calling sepecific season schedule

    Arg:
       season_key: key of the season
    Return:
       json data


    """
    self.check_token_active()
    schedule_url = self.api_path + "season/" + season_key +  "/schedule/"
    params = {}
    params["access_token"] = self.access_token
    response = self.get_response(schedule_url, params)
    return response  
  
  def get_season(self, season_key):
    """Calling Season API.

    Arg:
       season_key: key of the season
    Return:
       json data


    """
    self.check_token_active()
    season_url = self.api_path + "season/" + season_key + "/"
    params = {}
    params["access_token"] = self.access_token
    response = self.get_response(season_url, params)
    return response

  def get_season_stats(self, season_key):
    """Calling Season Stats API.

    Arg:
       season_key: key of the season
    Return:
       json data


    """
    self.check_token_active()
    season_stats_url = self.api_path + "season/" + season_key + "/stats/"
    params = {}
    params["access_token"] = self.access_token
    response = self.get_response(season_stats_url, params)
    return response
  
  def get_season_points(self, season_key):
    """Calling Season Points API.

    Arg:
       season_key: key of the season
    Return:
       json data


    """
    self.check_token_active()
    season_points_url = self.api_path + "season/" + season_key + "/points/"
    params = {}
    params["access_token"] = self.access_token
    response = self.get_response(season_points_url, params)
    return response
  
  def get_season_player_stats(self, season_key, player_key):
    """Calling Season Player Stats API.

    Arg:
       season_key: key of the season
       player_key: key of the player
    Return:
       json data


    """
    self.check_token_active()
    season_player_stats_url = self.api_path + "season/" + season_key + "/player/" + player_key + "/stats/"
    params = {}
    params["access_token"] = self.access_token
    response = self.get_response(season_player_stats_url, params)
    return response

  def get_overs_summary(self, match_key):
    """Calling Overs Summary API

    Arg:
       match_key: key of the match
    Return:
       json data



    """
    self.check_token_active()
    overs_summary_url = self.api_path + "match/" + match_key + "/overs_summary/"
    params = {}
    params["access_token"] = self.access_token
    response = self.get_response(overs_summary_url, params)
    return response

  def get_news_aggregation(self):
    """Calling News Aggregation API

    Return:
       json data


    """
    self.check_token_active()
    news_aggregation_url = self.api_path + "news_aggregation" + "/"
    params = {}
    params["access_token"] = self.access_token, 
    response = self.get_response(news_aggregation_url, params)
    return response
