import os
from utils import args
from Dataset import EEGdataloader
from models.EEGrunner import supervised, pre_training


def main():
    config = args.Initialization(args)

    config['problem'] = config['dataset']
    print(f"Config {config}")
    Data = EEGdataloader.data_loader(config)
    print(f"Data in main {Data}")

    # TODO add option to call rocket
    if config['Training_mode'] == 'Pre_Training':
        best_aggr_metrics_test, all_metrics = pre_training(config, Data)  # TODO save model or embeddings to file
    elif config['Training_mode'] == 'Supervised':  # TODO remove
        best_aggr_metrics_test, all_metrics = supervised(config, Data)
    # TODO call classifier here
    print_str = 'Best Model Test Summary: '
    for k, v in best_aggr_metrics_test.items():
        print_str += '{}: {} | '.format(k, v)
    print(print_str)

    with open(os.path.join(config['output_dir'], config['problem']+'_output.txt'), 'w') as file:
        for k, v in all_metrics.items():
            file.write(f'{k}: {v}\n')


if __name__ == '__main__':
    main()
