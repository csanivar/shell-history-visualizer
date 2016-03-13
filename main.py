import matplotlib.pyplot as plt
import sys

#Generate a dict with words with their correspoding frequency
def gen_data(hist):
    data = {}
    for x in hist:
        # Get the second word in the command (the first word will be the serial number of the command)
        fw = str(x.split()[1])
        #If the command starts with 'sudo', take the second word
        if fw == "sudo":
            try:
                fw = str(x.split()[2])
            except IndexError:
                pass

        if fw not in data:
            data[fw] = 1
        else:
            data[fw] += 1
    return data

#Plot a histogram of the dict
def plot_history(data):
    plt.bar(range(len(data)), data.values(), align="center")
    plt.xticks(range(len(data)), list(data.keys()), rotation="vertical")
    plt.show()

#Return the values with frequency greater than filter_frequency
def filter_data(data, filter_frequency):
    return dict((k, v) for k, v in data.iteritems() if v > filter_frequency)


#Sets utf-8 as default encoding
def fix_encoding():
    reload(sys)
    sys.setdefaultencoding("utf-8")


if __name__ == "__main__":
    fix_encoding()
    raw_data = [line.strip() for line in open("./.history", 'r')]
    dat = gen_data(raw_data)
    dat = filter_data(dat, 20)
    plot_history(dat)
