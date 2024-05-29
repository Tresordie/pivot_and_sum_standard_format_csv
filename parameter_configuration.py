# -*- coding: utf-8 -*-
'''
@File    :   parameter_configuration.py
@Time    :   2024/05/29 23:08:31
@Author  :   SimonYuan 
@Version :   1.0
@Site    :   https://tresordie.github.io/
@Desc    :   None
'''


"""
**********************************************************************
    standard format csv folder path(need to be pivoted and summary)
**********************************************************************
"""
config_csv_folder_path = {
    "pcba_otp_path": "./maple_dvt_parametric_format/otp",
    "pcba_mcu_selftest_path": "./maple_dvt_parametric_format/mcu_self_test",
    "pcba_bms_path": "./maple_dvt_parametric_format/bms",
    "semi_pack_test1_path": "",
    "semi_pack_test2_path": "",
    "pack_test1_path": "",
    "pack_test2_path": "",
}


"""
**********************************************************************
    optional to select separate test stations to summary data
**********************************************************************
"""
config_enable_disable_summary_generation = {
    "pcba_otp_generation": True,
    "pcba_mcu_selftest_generation": True,
    "pcba_bms_generation": True,
    "semi_pack_test1_generation": True,
    "semi_pack_test2_generation": True,
    "pack_test1_generation": True,
    "pack_test2_generation": True,
}


"""
***************************************************
    standard csv log head row VS index
***************************************************
"""
general_column_header_index_dict = {
    "record_index": 0,
    "test_name": 1,
    "lower_limit": 2,
    "upper_limit": 3,
    "units": 4,
    "test_value": 5,
    "test_time": 6,
    "pass_fail_status": 7,
    "overall_test_result": 8,
    "exit_status": 9,
    "test_run_uuid": 10,
    "sn": 11,
    "start_time": 12,
    "end_time": 13,
    "work_order": 14,
    "test_station_name": 15,
    "test_station_id": 16,
}


dut_info_in_summary_csv_header = [
    # Work order and others
    "SerialNumber",
    "TestStation",
    "WorkOrder",
    "StartTime",
    "EndTime",
    "CycleTime(sec)",
    "OverallResult",
    "UUID",
]


"""
*****************************************************************************
    feed correct demo csv log to decide test items and summary csv header
*****************************************************************************
"""
maple_pcba_otp_demo_path = (
    "./demo/otp/20240515173830_PASS_SD2409MBMS205001A_Maple-BHBCS-1.csv"
)

maple_pcba_mcu_selftest_demo_path = (
    "./demo/mcu_self_test/20240513165112_PASS_SD2408MBHA2010227_Maple-BHBCS-2.csv"
)

maple_pcba_bms_demo_path = (
    "./demo/bms/20240524152735_PASS_SD2409MBMS205001A_Maple-BHBCS-3.csv"
)

maple_semi_pack1_demo_path = (
    "./demo/semi_pack/20240511204001_PASS_SD2419MBLC2010112_Maple-C-7.csv"
)

maple_semi_pack2_demo_path = (
    "./demo/semi_pack/20240513145657_PASS_SD2420MBAT2010057_Maple-C-10.csv"
)

maple_pack1_demo_path = (
    "./demo/pack/20240423175934_PASS_SD2412MBAT2010243_Maple-C-13.csv"
)

maple_pack2_demo_path = (
    "./demo/pack/20240423180502_PASS_SD2412MBAT2010243_Maple-C-14.csv"
)


"""
*****************************************************************************
    aws csv logs folder path and maple build stage
*****************************************************************************
"""
aws_csv_log_folder = "./aws_csv"
maple_build_stage = 'dvt'
