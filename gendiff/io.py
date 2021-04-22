def load(file_path):
    """
    Load file from file system
    """

    with open(file_path, mode='r') as opened_file:
        data = opened_file.read()

    return data
