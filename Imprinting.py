# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:32:33 2019

@author: admin
"""

import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.distributed as dist
import torch.optim
import torch.utils.data
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import torchvision.datasets as dest

#基础设置
class Config():
    #novel_class的个数
    num_class = 100
    #每一类训练样本的个数
    num_train = 5
    #每一类测试样本的个数
    num_test = 20

#数据预处理
normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],       
                                     std=[0.229, 0.224, 0.225])
transform = transforms.Compose([
        transforms.RandomResizedCrop(224),      # 随机切再resize成给定的size大小
        transforms.RandomHorizontalFlip(),    # 概率为0.5，随机水平翻转。
        transforms.ToTensor(),
        normalize]
        )

#加载数据
img_folder = torchvision.datasets.ImageFolder(root = 'E:/Omniglot/omniglot-py/images_background/Armenian/',
                                 transform = transform)


class ImageLoader(torch.utils.data.Dataset):
    def __init__(self,ImageFolder,transform=True,num_class=100,num_sample):
        #选择novel_class
        for index in range(len(ImageFolder.classes))
        self.img_list = img_list
        
        self.transform = transform
        self.num_class = num_class
        
    def 
        