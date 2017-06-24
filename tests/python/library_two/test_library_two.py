from library_two import library_two


def test_library_two_two_happy_path(capsys):
    library_two.two()

    out, err = capsys.readouterr()

    assert out == 'two\n'
