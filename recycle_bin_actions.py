import ctypes
import os
import winshell
from winotify import Notification

shell32 = ctypes.WinDLL("shell32.dll") 
icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico")
file_names = []

# --- SHEmptyRecycleBinW setup ---
shell32.SHEmptyRecycleBinW.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_uint]
shell32.SHEmptyRecycleBinW.restype = ctypes.c_long

# --- SHQueryRecycleBinW setup ---
class SHQUERYRBINFO(ctypes.Structure):
    _fields_ = [
        ("cbSize", ctypes.c_ulong),
        ("i64Size", ctypes.c_ulonglong),
        ("i64NumItems", ctypes.c_ulonglong)
    ]

shell32.SHQueryRecycleBinW.argtypes = [ctypes.c_wchar_p, ctypes.POINTER(SHQUERYRBINFO)]
shell32.SHQueryRecycleBinW.restype = ctypes.c_long

# --- Flags for SHEmptyRecycleBinW: skip confirmation dialog, skip the "sound", skip progress UI ---
NO_CONFIRMATION = 0x00000001
NO_PROGRESS_UI = 0x00000002
NO_SOUND = 0x00000004
EMPTY_FLAGS = NO_CONFIRMATION | NO_PROGRESS_UI | NO_SOUND


# --- Functions ---

def get_item_count_in_recycle_bin():
    """Using SHQueryRecycleBinW, returns the amount of items currently in the user's recycle bin."""
    info = SHQUERYRBINFO()
    info.cbSize = ctypes.sizeof(SHQUERYRBINFO)  # must be set before calling

    result = shell32.SHQueryRecycleBinW(None, ctypes.byref(info))  # None = check all drives

    if result != 0:  # non-zero means something went wrong
        raise RuntimeError(f"SHQueryRecycleBinW failed with code {result}")

    return info.i64NumItems


def empty_recycle_bin():
    """Using SHEmptyRecycleBinW, empties the user's recycle bin with no confirmation, sound, or progress UI."""
    global file_names

    file_names = [os.path.basename(item.original_filename()) for item in winshell.recycle_bin()]
    result = shell32.SHEmptyRecycleBinW(None, None, EMPTY_FLAGS)  # None, None = no window, all drives

    if result != 0:
        raise RuntimeError(f"SHEmptyRecycleBinW failed with code {result}")

def notify_recycle_bin_emptied(items_removed_count: int):
    """
    Using a winotify notification, alerts the user that items_removed_count were removed from their recycle bin.
    Shows the first MAX_NAMES_SHOWN removed items by name, then how many more there were.

    :param items_removed_count: The number of items that were removed from the recycle bin.
    """
    global file_names

    MAX_NAMES_SHOWN = 3
    shown_names = "\n".join(file_names[:MAX_NAMES_SHOWN])
    if len(file_names) > MAX_NAMES_SHOWN:
        shown_names += f"\n...and {len(file_names) - MAX_NAMES_SHOWN} more"

    alert = Notification(
        app_id="BinSweep",
        title="Recycle Bin Emptied",
        msg=f"{items_removed_count} item(s) were removed from your recycle bin. \n\n" + shown_names,
        duration="short", 
        icon=icon_path
    )
    alert.show()
