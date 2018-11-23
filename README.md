# Streaming videos - Google Hashcode 2017
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)

Solution to the 2017 Google hashcode online qualification round about streaming videos

## Algorithm

The algorithm is inspired by a greedy approach to solve the [knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem).
More explanation to come...

## Solutions obtained
The scores have been calculated with @vitowalteranelli repository code. [REPO](https://github.com/vitowalteranelli/Google-HashCode-Playground)

The scores obtained are the following:

| File                   | Execution time | Score   |
|------------------------|:--------------:|:-------:|
| me_at_the_zoo          | 0.02s          | 414.342 |
| videos_worth_spreading | 1.11s          | 252.701 |
| trending_today         | 13.8s          | 25.630  |
| kittens                | 117.6s         | 75.138  |

I have noticed that the main issue with my algorithm is that since most endpoints are connected to the same
cache servers, I am wasting a lot of cache space placing the videos in several cache servers, so it may be better to just include each video in one cache server. This will be implemented
in the next version of the program.

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.