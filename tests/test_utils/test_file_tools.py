from src.utils.file_tools import is_image_file


def test_is_image_file():
    file_name = 'abc.txt'
    assert not is_image_file(file_name)

    file_name = 'abc.png'
    assert is_image_file(file_name)

    file_name = '.abc.png'
    assert not is_image_file(file_name)
    assert is_image_file(file_name, ignore_hidden_file=False)

