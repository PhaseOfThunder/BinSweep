# This is the main file, program execution happens here

import recycle_bin_actions as rb
import os
import sys
from PySide6.QtCore import Qt, QTimer, QSettings
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QApplication, QSystemTrayIcon, QWidget, QFrame, QVBoxLayout,
                               QHBoxLayout, QLabel, QSpinBox, QPushButton, QMenu)

class TrayPanel(QWidget):
    """The small popup panel shown when the tray icon is left-clicked."""

    def __init__(self, timer: QTimer):
        super().__init__(None, Qt.Popup | Qt.FramelessWindowHint)  # auto-hides when you click elsewhere
        self.setAttribute(Qt.WA_TranslucentBackground)  # lets the frame below have rounded corners
        self.timer = timer

        frame = QFrame(self)
        frame.setObjectName("panel")
        frame.setStyleSheet("""
            #panel { background: #2b2d30; border: 1px solid #43454a; border-radius: 10px; }
            QLabel { color: #dfe1e5; }
            #title { font-size: 15px; font-weight: bold; }
            #quit { background: #c94f4f; color: white; border: none; border-radius: 6px; padding: 6px; }
            #quit:hover { background: #db5c5c; }
        """)

        title = QLabel("BinSweep")
        title.setObjectName("title")

        # --- Check frequency ---
        frequency_box = QSpinBox()
        frequency_box.setRange(1, 3600)
        frequency_box.setSuffix(" s")
        frequency_box.setValue(timer.interval() // 1000)
        frequency_box.valueChanged.connect(self.set_check_frequency)

        frequency_row = QHBoxLayout()
        frequency_row.addWidget(QLabel("Check every"))
        frequency_row.addWidget(frequency_box)

        # --- Quit button ---
        quit_button = QPushButton("Quit BinSweep")
        quit_button.setObjectName("quit")
        quit_button.clicked.connect(QApplication.quit)

        layout = QVBoxLayout(frame)
        layout.addWidget(title)
        layout.addLayout(frequency_row)
        layout.addStretch()
        layout.addWidget(quit_button)

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.addWidget(frame)
        self.setFixedSize(260, 150)

    def set_check_frequency(self, seconds: int):
        """Applies the new check frequency and saves it so it's remembered next launch."""
        self.timer.setInterval(seconds * 1000)
        settings.setValue("check_frequency", seconds)

    def show_above(self, icon_rect):
        """Places the panel just above the tray icon (like JetBrains Toolbox), kept on screen."""
        screen = QApplication.screenAt(icon_rect.center()) or QApplication.primaryScreen()
        area = screen.availableGeometry()  # screen minus the taskbar

        x = icon_rect.center().x() - self.width() // 2
        y = area.bottom() - self.height() - 8
        x = max(area.left() + 8, min(x, area.right() - self.width() - 8))

        self.move(x, y)
        self.show()
        self.activateWindow()

def check_recycle_bin():
    item_count = rb.get_item_count_in_recycle_bin()
    if item_count > 0:
        rb.empty_recycle_bin()
        rb.notify_recycle_bin_emptied(item_count)
        
app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)  # ensure hiding the panel does not kill the app

settings = QSettings("BinSweep", "BinSweep")  # saved in the registry under HKEY_CURRENT_USER\Software\BinSweep

timer = QTimer()
timer.setInterval(settings.value("check_frequency", 5, type=int) * 1000)  # defaults to 5s on first launch
timer.timeout.connect(check_recycle_bin)
timer.start()

panel = TrayPanel(timer)

icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico")
tray = QSystemTrayIcon(QIcon(icon_path))
tray.setToolTip("BinSweep")

# Left-click opens the panel
tray.activated.connect(
    lambda reason: panel.show_above(tray.geometry()) if reason == QSystemTrayIcon.Trigger else None
)

# Right-click gives a plain menu as a fallback
menu = QMenu()
quit_action = QAction("Quit")
quit_action.triggered.connect(app.quit)
menu.addAction(quit_action)
tray.setContextMenu(menu)

tray.show()
sys.exit(app.exec())