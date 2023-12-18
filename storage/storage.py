import boto3
import logging
import os
from google.cloud import storage


class Storage:
    """Files uploading to different cloud functionalities are defined in this class.
    
    """

    def __init__(self, config={}) -> None:
        """Constructor for class Storage to initialize it's variables.
        
        Args:
            config: The config data to initialize instance variables.
        """

        self.file_types = {}
        self.file_types['images'] = config.get('images', [])
        self.file_types['media'] = config.get('media', [])
        self.file_types['documents'] = config.get('documents', [])
        self.targets = config.get('targets', [])
        self.files = list()

    def process_files(self, directory):
        """Process files in a given directory.
        
        Args:
            directory: The directory of files to process.
        """
        try:
            for root, _, files in os.walk(directory):
                for file in files:
                    self.files.append(os.path.join(root, file))
        except Exception as e:
            logging.error(str(e))

    def upload_files(self):
        """Upload files in to cloud storage.
        
        """
        try:
            for file in self.files:
                file_extension = file.lower().split('.')[-1]

                for target in self.targets:
                    upload = getattr(self, 'upload_to_' + target)
                    client = getattr(self, 'get_' + target + '_client')(self.targets[target])

                    for file_type in self.targets[target].get('files'):
                        
                        if file_extension in self.file_types[file_type]:

                            upload(client, file, self.targets[target])
        except Exception as e:
            logging.error(str(e))
    
    def get_aws_client(self, config):
        """Create AWS S3 client for the given configuration.
        
        Args:
            config: The config data for AWS S3 client.
        """
        try:
            return boto3.client(
                's3', 
                aws_access_key_id=config['s3']['access_key'], 
                aws_secret_access_key=config['s3']['secret_key']
            )
        except Exception as e:
            logging.error(str(e))

    def upload_to_aws(self, client, file_path, config):
        """Upload file into AWS S3.
        
        Args:
            client: The AWS S3 client for connectivity.
            file_path: The file path to upload into cloud.
            config: The config data with bucket details.
        """
        try:
            logging.info(f"Uploading {file_path} to AWS S3")
            return client.upload_file(file_path, config['s3']['bucket'], os.path.basename(file_path))
        except Exception as e:
            logging.error(str(e))
    
    def get_gcs_client(self, config):
        """Create Google Cloud Storage client for the given configuration.
        
        Args:
            config: The config data for Google Cloud Storage client.
        """
        try:
            os.environ["GOOGLE_CLOUD_PROJECT"] = config['cloud']['project']
            return storage.Client()
        except Exception as e:
            logging.error(str(e))

    def upload_to_gcs(self, client, file_path, config):
        """Upload file into Google Cloud Storage.
        
        Args:
            client: The Google Cloud Storage client for connectivity.
            file_path: The file path to upload into cloud.
            config: The config data with bucket details.
        """
        try:
            logging.info(f"Uploading {file_path} to Google Cloud Storage")
            return client.bucket( config['cloud']['bucket']).blob(os.path.basename(file_path)).upload_from_filename(file_path)
        except Exception as e:
            logging.error(str(e))
