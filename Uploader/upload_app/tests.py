import unittest
from unittest.mock import mock_open, patch

from tasks import process_file


class FileProcessingTestCase(unittest.TestCase):
    def test_process_file(self):
        class File:
            def __init__(self, path):
                self.path = path
                self.processed = False

            def save(self):
                pass

        file1 = File('file1.txt')
        file2 = File('file2.txt')


        file1_content = 'Hello, World!'
        file2_content = 'Testing file processing'


        with patch('builtins.open', mock_open(read_data=file1_content)) as mock_file1, \
             patch('builtins.open', mock_open(read_data=file2_content)) as mock_file2:
            process_file(file1)
            process_file(file2)
            mock_file1.assert_called_once_with(file1.path, 'r')
            mock_file2.assert_called_once_with(file2.path, 'r')
            self.assertEqual(file1_content.upper(), file1.processed)
            self.assertEqual(file2_content.upper(), file2.processed)
            mock_file1.assert_called_with(file1.path, 'w')
            mock_file2.assert_called_with(file2.path, 'w')
            self.assertTrue(file1.processed)
            self.assertTrue(file2.processed)
            file1.save.assert_called_once()
            file2.save.assert_called_once()

            if __name__ == '__main__':
                unittest.main()