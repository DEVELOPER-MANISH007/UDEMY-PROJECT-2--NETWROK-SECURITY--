form dataclasses import dataclasses

@dataclasses
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str
