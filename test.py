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

from pycricket import *
import logging

testcase_logger = logging.getLogger('RcaApp test case')
testcase_logger.setLevel(logging.INFO) #Now we used INFO only
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
testcase_logger.addHandler(ch)


def test_rac_library(rca_app):
	free_season_key = 'dev_season_2014'
	free_match_key = 'dev_season_2014_q3'
	player_key = 'player_y2'

	testcase_logger.info("Match (full_card) - " + \
		str(rca_app.get_match(free_match_key)['status']))
	testcase_logger.info("Match (summary_card) - " + \
		str(rca_app.get_match(free_match_key, "summary_card")['status']))
	testcase_logger.info("Match (micro_card) - " + \
		str(rca_app.get_match(free_match_key, "micro_card")['status']))

	testcase_logger.info("Recent Matches (micro_card) - " + \
		str(rca_app.get_recent_matches()['status']))
	testcase_logger.info("Recent Matches (summary_card) - " + \
		str(rca_app.get_recent_matches('summary_card')['status']))
	
	testcase_logger.info("Season - " + \
		str(rca_app.get_season(free_season_key)['status']))

	testcase_logger.info("Season (summary_card) - " + \
		str(rca_app.get_season(free_season_key, 'summary_card')['status']))

	testcase_logger.info("Recent Season Matches - " + \
		str(rca_app.get_recent_season_matches(free_season_key)['status']))

	testcase_logger.info("Recent Season - " + \
		str(rca_app.get_recent_seasons()['status'] ))

	testcase_logger.info("Recent Season  Stats- " + \
		str(rca_app.get_season_stats(free_season_key)['status']))

	testcase_logger.info("Season Points (YYYY-MM-DD) - " + \
		str(rca_app.get_season_points(free_season_key)['status']))

	testcase_logger.info("Season Player Stats - " + \
		str(rca_app.get_season_player_stats(free_season_key, player_key)['status']))

	testcase_logger.info("Schedule - " + \
		str(rca_app.get_schedule()['status']))
	
	testcase_logger.info("Schedule (YYYY-MM) - " + \
		str(rca_app.get_schedule("2016-02")['status']))

	testcase_logger.info("Schedule (YYYY-MM-DD) - " + \
		str(rca_app.get_schedule("2016-02-02")['status']))
		
	testcase_logger.info("Overs Summary - " + \
		str(rca_app.get_overs_summary(free_match_key)['status']))

	testcase_logger.info("News Aggregation - " + \
		str(rca_app.get_news_aggregation()['status']))


print "-----------------------"
print "Using RcaStorageHandler"
print "-----------------------"

#RcaStorageHandler
cache_handler = RcaStorageHandler()
rca_app = RcaApp(
              "access_key", \
              "secret_key", \
              "com.yourcompany.appname", \
              cache_handler
            )

test_rac_library(rca_app)

print ""
print "---------------------------"
print "Using RcaFileStorageHandler"
print "---------------------------"

# RcaFileStorageHandler
file_cache_handler = RcaFileStorageHandler()
rca_app = RcaApp(
              "access_key", \
              "secret_key", \
              "com.yourcompany.appname", \
              file_cache_handler
            )

test_rac_library(rca_app)
print "---------------------------"
print "Done"


