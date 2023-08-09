#!/home/coder/miniconda/bin/python
import json
import os
import re
import sys
from os.path import isfile, join
from xml.etree import ElementTree
from shutil import copy2
import pytest
import numpy as np


def grade():
    copy_submission()
    assignment = find_assignment()
    # Report written to an XML file (`--junitxml` flag), which you can parse
    sys.path.append(os.path.join(os.path.dirname(__file__), 'solutions'))
    log_file = '/grader/log.xml'
    result = pytest.main([f'autograde/tests/test_{assignment}', f'--junitxml={log_file}'])

    if result == pytest.ExitCode.OK:
        write_feedback(1.0, "You've passed this assignment! You're ready to move on to the next topic.")
    elif result == pytest.ExitCode.TESTS_FAILED:
        score = get_score(log_file)
        write_feedback(score, get_failure_message(log_file))
    else:
        write_feedback(0.0, "We were unable to grade your submission. Please reach out to us in the forums.")

def copy_submission():
    # Coursera recommends copying submissions out of '/shared/submission'
    # before attempting to assess them.
    submit_path = '/shared/submission'
    os.mkdir('/grader')
    # Note that I'm not recursing into a directory of files.
    # You will need a different solution if the assignment uses multiple files.
    files = [f for f in os.listdir(submit_path) if isfile(join(submit_path, f))]
    for file in files:
        copy2(join(submit_path, file), join('/grader', file))
    sys.path.append('/grader')


def find_assignment():
    assign_path = '/grader'
    files = [f for f in os.listdir(assign_path) if isfile(join(assign_path, f))]
    for file in files:
        # My favorite Twitter joke this week:
        # the name for a group of regexes is 'regrets'
        if re.match(r'assessment\d?\.py', file):
            return file


def get_failure_message(log_location):
    # Only grabbing the first failure in the report.
    # You could certainly offer a full report to learners.
    doc = ElementTree.parse(log_location)
    root = doc.getroot()
    out = ''
    for failure in root.iter('failure'):
        message = failure.get('message')
        break_index = message.find('\n')
        if break_index >= 0:
            message = message[:break_index]
        if 'AssertionError' in message:
            out += message + '\n'
        else:
            out += message + '\n'
    return out


def write_feedback(score, message):
    document = {'fractionalScore': score, 'feedback': message}
    with open('/shared/feedback.json', 'w') as feedback:
        json.dump(document, feedback)

def get_score(log_file):
    doc = ElementTree.parse(log_file)
    root = doc.getroot()
    test = root.findall('testsuite')[0]
    ntests = float(test.get('tests'))
    nfailed = float(test.get('errors')) + float(test.get('failures')) + float(test.get('skipped'))
    return (ntests - nfailed) / ntests

# def test_solutions():
#     sys.path.append(os.path.join(os.path.dirname(__file__), 'solutions'))
#     log_file = './log.xml'
#     pytest.main(['-rA', 'autograde/tests/', f'--junitxml={log_file}'])
#     score = get_score(log_file)
#     print(get_failure_message(log_file))
#     print(f'Score = {score*100}')

def test_solutions():
    sys.path.append(os.path.join(os.path.dirname(__file__), 'solutions'))
    sys.path.append(os.path.join(os.path.dirname(__file__), 'assessment_evaluation'))
    log_file = './log.xml'
    pytest.main(['-rA', 'autograde/tests/', f'--junitxml={log_file}'])
    score = get_score(log_file)
    print(get_failure_message(log_file))
    print(f'Score = {score*100}')

if __name__ == "__main__":
    os.chdir('/home/coder/project/')
    workspace = os.environ.get('WORKSPACE_TYPE')
    if workspace is None:
        # Variable not set when running in autograder environment.
        # Run grading script on learner submission.
        grade()
    elif workspace == 'instructor':
        test_solutions()
