from slapping.slap_that_like_button import LikeState, slap_many
# vscode now knows src is the source code folder and no longer required.
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ('ll', LikeState.empty),
    ('dd', LikeState.empty),
    ('ld', LikeState.disliked),
    ('dl', LikeState.liked),
    ('ldd', LikeState.empty),
    ('lldd', LikeState.empty),
    ('ddl', LikeState.liked)

])
def test_multi_slaps(test_input, expected):
    assert slap_many(LikeState.empty, test_input) is expected


@pytest.mark.skip(reason="regexes not supported yet")
def test_regex_slaps():
    assert slap_many(LikeState.empty, '[ld]*ddl') is LikeState.liked


@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1


def test_invalid_slap():
    with pytest.raises(ValueError):  # I expect determinated exception
        slap_many(LikeState.empty, "x")


"""def test_db_slap(db_conn):
    db_conn.read_slaps()
    """


def test_print(capture_stdout):
    print("Hello")
    assert capture_stdout["stdout"] == "Hello\n"
