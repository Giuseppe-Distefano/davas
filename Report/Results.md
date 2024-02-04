# Domain Adaptation Via Activation Shaping

## Baseline

![Network 0, Baseline](./images/n0.png)

| Experiment | Source &rightarrow; Target | Accuracy | Loss |
| :---: | :---: | :---: | :---: |
| 0.1.1 | Art Painting &rightarrow; Cartoon | 54.61 | 0.01065 |
| 0.1.2 | Art Painting &rightarrow; Sketch | 40.37 | 0.01519 |
| 0.1.3 | Art Painting &rightarrow; Photo | 95.93 | 0.00107 |

## Random activation maps

### Activation Shaping module after last convolutional layer

![Network 1, ASH module after last convolutional layer](./images/n1.png)

| Experiment | Mask out ratio | Source &rightarrow; Target | Accuracy | Loss |
| :---: | :---: | :---: | :---: | :---: |
| 1.1.1 | 0.1 | Art Painting &rightarrow; Cartoon | 43.26 | 0.01154 |
| 1.1.2 | 0.1 | Art Painting &rightarrow; Sketch | 38.08 | 0.01416 |
| 1.1.3 | 0.1 | Art Painting &rightarrow; Photo | 91.56 | 0.00310 |
| 2.1.1 | 0.4 | Art Painting &rightarrow; Cartoon | 43.00 | 0.01195 |
| 2.1.2 | 0.4 | Art Painting &rightarrow; Sketch | 39.76 | 0.01391 |
| 2.1.3 | 0.4 | Art Painting &rightarrow; Photo | 91.02 | 0.00365 |
| 2.1.4 | 0.55 | Art Painting &rightarrow; Cartoon | 43.98 | 0.01153 |
| 2.1.5 | 0.55 | Art Painting &rightarrow; Sketch | 39.48 | 0.01382 |
| 2.1.6 | 0.55 | Art Painting &rightarrow; Photo | 89.94 | 0.00407 |
| 2.1.7 | 0.75 | Art Painting &rightarrow; Cartoon | 42.96 | 0.01206 |
| 2.1.8 | 0.75 | Art Painting &rightarrow; Sketch | 37.24 | 0.01415 |
| 2.1.9 | 0.75 | Art Painting &rightarrow; Photo | 87.90 | 0.00524 |

### Activation Shaping module after each convolutional layer

![Network 2, ASH module after each convolutional layer](./images/n2.png)

| Experiment | Mask out ratio | Source &rightarrow; Target | Accuracy | Loss |
| :---: | :---: | :---: | :---: | :---: |
| 1.2.1 | 0.1 | Art Painting &rightarrow; Cartoon | 20.31 | 0.01531 |
| 1.2.2 | 0.1 | Art Painting &rightarrow; Sketch | 16.44 | 0.01572 |
| 1.2.3 | 0.1 | Art Painting &rightarrow; Photo | 28.14 | 0.01549 |
| 2.2.1 | 0.4 | Art Painting &rightarrow; Cartoon | 16.13 | 0.01560 |
| 2.2.2 | 0.4 | Art Painting &rightarrow; Sketch | 10.13 | 0.01614 |
| 2.2.3 | 0.4 | Art Painting &rightarrow; Photo | 21.98 | 0.01592 |
| 2.2.4 | 0.55 | Art Painting &rightarrow; Cartoon | 16.81 | 0.01563 |
| 2.2.5 | 0.55 | Art Painting &rightarrow; Sketch | 7.56 | 0.01622 |
| 2.2.6 | 0.55 | Art Painting &rightarrow; Photo | 23.89 | 0.01589 |
| 2.2.7 | 0.75 | Art Painting &rightarrow; Cartoon | 17.11 | 0.01567 |
| 2.2.8 | 0.75 | Art Painting &rightarrow; Sketch | 6.77 | 0.01623 |
| 2.2.9 | 0.75 | Art Painting &rightarrow; Photo | 22.34 | 0.01591 |

### Activation Shaping module after every three convolutional layers

![Network 3, ASH module after every three convolutional layers](./images/n3.png)

| Experiment | Mask out ratio | Source &rightarrow; Target | Accuracy | Loss |
| :---: | :---: | :---: | :---: | :---: |
| 1.3.1 | 0.1 | Art Painting &rightarrow; Cartoon | 31.48 | 0.01521 |
| 1.3.2 | 0.1 | Art Painting &rightarrow; Sketch | 23.11 | 0.01460 |
| 1.3.3 | 0.1 | Art Painting &rightarrow; Photo | 66.41 | 0.00796 |
| 2.3.1 | 0.4 | Art Painting &rightarrow; Cartoon | 27.65 | 0.01524 |
| 2.3.2 | 0.4 | Art Painting &rightarrow; Sketch | 22.02 | 0.01535 |
| 2.3.3 | 0.4 | Art Painting &rightarrow; Photo | 53.47 | 0.01126 |
| 2.3.4 | 0.55 | Art Painting &rightarrow; Cartoon | 25.21 | 0.01531 |
| 2.3.5 | 0.55 | Art Painting &rightarrow; Sketch | 22.91 | 0.01531 |
| 2.3.6 | 0.55 | Art Painting &rightarrow; Photo | 42.63 | 0.01317 |
| 2.3.7 | 0.75 | Art Painting &rightarrow; Cartoon | 19.75 | 0.01558 |
| 2.3.8 | 0.75 | Art Painting &rightarrow; Sketch | 20.11 | 0.01542 |
| 2.3.9 | 0.75 | Art Painting &rightarrow; Photo | 30.12 | 0.01509 |

## Adapting activation maps across domains

![Network 4, ASH module at layer2.1.conv2](./images/n4.png)

| Experiment | Source &rightarrow; Target | Accuracy | Loss |
| :---: | :---: | :---: | :---: |
| 3.1.1 | Art Painting &righarrow; Cartoon | 68.64 | 0.00711 |
| 3.1.2 | Art Painting &righarrow; Sketch | 51.08 | 0.01056 |
| 3.1.3 | Art Painting &righarrow; Photo | 95.81 | 0.00104 |
