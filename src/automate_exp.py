'''
Automate Many experiments of Throttlebot
'''

import argparse
from run_throttlebot import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_runs", help="Number of times to run the experiment")
    parser.add_argument("--config_file1", help="Configuration File for Throttlebot Execution")
    parser.add_argument("--resource_config", help='Default Resource Allocation for Throttlebot')
    args = parser.parse_args()

    for count in range(int(args.num_runs)):
        sys_config, workload_config, filter_config = parse_config_file(args.config_file1)
        
        mr_allocation = parse_resource_config_file(args.resource_config, sys_config)

        mr_allocation = filter_mr(mr_allocation,
                                  sys_config['stress_these_resources'],
                                  sys_config['stress_these_services'],
                                  sys_config['stress_these_machines'])

        run(sys_config, workload_config, filter_config, mr_allocation)
