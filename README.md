# py-cricket Library for Python from Roanuz Cricket API
Cricket API Library for Python using Roanuz Cricket API's.  Easy to install and simple way to access all Cricket API's. Its a Python library for showing Live Cricket Score, Cricket Schedule and Statistics.

Avialble match and season for testing are,
* `[match key ="iplt20_2013_g30"]`
* `[season key="dev_season_2014"]`


## Get Started
1. install py-cricket using 'pip install py-cricket'

2. Create a Cricket API App [My APP Login](https://www.cricketapi.com/login/?next=/apps/)

3. Import py-cricket and create Authentication using 'RcaFileStorageHandler' or 'RcaStorageHandler' approach. For accessing each API     we need to get the 'AccessToken'
   
   ## Example
   ```rust
   //Use your Cricket API Application detailas below.

   i). Handler = RcaStorageHandler()
       start = py-cricket.RcaApp(
                  "Your_AccessKey", \
                  "Your_ScreteKey", \
                  "Your_APP_ID", \
                  Handler
               )

   'OR'

   ii). Handler = RcaFileStorageHandler()
        start = py-cricket.RcaApp(
                   "Your_AccessKey", \
                   "Your_ScreteKey", \
                   "Your_App_ID", \
                   Handler
                )
    // After Completing Authentication you can successfully access the API's. For example,  

    Match API   start.get_match("iplt20_2013_g30") //Return Match information in json format
    Season API  start.get_season("dev_season_2014") //Return Season information in json format
    ```  


### Here is List of Roanuz Cricket API's

* [Match API](https://www.cricketapi.com/docs/match_api/).  'get_match("match_key")'
* [Recent Matches API](https://www.cricketapi.com/docs/recent_match_api/).  'get_recent_matches()'
* [Recent Season API](https://www.cricketapi.com/docs/recent_season_api/).  'get_recent_seasons()'
* [Schedule API](https://www.cricketapi.com/docs/schedule_api/).  'get_schedule()'
* [Season API](https://www.cricketapi.com/docs/season_api/).  'get_season("season_key")'
* [Season Stats API](https://www.cricketapi.com/docs/season_stats_api/).  'get_season_stats("season_key")'
* [Season Points API](https://www.cricketapi.com/docs/season_points_api/).  'get_season_points("season_key")'
* [Season Player Stats API](https://www.cricketapi.com/docs/season_player_stats_api/).  'get_season_player_stats("season_key", "player_key")'
* [Over Summary API](https://www.cricketapi.com/docs/over_summary_api/).  'get_overs_summary("match_key")'
* [News Aggregation API](https://www.cricketapi.com/docs/news_aggregation_api/).  'get_news_aggregation()'



## Roanuz Cricket API
This Library uses the Roanuz Cricket API for fetching cricket scores and stats. Learn more about Litzscore Cricket API on https://www.cricketapi.com/ . Feel free to contact their amazing support team, if you got struck.
