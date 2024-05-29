# -*- coding: utf-8 -*-
'''
@File    :   general_test_stations_class.py
@Time    :   2024/05/29 22:30:13
@Author  :   SimonYuan 
@Version :   1.0
@Site    :   https://tresordie.github.io/
@Desc    :   None
'''


import re
import os
from csv_operate import *


class general_test_stations(object):
    def __init__(
        self,
        prefix_summary_file,
        prefix_summary_file_sort,
        dut_info_in_summary_csv_header,
        general_column_header_index_dict,
        feed_demo_csv_log_path,
    ):
        """_summary_
            1.general purpose class which can pivot and summary standard format csv log which we defined on monolith
            2.output file_name will be "prefix_summary_file_timestamp.csv" and "prefix_summary_file_sort_timestamp.csv"
                2.1 "prefix_summary_file_sort_timestamp.csv" is sorting result of "prefix_summary_file_timestamp.csv" by test start time
        Args:
            prefix_summary_file (_type_): prefix of summary file name
            prefix_summary_file_sort (_type_): prefix of file name which sorted prefix_summary_file by test start time
            dut_info_in_summary_csv_header (_type_): data(except test items) need to be recorded into output summary csv file (SN, WorkOrder ...)
            general_column_header_index_dict (_type_): dict to describe standard format csv head row
            feed_demo_csv_log_path (_type_): use one standard format csv log as demo to feed the class, it will get all test items
        """
        self.sorted_date = generate_time_stamp()

        self.prefix_summary_file = prefix_summary_file
        self.prefix_summary_file_sort = prefix_summary_file_sort

        self.summary_file = self.prefix_summary_file + "_" + self.sorted_date + ".csv"
        self.summary_file_sort = (
            self.prefix_summary_file_sort + "_" + self.sorted_date + ".csv"
        )

        self.test_items = []
        self.csv_head = []

        self.general_column_header_index_dict = general_column_header_index_dict

        tmp_test_items_list = pd_read_csv_column_by_name_header_set(
            feed_demo_csv_log_path, "test_name"
        )

        # SN, TestStation, WorkOrder, StartTime, EndTime, CycleTime, OverallResult, UUID ...
        for i in range(len(dut_info_in_summary_csv_header)):
            self.csv_head.append(dut_info_in_summary_csv_header[i])

        # get station's all test itesm from csv demo log
        for i in range(len(tmp_test_items_list)):
            self.test_items.append(tmp_test_items_list[i])
            self.csv_head.append(tmp_test_items_list[i])

        tmp_test_items_list = []

    def create_csv_file_with_header(self):
        creat_csv(self.summary_file, self.csv_head)

    def dut_info_append_into_summay_csv(self, full_file_name):
        tmp_dut_info_list = []

        # SN
        tmp_dut_info_list.append(
            read_csv_cell(
                full_file_name,
                1,
                self.general_column_header_index_dict["sn"],
            )
        )

        # Test Station
        tmp_dut_info_list.append(
            read_csv_cell(
                full_file_name,
                1,
                self.general_column_header_index_dict["test_station_name"],
            )
        )

        # Work Order
        tmp_dut_info_list.append(
            read_csv_cell(
                full_file_name,
                1,
                self.general_column_header_index_dict["work_order"],
            )
        )

        # Start Time
        start_time = ""
        start_time = read_csv_cell(
            full_file_name,
            1,
            self.general_column_header_index_dict["start_time"],
        )
        # print(start_time)
        tmp_dut_info_list.append(str(start_time) + "\t")

        # End Time
        end_time = ""
        end_time = read_csv_cell(
            full_file_name,
            1,
            self.general_column_header_index_dict["end_time"],
        )
        # print(end_time)
        tmp_dut_info_list.append(str(end_time) + "\t")

        # Cycle Time
        tmp_dut_info_list.append(calculate_cycle_time(start_time, end_time))

        # overall result
        tmp_dut_info_list.append(
            read_csv_cell(
                full_file_name,
                1,
                self.general_column_header_index_dict["overall_test_result"],
            )
        )

        # uuid
        tmp_dut_info_list.append(
            read_csv_cell(
                full_file_name,
                1,
                self.general_column_header_index_dict["test_run_uuid"],
            )
        )

        return tmp_dut_info_list

    def test_items_append_into_summay_csv(
        self,
        full_file_name,
        tester_csv_log_test_name_column_list,
        list_write_to_summary_csv,
    ):
        """_summary_

        Args:
            full_file_name (_type_): tester parametric csv log path
            tester_csv_log_test_name_column_list (_type_): tester parametric csv log column 'test_name' list
            list_write_to_summary_csv (_type_): list which need to be wrote into summary csv file
        """
        for i in range(len(self.test_items)):
            if self.test_items[i] in tester_csv_log_test_name_column_list:
                list_write_to_summary_csv.append(
                    read_csv_cell(
                        full_file_name,
                        tester_csv_log_test_name_column_list.index(self.test_items[i]),
                        self.general_column_header_index_dict["test_value"],
                    )
                )
            else:
                list_write_to_summary_csv.append("")

        # for key in self.test_items.keys():
        #     if self.test_items[key] in column_test_name:
        #         list_write_to_summary_csv.append(
        #             read_csv_cell(
        #                 full_file_name,
        #                 column_test_name.index(self.test_items[key]),
        #                 self.general_column_header_index_dict["test_value"],
        #             )
        #         )
        #     else:
        #         list_write_to_summary_csv.append("")

    def search_integrate_csv_files(self, path):
        file_name_list = os.listdir(path)
        # print(file_name_list)
        for fn in file_name_list:
            """
            re.search(pattern, string, flags=0): scan all string list and return 1st matched string
            pattern: matched formatted types
            string:  need to be matched
            flags:   control match way
            """
            if re.search(r"\.csv$", fn):
                if fn != self.summary_file:
                    full_file_name = os.path.join(path, fn)
                    print(full_file_name)
                    tmp_list = []

                    if get_rows_quantity(full_file_name):
                        # Part1: SN, TestStation, WorkOrder这些信息
                        tmp_list = self.dut_info_append_into_summay_csv(full_file_name)

                        # Part2: Test items
                        tester_csv_log_test_name_column_list = read_csv_one_column(
                            full_file_name,
                            self.general_column_header_index_dict["test_name"],
                        )

                        self.test_items_append_into_summay_csv(
                            full_file_name,
                            tester_csv_log_test_name_column_list,
                            tmp_list,
                        )

                        write_row_to_csv(tmp_list, self.summary_file)
