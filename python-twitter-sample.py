#!/usr/bin/python
#Created : Thu 06 Aug 2015 02:15:25 PM MYT
#Last Modified : Fri 21 Aug 2015 05:05:53 PM UTC

import site
import os
import sys
import twitter

CONSUMER_SECRET = "pd4FVhqBHYkCvNwLnREvmPLmzakU5XL8iuMtfalAw7xu650kV6"

CONSUMER_KEY = "nybx7FHQTJl7u3I9rOpJrmduw"

ACCESS_TOKEN = "16709672-2CtfNKKaJWE1dTDz6M0EbBOCsvQ3DiQ9OjVQpjQsh"

ACCESS_TOKEN_SECRET = "YEiR4IizOObY9mjnTtcpAfobjrAsmIKZPwTj0SMeA1Els"

api = twitter.Api(CONSUMER_KEY,
                    CONSUMER_SECRET,
                    ACCESS_TOKEN,
                    ACCESS_TOKEN_SECRET)


#print api.VerifyCredentials()

#story = raw_input("Type the status here: \n")

#status = api.PostUpdate(story)

#user = "awangjangok"
#text = "cubaan sekali lagi"

#d = api.PostDirectMessage(user, text)

#aku = api.GetFriends("awangjangok")

#home = api.GetHomeTimeline()

#print home

#direct = api.PostDirectMessage(user, text)

#statuses = api.GetUserTimeline(screen_name="sirjoelabi")

#print [s.text for s in statuses]

d = api.PostDirectMessage(screen_name="@awangjangok", text="Usaha tangga kejayaan") #successful
