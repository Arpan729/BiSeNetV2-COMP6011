from configs.base_config import BaseConfig   

class MyConfig(BaseConfig):
    def __init__(self):
        super().__init__()

        # ================== Basic Settings ==================
        self.task = 'predict'
        self.model = 'bisenetv2'

        # ================== Dataset ==================
        self.dataset = 'cityscapes'
        self.dataroot = r"D:\Comp6011 report 1\CityScapes"  
        self.data_root = r"D:\Comp6011 report 1\CityScapes" 
        self.test_data_folder = r"D:\Comp6011 report 1\CityScapes\leftImg8bit\val\frankfurt"

        self.num_class = 19

        # ================== Training Settings ==================
        self.crop_size = 512
        self.train_bs = 2
        self.test_bs = 2
        self.val_bs =2                    
        self.total_epoch = 100
        self.base_lr = 0.01
        # self.num_workers = 4
        self.base_workers = 0
        self.use_aux= True
        self.amp_training = True
       

        # ================== Fix Test Loader Error ==================
        # self.test_split = False
        # self.test_data_root = None
        # self.test_data_folder = None
        self.resume_training = True

        # ================== Output ==================
        self.save_dir = './runs/bisenetv2_cityscapes'
        
        self.save_dir = r'D:\Comp6011 report 1\BiseNetv2\realtime-semantic-segmentation-pytorch\runs\bisenetv2_cityscapes'

        self.load_ckpt = True
        self.load_ckpt_path = r'D:\Comp6011 report 1\BiseNetv2\realtime-semantic-segmentation-pytorch\runs\bisenetv2_cityscapes\last.pth'

if __name__ == '__main__':
    config = MyConfig()