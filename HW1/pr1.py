try:
    def impor(filename):
        with open(filename,"r") as f:
            print(f.read())
    impor("HW1/file1.txt")
    impor("HW1/file2.txt")
    impor("HW1/file3.txt")
except FileNotFoundError:
    print("File not found)")

