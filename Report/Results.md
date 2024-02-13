# Domain Adaptation Via Activation Shaping

## Baseline

![Network 0, Baseline](./images/n0.png)

| Experiment | Source &rightarrow; Target | Accuracy | Loss |
| :---: | :---: | :---: | :---: |
| 0.1.1 | Art Painting &rightarrow; Cartoon | 54.61 | 0.01065 |
| 0.1.2 | Art Painting &rightarrow; Sketch | 40.42 | 0.01512 |
| 0.1.3 | Art Painting &rightarrow; Photo | 95.93 | 0.00107 |

## Random activation maps

### Activation Shaping module after last convolutional layer

![Network 1, ASH module after last convolutional layer](./images/n1.png)

| Experiment | Mask out ratio | Source &rightarrow; Target | Accuracy | Loss |
| :---: | :---: | :---: | :---: | :---: |
| 1.1.1 | 0.1 | Art Painting &rightarrow; Cartoon | 43.17 | 0.01155 |
| 1.1.2 | 0.1 | Art Painting &rightarrow; Sketch | 38.23 | 0.01416 |
| 1.1.3 | 0.1 | Art Painting &rightarrow; Photo | 91.50 | 0.00309 |
| 2.1.1 | 0.4 | Art Painting &rightarrow; Cartoon | 43.90 | 0.01151 |
| 2.1.2 | 0.4 | Art Painting &rightarrow; Sketch | 39.81 | 0.01391 |
| 2.1.3 | 0.4 | Art Painting &rightarrow; Photo | 91.02 | 0.00365 |
| 2.1.4 | 0.55 | Art Painting &rightarrow; Cartoon | 44.03 | 0.01152 |
| 2.1.5 | 0.55 | Art Painting &rightarrow; Sketch | 39.45 | 0.01382 |
| 2.1.6 | 0.55 | Art Painting &rightarrow; Photo | 89.94 | 0.00407 |
| 2.1.7 | 0.75 | Art Painting &rightarrow; Cartoon | 42.92 | 0.01206 |
| 2.1.8 | 0.75 | Art Painting &rightarrow; Sketch | 37.21 | 0.01415 |
| 2.1.9 | 0.75 | Art Painting &rightarrow; Photo | 88.02 | 0.00524 |

### Activation Shaping module after each convolutional layer

![Network 2, ASH module after each convolutional layer](./images/n2.png)

| Experiment | Mask out ratio | Source &rightarrow; Target | Accuracy | Loss |
| :---: | :---: | :---: | :---: | :---: |
| 1.2.1 | 0.1 | Art Painting &rightarrow; Cartoon | 21.80 | 0.01527 |
| 1.2.2 | 0.1 | Art Painting &rightarrow; Sketch | 16.98 | 0.01557 |
| 1.2.3 | 0.1 | Art Painting &rightarrow; Photo | 27.31 | 0.01549 |
| 2.2.1 | 0.4 | Art Painting &rightarrow; Cartoon | 18.09 | 0.01561 |
| 2.2.2 | 0.4 | Art Painting &rightarrow; Sketch | 8.88 | 0.01613 |
| 2.2.3 | 0.4 | Art Painting &rightarrow; Photo | 21.98 | 0.01596 |
| 2.2.4 | 0.55 | Art Painting &rightarrow; Cartoon | 16.68 | 0.01567 |
| 2.2.5 | 0.55 | Art Painting &rightarrow; Sketch | 7.51 | 0.01626 |
| 2.2.6 | 0.55 | Art Painting &rightarrow; Photo | 23.17 | 0.01600 |
| 2.2.7 | 0.75 | Art Painting &rightarrow; Cartoon | 17.62 | 0.01563 |
| 2.2.8 | 0.75 | Art Painting &rightarrow; Sketch | 7.61 | 0.01623 |
| 2.2.9 | 0.75 | Art Painting &rightarrow; Photo | ----- | ------- |

### Activation Shaping module after every three convolutional layers

![Network 3, ASH module after every three convolutional layers](./images/n3.png)

| Experiment | Mask out ratio | Source &rightarrow; Target | Accuracy | Loss |
| :---: | :---: | :---: | :---: | :---: |
| 1.3.1 | 0.1 | Art Painting &rightarrow; Cartoon | 32.31 | 0.01509 |
| 1.3.2 | 0.1 | Art Painting &rightarrow; Sketch | 22.35 | 0.01471 |
| 1.3.3 | 0.1 | Art Painting &rightarrow; Photo | 67.19 | 0.00790 |
| 2.3.1 | 0.4 | Art Painting &rightarrow; Cartoon | 26.83 | 0.01531 |
| 2.3.2 | 0.4 | Art Painting &rightarrow; Sketch | 21.46 | 0.01537 |
| 2.3.3 | 0.4 | Art Painting &rightarrow; Photo | 53.47 | 0.01120 |
| 2.3.4 | 0.55 | Art Painting &rightarrow; Cartoon | 25.73 | 0.01530 |
| 2.3.5 | 0.55 | Art Painting &rightarrow; Sketch | 22.42 | 0.01530 |
| 2.3.6 | 0.55 | Art Painting &rightarrow; Photo | 43.17 | 0.01320 |
| 2.3.7 | 0.75 | Art Painting &rightarrow; Cartoon | 20.35 | 0.01555 |
| 2.3.8 | 0.75 | Art Painting &rightarrow; Sketch | 19.37 | 0.01547 |
| 2.3.9 | 0.75 | Art Painting &rightarrow; Photo | ----- | ------- |

## Adapting activation maps across domains

![Network 4, ASH module at layer2.1.conv2](./images/n4.png)

| Experiment | Source &rightarrow; Target | Accuracy | Loss |
| :---: | :---: | :---: | :---: |
| 3.1.1 | Art Painting &righarrow; Cartoon | 55.29 | 0.00962 |
| 3.1.2 | Art Painting &righarrow; Sketch | 39.42 | 0.01260 |
| 3.1.3 | Art Painting &righarrow; Photo | 89.52 | 0.00238 |
