from adb import ADB

class Files:
    
    @staticmethod
    def pull(dev_id: str, path_from: str, path_to: str):
        """
        Print ADB pull execution into terminal
        :dev_id: device id
        :path_from: Path to file on the device
        :path_to: Path to save a file
        """

        command = "adb -s {dev_id} pull {path_from} {path_to}".format(dev_id=dev_id, path_from=path_from, path_to=path_to)
        output = ADB._get_terminal_output(command)
        print("I: {}".format(output))
    
    @staticmethod
    def push(dev_id: str, path_file: str, path_to: str):
        """
        Print ADB push execution into terminal
        :dev_id: device id
        :path_file: Path to file
        :path_to: Path to save file in the device
        
        TODO: Check File existance before push
        """

        command = "adb -s {dev} push {path_file} {path_to}".format(dev=dev_id, path_file=path_file, path_to=path_to)
        output = ADB._get_terminal_output(command)
        print("I: {}".format(output))

    @staticmethod
    def delete(dev_id: str, path_file: str):
        """
        Method to delete file a device
        :dev_id: Device ID
        :path_file: Path to file

        TODO: Test
        TODO: Add check before executing
        TODO: Add check after executing
        """

        command = "adb -s {dev} shell rm {path}".format(dev=dev_id, path=path_file)
        ADB.exec_adb(command)