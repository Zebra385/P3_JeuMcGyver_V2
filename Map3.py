#import numpy as np
#class Map
    #def __init__(self,file_map):
      #  data = np.genfromtxt("yourfile.dat", delimiter="\n")
        #read the file map
import os

# handle files using a callback method, prevents repetition
def _FileIO__file_handler(file_path, mode, callback = lambda f: None):
  f = open(file_path, mode)
  try:
    return callback(f)
  except Exception as e:
    raise IOError("Failed to %s file" % ["write to", "read from"][mode.lower() in "r rb r+".split(" ")])
  finally:
    f.close()


class FileIO:
  # return the contents of a file
  def read(self, mode = "r"):
    return __file_handler(self, mode, lambda rf: rf.read())

  # get the lines of a file
  def lines(self, mode = "r", filter_fn = lambda line: len(line) > 0):
    return [line for line in FileIO.read(self, mode).strip().split("\n") if filter_fn(line)]

  # create or update a file (NOTE: can also be used to replace a file's original content)
  def write(self, new_content, mode = "w"):
    return __file_handler(self, mode, lambda wf: wf.write(new_content))

  # delete a file (if it exists)
  def delete(self):
    return os.remove() if os.path.isfile(self) else None

def main ():
    file_ext_lines = FileIO.lines("maps.txt")
    for j, line in enumerate(file_ext_lines):
      l =[i for i in line]
      print(l)
    for j, line in enumerate(file_ext_lines):
      print("{}".format(line))


if __name__ == "__main__":  # Main is to star the play like a programm
    main()