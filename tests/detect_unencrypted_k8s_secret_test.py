from __future__ import annotations

import pytest

from pre_commit_hooks.detect_unencrypted_k8s_secret import main
from testing.util import get_resource_path


@pytest.mark.parametrize(
    ('filename', 'expected_retval'), (
        ('k8ssecret_unencrypted.yaml', 1),
        ('k8ssecret_encrypted.yaml', 0),
        ('k8smissing_kind.yaml', 0),
        ('k8sconfigmap.yaml', 0),
    ),
)
def test_main(filename, expected_retval):
    ret = main([get_resource_path(filename)])
    assert ret == expected_retval
