from monit.monit_cli import Monit


def int_or_str(value):
    try:
        return int(value)
    except ValueError:
        return value


__version__ = '1.0.3'
VERSION = tuple(map(int_or_str, __version__.split('.')))

__all__ = ['Monit']
