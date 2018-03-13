import time

from argparse import ArgumentParser

from process.generate import file_processor

from utils.config import get_config 
from utils.constants import *
from utils.strings import *
from utils.util import *

def main(config_file_path):
    config_parser = get_config_parser(config_file_path)#加载配置信息路径
    config = get_config(config_parser)#配置信息
    logger = get_logger(config)   #运行日志

    file_processor(config[TRANSACTIONS_FILE], config[DATASET_PATH]) #数据文件预处理:交易数据信息配置,数据路径配置信息

if __name__ == "__main__":
    arg_parser = ArgumentParser(description='Deep Q Trading with DeepSense Architecture')#原来这个神经网络架构叫做DeepSense
    arg_parser.add_argument('--config', dest='file_path',#字典的key,把配置文件的路径加载进来
                            help='Path for the configuration file')
    args = arg_parser.parse_args()
    main(vars(args)['file_path'])



