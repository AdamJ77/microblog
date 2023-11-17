from pathlib import Path
from subprocess import check_output

from setuptools import find_packages, setup


BACKEND_PATH = Path(__file__).parent
ROOT = BACKEND_PATH.parent


def git_tag() -> str:
    return check_output(['git', 'describe'], encoding='utf-8').strip()


def read_requirements(path) -> list[str]:
    with open(path) as f:
        return f.read().splitlines(keepends=False)


setup(
    name='microblog-api',
    packages=find_packages(include=['api*']),
    include_package_data=True,
    install_requires=read_requirements(BACKEND_PATH/'requirements.txt'),
    use_scm_version={
        "root": ROOT
    },
    setup_requires='setuptools_scm',
    extras_require={
        'dev': read_requirements(BACKEND_PATH/'requirements.dev.txt')
    },
    entry_points={
        'console_scripts': [
            'microblog-api=api.__main__:main'
        ]
    }
)
