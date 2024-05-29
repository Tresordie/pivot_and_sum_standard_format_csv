# -*- coding: utf-8 -*-
'''
@File    :   summary_script.py
@Time    :   2024/05/29 22:33:32
@Author  :   SimonYuan 
@Version :   1.0
@Site    :   https://tresordie.github.io/
@Desc    :   None
'''


from general_test_stations_class import *
from parameter_configuration import *
from maple_csv_log_categorized_by_test_station import *


if __name__ == "__main__":
    """
    ***************************************************
        config csv folder path
    ***************************************************
    """
    maple_csv_log_categorized_by_test_station = (
        maple_csv_log_categorized_by_test_station(aws_csv_log_folder, maple_build_stage)
    )

    maple_csv_log_categorized_by_test_station.match_csv_log_with_keywords()

    """
    ***************************************************
        pcba_otp test summary
    ***************************************************
    """
    if config_enable_disable_summary_generation["pcba_otp_generation"]:
        maple_otp_ft_test = general_test_stations(
            "maple_otp_ft_summary",
            "maple_otp_ft_summary_sort",
            dut_info_in_summary_csv_header,
            general_column_header_index_dict,
            maple_pcba_otp_demo_path,
        )
        maple_otp_ft_test.create_csv_file_with_header()
        maple_otp_ft_test.search_integrate_csv_files(
            # config_csv_folder_path["pcba_otp_path"]
            maple_csv_log_categorized_by_test_station.pcba_otp_path
        )

        sort_csv(
            maple_otp_ft_test.summary_file,
            "StartTime",
            True,
            True,
            maple_otp_ft_test.summary_file_sort,
        )

    """
    ***************************************************
        pcba_mcu_self test summary
    ***************************************************
    """
    if config_enable_disable_summary_generation["pcba_mcu_selftest_generation"]:
        maple_mcu_selftest_ft_test = general_test_stations(
            "maple_mcu_selftest_ft_summary",
            "maple_mcu_selftest_ft_summary_sort",
            dut_info_in_summary_csv_header,
            general_column_header_index_dict,
            maple_pcba_mcu_selftest_demo_path,
        )
        maple_mcu_selftest_ft_test.create_csv_file_with_header()
        maple_mcu_selftest_ft_test.search_integrate_csv_files(
            # config_csv_folder_path["pcba_mcu_selftest_path"]
            maple_csv_log_categorized_by_test_station.pcba_mcu_selftest_path
        )

        sort_csv(
            maple_mcu_selftest_ft_test.summary_file,
            "StartTime",
            True,
            True,
            maple_mcu_selftest_ft_test.summary_file_sort,
        )

    """
    ***************************************************
        pcba_bms test summary
    ***************************************************
    """
    if config_enable_disable_summary_generation["pcba_bms_generation"]:
        maple_bms_ft_test = general_test_stations(
            "maple_bms_ft_summary",
            "maple_bms_ft_summary_sort",
            dut_info_in_summary_csv_header,
            general_column_header_index_dict,
            maple_pcba_bms_demo_path,
        )
        maple_bms_ft_test.create_csv_file_with_header()
        maple_bms_ft_test.search_integrate_csv_files(
            # config_csv_folder_path["pcba_bms_path"]
            maple_csv_log_categorized_by_test_station.pcba_bms_test_path
        )

        sort_csv(
            maple_bms_ft_test.summary_file,
            "StartTime",
            True,
            True,
            maple_bms_ft_test.summary_file_sort,
        )

    """
    ***************************************************
        semi_pack1 test summary
    ***************************************************
    """
    if config_enable_disable_summary_generation["semi_pack_test1_generation"]:
        maple_semi_pack1_test = general_test_stations(
            "maple_semi_pack1_ft_summary",
            "maple_semi_pack1_ft_summary_sort",
            dut_info_in_summary_csv_header,
            general_column_header_index_dict,
            maple_semi_pack1_demo_path,
        )
        maple_semi_pack1_test.create_csv_file_with_header()
        maple_semi_pack1_test.search_integrate_csv_files(
            # config_csv_folder_path["pcba_bms_path"]
            maple_csv_log_categorized_by_test_station.semipack1_test_path
        )

        sort_csv(
            maple_semi_pack1_test.summary_file,
            "StartTime",
            True,
            True,
            maple_semi_pack1_test.summary_file_sort,
        )

    """
    ***************************************************
        semi_pack2 test summary
    ***************************************************
    """
    if config_enable_disable_summary_generation["semi_pack_test2_generation"]:
        maple_semi_pack2_test = general_test_stations(
            "maple_semi_pack2_ft_summary",
            "maple_semi_pack2_ft_summary_sort",
            dut_info_in_summary_csv_header,
            general_column_header_index_dict,
            maple_semi_pack2_demo_path,
        )
        maple_semi_pack2_test.create_csv_file_with_header()
        maple_semi_pack2_test.search_integrate_csv_files(
            # config_csv_folder_path["pcba_bms_path"]
            maple_csv_log_categorized_by_test_station.semipack2_test_path
        )

        sort_csv(
            maple_semi_pack2_test.summary_file,
            "StartTime",
            True,
            True,
            maple_semi_pack2_test.summary_file_sort,
        )

    """
    ***************************************************
        pack1 test summary
    ***************************************************
    """
    if config_enable_disable_summary_generation["pack_test1_generation"]:
        maple_pack1_test = general_test_stations(
            "maple_pack1_ft_summary",
            "maple_pack1_ft_summary_sort",
            dut_info_in_summary_csv_header,
            general_column_header_index_dict,
            maple_pack1_demo_path,
        )
        maple_pack1_test.create_csv_file_with_header()
        maple_pack1_test.search_integrate_csv_files(
            # config_csv_folder_path["pcba_bms_path"]
            maple_csv_log_categorized_by_test_station.pack1_test_path
        )

        sort_csv(
            maple_pack1_test.summary_file,
            "StartTime",
            True,
            True,
            maple_pack1_test.summary_file_sort,
        )

    """
    ***************************************************
        pack2 test summary
    ***************************************************
    """
    if config_enable_disable_summary_generation["pack_test2_generation"]:
        maple_pack2_test = general_test_stations(
            "maple_pack2_ft_summary",
            "maple_pack2_ft_summary_sort",
            dut_info_in_summary_csv_header,
            general_column_header_index_dict,
            maple_pack2_demo_path,
        )
        maple_pack2_test.create_csv_file_with_header()
        maple_pack2_test.search_integrate_csv_files(
            # config_csv_folder_path["pcba_bms_path"]
            maple_csv_log_categorized_by_test_station.pack2_test_path
        )

        sort_csv(
            maple_pack2_test.summary_file,
            "StartTime",
            True,
            True,
            maple_pack2_test.summary_file_sort,
        )
