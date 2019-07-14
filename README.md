# <img src="/img/py.png" width="32" height="32"> ADB Commands

Python package for executing adb commands.

> Requirements: <br>
> Android SDK Tools - https://developer.android.com/studio/releases/sdk-tools <br>
> adb - PATH variable

Install with PIP <br>
`pip install git+https://github.com/sergius-la/adb.git`

Usage example:
```python
dev_id = ADB.get_connected_devices()[0]
ADB.swipe(dev_id, 370, 1200, 370, 160)
```

[List of commands](https://github.com/sergius-la/Cheatsheet/blob/master/adb/adb.md)

## Cookbook
- __[Info:](/py_adb/info.py)__
    - `get_environment(package)`

***

## Commands
- __[ADB:](/py_adb/adb.py)__
  - `get_connected_devices()`
  - TODO: Add Dependensys into setup.py
- __[User actions:](/py_adb/user_actions.py)__
  - `tap(x, y)`
  - `stipe(x1, y1, x2, y2)`
  - `send_text(text)`
  - TODO: OpenNotifications
  - TODO: PressBack
  - TODO: Apps
  - TODO: LockDevice
- __[Device info:](/py_adb/device_info.py)__
  - `get_PID(process_name)`
  - `get_meminfo(package)`
  - `save_meminfo(path, package)`
  - `get_package_activity()`
  - `get_android_version(Device ID)`
  - `getprop(Device ID)`
  - `all_getprop(Device ID)`
  - `get_prop(Device ID, Properties)`
    - [All Properties](/py_adb/android_properties.py)
- __[Device manipulations:](/py_adb/device_manipulations.py)__
  - `set_screen_brightness(0 to 255)`
  - `screenshot(path_save_device)`
  - `get_screenshot(path_device, path_save, delete=False)`
  - TODO: Bluetoth On/Off
  - TODO: Screen Caption
- __[Files:](/py_adb/files.py)__
  - `pull(path_from, path_to)`
  - `push(path_file, path_to)`
  - `delete(path_file)`
- __[Package info:](/py_adb/package_info.py)__
  - `get_list_packages()`
  - `get_packahe_version(package)`
- __[Package manipulations:](/py_adb/package_manipulations.py)__
  - `clear_package_cache(package)`
  - `install_app(path_package)`
  - `start_package(package_name)`
  - `close_package(package_name)`
  - `grant_permission(package_name, permissions)`
  - `revoke_permission(package_name, permissions)`
- __[Layout:](/py_adb/layout.py)__
  - `dump_layout()`
  - `get_layout(path_save)`
  - TODO: Search Element
- __[Utility:]()__
  - `Paths`
  - `Config`