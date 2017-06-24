from library_one import library_one


def test_sanity():
    assert 1 == 1


def test_library_one_one_happy_path(capsys):
    library_one.one()

    out, err = capsys.readouterr()

    assert out == 'one\n'
