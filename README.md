# Research-few-shot
将预训练好的Res50的fc层设置为2048*100，冻结前面所有层，fine-tune baesd on mini-imagenet
## Res-few-shot:
training code
## train_tar
mini-imagenet中的类别，及其在image-net中对应的位置（0~999）
## weight_900:
去掉mini-imagenet中overlap的部分后fc的权重矩阵（2048*900）
## bias_900:
去掉mini-imagenet中overlap的部分后fc的偏置矩阵
## 03
一轮epoch的结果
