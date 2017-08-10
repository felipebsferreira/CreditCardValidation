from setuptools import setup

requires = [
    'pyramid',
    'pyramid_chameleon',
]

setup(name='credit_card',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = credit_card:main
      """,
)
