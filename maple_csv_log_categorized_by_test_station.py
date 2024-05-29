# -*- coding: utf-8 -*-
'''
@File    :   maple_csv_log_categorized_by_test_station.py
@Time    :   2024/05/26 11:27:56
@Author  :   SimonYuan 
@Version :   1.0
@Site    :   https://tresordie.github.io/
@Desc    :   AWS csv folder with all functional test csv mixed together
'''


import os
import re
import shutil
import pandas as pd
from csv_operate import *


class maple_csv_log_categorized_by_test_station(object):
    def __init__(self, aws_csv_log_folder_path, maple_build_stage):
        self.pcba_otp_test_station_name = "Maple-BHBCS-1"
        self.pcba_mcu_selftest_test_station_name = "Maple-BHBCS-2"
        self.pcba_bms_test_station_name = "Maple-BHBCS-3"
        self.semipack1_test_station_name = "Maple-C-7"
        self.semipack2_test_station_name = "Maple-C-10"
        self.pack1_test_station_name = "Maple-C-13"
        self.pack2_test_station_name = "Maple-C-14"

        # category folder
        self.maple_build_stage = maple_build_stage
        self.pcba_otp_path = "./" + self.maple_build_stage + "/" + "pcba_otp"
        self.pcba_mcu_selftest_path = (
            "./" + self.maple_build_stage + "/" + "pcba_mcu_selftest"
        )
        self.pcba_bms_test_path = "./" + self.maple_build_stage + "/" + "pcba_bms_test"
        self.semipack1_test_path = (
            "./" + self.maple_build_stage + "/" + "semipack1_test"
        )
        self.semipack2_test_path = (
            "./" + self.maple_build_stage + "/" + "semipack2_test"
        )
        self.pack1_test_path = "./" + self.maple_build_stage + "/" + "pack1_test"
        self.pack2_test_path = "./" + self.maple_build_stage + "/" + "pack2_test"

        self.mkdir(self.maple_build_stage)
        self.mkdir(self.pcba_otp_path)
        self.mkdir(self.pcba_mcu_selftest_path)
        self.mkdir(self.pcba_bms_test_path)
        self.mkdir(self.semipack1_test_path)
        self.mkdir(self.semipack2_test_path)
        self.mkdir(self.pack1_test_path)
        self.mkdir(self.pack2_test_path)

        self.csv_log_search_folder_path = aws_csv_log_folder_path

    def mkdir(self, path):
        # print current function name
        # print(sys._getframe().f_code.co_name)
        folder = os.path.exists(path)
        if not folder:
            # print("folder not exist, creating folder!")
            os.makedirs(path)
        # else:
        #     print("folder exist!")

    def read_and_match_test_station_name_from_filename(self, filename):
        if self.pcba_otp_test_station_name in filename:
            full_file_name_path = os.path.join(
                self.csv_log_search_folder_path, filename
            )
            # print(full_file_name_path)
            shutil.copy(
                full_file_name_path,
                self.pcba_otp_path,
            )

        elif self.pcba_mcu_selftest_test_station_name in filename:
            full_file_name_path = os.path.join(
                self.csv_log_search_folder_path, filename
            )
            shutil.copy(
                full_file_name_path,
                self.pcba_mcu_selftest_path,
            )

        elif self.pcba_bms_test_station_name in filename:
            full_file_name_path = os.path.join(
                self.csv_log_search_folder_path, filename
            )
            shutil.copy(
                full_file_name_path,
                self.pcba_bms_test_path,
            )

        elif self.semipack1_test_station_name in filename:
            full_file_name_path = os.path.join(
                self.csv_log_search_folder_path, filename
            )
            shutil.copy(
                full_file_name_path,
                self.semipack1_test_path,
            )

        elif self.semipack2_test_station_name in filename:
            full_file_name_path = os.path.join(
                self.csv_log_search_folder_path, filename
            )
            shutil.copy(
                full_file_name_path,
                self.semipack2_test_path,
            )

        elif self.pack1_test_station_name in filename:
            full_file_name_path = os.path.join(
                self.csv_log_search_folder_path, filename
            )
            shutil.copy(
                full_file_name_path,
                self.pack1_test_path,
            )

        elif self.pack2_test_station_name in filename:
            full_file_name_path = os.path.join(
                self.csv_log_search_folder_path, filename
            )
            shutil.copy(
                full_file_name_path,
                self.pack2_test_path,
            )

    # match csv logs with keywords in filename
    def match_csv_log_with_keywords(self):
        file_name_list = os.listdir(self.csv_log_search_folder_path)
        # print(file_name_list)

        for fn in file_name_list:
            if re.search(r"\.csv$", fn):
                self.read_and_match_test_station_name_from_filename(fn)


if __name__ == "__main__":
    maple_csv_log_categorized_by_test_station = (
        maple_csv_log_categorized_by_test_station(
            "./aws_csv",
            "dvt",
        )
    )

    maple_csv_log_categorized_by_test_station.match_csv_log_with_keywords()
