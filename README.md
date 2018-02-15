# py-cricket library for Roanuz Cricket API
py-cricket library for Python using Roanuz Cricket API's.  Easy to install and simple way to access all Roanuz Cricket API's. Its a Python library for getting Live Cricket Score, Cricket Schedule and Statistics.


## Getting started
1. Install py-cricket using `pip install py-cricket`

2. Create a Cricket API App here [My APP Login](https://www.cricketapi.com/login/?next=/apps/)

3. Import pycricket and create Authentication using 'RcaFileStorageHandler' or 'RcaStorageHandler' approach.For accessing each API we need to get the 'AccessToken' 

    ## Example

    ```rust
    //Use your Cricket API Application details below.

    //RcaStorageHandler
    import pycricket
    handler = pycricket.RcaStorageHandler()
    start = pycricket.RcaApp(access_key="Your_AccessKey", \
                            secret_key="Your_SecretKey", \
                            app_id="Your_APP_ID", \
                            store_handler=handler \
                           )

    'OR'

    //RcaFileStorageHandler(from environmental variable)

    Environmental variable:
        RCA_ACCESS_KEY = access_key
        RCA_SECRET_KEY = secret_key
        RCA_APP_ID = app_id

    handler = pycricket.RcaFileStorageHandler()
    start = pycricket.RcaApp(store_handler=handler)

    // After Completing Authentication you can successfully access the API's.

    start.get_match("iplt20_2013_g30") //Return Match information in json format
    start.get_season("dev_season_2014") //Return Season information in json format
    For more free API's visit : https://www.cricketapi.com/docs/freeapi/
    ```


 ### List of Roanuz Cricket API

* [Match API](https://www.cricketapi.com/docs/match_api/)  start.get_match("match_key")
* [Ball by ball API](https://www.cricketapi.com/docs/ball_by_ball_api/) start.get_ball_by_ball("match_key", over_key="over_key")
* [Recent Matches API](https://www.cricketapi.com/docs/recent_match_api/)  start.get_recent_matches()
* [Player Stats API](https://www.cricketapi.com/docs/player_stats_api/)  start.get_player_stats("player_key", "league_or_board_key")
* [Recent Season API](https://www.cricketapi.com/docs/recent_season_api/)  start.get_recent_seasons()
* [Schedule API](https://www.cricketapi.com/docs/schedule_api/)  start.get_schedule()
* [Season API](https://www.cricketapi.com/docs/season_api/)  start.get_season("season_key")
* [Season Stats API](https://www.cricketapi.com/docs/season_stats_api/)  start.get_season_stats("season_key")
* [Season Team API](https://www.cricketapi.com/docs/season_team_api/)  start.get_season_team("season_key", "season_team_key")
* [Season Points API](https://www.cricketapi.com/docs/season_points_api/)  start.get_season_points("season_key")
* [Season Player Stats API](https://www.cricketapi.com/docs/season_player_stats_api/)  start.get_season_player_stats("season_key", "player_key")
* [Over Summary API](https://www.cricketapi.com/docs/over_summary_api/)  start.get_overs_summary("match_key")
* [News Aggregation API](https://www.cricketapi.com/docs/news_aggregation_api/)  start.get_news_aggregation()

 ## Roanuz Cricket API 
	This Library uses the Roanuz Cricket API for fetching cricket scores and stats.
    Learn more about Litzscore Cricket API on https://www.cricketapi.com/ 

 ## Contact:
    Feel free to call us anytime, We have an amazing team to support you.
    You can contact us at : support@cricketapi.com
