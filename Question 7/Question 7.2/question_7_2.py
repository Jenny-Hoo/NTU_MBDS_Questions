L = [4,8,5,9,6,7]

def coordinates_to_index(x):
    index = L[0]*L[1]*L[2]*L[3]*L[4]*x[5] + L[0]*L[1]*L[2]*L[3]*x[4] + L[0]*L[1]*L[2]*x[3] + L[0]*L[1]*x[2] + L[0]*x[1] + x[0]
    return index

def index_to_coordinates(index):
    x = ""
    tmp = index
    for i in range(5):
        s = tmp % L[i]
        x = x + str(int(s))
        x = x + "\t"
        tmp = (tmp - s) / L[i]
    x = x + str(int(tmp))
    return x

def main():
    path1 = "input_coordinates_7_2.txt"
    path2 = "input_index_7_2.txt"
    f1 = open("output_index_7_2.txt","w")
    f1.write("index\n")
    f2 = open("output_coordinates_7_2.txt","w")
    f2.write("x1\tx2\tx3\tx4\tx5\tx6\n")
    with open(path1) as files:
        next(files)
        for line in files:
            if line.strip() == "":
                continue
            line = line.replace('\n','').replace('\r','').split('\t')
            line = list(map(int, line))
            f1.write("{}\n".format(coordinates_to_index(line)))
        f1.close()
    with open(path2) as files:
        next(files)
        for line in files:
            if line.strip() == "":
                continue
            line = line.replace('\n','').replace('\r','')
            x = index_to_coordinates(int(line))
            f2.write("{}\n".format(x))
        f2.close()


if __name__ == "__main__":
    main()
