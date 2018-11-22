import time
from problem_data import ProblemData

input_file = 'input_datasets/me_at_the_zoo.in'
output_file = 'me_at_the_zoo.out'

if __name__=='__main__':
    start_time = time.time()
    data = ProblemData()
    data.load_data(input_file)
    data.compute_video_values()
    data.compute_total_values()
    data.fill_caches()
    print("Executed in {} seconds.".format(time.time() - start_time))
