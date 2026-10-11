# About BinSweep

BinSweep is a free Python utility I created that automatically empties the Recycle Bin on Windows as a background tool.
I made this because I do not use the Recycle Bin and personally despise it. BinSweep essentially removes the need to even think about it.
**Warning:** I am NOT responsible if you lose something important.

BinSweep checks every 5 seconds for items in your Recycle Bin. If it finds any, it automatically empties them and sends a quick notification showing how many items were removed.
If no items are found, it does nothing and goes back to sleep for another 5 seconds before checking again.
I promise this is not a hack; BinSweep does not look at any of your files in or out of your Recycle Bin. It only counts and empties items in the Recycle Bin.

1. Tested using Task Manager on my computer with 16 GB of DDR4 RAM. It uses about 1.5–2 MB of RAM while idle in the background.
2. BinSweep is a 100% background process, meaning there is no UI, setup, or configuration required. Just run the .exe file, and it will work.
3. It is only guaranteed to work for Windows 11 with standard 64-bit architecture; other architectures or Windows versions I cannot guarantee.
4. To stop BinSweep, simply open Task Manager, search for BinSweep, and end the task.

If you love BinSweep and want it to always run, you can use Windows Task Scheduler to auto-run BinSweep when you log into your computer. This way, you do not have to manually run the .exe file every time.
If you do not know how to do this, look it up on Google. It is simple and should take no more than 5 minutes.

I am open to all suggestions, feedback, or concerns regarding BinSweep.

PYTHON EXE BUILT USING THE FOLLOWING COMMAND: pyinstaller --onefile --noconsole main.py
SOME ANTIVIRUS TOOLS FLAG --onefile PYINSTALLER APPS AS MALWARE FREQUENTLY. EXPECT THIS & WINDOWS ANTI-VIRUS ISSUES. CHECK THE VirusTotal REPORT TO SEE FULL DETAILS
