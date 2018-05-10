# -*- coding: utf-8 -*-

"""Console script for ripa."""
import sys
import click
import requirements
from ripa import ripa

@click.command()
@click.option('-r', #prompt='Requirements file',
              type=click.File('r'),
              required=False,
              help='The name of the requirements file')
@click.argument('package', nargs=-1)
def main(r, package):
    """Console script for ripa."""
    todo = []

    print(r, package)
    
    for name in package:
        result = list(requirements.parse(name))[0]
        print(result)
        todo.append(result)

    if r:
        for req in requirements.parse(r):
            todo.append(req)

    ripa.process(todo)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
