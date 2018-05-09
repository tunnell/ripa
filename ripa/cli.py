# -*- coding: utf-8 -*-

"""Console script for ripa."""
import sys
import click
import subprocess
import requirements


@click.command()
@click.option('--file', prompt='Requirements file',
              type=click.File('r'),
              default='requirements.txt',
              help='The name of the requirements fiile')
def main(file):
    """Console script for ripa."""

    # For each requirement, determine if in Anaconda                                                                        
    pip_todo = {}
    
    for req in requirements.parse(file):
        command = 'conda install -y %s=%s' % (req.name, req.specs[0][-1])

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

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
