import os
import sys
import logging
import traceback
from optparse import OptionParser
import random

from symbolic.loader import *
from symbolic.explore import ExplorationEngine

print("PyExZ3 (Python Exploration with Z3)")

sys.path = [os.path.abspath(os.path.join(os.path.dirname(__file__)))] + sys.path

usage = "usage: %prog [options] <path to a *.py file>"
parser = OptionParser(usage=usage)

parser.add_option("-l", "--log", dest="logfile", action="store", help="Save log output to a file", default="")
parser.add_option("-s", "--start", dest="entry", action="store", help="Specify entry point", default="")
parser.add_option("-g", "--graph", dest="dot_graph", action="store_true", help="Generate a DOT graph of execution tree")
parser.add_option("-m", "--max-iters", dest="max_iters", type="int", help="Run specified number of iterations", default=1)
parser.add_option("--cvc", dest="cvc", action="store_true", help="Use the CVC SMT solver instead of Z3", default=False)
parser.add_option("--z3", dest="cvc", action="store_false", help="Use the Z3 SMT solver")
parser.add_option("-f", "--folder", dest="logfolder", action="store", help="Specify folder to save log files", default="logs")

(options, args) = parser.parse_args()

if len(args) == 0 or not os.path.exists(args[0]):
    parser.error("Missing app to execute")
    sys.exit(1)

solver = "cvc" if options.cvc else "z3"

filename = os.path.abspath(args[0])

# Get the object describing the application
app = loaderFactory(filename, options.entry)
if app is None:
    sys.exit(1)
#print("Exploring " + app.getFile() + "." + app.getEntry())
entry_point= app.getEntry()
if entry_point:
    print("Exploring "+ app.getFile() + "." + app.getEntry())
else:
    print("Exploring "+ app.getFile() + "(No specific entry point found)")




result = None
total_assertion_errors = 0

try:
    # Create log folder if it doesn't exist
    log_folder = os.path.abspath(options.logfolder)
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    for iteration in range(options.max_iters):
        # Set up log file for this iteration
        log_filename = os.path.join(log_folder, f"iteration_{iteration + 1}.log")
        logger = logging.getLogger(f"Iteration_{iteration + 1}")
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(log_filename)
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        try:
            #engine = ExplorationEngine(app.createInvocation(), solver=solver)
            invocation= app.createInvocation() if app.getEntry() else [filename]
            engine = ExplorationEngine(invocation, solver=solver)
            generatedInputs, returnVals, path = engine.explore(options.max_iters)
            # check the result
            result = app.executionComplete(returnVals)

            # output DOT graph
            if options.dot_graph:
                dot_filename = os.path.join(log_folder, f"{filename}_{iteration+1}.dot")
                with open(dot_filename, "w") as file:
                    file.write(path.toDot())

            if result is not None and result is not True:
                # Log the assertion error
                total_assertion_errors += 1
                logger.error("AssertionError occurred: %s", result)
            else:
                logger.info("Generated Test Cases:")
                for i, test_case in enumerate(generatedInputs):
                    if i >= 10:
                        break
                    # Modify generatedInputs with random numbers
                    logger.info(f"Test Case {i + 1}: {generatedInputs[i]}")

        except ImportError as e:
            # createInvocation can raise this
            logger.error(e)
            sys.exit(1)

        except AssertionError as e:
            # Catch and log assertion errors
            total_assertion_errors += 1
            logger.error("AssertionError occurred: %s", e)
            # Continue exploration with a new test case
            continue

        except Exception as e:
            # Catch and log any other exceptions
            logger.error("An error occurred: %s", e)
            # Continue exploration with a new test case
            continue

except Exception as e:
    logging.error("An error occurred: %s", e)

# Calculate the percentage of assertion errors
if options.max_iters > 0:
    percentage = (total_assertion_errors / options.max_iters) * 100
else:
    percentage = 0

print(f"Condition Coverage using DSE: {percentage}%")

sys.exit(0)


