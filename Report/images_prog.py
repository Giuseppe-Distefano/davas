import matplotlib.pyplot as plt
import numpy as np

##### GLOBAL VARIABLES #####
input_filename = './Report/ResultsProg.csv'
images_output_folder = './Report/images/progressive/'


##### DATA STRUCTURES #####
class Record:
    def __init__ (self, experiment, mask_out_ratio, accuracy, loss):
        self.id = experiment
        self.mask_out_ratio = mask_out_ratio
        self.accuracy = accuracy
        self.loss = loss

    def __str__ (self):
        return self.id + ', ' + str(self.mask_out_ratio) + ', ' + str(self.accuracy) + ', ' + str(self.loss)
    
    def compute_improvement (self, baseline):
        if self.id.endswith('1'): return self.accuracy - baseline[0].accuracy
        elif self.id.endswith('2'): return self.accuracy - baseline[1].accuracy
        else: return self.accuracy - baseline[2].accuracy


##### FUNCTIONS #####
# ----- Import data -----
def import_data ():
    lines = []
    file = open(input_filename, 'r')
    for line in file:
        name, mor, acc, loss = line.split(',')
        record = Record(name, float(mor), float(acc), float(loss))
        lines.append(record)
    file.close()
    return lines


# ----- Identify the baseline experiments -----
def identify_baseline (experiments):
    return [experiments[0], experiments[1], experiments[2]]


# ----- Compute average improvement for an experiment -----
def compute_average_improvement (experiments, baseline, experiment_name):
    experiments = [experiment for experiment in experiments if experiment.id.startswith(experiment_name)]
    return (sum([experiment.compute_improvement(baseline) for experiment in experiments]) / 3)


# ----- Plot the stems for the experiment -----
def plot_stem (experiments, baseline, experiment_name):
    exps = [experiment for experiment in experiments if experiment.id.startswith(experiment_name)]
    if len(exps)==0: return
    
    x = ['Cartoon', 'Sketch', 'Photo']
    y1 = [experiment.accuracy for experiment in baseline]
    y2 = [experiment.accuracy for experiment in exps]

    plt.figure()
    plt.xlabel('Accuracy')
    if experiment_name=='0':
        for i in range(3):
            plt.barh(x[i], y1[i], color='blue', height=0.3)
        plt.title('Baseline')
    else:
        for i in range(3):
            plt.stem(x[i], y1[i], linefmt='blue', markerfmt='bo', basefmt=' ', orientation='horizontal')
            plt.stem(x[i], y2[i], linefmt='red', markerfmt='ro', basefmt=' ', orientation='horizontal')
        plt.title('Experiment ' + experiment_name)
        plt.legend(['Baseline', 'Experiment'])
    plt.savefig(images_output_folder + 'stems/' + experiment_name.replace('.', '_') + '.png')
    plt.close()


# ----- Stems -----
def stems (experiments, baseline, experiment_name):
    if experiment_name=='0':
        plot_stem(experiments, baseline, experiment_name)
    
    elif experiment_name=='1.1':
        plot_stem(experiments, baseline, experiment_name)
        for i in range(26):
            sub_experiment_name = experiment_name + str(i+1)
            plot_stem(experiments, baseline, sub_experiment_name)
    
    elif experiment_name=='1.2':
        plot_stem(experiments, baseline, experiment_name)
        for i in range(15):
            sub_experiment_name = experiment_name + str(i+1)
            plot_stem(experiments, baseline, sub_experiment_name)
    
    elif experiment_name=='1.3':
        plot_stem(experiments, baseline, experiment_name)
        for i in range(12):
            sub_experiment_name = experiment_name + str(i+1)
            plot_stem(experiments, baseline, sub_experiment_name)
    
    elif experiment_name=='1.4':
        plot_stem(experiments, baseline, experiment_name)
        for i in range(8):
            sub_experiment_name = experiment_name + str(i+1)
            plot_stem(experiments, baseline, sub_experiment_name)
    
    elif experiment_name=='1.5':
        plot_stem(experiments, baseline, experiment_name)
        for i in range(4):
            sub_experiment_name = experiment_name + str(i+1)
            plot_stem(experiments, baseline, sub_experiment_name)

    elif experiment_name=='3.1':
        plot_stem(experiments, baseline, experiment_name)

    elif experiment_name=='3.2':
        plot_stem(experiments, baseline, experiment_name)


