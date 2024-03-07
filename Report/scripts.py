input_filename = "ResultsProg.csv"

configurations = {}
improvements = {}
avg_improvements = {}


def import_data ():
    # Read the data from the input file and store it in the configurations dictionary
    for line in open(input_filename):
        experiment, mask_out_ratio, accuracy, loss = line.strip().split(',')
        configurations[experiment] = (float(mask_out_ratio), float(accuracy), float(loss))
    
    # Record results for the baseline
    baseline1 = configurations["0.1"][1]
    baseline2 = configurations["0.2"][1]
    baseline3 = configurations["0.3"][1]

    # Comptue the improvement for each configuration with respect to the baseline
    for conf in configurations:
        if conf.endswith("1"): improvements[conf] = configurations[conf][1] - baseline1
        if conf.endswith("2"): improvements[conf] = configurations[conf][1] - baseline2
        elif conf.endswith("3"): improvements[conf] = configurations[conf][1] - baseline3


# Compute the average improvement for a given section
def compute_avg_improvement (section):
    avg_imp = (improvements[section+".1"] + improvements[section+".2"] + improvements[section+".3"]) / 3.0
    return avg_imp


# Summarize average improvement for all sections
def show_improvements ():
    for i in range(1,4):
        if i==1:
            for j in range(1,27):
                section = "1." + str(i) + "." + str(j)
                avg = compute_avg_improvement(section)
                avg_improvements[section] = avg
        elif i==2:
            for j in range(1,16):
                section = "1." + str(i) + "." + str(j)
                avg = compute_avg_improvement(section)
                avg_improvements[section] = avg
        elif i==3:
            for j in range(1,13):
                section = "1." + str(i) + "." + str(j)
                avg = compute_avg_improvement(section)
                avg_improvements[section] = avg

    for i in avg_improvements: print(i, avg_improvements[i])


# Select the best subsections
def top_k_subsections (k):
    top_k = sorted(avg_improvements, key=avg_improvements.get, reverse=True)[:k]
    for i in top_k: print(i, avg_improvements[i])


# Main of the program
if __name__=='__main__':
    import_data()
    show_improvements()
    #top_k_subsections(5)
