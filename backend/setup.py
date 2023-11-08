from subprocess import check_output

from setuptools import find_packages, setup


def git_tag() -> str:
    return check_output(['git', 'describe'], encoding='utf-8').strip()


def read_requirements(path) -> list[str]:
    with open(path) as f:
        return f.read().splitlines(keepends=False)


setup(
    name='microblog-api',
    version=git_tag(),
    packages=find_packages(include=['api*']),
    include_package_data=True,
    install_requires=read_requirements('./requirements.txt'),
    extras_require={'dev': read_requirements('./requirements.dev.txt')},
    entry_points={
        'console_scripts': [
            'microblog-api=api.__main__:main'
        ]
    }
)
