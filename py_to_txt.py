import sys

def readFile(path):
    array = []
    with open(path, "r") as file:
        array = file.readlines()
    return array

def createHeaderFile(path, array):
    with open(path, "w") as file:
        file.write(f"static const char *python_script =\n")
        for line in array:
            file.write("\"" + line.strip("\n") + "\\n" + "\"" + "\n")
        file.write(";")

def main(param):
    array = readFile(param[1])
    createHeaderFile(param[2], array)

if __name__ == "__main__":
    main(sys.argv)