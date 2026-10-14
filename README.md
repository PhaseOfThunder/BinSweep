# About BinSweep

> [!WARNING]
> **BinSweep permanently deletes everything in your Recycle Bin. There are ZERO recovery options.**
> This includes anything already in your Recycle Bin the moment you first start it, so check it before you run BinSweep.

## About

BinSweep is a free Python utility I created that automatically empties the Recycle Bin on Windows in the background.
I made this because I do not use the Recycle Bin and personally despise it. BinSweep essentially removes the need to even think about it.

You set a custom **check frequency**, and BinSweep will check your Recycle Bin every that many seconds. If it finds any items, it empties them and sends a quick notification showing how many items were removed, plus the names of the first 3.
If no items are found, it does nothing and goes back to sleep.

BinSweep does not open, read, modify, or store the contents of any of your files, in or out of your Recycle Bin. It only counts the items, empties the bin, and shows the item names. 
BinSweep is open source, so you can see exactly what it does in the files in this repository.

- **Memory usage:** ~25 MB on average (measured with Task Manager on my PC)
- **Not a full app:** it only has a small UI in the system tray and runs mostly in the background
- **Supported:** Windows 11, 64-bit. Other Windows versions or architectures may work, but I cannot guarantee it

## Install

1. Download `BinSweep.zip` from the [Releases](../../releases) page.
2. Unzip/extract it, and DO NOT modify anything.
3. Run `BinSweep.exe`.

> [!IMPORTANT]
> Keep `BinSweep.exe` and the `_internal` folder next to each other. The exe will not start without `_internal`.

## Usage

Click the BinSweep icon in the system tray (next to the clock) to open the panel. If you do not see it, click the **^** arrow; Windows hides new tray icons by default.

- **Change the check frequency:** enter the time in seconds in the panel. It is saved and remembered next time.
- **Quit:** click the red **Quit BinSweep** button, or right-click the tray icon and choose **Quit**.

### Start BinSweep automatically

If you love BinSweep and want it to start when you log in, so you do not have to run the .exe manually every time:

1. Press **Win + R**, type `shell:startup`, and press Enter.
2. In the folder that opens, right-click → **New → Shortcut** and pick your `BinSweep.exe`.

That's it. To undo this, delete the shortcut from that folder.

## Antivirus / SmartScreen

BinSweep is an unsigned exe from an 'unknown' developer (me), and it deletes files, so some antivirus tools may flag it. Expect this.

If Windows shows **"Windows protected your PC"**, click **More info → Run anyway**. If you would rather not trust the exe, you can run it from source instead (see below).

## Uninstall

1. Quit BinSweep from the tray.
2. Delete the BinSweep folder, plus the startup shortcut if you made one.
3. *(Optional)* Delete the saved settings: open `regedit` and delete `HKEY_CURRENT_USER\Software\BinSweep`.

## Feedback

I am open to all suggestions, feedback, or concerns regarding BinSweep. 
Feel free to report any issues in the comments or directly to me.
