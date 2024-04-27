import os
import zipfile

src_path = os.path.join('typescript_additional_files')
archive_name = 'typescript_additional_files.zip'
archive_path = os.path.join(archive_name)

with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as archive_file:
    for dirpath, dirnames, filenames in os.walk(src_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            archive_file_path = os.path.relpath(file_path, src_path)
            archive_file.write(file_path, archive_file_path)

with zipfile.ZipFile(archive_path, 'r') as archive_file:
    bad_file = zipfile.ZipFile.testzip(archive_file)

    if bad_file:
        raise zipfile.BadZipFile(
            'CRC check failed for {} with file {}'.format(archive_path, bad_file))