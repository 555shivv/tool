# [Internal Documentation] Python DSE Tool Installation Guide

<table width="100%">
  <tr>
    <td><strong>Author:</strong> Sarvan Shivani</td>
    <td align="right"><strong>Last Updated:</strong> 27-03-2025</td>
  </tr>
</table>

This document provides step-by-step instructions to install the Python-based DSE tool on any Ubuntu system.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Tested Versions](#tested-versions)
3. [Dependency overview](#dependency-overview)
4. [Prerequisites](#prerequisites)
5. [Step-by-Step Installation](#step-by-step-installation)
6. [Usage](#usage)
7. [Troubleshooting and Resources](#troubleshooting-and-resources)
8. [License](#license)

---

## Introduction

Dynamic symbolic execution is a structural testing technique that systematically explores feasible paths of the program under test by running the program with different test
inputs to improve code coverage. This tool is designed to automate the process of dynamic symbolic execution for Python programs.
---

## Tested Versions

The following versions were used during testing:

- **Ubuntu Version:** Ubuntu 24.04.1 LTS
- **Tool Versions:**
  - python : v3.12.3
  - z3 : v4.13.3

---


## Prerequisites

Ensure the following are in place before beginning the installation:

- Ubuntu 20.04 or later
- Internet connection
- Administrator privileges (sudo access)

---

## Step-by-Step Installation

1. **Update System:**

   It is important to keep your system packages up-to-date to ensure compatibility and security.

   ```bash
   sudo apt-get update
   ```

2. **Install Dependencies:**

   Here we install the following dependencies:

   ```bash
   sudo apt-get install -y python-is-python3 python3 git 
   ```

3. **Clone DSE Repository:**

   Clone the ESBMC repository from GitHub to get the latest source code.

   ```bash
   git clone https://github.com/555shiv/tool.git
   ```

4. **Install Z3 python package**
    After cloning github repository navigate to DSE/PyExZ3-clone/PyExZ3-clone folder and run the following commands.
    - 4.1. **Set up python virtual environment**
   Create a new virtual environment and activate it
   ```bash
   python3 -m venv .venv
   ```
   - 4.2. **Activate virtual environment**
   ```bash
   source .venv/bin/activate
   ```
   
    - 4.3. **Install the python package using pip**

    ```bash
   pip install z3
   deactivate
   ```



   - 4.4. **Script file to run the tool**
        - change the mode of script file to run DSE tool

            ```bash
            cd chmod +x dse_run.sh
            ```

   
## Usage

To use DSE:

1. Activate the Virtual Environment (if applicable):

   ```bash
   source ./.venv/bin/activate
   ```

2. Navigate to the PyExZ3-clone Directory:

   ```bash
   cd DSE/PyExZ3-clone/PyExZ3-clone/
   ```

3. Run a Basic Execution Test :

   Use the following command to check if DSE is working correctly

   ```bash
   ./dse_run.sh <path_to_python_file>  [iterations]
   ```

   Example

   ```bash
   ./dse_run.sh test_bench/dfs.py 5
   ```

## Troubleshooting and Resources

If you encounter any issues during the installation, refer to the official documentation or seek help from the community forums.

- [Official DSE Repository](https://github.com/thomasjball/PyExZ3.git)


## License

This documentation is intended solely for guiding users on installing and using the tool. We are not affiliated with the official  repository or its maintainers in any manner. For the official repository and license information, please visit the [DSE GitHub](https://github.com/thomasjball/PyExZ3?tab=readme-ov-file)
