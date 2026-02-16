from setuptools import setup, find_packages

setup(
    name="peachy-hehe",
    version="0.1.0",
    packages=find_packages(include=['games_project_yuzhakova', 'games_project_yuzhakova.*']),
    package_data={
        'games_project_yuzhakova': ['**/*.py', '**/__init__.py', 'py.typed'],
    },
    include_package_data=True,
    install_requires=['prompt>=0.4.1'],
    entry_points={
        'console_scripts': [
            'vd-games = games_project_yuzhakova.VD_games.scripts.VD_main:main',
            'vd-even = games_project_yuzhakova.VD_games.scripts.VD_even:main',
            'vd-calc = games_project_yuzhakova.VD_games.scripts.brain_calc:main',
            'vd-gcd = games_project_yuzhakova.VD_games.scripts.VD_gcd:main',
        ],
    },
)
