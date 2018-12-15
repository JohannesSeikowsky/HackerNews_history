"""
 Module for retrieving the top 30 posts on HN for any given day.

 Structure
 - get all available timestamps - one randomly chosen tiemstamp for each day that HN has been crawled by the WayBackMachine
 - retrieve the timestamp of the particular day for which you want to get the top HN posts
 - get that day's html from the WBM by using the relevant timestamp in a request
 - from the returned html, parse out the top HN posts
"""

import json, pickle, csv
# import requests
# from bs4 import BeautifulSoup
from utilities.functional_utils import *
from data.helpers import months_and_days, month_index
from collections import Counter
from matplotlib import pyplot as plt


# get all timestamps - one randomly chosen one for each day
timestamps = pickle_in("data/timestap_for_each_day.pickle")

# extracting posts for a day
def get_html_of_day(day_code):
	timestamp_of_day = timestamps[day_code]
	res = requests.get("http://web.archive.org/web/{}/https://news.ycombinator.com".format(timestamp_of_day))
	return res.text

def extract_posts_from_html(input_html):
	soup = BeautifulSoup(input_html, "html.parser")
	links = soup.findAll("span", {"class": "sitestr"})
	urls = []
	for each in links:
		urls.append(each.text)
	return urls

def get_posts_of_a_day(target_day):
	days_html = get_html_of_day(target_day)
	days_posts = extract_posts_from_html(days_html)
	return days_posts


# extracting posts of a month
def extract_posts_of_a_month(year, month, no_of_days):
	# getting day codes
	day_codes = []
	for each in range(1, no_of_days+1):
		each = str(each)
		if len(each) == 1:
			each = "0" + each

		day_code = year + month + each
		day_codes.append(day_code)
	print(day_codes)

	# getting top posts
	csv_path = "data/results/" + year + "-" + month + ".csv"
	failed_days = []
	for each in day_codes:
		try:
			res = get_posts_of_a_day(each)
			print(res)
			write_to_csv(csv_path, [each, res])
		except Exception as e:
			failed_days.append(each)
			print("\n\n", e, "\n\n")

	# recording those days that didn't work out
	for each in failed_days:
		with open("data/failed_days.txt", "a") as f:
			f.write(each + "\n")


# extracting posts of a year
def get_posts_of_a_year(year):
	# extract for a given year all posts and puts the posts of each month of that
	# year in its own file
	for each in months_and_days:
		try:
			month = each[0]
			no_of_days = each[1]
			extract_posts_of_a_month(year, month, no_of_days)
		except:
			pass


def get_all_posts_of_interval(start_month, start_year, end_month, end_year):
	"""gets all posts that were on HN in the provided time interval.
		(so far just occurance - we're not accunting for position)
		Pass single digit months like so - "01" """

	start_index = month_index.index((start_month, start_year))
	end_index = month_index.index((end_month, end_year))

	all_posts = []
	for each_index in range(start_index, end_index+1):
		month = month_index[each_index]
		csv_file = month[1] + "-" + month[0] + ".csv"

		with open("data/results/" + csv_file) as f:
			reader = csv.reader(f)

			for row in reader:
				# print(row)
				posts_lists = eval(row[1])

				for each in posts_lists:
					all_posts.append(each)
	return all_posts
