import os
import sys
import logging
import traceback
from optparse import OptionParser
from tabulate import tabulate  # Import tabulate for structured output
import random

from symbolic.loader import *
from symbolic.explore import ExplorationEngine

print("🔍 PyExZ3 - Python Exploration with Z3 🔍")

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
    parser.error("❌ Error: Missing Python file for execution!")
    sys.exit(1)

solver = "cvc" if options.cvc else "z3"
filename = os.path.abspath(args[0])

# Get the object describing the application
app = loaderFactory(filename, options.entry)
if app is None:
    sys.exit(1)

print(f"🚀 Exploring `{app.getFile()}.{app.getEntry()}` using `{solver.upper()}` Solver")

result = None
total_assertion_errors = 0
test_cases = []  # Store test case results

try:
    log_folder = os.path.abspath(options.logfolder)
    os.makedirs(log_folder, exist_ok=True)

    for iteration in range(options.max_iters):
        log_filename = os.path.join(log_folder, f"iteration_{iteration + 1}.log")
        logger = logging.getLogger(f"Iteration_{iteration + 1}")
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(log_filename)
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        try:
            engine = ExplorationEngine(app.createInvocation(), solver=solver)
            generatedInputs, returnVals, path = engine.explore(options.max_iters)
            result = app.executionComplete(returnVals)

            if options.dot_graph:
                dot_filename = os.path.join(log_folder, f"{filename}_{iteration+1}.dot")
                with open(dot_filename, "w") as file:
                    file.write(path.toDot())

            if result is not None and result is not True:
                total_assertion_errors += 1
                logger.error(f"🚨 AssertionError: {result}")
            else:
                for i, test_case in enumerate(generatedInputs):
                    if i >= 10:
                        break
                    test_cases.append([i + 1, str(generatedInputs[i]), returnVals[i]])  # Store formatted test cases

        except ImportError as e:
            logger.error(f"❌ ImportError: {e}")
            sys.exit(1)

        except AssertionError as e:
            total_assertion_errors += 1
            logger.error(f"🚨 AssertionError: {e}")
            continue

        except Exception as e:
            logger.error(f"⚠️ Exception: {e}")
            continue

except Exception as e:
    logging.error(f"💥 Critical Error: {e}")

# Display results in tabular format
if test_cases:
    print("\n📊 **Generated Test Cases:**")
    print(tabulate(test_cases, headers=["Path", "Input", "Output"], tablefmt="grid"))

# Display Total Paths Explored
#print(f"\n✅ **Total Paths Explored:** {len(test_cases)}")

# Calculate and print Condition Coverage Percentage
coverage = (total_assertion_errors / options.max_iters) * 100 if options.max_iters > 0 else 0
print(f"\n📈 **Condition Coverage using DSE:** {coverage:.2f}%\n")

sys.exit(0)
