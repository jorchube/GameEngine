from unittest.mock import patch

patchers = []


def start_patch(test_case, target):
    patcher = patch(target, autospec=True)
    patchers.append(patcher)
    setattr(test_case, target.split('.')[-1], patcher.start())


def stop_patches():
    global patchers
    [patcher.stop() for patcher in patchers]
    patchers = []
