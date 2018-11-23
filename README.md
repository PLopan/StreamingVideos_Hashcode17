# Streaming videos - Google Hashcode 2017
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)

Solution to the 2017 Google hashcode online qualification round about streaming videos

## Algorithm

The algorithm is inspired by a greedy approach to solve the [knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem).

First, for each endpoint we compute the value of a (video, cache) pair as the time saved placing the video in the cache server
times the number of requests it has, we divide that amount over the size in MB it takes in the cache server, 
this way we get a time saved per MB value. Following this, we consider an overall score for a (video, cache) pair as sum
of the values of that pair for every endpoint. So the pairs with the biggest overal value are the first ones to be chosen.

## Solutions obtained
The scores have been calculated with @vitowalteranelli repository code. [REPO](https://github.com/vitowalteranelli/Google-HashCode-Playground)

The scores obtained are the following:

| File                   | Execution time | Score   |
|------------------------|:--------------:|:-------:|
| me_at_the_zoo          | 0,02s          | 414.342 |
| videos_worth_spreading | 1,11s          | 252.701 |
| trending_today         | 13,8s          |  25.630 |
| kittens                | 117,6s         |  75.138 |
| OVERALL                | 132,53s        | 767.811 |

I have noticed that the main issue with my algorithm is that since most endpoints are connected to the same
cache servers, I am wasting a lot of cache space placing the videos in several cache servers, so it may be better to 
just include each video in one cache server. 


The second version takes into account that each video can only be placed in one cache and we get the following results:

| File                   | Execution time | Score    |
|------------------------|:--------------:|:--------:|
| me_at_the_zoo          |   0,005s       | 401.234  |
| videos_worth_spreading |   1,20s        | 164.770  |
| trending_today         |  14,14s        | 499.979  |
| kittens                | 125,5s         | 1.008.080|
| OVERALL                | 140,845s       | 2.074.063|

As we can see in the table, the results are way better (in videos_worth_spreading is where more points are lost).
To see it in perspective, during the qualification round the maximun score was 2.651.999, whereas in the extended round
the maximun score was 2.653.781. The final algorithm achieves really good scores taking into consideration its speed.
 
## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.