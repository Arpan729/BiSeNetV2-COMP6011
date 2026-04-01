from configs.base_config import BaseConfig

class MyConfig(BaseConfig):
    def __init__(self):
        super().__init__()

        self.task = 'train'
        self.model = 'bisenetv2'

        self.dataset = 'cityscapes'                    
        self.data_root = r"D:\Comp6011 report 1\CamVid"

        self.num_class = 11                            # CamVid has 11 classes

        # CamVid friendly settings
        self.crop_size = 720
        self.train_bs = 8
        self.val_bs = 8
        self.test_bs = 8
        self.total_epoch = 200
        self.base_lr = 0.01
        self.base_workers = 4
        self.use_aux = True
        self.amp_training = True

        # Disable test if not needed
        # self.test_split = False
        # self.test_data_root = None

        self.save_dir = r'D:\Comp6011 report 1\BiseNetv2\realtime-semantic-segmentation-pytorch\runs\bisenetv2_camvid'
        self.load_ckpt = False

if __name__ == '__main__':
    config = MyConfig()