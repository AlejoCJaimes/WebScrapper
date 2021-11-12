import os


class AuxiliarFunctions:
    def __init__(self):
        self._sizefiles = []
        self._nameFiles = []

    def convert_bytes(self, size, unit=None):
        if unit == "KB":
            return str(round(size / 1024, 3)) + 'KB'
        elif unit == "MB":
            return str(round(size / (1024 * 1024), 3)) + ' MB'
        elif unit == "GB":
            return str(round(size / (1024 * 1024 * 1024), 3)) + ' GB'
        else:
            return str(size) + ' bytes'

    def found_files(self, path_dir):
        content = os.listdir(path_dir)
        for file in content:
            if os.path.isfile(os.path.join(path_dir, file)) and file.endswith('.xlsx'):
                self._nameFiles.append(file)
                self._sizefiles.append(self.convert_bytes(
                    os.path.getsize(path_dir + '/' + file), 'MB'))
        return dict(zip(self._nameFiles, self._sizefiles))