# ----- Plot models improvements vs threshold for the experiment -----
def plot_improvements (experiments, baseline, experiment_name, threshold=0.0):
    exps = [experiment for experiment in experiments if experiment.id.startswith(experiment_name)]
    if len(exps)==0: return

    x = np.arange(len(exps)/3)
    y1 = [experiment.compute_improvement(baseline) for experiment in exps if experiment.id.endswith('1')]
    y2 = [experiment.compute_improvement(baseline) for experiment in exps if experiment.id.endswith('2')]
    y3 = [experiment.compute_improvement(baseline) for experiment in exps if experiment.id.endswith('3')]
    y4 = threshold * np.ones(int(len(exps)/3))
    
    plt.figure()
    plt.xlabel('Position')
    plt.ylabel('Improvement')
    plt.plot(x, y1, 'r')
    plt.plot(x, y2, 'g')
    plt.plot(x, y3, 'y')
    if threshold!=0.0: plt.plot(x, y4, 'k', linestyle='dotted')
    plt.legend(['Cartoon', 'Sketch', 'Photo', 'Average', 'Threshold'])
    plt.title('Improvement for Section ' + experiment_name)
    exp_name = experiment_name.replace('.', '_')[0:-1]
    plt.savefig(images_output_folder + 'performance/' + exp_name + '.png')
    plt.close()


# ----- Plot models average improvements vs threshold for the experiment -----
def plot_avg_improvements (experiments, baseline, experiment_name, threshold=0.0):
    exps = [experiment for experiment in experiments if experiment.id.startswith(experiment_name)]
    if len(exps)==0: return

    x = np.arange(len(exps)/3)
    y1 = []
    y2 = []
    for i in range(int(len(exps)/3)):
        sub_experiment_name = experiment_name + str(i+1)
        y1.append(compute_average_improvement(experiments, baseline, sub_experiment_name))
        if threshold!=0.0: y2.append(threshold)
    
    plt.figure()
    plt.xlabel('Position')
    plt.ylabel('Improvement')
    plt.plot(x, y1, 'b', linewidth=2.0)
    if threshold!=0.0: plt.plot(x, y2, 'k', linestyle='dotted')
    plt.legend(['Average', 'Threshold'])
    plt.title('Average Improvement for Section ' + experiment_name)
    exp_name = experiment_name.replace('.', '_')[0:-1]
    plt.savefig(images_output_folder + 'averages/' + exp_name + '.png')
    plt.close()


# ----- Plot accuracy vs threshold -----
def improvements (experiments, baseline, experiment_name):
    if experiment_name=='1.1.':
        plot_improvements(experiments, baseline, experiment_name, -9.0)
        plot_avg_improvements(experiments, baseline, experiment_name, -9.0)
    
    elif experiment_name=='1.2.':
        plot_improvements(experiments, baseline, experiment_name, -5.0)
        plot_avg_improvements(experiments, baseline, experiment_name, -5.0)
    
    elif experiment_name=='1.3.':
        plot_improvements(experiments, baseline, experiment_name, -9.0)
        plot_avg_improvements(experiments, baseline, experiment_name, -9.0)
    
    elif experiment_name=='1.4.':
        plot_improvements(experiments, baseline, experiment_name, -18.0)
        plot_avg_improvements(experiments, baseline, experiment_name, -18.0)
    
    elif experiment_name=='1.5.':
        plot_improvements(experiments, baseline, experiment_name)
        plot_avg_improvements(experiments, baseline, experiment_name)


# ----- Plot average improvements when using random activation maps -----
def plot_ram_improvements (experiments, baseline, experiment_name):
    exps = [experiment for experiment in experiments if (experiment.id.split('.')[0]=='2' and experiment.id.split('.')[2]==experiment_name)]
    if len(exps)==0: return

    x = [0.00, 0.25, 0.50, 0.75, 1.00]
    y1 = [experiment.accuracy for experiment in exps if experiment.id.endswith('1')]
    t1 = baseline[0].accuracy * np.ones(5)
    y2 = [experiment.accuracy for experiment in exps if experiment.id.endswith('2')]
    t2 = baseline[1].accuracy * np.ones(5)
    y3 = [experiment.accuracy for experiment in exps if experiment.id.endswith('3')]
    t3 = baseline[2].accuracy * np.ones(5)

    plt.figure()
    plt.xlabel('Mask Out Ratio')
    plt.ylabel('Improvement')
    plt.plot(x, y1, 'r')
    plt.plot(x, t1, 'r', linestyle='dotted')
    plt.plot(x, y2, 'g')
    plt.plot(x, t2, 'g', linestyle='dotted')
    plt.plot(x, y3, 'b')
    plt.plot(x, t3, 'b', linestyle='dotted')
    plt.legend(['Cartoon', 'Cartoon Threshold', 'Sketch', 'Sketch Threshold', 'Photo', 'Photo Threshold'])
    if experiment_name=='1': plt.title('Accuracy for layer2.1.conv2')
    elif experiment_name=='2': plt.title('Accuracy for layer1.1.bn1, layer2.1.conv2')
    elif experiment_name=='3': plt.title('Accuracy for layer1.1.conv1')
    elif experiment_name=='4': plt.title('Accuracy for layer1.1.bn2')
    elif experiment_name=='5': plt.title('Accuracy for layer1.1.bn2, layer2.1.bn2')
    plt.savefig(images_output_folder + 'performance/2_x_' + experiment_name + '.png')
    plt.close()


