import rumps, webbrowser

class StatusBarApp(rumps.App):
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
        

if __name__ == "__main__":
    StatusBarApp("pythonexplainedto.me").run()
