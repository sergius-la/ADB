from py_adb.adb import ADB

import os


class DeviceInfo:

    @staticmethod
    def get_pid(dev_id: str, ps: str) -> str:
        """
        Method return pid of package of process
        :dev_id: device id
        :ps: process or package name
        
        TODO: Fix for processes with multiple PIDs
        """
        command = "adb -s {dev} shell ps | grep {ps} | cut -d ' ' -f 4".format(dev=dev_id, ps=ps)
        print(command)
        pid = ADB.get_terminal_output(command)
        return pid[0].strip() if len(pid) > 0 else ""
    
    @staticmethod
    def get_meminfo(dev_id, ps="") -> list:
        """
        Method return dumpsys meminfo memory snapshot, by default will return system memory
        :dev_id: device id
        :ps: pid or process name
        """

        command = "adb -s {dev} shell dumpsys  meminfo {ps}".format(dev=dev_id, ps=ps)
        return ADB.get_terminal_output(command)
    
    @staticmethod
    def save_meminfo(dev_id: str, path: str, ps=""):
        """
        Method save meminfo into txt files
        :path: path to save file
        :ps: By default system, pid or package name
        TODO: Refactor, add Utility 
        """
        filename = "sys" if ps == "" else ps
        command = "adb -s {dev} shell dumpsys meminfo {ps} > {path}.txt".format(
            dev=dev_id, ps=ps, path=os.path.join(path, filename))
        ADB.exec_adb(command) 

    @staticmethod
    def get_current_activity(dev_id: str) -> dict:
        """
        Method return dict{activity, package} from current screen
        """

        command = "adb -s {dev} shell dumpsys window windows | grep -E 'mCurrentFocus'".format(dev=dev_id)
        output = ADB.get_terminal_output(command)[0]
        if "/" in output:
            raw = output.strip().split("/")
            activity = raw[1][:len(raw[1]) - 1:]
            package = raw[0].split(" ").pop()
            return {"activity": activity, "package": package}
        elif "StatusBar" in output:
            return {"activity": "StatusBar", "package": "AndroidStatusBar"}
        else:
            print("W: {}".format(output))

    @staticmethod
    def all_getprop(dev_id: str) -> dict:
        """
        Return getprop values in format dict{property:value}

        :dev_id: Device ID
        """

        command = "adb -s {dev} shell getprop".format(dev=dev_id)
        raw_getprop = ADB.get_terminal_output(command)
        dict_getprop = {}
        for line in raw_getprop:
            raw = line.strip().replace("[", "").replace("]", "").split(":")
            dict_getprop[raw[0].strip()] = raw[1].strip()
        return dict_getprop
    
    @staticmethod
    def get_prop(dev_id, *properties) -> dict:
        """
        Print selected properties

        :dev_id: Device ID
        :Properties: properties
        """
        
        device_info = {}
        all_prop = DeviceInfo.all_getprop(dev_id)
        for pr in properties:
            prop = all_prop.get(pr.value.get("prop"))
            name = pr.value.get("name")
            device_info[name] = prop
        return device_info

    @staticmethod
    def get_display_size(dev_id) -> dict:
        """
        Return a display size in dict{'width': <str>, 'hight': <str>}

        :dev_id: Device ID
        """
        
        size = {}
        command = "adb -s {dev} shell wm size".format(dev=dev_id)
        out = ADB.get_terminal_output(command)
        if len(out) == 1 and "Physical size:" in out[0]:
            raw = out[0].split("x")
            print(raw)
            size["width"] = int(raw[0].split(":")[1].strip())
            size["height"] = int(raw[1].strip())
        else:
            print("W: {out}".format(out=out))
        return size

    @staticmethod
    def is_locked(dev_id) -> bool:
        """
        Return is device locked

        :dev_id: Device ID
        """

        command = "adb -s {dev} shell dumpsys window | grep 'mShowingLockscreen'".format(dev=dev_id)
        out = ADB.get_terminal_output(command)[0].split()
        for line in out:
            raw = line.strip().split("=")
            if "mDreamingLockscreen" in raw[0]:
                if raw[1] == "true":
                    return True
            if "mShowingLockscreen" in raw[0]:
                if raw[1] == "true":
                    return True
        return False

if __name__ == "__main__":
#     # system_process = "com.android.systemui"
    dev_id = ADB.get_connected_devices()[0]

    x = DeviceInfo.get_current_activity(dev_id)
    print(x)
    # size = DeviceInfo.get_display_size(dev_id)
    # print(size)
    # print(DeviceInfo.get_package_activity(dev_id, "com.android.vending"))
    # DeviceInfo.get_prop(dev_id, Properties.BRAND, Properties.MODEL)
