class FileReplace:
    """Replace a substring within a file."""

    def __init__(self, filename: str, content: str):
        """Replace the content of file.

        Args:
            filename (str): name of the file
            content (str): content of the file
        """
        self.filename = filename
        with open(self.filename, "w+") as f:
            f.write(content)

    def read_file(self):
        """Read the content of file and print it"""
        with open(self.filename) as f:
            print(f.read())

    def replace(self, old: str, new: str):
        """Replace the substring with new string in the file

        Args:
            old (str): string to be replaced
            new (str): new string value for replacing
        """
        fin = open(self.filename, "r")
        data = fin.read()
        fin.close()
        with open(self.filename, "w") as fout:
            fout.write(data.replace(old, new))


file1 = FileReplace("example.txt", "This is a placement assignment")
file1.read_file()  # This is a placement assignment
file1.replace("placement", "screening")
file1.read_file()  # This is a screening assignment
