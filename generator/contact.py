from model.contact import Contact
import random
import string
import os.path
import getopt
import sys
import jsonpickle


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


def random_string(maxlen):
    symbols = string.ascii_letters + " "*2
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


n = 5
f = "data/contacts.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


testdata = [Contact(firstname="", middlename="",
                    lastname="")] + [Contact(firstname=random_string(5), middlename=random_string(10),
                    lastname=random_string(10)) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))