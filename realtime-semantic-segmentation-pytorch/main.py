from core import SegTrainer
from configs.bisenetv2_camvid import MyConfig
import multiprocessing

import warnings
warnings.filterwarnings("ignore")


if __name__ == '__main__':
    config = MyConfig()
    multiprocessing.freeze_support()

    config.init_dependent_config()

    print(f"Starting task: {config.task}")
    print(f"Dataset root: {config.dataroot}")
    print(f"Model: {config.model} | Batch size: {config.train_bs}")

    # If you want to use command-line arguments, please uncomment the following line
    #config = load_parser(config)

    trainer = SegTrainer(config)

    if config.task == 'train':
        trainer.run(config)
    elif config.task == 'val':
        trainer.validate(config)
    elif config.task == 'predict':
        trainer.predict(config)
    else:    
        raise ValueError(f'Unsupported task type: {config.task}.\n')