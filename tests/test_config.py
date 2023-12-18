import json
import os
import pytest
from storage import Config

class TestConfig:

    file_path = os.path.join(os.path.dirname(__file__), 'data')

    def test_read_config_with_json(self):
        expected_result = {
            "images": [
                "jpg",
                "png",
                "svg",
                "webp"
            ]
        }
        conf = Config(os.path.join(self.file_path, 'json_config.json'))
        assert expected_result == conf.read_config()

    def test_read_config_with_yaml(self):
        expected_result = {
            "images": [
                "jpg",
                "png",
                "svg",
                "webp"
            ]
        }
        conf = Config(os.path.join(self.file_path, 'yaml_config.yaml'))
        assert expected_result == conf.read_config()

    def test_read_config_with_cfg(self):
        expected_result = {'Config': {'images': 'jpg, png, svg, webp'}}
        conf = Config(os.path.join(self.file_path, 'cfg_config.cfg'))
        assert expected_result == conf.read_config()

    def test_read_config_with_error(self):
        with pytest.raises(ValueError, match="Unsupported configuration file format: txt"):
            Config(os.path.join(self.file_path, 'text_config.txt'))

    def test_write_config_with_json(self):
        conf = Config(os.path.join(self.file_path, 'json_config.json'))
        conf.write_config('json', os.path.join(self.file_path, 'json_output.json'))
        expected_result = {
            "images": [
                "jpg",
                "png",
                "svg",
                "webp"
            ]
        }
        with open(os.path.join(self.file_path, 'json_output.json'), 'r') as f:
            assert expected_result == json.load(f)

    def test_write_config_with_env(self):
        conf = Config(os.path.join(self.file_path, 'json_config.json'))
        conf.write_config('env', os.path.join(self.file_path, 'env_output.env'))
        expected_result = "images=['jpg', 'png', 'svg', 'webp']\n"
        with open(os.path.join(self.file_path, 'env_output.env'), 'r') as f:
            assert expected_result == f.read()

    def test_write_config_with_error(self):
        conf = Config(os.path.join(self.file_path, 'json_config.json'))
        with pytest.raises(ValueError, match="Unsupported output format: txt"):
            conf.write_config('txt', os.path.join(self.file_path, 'text_output.txt'))
