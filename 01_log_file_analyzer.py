"""
Description: a script that reads a specified log file for specific error and generates a summary report.
Steps for task completion:
1. Identify the file
2. Locate the file and set the path
3. Open and read the file (will probably need elevated privileges)
4. Locate the specific text that we want to read.
5. Print out that text.
6. Close the file and exit.
"""


class LogAnalyzer:
    def __init__(self, file_path: str, key_word: str):
        self.file_path = file_path
        self.key_word = key_word.lower()

    def check_file_exists(self):
        """
        This method checks if the file exists.
        """
        # handle errors with try-except method.
        try:
            if self.file_path:
                read_file = self.read_log()
                return read_file
        except FileNotFoundError as err:
            print(err)

    def read_log(self) -> str | None:
        """
        This method opens the file and reads the log. It searches for specific key word like
        'warning' or 'error'.
        """
        # open and read the file. We use with here so it can close the file at the end.
        with open(self.file_path, "r") as open_file:
            # for every line in the file, if the line contains specific keyword (error), it will return the whole line
            for line in open_file:
                if self.key_word in line:
                    print(line)


sample_file = LogAnalyzer("/var/log/dmesg", "warn")
sample_file.check_file_exists()
