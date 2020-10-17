import pickle
import time
from PIL.Image import merge

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from tqdm import tqdm

IMG_PATH = r'C:\Users\LWRF4\Desktop\Folder\LeiGod\gamelib\uploads\game_background\2019-07-27\1564218853218880.png'

if __name__ == '__main__':

    # img=Image.open(IMG_PATH)
    # img_np=np.array(img)
    # print('type(img_np)',type(img_np),'img_np.shape:',img_np.shape)

    # id_list = ['涛哥','dog1et']
    # id_dict = {'涛哥':'dog1et'}
    # m_list = [id_list,id_dict]
    # with open(r'C:\Users\LWRF4\Github\Wifi-detection\data\list.p','wb') as file:
    #     pickle.dump(m_list,file)

    with open(r'C:\Users\LWRF4\Github\Wifi-detection\data\list.p','rb') as file:
        read_l = pickle.load(file)
    
    print('type(read_l)',type(read_l),'read_l.shape:',len(read_l),'\n',read_l)
    # plt.imshow(read_p)
    # plt.show()
    
