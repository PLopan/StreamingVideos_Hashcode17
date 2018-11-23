import time
from problem_data import ProblemData

dataset = 'kittens'
input_file = 'input_datasets/{}.in'.format(dataset)
output_file = 'output/' + dataset + '.out'

if __name__=='__main__':
    start_time = time.time()
    data = ProblemData()
    data.load_data(input_file)
    data.compute_video_values()
    data.compute_total_values()
    data.fill_caches()
    data.write_output_file(output_file)
    print("Executed in {} seconds.".format(time.time() - start_time))
