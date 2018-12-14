""" HN historic """
import requests, json, pickle, csv
from bs4 import BeautifulSoup
from utilities.functional_utils import *
from retrieving_posts import *
from data.helpers import months_and_days, month_index
from collections import Counter
from matplotlib import pyplot as plt


# Getting frequency of occurance of given site for each month since Oct 2015
def get_freqs(target):
	results = []
	# count the target sites occurances for each month
	for each in month_index:
		# for outputting purposes
		month = each[0] + "-" + each[1]
		# get all posts of month
		posts_in_month = []
		csv_file = "data/results/" + each[1] + "-" + each[0] + ".csv"
		
		with open(csv_file) as f:
			csv_reader = csv.reader(f)
			for row in csv_reader:
				posts_of_day = eval(row[1])
				for each in posts_of_day:
					posts_in_month.append(each)

		# count the target sites occurances
		target_frequency = posts_in_month.count(target)
		# add result for month to overall results
		results.append((month, target_frequency))
	return results

def get_frequencies(target):
	if isinstance(target, str):
		res = get_freqs(target)
		return res
	else:
		res = {}
		for each in target:
			each_res = get_freqs(each)
			res[each] = each_res
		return res

# print(get_frequencies("github.com"))
# print(get_frequencies(["nytimes.com", "github.com"]))



# Graphing frequency of occurance of given site for each month since Oct 2015
def plot_sequence(seq):
	months = []
	freq_count = []
	for each in seq:
		months.append(each[0])
		freq_count.append(each[1])
	plt.plot(months, freq_count)


def graph_frequencies(target):
	plt.title("Appearances on HN")
	plt.xlabel("Months")
	plt.xlabel("Frequency")

	if isinstance(target, str):
		results = get_frequencies(target)
		plot_sequence(results)
		plt.show()
	else:
		results = get_frequencies(target)
		titles = []
		for k, v in results.items():
			titles.append(k)
			plot_sequence(v)

		plt.legend(titles)
		plt.show()

graph_frequencies("scientificamerican.com")
# graph_frequencies(["yahoo.com", "google.com"])



# Getting posts that occured most frequently in a certain time interval
def get_top_in_interval(start_month, start_year, end_month, end_year, top_x=50):
	""" Get all posts of interval. Frequency rank them. Print out results for requested period. """
	all_posts = get_all_posts_of_interval(start_month, start_year, end_month, end_year)
	# using Counter from collections module to get a count for each element in the list of all posts
	counter = Counter(all_posts)
	# sorting the dict-like return value of Counter according to each elements count/frequency
	sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
	# get top x 
	res = sorted_counter[:top_x]
	# print results
	rank = 1
	for each in res:
		print(str(rank) + ". " + each[0] + " - " + str(each[1]))
		rank += 1
	return res

# Getting posts that occured most frequently since we have data (Oct 2015)
def get_top(x_top):
	res = get_top_in_interval("10", "2015", "11", "2018", x_top)
	return res

# get_top_in_interval("09", "2017", "11", "2018", 100)
# get_top(35)
