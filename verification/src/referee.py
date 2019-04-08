from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "easy_unpack"
    FUNCTION_NAMES = {
        "python_3": "easy_unpack",
        "js_node": "easyUnpack"
    }
    ENV_COVERCODE = {
        ENV_NAME.PYTHON: '''

def cover(func, in_data):
    ret = func(tuple(in_data))
    assert isinstance(ret, tuple), 'A tuple should be returned'
    return list(ret)

'''
    }