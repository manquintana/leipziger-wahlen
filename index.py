#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:28:11 2026

@author: mqu
"""

import pandas as pd

data_url = "https://statistik.leipzig.de/opendata/api/values?kategorie_nr=15&rubrik_nr=6&periode=d&format=json"
df_votes = pd.read_json(data_url)

df_votes = df_votes.drop(["merkmal_1", "merkmal_2", "merkmal_3", "merkmal_4", "periode", "kategorie_Nr", "rubrik_Nr", "jahr", "uri", "id", "einheit", "kategorie", "rubrik"], axis = 1)
df_votes = df_votes.rename(columns={"name": "party","wert": "value", "jahr_Nr": "year"})

df_votes["year"] = df_votes["year"].astype(str).str[0:4]

df_votes.to_json("data/historic.json")
df_votes.to_csv("data/historic.csv", index = None)
