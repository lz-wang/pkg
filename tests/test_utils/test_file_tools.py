from src.utils.file_tools import is_image_file, find_files
from env import TEST_DATA_ROOT
import os


def test_is_image_file():
    file_name = 'abc.txt'
    assert not is_image_file(file_name)

    file_name = 'abc.png'
    assert is_image_file(file_name)

    file_name = '.abc.png'
    assert not is_image_file(file_name)
    assert is_image_file(file_name, ignore_hidden_file=False)


def test_find_files():
    files_root = os.path.join(TEST_DATA_ROOT, 'files')
    assert len(find_files(files_root, False, False)) == 10
    assert len(find_files(files_root, False, True)) == 7
    assert len(find_files(files_root, True, False)) == 6
    assert len(find_files(files_root, True, True)) == 5
    assert len(find_files(files_root)) == 5
