from updater import Updater

__version__ = '0.0.1'

upd = Updater(
    version=__version__,
    file_name=__file__,
    file_url='https://raw.githubusercontent.com/lemonyte/update/main/test.py',
    version_url='https://raw.githubusercontent.com/lemonyte/update/main/version.txt',
)

upd.update()
