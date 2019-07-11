import os

from py_adb.adb import ADB
from py_adb.layout import Layout

class TestLayout(object):

    # TODO: Util Path Class
    test_files = os.path.join(os.path.abspath(os.path.dirname(__file__)), "test_files")   
    
    def test_get_layout(self):
        dev_id = ADB.get_connected_devices()[0]
        print("I: Device - {}".format(dev_id))
        path_to_file = Layout.get_layout(dev_id, self.test_files)
        assert os.path.isfile(path_to_file)