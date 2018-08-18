from unittest import TestCase
from unittest.mock import patch

from pictures_analyzer.infra.local_files_finder import LocalFilesFinder


class TestLocalFilesFinder(TestCase):

    def setUp(self):
        self.local_files_finder = LocalFilesFinder()

    def test_list_directory_should_return_file_object_with_name_and_path_fulfilled_when_there_is_one_file_in_dir(self):
        # Given
        directory_path = './directory'
        with patch('os.listdir', return_value=['toto']) as os_patch:
            # When
            files_in_directory = self.local_files_finder.list_directory(directory_path)

            # Then
            os_patch.assert_called_once_with(directory_path)

        self.assertEqual(len(files_in_directory), 1)
        file = files_in_directory[0]
        self.assertEqual(file.name, 'toto')
        self.assertEqual(file.path, './directory/toto')

    def test_list_directory_should_return_two_files_objects_when_there_are_two_files_in_dir(self):
        # Given
        directory_path = './my_directory'
        with patch('os.listdir', return_value=['file1', 'file2']) as os_patch:
            # When
            files_in_directory = self.local_files_finder.list_directory(directory_path)

            # Then
            os_patch.assert_called_once_with(directory_path)

        self.assertEqual(len(files_in_directory), 2)
        file_1 = files_in_directory[0]
        self.assertEqual(file_1.name, 'file1')
        self.assertEqual(file_1.path, './my_directory/file1')
        file_2 = files_in_directory[1]
        self.assertEqual(file_2.name, 'file2')
        self.assertEqual(file_2.path, './my_directory/file2')
