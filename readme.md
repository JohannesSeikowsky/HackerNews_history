## HackerNews_history

Graph how often specific website(s) appeared on HN each month since Oct 2015.

Get the x most-frequently-occurring websites on HN for particular time period(s).


#### Use
`git clone https://github.com/JohannesSeikowsky/HackerNews_history.git`

`pip3 install matplotlib`

`cd hn_history`

`python3 main.py`

`run command you want in terminal`


#### Commands

`graph("scientificamerican.com")`

graphs no of appearances of scientificamerican.com for each month since Oct 2015

`graph(["yahoo.com", "google.com", "vox.com"])`

graphs no of appearances of yahoo, google and vox on the same graph

`get_top(35)`

displays top 35 sites between Oct 2015 and Nov 2018

`get_top_in_interval("03", "2017", "07", "2018")`

displays top 50 sites between March 2017 and July 2018

`get_top_in_interval("10", "2017", "10", "2018", 111)`

displays top 111 between October 2017 and October 2018


#### Background
I queried the Waybackmachine for all available snapshots of HackerNews.
For each available day I randomly chose one of the timestamps of that day,
retrieved it's HTML and extracted the top30 posts. I saved the results in csv files,
one for each month (in data/results). The main function of HackerNews_history
are relatively simple functions executed on these results.


For questions, write me - joseikowksy@gmail.com