# ----- Plot average improvements when using random activation maps -----
def plot_ram_avg_improvements (experiments, baseline):
    exps = [experiment for experiment in experiments if experiment.id.startswith('2.')]
    if len(exps)==0: return

    x = [0.00, 0.25, 0.50, 0.75, 1.00]
    y1 = [compute_average_improvement(experiments, baseline, '2.'+str(i+1)+'.1') for i in range(5)]
    y2 = [compute_average_improvement(experiments, baseline, '2.'+str(i+1)+'.2') for i in range(5)]
    y3 = [compute_average_improvement(experiments, baseline, '2.'+str(i+1)+'.3') for i in range(5)]
    y4 = [compute_average_improvement(experiments, baseline, '2.'+str(i+1)+'.4') for i in range(5)]
    y5 = [compute_average_improvement(experiments, baseline, '2.'+str(i+1)+'.5') for i in range(5)]

    plt.figure()
    plt.xlabel('Mask Out Ratio')
    plt.ylabel('Improvement')
    plt.plot(x, y1, 'r')
    plt.plot(x, y2, 'g')
    plt.plot(x, y3, 'y')
    plt.plot(x, y4, 'b')
    plt.plot(x, y5, 'm')
    plt.legend([
        'layer2.1.conv2',
        'layer1.1.bn1, layer2.1.conv2',
        'layer1.1.conv1',
        'layer1.1.bn2',
        'layer1.1.bn2, layer2.1.bn2'
    ])
    plt.title('Average Improvement for Random Activation Maps')
    plt.savefig(images_output_folder + 'averages/' + '2_x.png')
    plt.close()


# ----- Section 0 of the project -----
def baseline (experiments, baseline):
    stems(experiments, baseline, '0')


# ----- Section 1 of the project -----
def activation_shaping_modules (experiments, baseline):
    # 1.1 - One Activation Shaping module
    stems(experiments, baseline, '1.1')
    improvements(experiments, baseline, '1.1.')
    
    # 1.2 - Two Activation Shaping modules
    stems(experiments, baseline, '1.2')
    improvements(experiments, baseline, '1.2.')
    
    # 1.3 - Three Activation Shaping modules
    stems(experiments, baseline, '1.3')
    improvements(experiments, baseline, '1.3.')
    
    # 1.4 - Four Activation Shaping modules
    stems(experiments, baseline, '1.4')
    improvements(experiments, baseline, '1.4.')
    
    # 1.5 - Five Activation Shaping modules
    stems(experiments, baseline, '1.5')
    improvements(experiments, baseline, '1.5.')


# ----- Section 2 of the project -----
def random_activation_maps (experiments, baseline):
    # Average
    plot_ram_avg_improvements(experiments, baseline)

    # 2.x.1 - layer2.1.conv2
    plot_ram_improvements(experiments, baseline, '1')

    # 2.x.2 - layer1.1.bn1, layer2.1.conv2
    plot_ram_improvements(experiments, baseline, '2')

    # 2.x.3 - layer1.1.conv1
    plot_ram_improvements(experiments, baseline, '3')

    # 2.x.4 - layer1.1.bn2
    plot_ram_improvements(experiments, baseline, '4')

    # 2.x.5 - layer1.1.bn2, layer2.1.bn2
    plot_ram_improvements(experiments, baseline, '5')


# ----- Section 3 of the project -----
def adapting_activation_maps (experiments, baseline):
    # layer2.1.conv2
    stems(experiments, baseline, '3.1')
    improvements(experiments, baseline, '3.1.')

    # layer1.1.bn2
    stems(experiments, baseline, '3.2')
    improvements(experiments, baseline, '3.2.')


##### MAIN OF THE PROGRAM #####
if __name__=='__main__':
    data_experiments = import_data()
    data_baseline = identify_baseline(data_experiments)

    baseline(data_experiments, data_baseline)
    activation_shaping_modules(data_experiments, data_baseline)
    random_activation_maps(data_experiments, data_baseline)
    adapting_activation_maps(data_experiments, data_baseline)
