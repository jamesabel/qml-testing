
import osnap.installer

import app


def make_installer():
    osnap.installer.make_installer(app.__python_version__, app.__application_name__,
                                   app.__version__, app.__author__,
                                   'hello world for a taskbar app',
                                   'www.abel.co')


if __name__ == '__main__':
    make_installer()
