import os

extension = '.spec.ts'
path = r'C:\repos\cgts\ITACA-FRONT\front\front\src\app'


def remove_files():
    for folder, dirs, files in os.walk(path, topdown=False):
        for file in files:
            if file[-7:] == 'spec.ts':
                os.remove(folder + '\\' + file)


if __name__ == '__main__':
    remove_files()
