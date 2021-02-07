L1 = 50
L2 = 57

def coordinates_to_index(x1, x2):
    index = L1 * x2 + x1
    return index

def index_to_coordinates(index):
    x1 = index % L1
    x2 = int((index - x1) / L1)
    return x1, x2

def main():
    path1 = "input_coordinates_7_1.txt"
    path2 = "input_index_7_1.txt"
    f1 = open("output_index_7_1.txt","w")
    f1.write("index\n")
    f2 = open("output_coordinates_7_1.txt","w")
    f2.write("x1\tx2\n")
    with open(path1) as files:
        next(files)
        for line in files:
            if line.strip() == "":
                continue
            line = line.replace('\n','').replace('\r','').split('\t')
            f1.write("{}\n".format(coordinates_to_index(int(line[0]), int(line[1]))))
        f1.close()
    with open(path2) as files:
        next(files)
        for line in files:
            if line.strip() == "":
                continue
            line = line.replace('\n','').replace('\r','')
            x1,x2 = index_to_coordinates(int(line))
            f2.write("{}\t{}\n".format(x1,x2))
        f2.close()


if __name__ == "__main__":
    main()
