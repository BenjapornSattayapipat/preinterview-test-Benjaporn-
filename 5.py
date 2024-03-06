class WebsiteHistory:
    def __init__(self):
        self.history = []
        self.current_index = -1

    def input_url(self, url):
        self.history = self.history[:self.current_index + 1]
        self.history.append(url)
        self.current_index += 1

    def prev(self):
        if self.current_index > 0:
            self.current_index -= 1
            return self.history[self.current_index]
        else:
            return "No website to previous"

    def next(self):
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
            return self.history[self.current_index]
        else:
            return "No website to go"

    def current(self):
        if self.current_index >= 0:
            return "Now you on " + self.history[self.current_index]
        else:
            return "No website visited yet"

    def all(self):
        return self.history


# ตัวอย่างการใช้งาน
history = WebsiteHistory()

while True:
    command = input("ป้อนคำสั่ง (input [URL], prev, next, current, all): ").split()

    if command[0] == "input":
        if len(command) > 1:
            history.input_url(command[1])
        else:
            print("กรุณาป้อน URL ด้วยคำสั่ง input")

    elif command[0] == "prev":
        print(history.prev())

    elif command[0] == "next":
        print(history.next())

    elif command[0] == "current":
        print(history.current())

    elif command[0] == "all":
        print(history.all())

    else:
        print("คำสั่งไม่ถูกต้อง")
