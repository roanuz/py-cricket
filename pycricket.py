#!/usr/bin/env python
#
# Copyright 2016  Roanuz Softwares Private Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import requests
import ssl
import json
import logging
from datetime import datetime

# To avoid request library waring uncomment below two line
# import requests.packages.urllib3
# requests.packages.urllib3.disable_warnings()

from pycricket_storagehandler import *

logger = logging.getLogger('RcaApp')
logger.setLevel(logging.ERROR) #Now we handled INFO or ERROR level
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


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
        logger.info('Getting new access token')
        return True
      else:
        msg = "Error getting access_token, " + \
          "please verify your access_key, secret_key and app_id"
        logger.error(msg)
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
      response_data = json.loads(requests.post(url, params=params).text)
    else:
      response_data = json.loads(requests.get(url, params=params).text)
    
    if not response_data['status_code'] == 200:
      if "status_msg" in response_data:
        logger.error("Bad response: " + response_data['status_msg'])
      else:
        logger.error("Some thing went wrong, please check your " + \
                  "request params Example: card_type and date")

    return response_data

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
        logger.info('Access token expired, going to get new token')
        self.auth()
      else:
        expire_time = self.store_handler.get_value("expires")
        self.access_token = self.store_handler.get_value("access_token")
        logger.info('Access token noy expired yet')
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
  
  def get_season(self, season_key, card_type="micro_card"):
    """Calling Season API.

    Arg:
       season_key: key of the season
       card_type: optional, default to micro_card. Accepted values are 
       micro_card & summary_card 
    Return:
       json data


    """
    self.check_token_active()
    season_url = self.api_path + "season/" + season_key + "/"
    params = {}
    params["access_token"] = self.access_token
    params["card_type"] = card_type
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
    print "overs_summary_url", overs_summary_url
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