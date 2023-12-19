# SGCLMD
### SGCLMD: Signed Graph-based Contrastive Learning Model for Predicting Somatic Mutation-Drug Association 


![image](https://github.com/wangxiaosong96/SGCLMD/blob/main/SGCLMD-main/Images/graph.png)

## Tutorial
1. Split data for cross validation and indenpendent test experiment via the script split_data.py: python split_data.py fold_number DATANAME seed_indent seed_cross

2. To perform cross validation for finding the optimal hyperparameters by running the script command_optimal.py (if you don't want to finetune the hyperparameters, just skip this step):

3. python command_optimal.py --dataName DATANAME --exp_name mid_dim/num_layer/alp_beta --seed_cross seed_cross --seed_indent seed_indent

To get the experiment results by running the script command_optimal.py

## Requirements
In order to run this code, you need to install following dependencies:

pip install torch numpy sklearn torch_geometric
python >= 3.9
torch >= 1.7.0
scikit-learn >= 0.24.0
torch_geometric >= 2.1.0.post1

## Run Example
The number of train epochs for review is 300, as it is a small datsets. But for other three datsets, the number of training epochs is 2000.

python train.py --dataset=review-1 --epochs=300

## Contact

Please feel free to contact us if you need any help: xiaosongwang@ahau.edu.cn
