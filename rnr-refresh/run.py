#!/usr/bin/env python3

import sys
import argparse
import importlib
import readconfig as cfg

from method import *
from writelog import *

true_values = ['True', 'true', 'TRUE', 'T', 't']
false_values = ['False', 'false', 'FALSE', 'F', 'f']

# Execution happens here
def main():
    # Start logging
    #start_log()
    
    # Set up command-line parser
    cmdparser = argparse.ArgumentParser()
    cmdparser.add_argument("configpath",
                            help="Path to configuration file (.cfg); defaults to using config/default.cfg",
                            nargs='?',
                            default="config/default.cfg")
    args = cmdparser.parse_args()
    if args.configpath == "config/default.cfg":
        log_it("No configuration file was selected; using " + args.configpath)
    
    log_it("=====\n Run started\n")
    
    # Genreal-purpose dictionary that gets passed everywhere
    hotpotato = {}
    
    # Read the config file
    hotpotato = cfg.read_config(args.configpath)
    
    # Ensure proper conversion of config file and header parameters in dictionary
    hotpotato = cfg.convert_values(hotpotato)
    
    # Dynamically import and call the main function of each method defined in cfg
    for x in get_value(hotpotato, 'methods'):
        if (x == 'data'):
            continue
        temp = __import__(x + '_method')
        print(hotpotato)
        hotpotato = temp.main(hotpotato)
        print(hotpotato)
    # Exit cleanly
    log_it("\n Current run tasks completed \n=====")
    sys.exit()
    
    #===============================
    # Optional Steps
    #  Basic error checking of config
    #===============================


####################
##     MAIN       ##
####################

if __name__ == "__main__":
    main()

