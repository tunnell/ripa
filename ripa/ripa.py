# -*- coding: utf-8 -*-

import click
import subprocess
import sys

"""Main module."""

def process(todo):
    """Install list of requirements

    'todo' is a list of Requiments objects from the requirements
    parser.  This function installs them by first Anaconda and, if
    that fails, pip.
    """

    # For each requirement, determine if in Anaconda                                                                                                                                                                                          
    pip_todo = {}

    for req in todo:
        if len(req.specs) and len(req.specs[0]):
            command = 'conda install -y %s=%s' % (req.name, req.specs[0][-1])
        else:
            command = 'conda install -y %s' % (req.name)

        try:
            output = subprocess.check_output(command,
                                             stderr=subprocess.STDOUT,
                                             shell=True,
                                             universal_newlines=True)
        except subprocess.CalledProcessError as exc:
            command2 = 'pip install -q %s' % req.line
            pip_todo[req.name] = command2
        else:
            click.echo('Anaconda: %s' % req.name)    


        # Do rest                                                                                                                                                                                                                                 
    for name, command2 in pip_todo.items():
        try:
            output = subprocess.check_output(command2,
                                             stderr=subprocess.STDOUT,
                                             shell=True,
                                             universal_newlines=True)
        except:
            click.ClickException('%s: Failed with pip too' % name)
        else:
            click.echo('pip: %s' % name)
