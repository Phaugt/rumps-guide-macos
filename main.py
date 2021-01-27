import rumps, webbrowser, os, sys, subprocess

def resource_path(relative_path):
    """for pyinstaller"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)

logo = resource_path('data/logo.icns')
logop = resource_path('data/logo.png')

OSASCRIPT = """
tell application "System Events"
    tell appearance preferences
        set dark mode to {mode}
    end tell
end tell

tell application "Terminal"
    set default settings to settings set "{theme}"
end tell

tell application "Terminal"
    set current settings of tabs of windows to settings set "{theme}"
end tell
"""

TERMINAL_THEMES = {
    False: 'Rasta light',
    True: 'Rasta',
}


def is_dark_mode() -> bool:
    """Return the current Dark Mode status."""
    result = subprocess.run(
        ['defaults', 'read', '-g', 'AppleInterfaceStyle'],
        text=True,
        capture_output=True,
    )
    return result.returncode == 0 and result.stdout.strip() == 'Dark'


def set_interface_style(dark: bool):
    """Enable/disable dark mode."""
    mode = 'true' if dark else 'false'  # mode can be {true, false, not dark}
    script = OSASCRIPT.format(mode=mode, theme=TERMINAL_THEMES[dark])
    result = subprocess.run(
        ['osascript', '-e', script],
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result
        

class StatusBarApp(rumps.App):
    def __init__(self):
        super(StatusBarApp, self).__init__('pythonexplainedto.me')
        self.icon = logop
    
    @rumps.clicked("pythonexplainedto.me")
    def web(self, _):
        webbrowser.open('https://pythonexplainedto.me', new=2)

    @rumps.clicked("Instagram")
    def insta(self, _):
        webbrowser.open('https://www.instagram.com/pythonexplainedto.me/', new=2)

    @rumps.clicked("GitHub")
    def gith(self, _):
        webbrowser.open('https://github.com/Phaugt', new=2)

    @rumps.clicked("Facebook")
    def face(self, _):
        webbrowser.open('https://www.facebook.com/pythonexplainedtome.me/', new=2)

    @rumps.clicked("Twitter")
    def twit(self, _):
        webbrowser.open('https://twitter.com/pythonexplained', new=2)

    @rumps.clicked("Darkmode")
    def dmtoggle(self, _):
        set_interface_style(not is_dark_mode())


if __name__ == "__main__":
    StatusBarApp().run()
