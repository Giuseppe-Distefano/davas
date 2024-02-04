# Domain Adaptation Via Activation Shaping

## Baseline

![Network 0, Baseline](./images/n0.png)

| Experiment | Source &rightarrow; Target | Accuracy | Loss |
| :---: | :---: | :---: | :---: |
| 0.1.1 | Art Painting &rightarrow; Cartoon |  |  |
| 0.1.2 | Art Painting &rightarrow; Sketch |  |  |
| 0.1.3 | Art Painting &rightarrow; Photo |  |  |

## Random activation maps

### Activation Shaping module after last convolutional layer

![Network 1, ASH module after last convolutional layer](./images/n1.png)

| Experiment | Mask out ratio | Source &rightarrow; Target | Accuracy | Loss |
| :---: | :---: | :---: | :---: | :---: |
| 1.1.1 | 0.1 | Art Painting &rightarrow; Cartoon |  |  |
| 1.1.2 | 0.1 | Art Painting &rightarrow; Sketch |  |  |
| 1.1.3 | 0.1 | Art Painting &rightarrow; Photo |  |  |
| 2.1.1 | 0.4 | Art Painting &rightarrow; Cartoon |  |  |
| 2.1.2 | 0.4 | Art Painting &rightarrow; Sketch |  |  |
| 2.1.3 | 0.4 | Art Painting &rightarrow; Photo |  |  |
| 2.1.4 | 0.55 | Art Painting &rightarrow; Cartoon |  |  |
| 2.1.5 | 0.55 | Art Painting &rightarrow; Sketch |  |  |
| 2.1.6 | 0.55 | Art Painting &rightarrow; Photo |  |  |
| 2.1.7 | 0.75 | Art Painting &rightarrow; Cartoon |  |  |
| 2.1.8 | 0.75 | Art Painting &rightarrow; Sketch |  |  |
| 2.1.9 | 0.75 | Art Painting &rightarrow; Photo |  |  |

### Activation Shaping module after each convolutional layer

![Network 2, ASH module after each convolutional layer](./images/n2.png)

| Experiment | Mask out ratio | Source &rightarrow; Target | Accuracy | Loss |
| :---: | :---: | :---: | :---: | :---: |
| 1.2.1 | 0.1 | Art Painting &rightarrow; Cartoon |  |  |
| 1.2.2 | 0.1 | Art Painting &rightarrow; Sketch |  |  |
| 1.2.3 | 0.1 | Art Painting &rightarrow; Photo |  |  |
| 2.2.1 | 0.4 | Art Painting &rightarrow; Cartoon |  |  |
| 2.2.2 | 0.4 | Art Painting &rightarrow; Sketch |  |  |
| 2.2.3 | 0.4 | Art Painting &rightarrow; Photo |  |  |
| 2.2.4 | 0.55 | Art Painting &rightarrow; Cartoon |  |  |
| 2.2.5 | 0.55 | Art Painting &rightarrow; Sketch |  |  |
| 2.2.6 | 0.55 | Art Painting &rightarrow; Photo |  |  |
| 2.2.7 | 0.75 | Art Painting &rightarrow; Cartoon |  |  |
| 2.2.8 | 0.75 | Art Painting &rightarrow; Sketch |  |  |
| 2.2.9 | 0.75 | Art Painting &rightarrow; Photo |  |  |

### Activation Shaping module after every three convolutional layers

![Network 3, ASH module after every three convolutional layers](./images/n3.png)

| Experiment | Mask out ratio | Source &rightarrow; Target | Accuracy | Loss |
| :---: | :---: | :---: | :---: | :---: |
| 1.3.1 | 0.1 | Art Painting &rightarrow; Cartoon |  |  |
| 1.3.2 | 0.1 | Art Painting &rightarrow; Sketch |  |  |
| 1.3.3 | 0.1 | Art Painting &rightarrow; Photo |  |  |
| 2.3.1 | 0.4 | Art Painting &rightarrow; Cartoon |  |  |
| 2.3.2 | 0.4 | Art Painting &rightarrow; Sketch |  |  |
| 2.3.3 | 0.4 | Art Painting &rightarrow; Photo |  |  |
| 2.3.4 | 0.55 | Art Painting &rightarrow; Cartoon |  |  |
| 2.3.5 | 0.55 | Art Painting &rightarrow; Sketch |  |  |
| 2.3.6 | 0.55 | Art Painting &rightarrow; Photo |  |  |
| 2.3.7 | 0.75 | Art Painting &rightarrow; Cartoon |  |  |
| 2.3.8 | 0.75 | Art Painting &rightarrow; Sketch |  |  |
| 2.3.9 | 0.75 | Art Painting &rightarrow; Photo |  |  |

## Adapting activation maps across domains

![Network 4, ASH module at layer2.1.conv2](./images/n4.png)

| Experiment | Source &rightarrow; Target | Accuracy | Loss |
| :---: | :---: | :---: | :---: |
| 3.1.1 | Art Painting &righarrow; Cartoon |  |  |
| 3.1.2 | Art Painting &righarrow; Sketch |  |  |
| 3.1.3 | Art Painting &righarrow; Photo |  |  |
