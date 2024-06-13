# DAVAS - Domain Adaptation Via Activation Shaping

Repository for the "*Activation Shaping for Domain Adaptation*" project

<a href="https://didattica.polito.it/pls/portal30/gap.pkg_guide.viewGap?p_cod_ins=01URWOV&p_a_acc=2024&p_header=S&p_lang=IT&multi=N">Advanced Machine Learning</a> course 2023/2024 @ <a href="https://www.polito.it/">PoliTo</a>

## Abstract

Domain adaptation is a discipline founded on the premise that all predictions can rely on features that are indiscriminate between the Source and Test domains. It underlies the study of Domain Shift, which focuses on differences in the distributions of data between the Test and Source domains, resulting in a deterioration in the performance of the model itself.

Activation Shaping comes to the aid of this research through the modification of activation maps in an architecture, and can be used as a method in the out-of-detection (OOD) process by answering the question ”Do models know when they do not?”.

Our project begins with the retrieval of activation maps to apply to the output of the reference ResNet18 model, and subsequently we will try to switch off some outputs to see how this process can be adaptive to changing network conditions. Finally, we continue in Domain Adaptation by combining the characteristics of the Test domain with the Source domain and manipulating the architecture from previous stages with some binarization ablation experiments.

## Authors

Bar Giorgio

Distefano Giuseppe

Incaviglia Salvatore

## Usage

To reproduce the "**Baseline**" subsection of the project, use the following code mockup:

```bash
launch_scripts/baseline.sh ${target_domain}

# For Example
# launch_scripts/baseline.sh cartoon
```

To reproduce the "**Finding the best configurations**" subsection of the project, use the following code mockup:

```bash
launch_scripts/random.sh ${target_domain} ${module_placement} ${mask_out_ratio}

# For Example
# launch_scripts/random.sh cartoon "'layer1.1.bn2', 'layer2.1.conv2'" 0.25
```

To reproduce the "**Domain Adaptation**" subsection of the project, use the following code mockup:

```bash
launch_scripts/domain_adaptation.sh ${target_domain} ${module_placement}

# For Example
# launch_scripts/domain_adaptation.sh cartoon "'layer1.1.bn2', 'layer2.1.conv2'"
```

To reproduce the "**Ablation studies, First variation**" subsection of the project, use the following code mockup:

```bash
launch_scripts/random_no_binarization.sh ${target_domain} ${module_placement} ${mask_out_ratio}
launch_scripts/domain_adaptation_no_binarization.sh ${target_domain} ${module_placement}

# For Example
# launch_scripts/random_no_binarization.sh cartoon "'layer1.1.bn2', 'layer2.1.conv2'" 0.25
# launch_scripts/domain_adaptation_no_binarization.sh cartoon "'layer1.1.bn2', 'layer2.1.conv2'"
```

To reproduce the "**Ablation studies, Second variation**" subsection of the project, use the following code mockup:

```bash
launch_scripts/random_top_k.sh ${target_domain} ${module_placement} ${mask_out_ratio} ${k_values}
launch_scripts/domain_adaptation_top_k.sh ${target_domain} ${module_placement} ${k_values}

# For example
# launch_scripts/random_top_k.sh sketch "'layer2.1.bn2'" 0.5 "1.0, 1.0, 1.0, 0.5"
# launch_scripts/domain_adaptation_top_k.sh sketch "'layer2.1.bn2'" "1.0, 1.0, 1.0, 0.5"
```

## Starting project

<a href="https://arxiv.org/abs/1505.07818">GitHub project repository</a>
