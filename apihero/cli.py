import os
from .builder import MultiPageBuilder


def main(argv=None):
    base_dir = os.getcwd()
    output_dir = os.path.join(base_dir, 'output')
    wrapper = MultiPageBuilder(base_dir, output_dir)
    wrapper.build()
