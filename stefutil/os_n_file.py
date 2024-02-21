"""
os-related
"""

import os
from os.path import join as os_join
from pathlib import Path
from typing import Union


__all__ = ['get_hostname', 'stem']


def get_hostname() -> str:
    return os.uname().nodename


def stem(path: Union[str, Path], keep_ext=False, top_n: int = None) -> Union[str, Path]:
    """
    :param path: A potentially full path to a file
    :param keep_ext: If True, file extensions is preserved
    :param top_n: If given, keep the top `top_n` parent directories
    :return: The file name, without parent directories
    """
    if top_n:
        ret = stem(path=path, keep_ext=keep_ext, top_n=None)
        if isinstance(path, Path):

            dirs = []
            for _ in range(top_n):
                path = path.parent
                dirs.append(path.name)
            dirs.reverse()
        else:
            dirs = path.split(os.sep)
            dirs = dirs[-top_n-1:-1]
        return os_join(*dirs, ret)
    else:
        return os.path.basename(path) if keep_ext else Path(path).stem


if __name__ == '__main__':
    def check_stem():
        n = 3
        path = __file__
        path_ = Path(path)
        print(path)
        print(stem(path, top_n=n))
        print(path_)
        print(stem(path_, top_n=n))
    check_stem()
