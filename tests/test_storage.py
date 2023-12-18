import os
import pytest
from storage import Config, Storage

class TestStorage:

    file_path = os.path.join(os.path.dirname(__file__), 'data')

    def test_process_files(self):
        expected_result = [os.path.join(self.file_path, 'file_directory', 'sample.csv')]
        conf = Config(os.path.join(self.file_path, 'json_config.json'))
        storage = Storage(conf.config)
        storage.process_files(os.path.join(self.file_path, 'file_directory'))
        assert expected_result == storage.files

    def test_upload_files(self):
        conf = Config(os.path.join(self.file_path, 'json_config.json'))
        storage = Storage(conf.config)
        storage.files = [os.path.join(self.file_path, 'file_directory', 'sample.csv')]
        storage.upload_files()
