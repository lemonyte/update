import requests
import typing
from .exceptions import FetchException, UpdateException


class Updater:
    def __init__(self, file_name: str, version: typing.Union[str, typing.Tuple[int, ...]], file_url: str, version_url: str):
        self.file_name = file_name
        self.version = version
        self.file_url = file_url
        self.version_url = version_url
        if isinstance(self.version, str):
            try:
                self.version = tuple(int(i) for i in self.version.split('.'))
            except ValueError:
                raise ValueError("Failed to parse provided version number. Please provide a valid version number.")

    def check(self, version_url: str = None) -> bool:
        """Fetch the latest version number from the GitHub repository.
        If the retrieved version number is greater than the provided version, return True.
        """
        if not version_url:
            version_url = self.version_url
        try:
            latest_version = requests.get(version_url).text.strip()
        except Exception:
            raise FetchException("Failed to check for updates. Please download the latest version manually.")
        try:
            latest_version = tuple(int(i) for i in latest_version.split('.'))
        except ValueError:
            raise FetchException("Failed to parse fetched version number. Please download the latest version manually.")
        return latest_version > self.version

    def download(self, file_url: str = None):
        if not file_url:
            file_url = self.file_url
        try:
            return requests.get(file_url).content
        except Exception:
            raise FetchException("Failed to fetch updated file. Please download the latest version manually.")

    def update(self, file_url: str = None, file_name: str = None):
        if not file_url:
            file_url = self.file_url
        if not file_name:
            file_name = self.file_name
        update_available = self.check()
        if update_available:
            new_file = self.download(file_url)
            with open(file_name, 'wb') as file:
                file.write(new_file)

    def _check_internet(self):  # TODO
        try:
            pass
        except Exception:
            raise FetchException("Failed to check for updates. Internet connection required.")
