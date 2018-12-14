# supporting utility functions
import pickle, requests, json, csv

def pickle_out(pickle_file, input_object):
	pickle_file = open(pickle_file, "wb")
	pickle.dump(input_object, pickle_file)
	pickle_file.close()

def pickle_in(pickle_file):
	pickle_obj = open(pickle_file, "rb")
	res = pickle.load(pickle_obj)
	return res

def write_to_csv(csv_path, row):
	with open(csv_path, "a", newline="") as f:
		writer = csv.writer(f)
		writer.writerow(row)

def query_wbm_for_timestamps(target_site):
	""" query Waybackmachine for all recorded timestamps of target site - other data points are also available """
	data_point = "timestamp"
	wbm_api = "http://web.archive.org/cdx/search/cdx?url=https://{}&fl={}&output=json".format(target_site, data_point)
	resp = requests.get(wbm_api)
	res = json.loads(resp.text)
	return res
