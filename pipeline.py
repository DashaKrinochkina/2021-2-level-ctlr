"""
Pipeline for text processing implementation
"""
from pathlib import Path


class EmptyDirectoryError(Exception):
    """
    No data to process
    """


class InconsistentDatasetError(Exception):
    """
    Corrupt data:
        - numeration is expected to start from 1 and to be continuous
        - a number of text files must be equal to the number of meta files
        - text files must not be empty
    """


class MorphologicalToken:
    """
    Stores language params for each processed token
    """

    def __init__(self, original_word):
        pass

    def get_cleaned(self):
        """
        Returns lowercased original form of a token
        """
        pass

    def get_single_tagged(self):
        """
        Returns normalized lemma with MyStem tags
        """
        pass

    def get_multiple_tagged(self):
        """
        Returns normalized lemma with PyMorphy tags
        """
        pass


class CorpusManager:
    """
    Works with articles and stores them
    """

    def __init__(self, path_to_raw_txt_data: str):
        pass

    def _scan_dataset(self):
        """
        Register each dataset entry
        """
        pass

    def get_articles(self):
        """
        Returns storage params
        """
        pass


class TextProcessingPipeline:
    """
    Process articles from corpus manager
    """

    def __init__(self, corpus_manager: CorpusManager):
        pass

    def run(self):
        """
        Runs pipeline process scenario
        """
        pass

    def _process(self, raw_text: str):
        """
        Processes each token and creates MorphToken class instance
        """
        pass


def validate_dataset(path_to_validate):
    """
    Validates folder with assets
    """
    if isinstance(path_to_validate, str):
        path_to_validate = Path(path_to_validate)

    if not path_to_validate.exists():
        raise FileNotFoundError

    if not path_to_validate.is_dir():
        raise NotADirectoryError

    children = [child for child in path_to_validate.glob('*')]
    if not children:
        raise EmptyDirectoryError

    for child in children:
        if 'txt' in str(child):
            with open(child, 'r', encoding='utf-8') as file:
                text = file.read()
                if not text:
                    raise InconsistentDatasetError

    counter_t = 0
    counter_m = 0
    for file_name in children:
        if 'meta' in str(file_name):
            counter_m += 1
        elif 'txt' in str(file_name):
            counter_t += 1

    if counter_t != counter_m:
        raise InconsistentDatasetError


def main():
    pass


if __name__ == "__main__":
    main()
