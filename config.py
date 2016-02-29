import os

environ_keys = [
    'BUILDER_ROOT_DIR',
    'BUILDER_HOME',
    'BUILDER_HOME_DISPOSABLE',
    'RUNNER_MODE',
    'RUNNER_CONFIG_PATH',
    'RUNNER_IMAGE',
    'RUNNER_USER',
    'RUNNER_VOLUME',
    'RUNNER_HOME_VOLUME',
    'RUNNER_REMOVE',
    'DOCKER_URL',
]

for key in environ_keys:
    value = os.environ.get(key, None)

    if value is None:
        continue

    if value.lower() == 'true':
        value = True
    elif value.lower() == 'false':
        value = False

    globals()[key] = value

del os, environ_keys, key
