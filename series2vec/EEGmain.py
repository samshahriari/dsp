import os
from utils import args
from Dataset import dataloader
from models.EEGrunner import supervised, pre_training


def main():
    config = args.Initialization(args)

    # TODO add filename for EEGdata or incorporate everything into dataloader
    config['problem'] = "heartbeat.npy"
    print(f"Config {config}")
    Data = dataloader.data_loader(config)  # TODO add our own dataloader
    print(f"Data in main {Data}")

    if config['Training_mode'] == 'Pre_Training':
        best_aggr_metrics_test, all_metrics = pre_training(config, Data)
    elif config['Training_mode'] == 'Supervised':
        best_aggr_metrics_test, all_metrics = supervised(config, Data)

    print_str = 'Best Model Test Summary: '
    for k, v in best_aggr_metrics_test.items():
        print_str += '{}: {} | '.format(k, v)
    print(print_str)

    with open(os.path.join(config['output_dir'], config['problem']+'_output.txt'), 'w') as file:
        for k, v in all_metrics.items():
            file.write(f'{k}: {v}\n')


if __name__ == '__main__':
    main()
