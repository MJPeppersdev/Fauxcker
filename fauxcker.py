#!/usr/bin/python
from docopt import docopt

import fauxcker
from fauxcker.base import BaseDockerCommand
from fauxcker.pull import PullCommand
from fauxcker.images import ImagesCommand
from fauxcker.run import RunCommand

if __name__ == '__main__':
    arguments = docopt(fauxcker.__doc__, version=fauxcker.__version__)
    command = BaseDockerCommand
    if arguments['pull']:
        command = PullCommand
    elif arguments['images']:
        command = ImagesCommand
    elif arguments['run']:
        command = RunCommand

        cls = command(**arguments)
        cls.run(**arguments)
