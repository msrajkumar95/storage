import configparser
import json
import logging
import yaml

logging.basicConfig(level=logging.INFO)


class Config:
    """Configuration file processing functionalities are defined in this class.
    
    """
    
    def __init__(self, file) -> None:
        """Constructor for class Config to initialize it's variables.
        
        Args:
            file: The absolute path of configuration file.
        """
        
        self.file = file
        logging.info("Reading configuration data from file : %s", self.file)
        self.config = self.read_config()


    def read_config(self):
        """Read configuration file and load data into variable.
        
        """
        try:
            extension = self.file.lower().split('.')[-1]
            
            if extension == 'json':
                with open(self.file, 'r') as f:
                    self.config = json.load(f)
            elif extension in ['cfg', 'conf']:
                config = configparser.ConfigParser()
                config.read(self.file)
                self.config = {section: dict(config.items(section)) for section in config.sections()}
            elif extension == 'yaml':
                with open(self.file, 'r') as f:
                    self.config = yaml.safe_load(f)
            else:
                raise ValueError(f"Unsupported configuration file format: {extension}")
            return self.config
        except Exception as e:
            logging.error(str(e))
            raise e

    def write_config(self, format, file):
        """Write configuration data into given file.
        
        Args:
            format: The format of configuration file.
            file: The absolute path of configuration file.
        """
        try:
            if format == 'env':
                with open(file, 'w') as f:
                    for key, value in self.config.items():
                        f.write(f"{key}={value}\n")
            elif format == 'json':
                with open(file, 'w') as f:
                    json.dump(self.config, f, indent=2)
            else:
                raise ValueError(f"Unsupported output format: {format}")
        except Exception as e:
            logging.error(str(e))
            raise e
