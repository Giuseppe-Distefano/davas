if [ $# -eq 0 ]; then
    echo
    echo "Usage: ${0} target_domain module_placement k_values"
    echo
    echo "where module_placement is either the name of a layer enclosed in single"
    echo "quotation marks e.g. 'layer2.1.conv2' or a a list of layers enclosed in" 
    echo "double quotation marks e.g. \"'layer2.1.conv2', 'layer4.0.conv1'\" "
    echo
    echo "and k_values is a list of (four) values enclosed in "
#   echo "double quotation marks e.g. \"3136, 784, 196, 49\" "
    echo "double quotation marks e.g. \"0.6, 0.6, 0.6, 0.6\" "
    echo
    exit 1
fi

target_domain=${1}

if [[ "$2" =~ "'" ]]; then
    module_placement=${2}
else
    module_placement="'${2}'"
fi

# k_values="[3136, 784, 196, 49]"
# k_values="[0.6, 0.6, 0.6, 0.6]"
k_values=${3}

python main.py \
--experiment=domain_adaptation \
--experiment_name=domain_adaptation/${target_domain}/ \
--experiment_args="{'module_placement': [${module_placement}], 'extension': 'top_k', 'k_values': [${k_values}]}" \
--dataset_args="{'root': 'data/PACS', 'source_domain': 'art_painting', 'target_domain': '${target_domain}'}" \
--batch_size=128 \
--num_workers=5 \
--grad_accum_steps=1
