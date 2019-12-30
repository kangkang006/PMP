#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import threading
from ctypes import *
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import tkinter
from moduledata import moduledata_UI
from moduledata import moduledata_list

DevType = 4
DevIndex = 0
CANIndex_CAN1 = 0
CANIndex_CAN2 = 1
INKM_value = 0
Time_Num = 0
Time_Num1 = 0
Altitude_Num = 0
IntrinsicParameter_Num = 0
module_Num = 0
StartFailFlag = 0

class VCI_INIT_CONFIG(Structure):
    _fields_ = [("AccCode", c_int32),
                ("AccMask", c_int32),
                ("Reserved", c_int),
                ("Filter", c_ubyte),
                ("Timing0", c_ubyte),
                ("Timing1", c_ubyte),
                ("Mode", c_ubyte),
                ]
CAN1 = VCI_INIT_CONFIG()   # 定义结构对象
CAN1.AccCode = 0
CAN1.AccMask = 0xffffffff
CAN1.Reserved = 0
CAN1.Filter = 1
CAN1.Timing0 = 0x00            #500k  0x00      250k   0x01
CAN1.Timing1 = 0x1C            #500k  0x1C      250k   0x1c
CAN1.Mode = 0

CAN2 = VCI_INIT_CONFIG()   # 定义结构对象
CAN2.AccCode = 0
CAN2.AccMask = 0xffffffff
CAN2.Reserved = 0
CAN2.Filter = 1
CAN2.Timing0 = 0x01            #500k  0x00      250k   0x01
CAN2.Timing1 = 0x1C            #500k  0x1C      250k   0x1c
CAN2.Mode = 0

class VCI_CAN_OBJ(Structure):
    _fields_ = [("ID", c_int),
                ("TimeStamp", c_int),
                ("TimeFlag", c_ubyte),
                ("SendType", c_ubyte),
                ("RemoteFlag", c_ubyte),
                ("ExternFlag", c_ubyte),
                ("DataLen", c_ubyte),
                ("Data", c_ubyte*8),
                ("Reserved", c_ubyte*3),
                ]
Data1 = VCI_CAN_OBJ()
Data2 = VCI_CAN_OBJ()
Data3 = VCI_CAN_OBJ()
Data4 = VCI_CAN_OBJ()
Data5 = VCI_CAN_OBJ()
Data6 = VCI_CAN_OBJ()
Data7 = VCI_CAN_OBJ()
Data8 = VCI_CAN_OBJ()
Data9 = VCI_CAN_OBJ()
Data10 = VCI_CAN_OBJ()
Data11 = VCI_CAN_OBJ()
Data12 = VCI_CAN_OBJ()
Data13 = VCI_CAN_OBJ()
VIN_1 = VCI_CAN_OBJ()
VIN_2 = VCI_CAN_OBJ()
VIN_3 = VCI_CAN_OBJ()
TboxHeartBeat = VCI_CAN_OBJ()
CAN1_Receive = VCI_CAN_OBJ()
CAN2_Receive = VCI_CAN_OBJ()
Data = VCI_CAN_OBJ()
TboxWarning = VCI_CAN_OBJ()
TboxAltitude = VCI_CAN_OBJ()
module_data = VCI_CAN_OBJ()
# moduledata1_H = VCI_CAN_OBJ()
# moduledata2_L = VCI_CAN_OBJ()
# moduledata2_H = VCI_CAN_OBJ()
# moduledata3_L = VCI_CAN_OBJ()
# moduledata3_H = VCI_CAN_OBJ()
# moduledata4_L = VCI_CAN_OBJ()
# moduledata4_H = VCI_CAN_OBJ()
# moduledata5_L = VCI_CAN_OBJ()
# moduledata5_H = VCI_CAN_OBJ()
# moduledata6_L = VCI_CAN_OBJ()
# moduledata6_H = VCI_CAN_OBJ()
# moduledata7_L = VCI_CAN_OBJ()
# moduledata7_H = VCI_CAN_OBJ()

def my_print(Data):
    text1.insert(END, hex(Data.ID))
    text1.insert(END, ' ')
    text1.insert(END, hex(Data.DataLen))
    text1.insert(END, ' ')
    text1.insert(END, hex(Data.Data[0]))
    text1.insert(END, ' ')
    text1.insert(END, hex(Data.Data[1]))
    text1.insert(END, ' ')
    text1.insert(END, hex(Data.Data[2]))
    text1.insert(END, ' ')
    text1.insert(END, hex(Data.Data[3]))
    text1.insert(END, ' ')
    text1.insert(END, hex(Data.Data[4]))
    text1.insert(END, ' ')
    text1.insert(END, hex(Data.Data[5]))
    text1.insert(END, ' ')
    text1.insert(END, hex(Data.Data[6]))
    text1.insert(END, ' ')
    text1.insert(END, hex(Data.Data[7]))
    text1.insert(END, '\n')
    text1.see(END)

def my_print_Receive(Data):
    text.insert(END, hex(Data.ID))
    text.insert(END, ' ')
    text.insert(END, hex(Data.DataLen))
    text.insert(END, ' ')
    text.insert(END, hex(Data.Data[0]))
    text.insert(END, ' ')
    text.insert(END, hex(Data.Data[1]))
    text.insert(END, ' ')
    text.insert(END, hex(Data.Data[2]))
    text.insert(END, ' ')
    text.insert(END, hex(Data.Data[3]))
    text.insert(END, ' ')
    text.insert(END, hex(Data.Data[4]))
    text.insert(END, ' ')
    text.insert(END, hex(Data.Data[5]))
    text.insert(END, ' ')
    text.insert(END, hex(Data.Data[6]))
    text.insert(END, ' ')
    text.insert(END, hex(Data.Data[7]))
    text.insert(END, '\n')
    text.see(END)       #文本框滚动,自动显示最新的一行信息

def my_print_Warning(Data):
    text.insert(END, Data)
    text.insert(END, '\n')
    text.see(END)

root = tkinter.Tk()
root.title('增程测试')
root.state("zoomed")
# w = root.winfo_screenwidth()
# h = root.winfo_screenheight()
root.geometry("1200x800")
# scrollbar = Scrollbar(root,orient=VERTICAL)
# scrollbar.pack(side = RIGHT,fill =Y)
###############实时打印数据################################
e_RealTime_data1=tkinter.Label(root,text="接收数据")
e_RealTime_data1.pack()
e_RealTime_data1.place(x = 1190, y = 220, anchor = NW)
text = scrolledtext.ScrolledText(root, width=55, height=15)
text.pack()
text.place(x = 1190, y = 240, anchor = NW)
###############发送数据################################
e_RealTime_data2=tkinter.Label(root,text="发送数据")
e_RealTime_data2.pack()
e_RealTime_data2.place(x = 1190, y = 5, anchor = NW)
text1 = scrolledtext.ScrolledText(root, width=55, height=15)
text1.pack()
text1.place(x = 1190, y = 25, anchor = NW)
########################################################
dll = windll.LoadLibrary('D:/python test/PM_Plus/ControlCAN.dll')
Open_Status = dll.VCI_OpenDevice(DevType, DevIndex, 0)
print('Open_Status=',Open_Status)
text.insert(END, 'Open_Status=')
text.insert(END, Open_Status)
text.insert(END, '\n')
dll.VCI_InitCAN.argtypes = [c_int, c_int, c_int, VCI_INIT_CONFIG]
InitCAN1 = dll.VCI_InitCAN(DevType, DevIndex, CANIndex_CAN1, CAN1)
print('InitCAN1=',InitCAN1)
text.insert(END, 'InitCAN1=')
text.insert(END, InitCAN1)
text.insert(END, '\n')
InitCAN2 = dll.VCI_InitCAN(DevType, DevIndex, CANIndex_CAN2, CAN2)
print('InitCAN2=',InitCAN2)
text.insert(END, 'InitCAN2=')
text.insert(END, InitCAN2)
text.insert(END, '\n')
ClearBufferCAN1 = dll.VCI_ClearBuffer(DevType, DevIndex, CANIndex_CAN1)
print('ClearBufferCAN1=',ClearBufferCAN1)
text.insert(END, 'ClearBufferCAN1=')
text.insert(END, ClearBufferCAN1)
text.insert(END, '\n')
ClearBufferCAN2 = dll.VCI_ClearBuffer(DevType, DevIndex, CANIndex_CAN2)
print('ClearBufferCAN2=',ClearBufferCAN2)
text.insert(END, 'ClearBufferCAN2=')
text.insert(END, ClearBufferCAN2)
text.insert(END, '\n')
StartCAN1 = dll.VCI_StartCAN(DevType, DevIndex, CANIndex_CAN1)
print('StartCAN1=',StartCAN1)
text.insert(END, 'StartCAN1=')
text.insert(END, StartCAN1)
text.insert(END, '\n')
StartCAN2 = dll.VCI_StartCAN(DevType, DevIndex, CANIndex_CAN2)
print('StartCAN2=',StartCAN2)
text.insert(END, 'StartCAN2=')
text.insert(END, StartCAN2)
text.insert(END, '\n')

###############充电桩实时数据################################
e_RealTime_data=tkinter.Label(root,text="充电桩实时数据")
e_RealTime_data.pack()
e_RealTime_data.place(x = 0, y = 70, anchor = NW)
####################充电输出电流#######################################
e_OutCurrent_Label=tkinter.Label(root,text="充电输出电流（0.1A）")
e_OutCurrent_Label.pack()
e_OutCurrent_Label.place(x = 0, y = 100, anchor = NW)
default_value_OutCurrent = StringVar()
default_value_OutCurrent.set('0')
e_OutCurrent=tkinter.Entry(root,width=6,textvariable = default_value_OutCurrent)
e_OutCurrent.pack()
e_OutCurrent.place(x = 125, y = 100, anchor = NW)
###########################充电输出电压########################################
e_OutVoltage_Label=tkinter.Label(root,text="充电输出电压（0.1V）")
e_OutVoltage_Label.pack()
e_OutVoltage_Label.place(x = 0, y = 130, anchor = NW)
default_value_OutVoltage = StringVar()
default_value_OutVoltage.set('0')
e_OutVoltage=tkinter.Entry(root,width=6,textvariable = default_value_OutVoltage)
e_OutVoltage.pack()
e_OutVoltage.place(x = 125, y = 130, anchor = NW)
##########################输出接触器状态##########################################
e_OutKM_Label=tkinter.Label(root,text="输出接触器状态")
e_OutKM_Label.pack()
e_OutKM_Label.place(x = 0, y = 160, anchor = NW)

default_value_OutKM = StringVar()
e_OutKM=ttk.Combobox(root,textvariable = default_value_OutKM)
e_OutKM["values"] = ("断开0", "闭合1")
e_OutKM.current(0)      # 选择第一个
e_OutKM.pack()
e_OutKM.place(x = 125, y = 160, anchor = NW)
###########################充电接口电子锁状态##################################################
e_Lock_Label=tkinter.Label(root,text="充电接口电子锁状态")
e_Lock_Label.pack()
e_Lock_Label.place(x = 0, y = 190, anchor = NW)

default_value_Lock = StringVar()
e_Lock=ttk.Combobox(root,textvariable = default_value_Lock)
e_Lock["values"] = ("解锁0", "锁止1")
e_Lock.current(1)      # 选择第一个
e_Lock.pack()
e_Lock.place(x = 125, y = 190, anchor = NW)
#############################车辆通信状态###################################################
e_VehicleCom_Label=tkinter.Label(root,text="车辆通信状态")
e_VehicleCom_Label.pack()
e_VehicleCom_Label.place(x = 0, y = 220, anchor = NW)

default_value_VehicleCom = StringVar()
e_VehicleCom=ttk.Combobox(root,textvariable = default_value_VehicleCom)
e_VehicleCom["values"] = ("已连接0", "未连接1")
e_VehicleCom.current(0)      # 选择第一个
e_VehicleCom.pack()
e_VehicleCom.place(x = 125, y = 220, anchor = NW)
############################充电枪连接状态#########################################
e_ChargingGun_Label=tkinter.Label(root,text="充电枪连接状态")
e_ChargingGun_Label.pack()
e_ChargingGun_Label.place(x = 0, y = 250, anchor = NW)

default_value_ChargingGun = StringVar()
e_ChargingGun=ttk.Combobox(root,textvariable = default_value_ChargingGun)
e_ChargingGun["values"] = ("已连接0", "未连接1")
e_ChargingGun.current(0)      # 选择第一个
e_ChargingGun.pack()
e_ChargingGun.place(x = 125, y = 250, anchor = NW)
###############################单体电池最高电压#################################
e_SingleCellMaxVoltage_Label=tkinter.Label(root,text="单体电池最高电压(0.01V)")
e_SingleCellMaxVoltage_Label.pack()
e_SingleCellMaxVoltage_Label.place(x = 0, y = 280, anchor = NW)
default_value_SingleCellMaxVoltage = StringVar()
default_value_SingleCellMaxVoltage.set('0')
e_SingleCellMaxVoltage=tkinter.Entry(root,width=6,textvariable = default_value_SingleCellMaxVoltage)
e_SingleCellMaxVoltage.pack()
e_SingleCellMaxVoltage.place(x = 145, y = 280, anchor = NW)
#####################################单体电池最高电压编号######################################
e_SingleCellMaxVoltageNum_Label=tkinter.Label(root,text="单体电池最高电压编号")
e_SingleCellMaxVoltageNum_Label.pack()
e_SingleCellMaxVoltageNum_Label.place(x = 0, y = 490, anchor = NW)
default_value_SingleCellMaxVoltageNum = StringVar()
default_value_SingleCellMaxVoltageNum.set('0')
e_SingleCellMaxVoltageNum=tkinter.Entry(root,width=6,textvariable = default_value_SingleCellMaxVoltageNum)
e_SingleCellMaxVoltageNum.pack()
e_SingleCellMaxVoltageNum.place(x = 145, y = 490, anchor = NW)
###############################电池SOC#################################
e_SOC_Label=tkinter.Label(root,text="电池SOC(1%)")
e_SOC_Label.pack()
e_SOC_Label.place(x = 0, y = 310, anchor = NW)
default_value_SOC = StringVar()
default_value_SOC.set('0')
e_SOC=tkinter.Entry(root,width=6,textvariable = default_value_SOC)
e_SOC.pack()
e_SOC.place(x = 125, y = 310, anchor = NW)
##################################BMS电流需求_H&L(0.1 A/位；-400A 偏移)###################################
e_BMSCurrent_Label=tkinter.Label(root,text="BMS电流需求(0.1A/位)")
e_BMSCurrent_Label.pack()
e_BMSCurrent_Label.place(x = 0, y = 340, anchor = NW)
default_value_BMSCurrent = StringVar()
default_value_BMSCurrent.set('0')
e_BMSCurrent=tkinter.Entry(root,width=6,textvariable = default_value_BMSCurrent)
e_BMSCurrent.pack()
e_BMSCurrent.place(x = 145, y = 340, anchor = NW)
##################################BMS需求电压_H&L(0.1 V/位，0 V 偏移量)#########################################
e_BMSVoltage_Label=tkinter.Label(root,text="BMS电压需求(0.1V/位)")
e_BMSVoltage_Label.pack()
e_BMSVoltage_Label.place(x = 0, y = 370, anchor = NW)
default_value_BMSVoltage = StringVar()
default_value_BMSVoltage.set('0')
e_BMSVoltage=tkinter.Entry(root,width=6,textvariable = default_value_BMSVoltage)
e_BMSVoltage.pack()
e_BMSVoltage.place(x = 145, y = 370, anchor = NW)
#####################################充电机状态 (0:待机,1:工作, 2:充电完成(充满))##########################################
e_ChargerState_Label=tkinter.Label(root,text="充电机状态")
e_ChargerState_Label.pack()
e_ChargerState_Label.place(x = 0, y = 520, anchor = NW)

default_value_ChargerState = StringVar()
e_ChargerState=ttk.Combobox(root,textvariable = default_value_ChargerState)
e_ChargerState["values"] = ("待机0", "工作1", "充电完成（充满）2")
e_ChargerState.current(0)      # 选择第一个
e_ChargerState.pack()
e_ChargerState.place(x = 125, y = 520, anchor = NW)
#####################################电池组最低温度(1 ℃/位，-50 ℃偏移量)#############################################
e_BatteryTemMin_Label=tkinter.Label(root,text="电池组最低温度(1℃/位)")
e_BatteryTemMin_Label.pack()
e_BatteryTemMin_Label.place(x = 0, y = 400, anchor = NW)
default_value_BatteryTemMin = StringVar()
default_value_BatteryTemMin.set('0')
e_BatteryTemMin=tkinter.Entry(root,width=6,textvariable = default_value_BatteryTemMin)
e_BatteryTemMin.pack()
e_BatteryTemMin.place(x = 145, y = 400, anchor = NW)
#####################################电池组最高温度(1 ℃/位，-50 ℃偏移量)#############################################
e_BatteryTemMax_Label=tkinter.Label(root,text="电池组最高温度(1℃/位)")
e_BatteryTemMax_Label.pack()
e_BatteryTemMax_Label.place(x = 0, y = 430, anchor = NW)
default_value_BatteryTemMax = StringVar()
default_value_BatteryTemMax.set('0')
e_BatteryTemMax=tkinter.Entry(root,width=6,textvariable = default_value_BatteryTemMax)
e_BatteryTemMax.pack()
e_BatteryTemMax.place(x = 145, y = 430, anchor = NW)
####################################已充电电能_H&L(0.1kWh/位，偏移量0)####################################
e_ChargedPower_Label=tkinter.Label(root,text="已充电电能(0.1kWh/位)")
e_ChargedPower_Label.pack()
e_ChargedPower_Label.place(x = 0, y = 460, anchor = NW)
default_value_ChargedPower = StringVar()
default_value_ChargedPower.set('0')
e_ChargedPower=tkinter.Entry(root,width=6,textvariable = default_value_ChargedPower)
e_ChargedPower.pack()
e_ChargedPower.place(x = 145, y = 460, anchor = NW)
# #####################################单体电池最低电压######################################
# e_SingleCellMinVoltage_Label=tkinter.Label(root,text="单体电池最低电压(0.01V)")
# e_SingleCellMinVoltage_Label.pack()
# e_SingleCellMinVoltage_Label.place(x = 0, y = 490, anchor = NW)
# default_value_SingleCellMinVoltage = StringVar()
# default_value_SingleCellMinVoltage.set('0')
# e_SingleCellMinVoltage=tkinter.Entry(root,width=6,textvariable = default_value_SingleCellMinVoltage)
# e_SingleCellMinVoltage.pack()
# e_SingleCellMinVoltage.place(x = 145, y = 490, anchor = NW)
# ######################################模块输入继电器状态（0=断开，1=闭合）##############################################
# e_InKM_Label=tkinter.Label(root,text="模块输入继电器状态")
# e_InKM_Label.pack()
# e_InKM_Label.place(x = 0, y = 550, anchor = NW)
#
# default_value_InKM = StringVar()
# e_InKM=ttk.Combobox(root,textvariable = default_value_InKM)
# e_InKM["values"] = ("断开0", "闭合1")
# e_InKM.current(0)      # 选择第一个
# e_InKM.pack()
# e_InKM.place(x = 125, y = 550, anchor = NW)
######################################主充电板版本号H######################################
e_MainChargerVersionH_Label=tkinter.Label(root,text="主充电板版本号H")
e_MainChargerVersionH_Label.pack()
e_MainChargerVersionH_Label.place(x = 0, y = 700, anchor = NW)
default_value_MainChargerVersionH = StringVar()
default_value_MainChargerVersionH.set('0')
e_MainChargerVersionH=tkinter.Entry(root,width=6,textvariable = default_value_MainChargerVersionH)
e_MainChargerVersionH.pack()
e_MainChargerVersionH.place(x = 145, y = 700, anchor = NW)
######################################主充电板版本号L######################################
e_MainChargerVersionL_Label=tkinter.Label(root,text="主充电板版本号L")
e_MainChargerVersionL_Label.pack()
e_MainChargerVersionL_Label.place(x = 0, y = 730, anchor = NW)
default_value_MainChargerVersionL = StringVar()
default_value_MainChargerVersionL.set('0')
e_MainChargerVersionL=tkinter.Entry(root,width=6,textvariable = default_value_MainChargerVersionL)
e_MainChargerVersionL.pack()
e_MainChargerVersionL.place(x = 145, y = 730, anchor = NW)
######################################估算剩余充电时间_H&L(1 min/位，0 min 偏移量)######################################
e_RemainChargingTime_Label=tkinter.Label(root,text="估算剩余充电时间(1min/位)")
e_RemainChargingTime_Label.pack()
e_RemainChargingTime_Label.place(x = 0, y = 670, anchor = NW)
default_value_RemainChargingTime = StringVar()
default_value_RemainChargingTime.set('0')
e_RemainChargingTime=tkinter.Entry(root,width=6,textvariable = default_value_RemainChargingTime)
e_RemainChargingTime.pack()
e_RemainChargingTime.place(x = 155, y = 670, anchor = NW)
######################################辅充电板版本号H######################################
e_AssistChargerVersionH_Label=tkinter.Label(root,text="辅充电板版本号H")
e_AssistChargerVersionH_Label.pack()
e_AssistChargerVersionH_Label.place(x = 0, y = 760, anchor = NW)
default_value_AssistChargerVersionH = StringVar()
default_value_AssistChargerVersionH.set('0')
e_AssistChargerVersionH=tkinter.Entry(root,width=6,textvariable = default_value_AssistChargerVersionH)
e_AssistChargerVersionH.pack()
e_AssistChargerVersionH.place(x = 145, y = 760, anchor = NW)
######################################辅充电板版本号L######################################
e_AssistChargerVersionL_Label=tkinter.Label(root,text="辅充电板版本号L")
e_AssistChargerVersionL_Label.pack()
e_AssistChargerVersionL_Label.place(x = 0, y = 790, anchor = NW)
default_value_AssistChargerVersionL = StringVar()
default_value_AssistChargerVersionL.set('0')
e_AssistChargerVersionL=tkinter.Entry(root,width=6,textvariable = default_value_AssistChargerVersionL)
e_AssistChargerVersionL.pack()
e_AssistChargerVersionL.place(x = 145, y = 790, anchor = NW)
######################################启动失败原因/停止原因,见故障代码######################################
e_StartupFailCode_Label=tkinter.Label(root,text="启动失败/停止原因")
e_StartupFailCode_Label.pack()
e_StartupFailCode_Label.place(x = 0, y = 610, anchor = NW)
default_value_StartupFailCode = StringVar()
default_value_StartupFailCode.set('0')
e_StartupFailCode=tkinter.Entry(root,width=6,textvariable = default_value_StartupFailCode)
e_StartupFailCode.pack()
e_StartupFailCode.place(x = 145, y = 610, anchor = NW)
######################################停止状态：0x00-未知状态；0x01-完成;0x02-失败##############################################
e_StopStatus_Label=tkinter.Label(root,text="停止状态")
e_StopStatus_Label.pack()
e_StopStatus_Label.place(x = 0, y = 550, anchor = NW)

default_value_StopStatus = StringVar()
e_StopStatus=ttk.Combobox(root,textvariable = default_value_StopStatus)
e_StopStatus["values"] = ("未知状态0", "完成1", "失败2")
e_StopStatus.current(0)      # 选择第一个
e_StopStatus.pack()
e_StopStatus.place(x = 125, y = 550, anchor = NW)
######################################启动状态：0x00-未知状态；0x01-完成;0x02-失败##############################################
e_StartStatus_Label=tkinter.Label(root,text="启动状态")
e_StartStatus_Label.pack()
e_StartStatus_Label.place(x = 0, y = 580, anchor = NW)

default_value_StartStatus = StringVar()
e_StartStatus=ttk.Combobox(root,textvariable = default_value_StartStatus)
e_StartStatus["values"] = ("未知状态0", "完成1", "失败2")
e_StartStatus.current(0)      # 选择第一个
e_StartStatus.pack()
e_StartStatus.place(x = 125, y = 580, anchor = NW)

###############充电桩实时告警数据################################
e_RealTimeWarning_data=tkinter.Label(root,text="充电桩实时告警数据")
e_RealTimeWarning_data.pack()
e_RealTimeWarning_data.place(x = 300, y = 10, anchor = NW)
############################电表通讯异常################################
chVarElecCom = tkinter.IntVar()
check1 = tkinter.Checkbutton(root, text="电表通讯异常", variable=chVarElecCom)
check1.deselect()
check1.place(x = 300, y = 40, anchor = NW)
############################主辅充电板通讯异常################################
chVarChargerCom = tkinter.IntVar()
check2 = tkinter.Checkbutton(root, text="主辅充电板通讯异常", variable=chVarChargerCom)
check2.deselect()
check2.place(x = 300, y = 70, anchor = NW)
############################急停故障################################
chVarESTOP = tkinter.IntVar()
check3 = tkinter.Checkbutton(root, text="急停故障", variable=chVarESTOP)
check3.deselect()
check3.place(x = 300, y = 100, anchor = NW)
############################充电接口子锁故障################################
chVarChargerLock = tkinter.IntVar()
check4 = tkinter.Checkbutton(root, text="充电接口子锁故障", variable=chVarChargerLock)
check4.deselect()
check4.place(x = 300, y = 130, anchor = NW)
############################充电桩风扇故障################################
chVarChargerFan = tkinter.IntVar()
check5 = tkinter.Checkbutton(root, text="充电桩风扇故障", variable=chVarChargerFan)
check5.deselect()
check5.place(x = 300, y = 160, anchor = NW)
############################避雷器故障################################
chVarLightningArrester = tkinter.IntVar()
check6 = tkinter.Checkbutton(root, text="避雷器故障", variable=chVarLightningArrester)
check6.deselect()
check6.place(x = 300, y = 190, anchor = NW)
############################绝缘检测通讯超时故障################################
chVarInsulationDetect = tkinter.IntVar()
check7 = tkinter.Checkbutton(root, text="绝缘检测通讯超时故障", variable=chVarInsulationDetect)
check7.deselect()
check7.place(x = 300, y = 220, anchor = NW)
############################电池极性反接故障################################
chVarReversePolarity = tkinter.IntVar()
check8 = tkinter.Checkbutton(root, text="电池极性反接故障", variable=chVarReversePolarity)
check8.deselect()
check8.place(x = 300, y = 250, anchor = NW)
#############################1充电模块故障标志################################
chVarChargingModule1 = tkinter.IntVar()
check9 = tkinter.Checkbutton(root, text="#1充电模块故障标志1", variable=chVarChargingModule1)
check9.deselect()
check9.place(x = 300, y = 280, anchor = NW)
#############################2充电模块故障标志################################
chVarChargingModule2 = tkinter.IntVar()
check10 = tkinter.Checkbutton(root, text="#2充电模块故障标志1", variable=chVarChargingModule2)
check10.deselect()
check10.place(x = 300, y = 310, anchor = NW)
#############################3充电模块故障标志################################
chVarChargingModule3 = tkinter.IntVar()
check11 = tkinter.Checkbutton(root, text="#3充电模块故障标志1", variable=chVarChargingModule3)
check11.deselect()
check11.place(x = 300, y = 340, anchor = NW)
#############################4充电模块故障标志################################
chVarChargingModule4 = tkinter.IntVar()
check12 = tkinter.Checkbutton(root, text="#4充电模块故障标志1", variable=chVarChargingModule4)
check12.deselect()
check12.place(x = 300, y = 370, anchor = NW)
#############################5充电模块故障标志################################
chVarChargingModule5 = tkinter.IntVar()
check13 = tkinter.Checkbutton(root, text="#5充电模块故障标志1", variable=chVarChargingModule5)
check13.deselect()
check13.place(x = 300, y = 400, anchor = NW)
#############################6充电模块故障标志################################
chVarChargingModule6 = tkinter.IntVar()
check14 = tkinter.Checkbutton(root, text="#6充电模块故障标志1", variable=chVarChargingModule6)
check14.deselect()
check14.place(x = 300, y = 430, anchor = NW)
#############################7充电模块故障标志################################
chVarChargingModule7 = tkinter.IntVar()
check15 = tkinter.Checkbutton(root, text="#7充电模块故障标志1", variable=chVarChargingModule7)
check15.deselect()
check15.place(x = 300, y = 460, anchor = NW)
#############################充电模块总故障################################
chVarChargingModuleSum = tkinter.IntVar()
check16 = tkinter.Checkbutton(root, text="充电模块总故障", variable=chVarChargingModuleSum)
check16.deselect()
check16.place(x = 300, y = 490, anchor = NW)
#############################充电模块直流输出短路故障################################
chVarDCOutShort = tkinter.IntVar()
check17 = tkinter.Checkbutton(root, text="充电模块直流输出短路故障", variable=chVarDCOutShort)
check17.deselect()
check17.place(x = 300, y = 520, anchor = NW)
#############################母排电压异常################################
chVarBusVoltageAbnormal = tkinter.IntVar()
check18 = tkinter.Checkbutton(root, text="母排电压异常", variable=chVarBusVoltageAbnormal)
check18.deselect()
check18.place(x = 300, y = 550, anchor = NW)
#############################电池异常终止################################
chVarBatteryTermination = tkinter.IntVar()
check19 = tkinter.Checkbutton(root, text="电池异常终止", variable=chVarBatteryTermination)
check19.deselect()
check19.place(x = 300, y = 580, anchor = NW)
#############################单体电压超限################################
chVarSigleCellVoltageOver = tkinter.IntVar()
check20 = tkinter.Checkbutton(root, text="单体电压超限", variable=chVarSigleCellVoltageOver)
check20.deselect()
check20.place(x = 300, y = 610, anchor = NW)
#############################门禁故障################################
chVarEntranceGuardFault = tkinter.IntVar()
check21 = tkinter.Checkbutton(root, text="门禁故障", variable=chVarEntranceGuardFault)
check21.deselect()
check21.place(x = 300, y = 640, anchor = NW)
#############################直流输出接触器粘连故障################################
chVarDCOutKMAdhesion = tkinter.IntVar()
check22 = tkinter.Checkbutton(root, text="直流输出接触器粘连故障", variable=chVarDCOutKMAdhesion)
check22.deselect()
check22.place(x = 300, y = 670, anchor = NW)
#############################模块输入接触器粘连故障（KM3/KM4）################################
chVarINKMAdhesion = tkinter.IntVar()
check37 = tkinter.Checkbutton(root, text="模块输入接触器粘连故障", variable=chVarINKMAdhesion)
check37.deselect()
check37.place(x = 300, y = 700, anchor = NW)
#############################枪温度过高故障################################
chVarGunTemHigh = tkinter.IntVar()
check38 = tkinter.Checkbutton(root, text="枪温度过高故障", variable=chVarGunTemHigh)
check38.deselect()
check38.place(x = 300, y = 730, anchor = NW)
#############################输入欠压告警################################
chVarInputUnderVoltageWarning = tkinter.IntVar()
check39 = tkinter.Checkbutton(root, text="输入欠压告警1", variable=chVarInputUnderVoltageWarning)
check39.deselect()
check39.place(x = 300, y = 760, anchor = NW)
#############################输入欠压故障################################
chVarInputUnderVoltageFailure = tkinter.IntVar()
check40 = tkinter.Checkbutton(root, text="输入欠压故障", variable=chVarInputUnderVoltageFailure)
check40.deselect()
check40.place(x = 300, y = 790, anchor = NW)
#############################BMS中止错误原因################################
e_BMSAbortReason=tkinter.Label(root,text="BMS中止错误原因")
e_BMSAbortReason.pack()
e_BMSAbortReason.place(x = 750, y = 160, anchor = NW)
#############################电流过大################################
chVarCurrentOver = tkinter.IntVar()
check23 = tkinter.Checkbutton(root, text="电流过大", variable=chVarCurrentOver)
check23.deselect()
check23.place(x = 750, y = 190, anchor = NW)
#############################电压异常################################
chVarVoltageAbnormal = tkinter.IntVar()
check24 = tkinter.Checkbutton(root, text="电压异常", variable=chVarVoltageAbnormal)
check24.deselect()
check24.place(x = 750, y = 220, anchor = NW)
#############################BMS充电故障原因################################
e_BMSChargingFailReason=tkinter.Label(root,text="BMS充电故障原因")
e_BMSChargingFailReason.pack()
e_BMSChargingFailReason.place(x = 500, y = 10, anchor = NW)
#############################绝缘故障################################
chVarInsulationFail = tkinter.IntVar()
check25 = tkinter.Checkbutton(root, text="绝缘故障", variable=chVarInsulationFail)
check25.deselect()
check25.place(x = 500, y = 40, anchor = NW)
#############################输出连接器过温故障################################
chVarOutConnectorOverTem = tkinter.IntVar()
check26 = tkinter.Checkbutton(root, text="输出连接器过温故障", variable=chVarOutConnectorOverTem)
check26.deselect()
check26.place(x = 500, y = 70, anchor = NW)
#############################BMS元件、输出连接器过温################################
chVarBMSOutConnectorOverTem = tkinter.IntVar()
check27 = tkinter.Checkbutton(root, text="BMS元件、输出连接器过温", variable=chVarBMSOutConnectorOverTem)
check27.deselect()
check27.place(x = 500, y = 100, anchor = NW)
#############################充电连接器故障################################
chVarChargerConnector = tkinter.IntVar()
check28 = tkinter.Checkbutton(root, text="充电连接器故障", variable=chVarChargerConnector)
check28.deselect()
check28.place(x = 500, y = 130, anchor = NW)
#############################电池组温度过高故障################################
chVarBatteryTemHigh = tkinter.IntVar()
check29 = tkinter.Checkbutton(root, text="电池组温度过高故障", variable=chVarBatteryTemHigh)
check29.deselect()
check29.place(x = 500, y = 160, anchor = NW)
#############################高压继电器故障################################
chVarHighVoltageRelay = tkinter.IntVar()
check30 = tkinter.Checkbutton(root, text="高压继电器故障", variable=chVarHighVoltageRelay)
check30.deselect()
check30.place(x = 500, y = 190, anchor = NW)
#############################检测点2电压检测故障################################
chVarPoint2Voltage = tkinter.IntVar()
check31 = tkinter.Checkbutton(root, text="检测点2电压检测故障", variable=chVarPoint2Voltage)
check31.deselect()
check31.place(x = 500, y = 220, anchor = NW)
#############################其他故障################################
chVarOtherFault = tkinter.IntVar()
check32 = tkinter.Checkbutton(root, text="其他故障", variable=chVarOtherFault)
check32.deselect()
check32.place(x = 500, y = 250, anchor = NW)
#############################BMS中止充电原因################################
e_BMSStopChargeReason=tkinter.Label(root,text="BMS中止充电原因")
e_BMSStopChargeReason.pack()
e_BMSStopChargeReason.place(x = 500, y = 280, anchor = NW)
#############################达到所需求的SOC目标值################################
chVarReachSOC = tkinter.IntVar()
check33 = tkinter.Checkbutton(root, text="达到所需求的SOC目标值1", variable=chVarReachSOC)
check33.deselect()
check33.place(x = 500, y = 310, anchor = NW)
#############################达到总电压的设定值################################
chVarReachVoltage = tkinter.IntVar()
check34 = tkinter.Checkbutton(root, text="达到总电压的设定值1", variable=chVarReachVoltage)
check34.deselect()
check34.place(x = 500, y = 340, anchor = NW)
#############################达到单体电压的设定值################################
chVarReachSingleCellVoltage = tkinter.IntVar()
check35 = tkinter.Checkbutton(root, text="达到单体电压的设定值1", variable=chVarReachSingleCellVoltage)
check35.deselect()
check35.place(x = 500, y = 370, anchor = NW)
#############################充电机主动中止################################
chVarChargerActiveStop = tkinter.IntVar()
check36 = tkinter.Checkbutton(root, text="充电机主动中止1", variable=chVarChargerActiveStop)
check36.deselect()
check36.place(x = 500, y = 400, anchor = NW)
#############################输入过压告警################################
chVarInputOverVoltageWarning = tkinter.IntVar()
check41 = tkinter.Checkbutton(root, text="输入过压告警1", variable=chVarInputOverVoltageWarning)
check41.deselect()
check41.place(x = 750, y = 280, anchor = NW)
#############################输入过压故障################################
chVarInputOverVoltageFailure = tkinter.IntVar()
check42 = tkinter.Checkbutton(root, text="输入过压故障", variable=chVarInputOverVoltageFailure)
check42.deselect()
check42.place(x = 750, y = 310, anchor = NW)
#############################绝缘电阻低告警（>100ohm/v & <500ohm/v）################################
chVarInsulationResistorLowWarning = tkinter.IntVar()
check43 = tkinter.Checkbutton(root, text="绝缘电阻低告警1", variable=chVarInsulationResistorLowWarning)
check43.deselect()
check43.place(x = 750, y = 340, anchor = NW)
#############################枪温度过高告警################################
chVarGunTemHighWarning = tkinter.IntVar()
check44 = tkinter.Checkbutton(root, text="枪温度过高告警1", variable=chVarGunTemHighWarning)
check44.deselect()
check44.place(x = 750, y = 370, anchor = NW)
#######################################################################
#############################充电参数################################
e_ChargeParameters=tkinter.Label(root,text="充电参数")
e_ChargeParameters.pack()
e_ChargeParameters.place(x = 780, y = 400, anchor = NW)
####################################充电枪温度####################################
e_ChargingGunTem_Label=tkinter.Label(root,text="充电枪温度(1°C)")
e_ChargingGunTem_Label.pack()
e_ChargingGunTem_Label.place(x = 870, y = 400, anchor = NW)
default_value_ChargingGunTem = StringVar()
default_value_ChargingGunTem.set('0')
e_ChargingGunTem=tkinter.Entry(root,width=6,textvariable = default_value_ChargingGunTem)
e_ChargingGunTem.pack()
e_ChargingGunTem.place(x = 970, y = 400, anchor = NW)
####################################电表累计电量####################################
e_ChargingGunTem_Label=tkinter.Label(root,text="电表累计电量(0.01kW)")
e_ChargingGunTem_Label.pack()
e_ChargingGunTem_Label.place(x = 1015, y = 400, anchor = NW)
default_value_CumulativePower = StringVar()
default_value_CumulativePower.set('0')
e_CumulativePower=tkinter.Entry(root,width=6,textvariable = default_value_CumulativePower)
e_CumulativePower.pack()
e_CumulativePower.place(x = 1140, y = 400, anchor = NW)
####################################充电桩最大输出功率####################################
e_MaxOutputPower_Label=tkinter.Label(root,text="最大输出功率(0.1kW)")
e_MaxOutputPower_Label.pack()
e_MaxOutputPower_Label.place(x = 780, y = 430, anchor = NW)
default_value_MaxOutputPower = StringVar()
default_value_MaxOutputPower.set('0')
e_MaxOutputPower=tkinter.Entry(root,width=6,textvariable = default_value_MaxOutputPower,state = DISABLED)
e_MaxOutputPower.pack()
e_MaxOutputPower.place(x = 900, y = 430, anchor = NW)

default_value_MaxOutputPowerSet = StringVar()
default_value_MaxOutputPowerSet.set('0')
e_MaxOutputPowerSet=tkinter.Entry(root,width=6,textvariable = default_value_MaxOutputPowerSet)
e_MaxOutputPowerSet.pack()
e_MaxOutputPowerSet.place(x = 970, y = 430, anchor = NW)
####################################电流上升时间####################################
e_CurrentRiseTime_Label=tkinter.Label(root,text="电流上升时间(s)")
e_CurrentRiseTime_Label.pack()
e_CurrentRiseTime_Label.place(x = 780, y = 460, anchor = NW)
default_value_CurrentRiseTime = StringVar()
default_value_CurrentRiseTime.set('0')
e_CurrentRiseTime=tkinter.Entry(root,width=6,textvariable = default_value_CurrentRiseTime,state = DISABLED)
e_CurrentRiseTime.pack()
e_CurrentRiseTime.place(x = 900, y = 460, anchor = NW)

default_value_CurrentRiseTimeSet = StringVar()
default_value_CurrentRiseTimeSet.set('0')
e_CurrentRiseTimeSet=tkinter.Entry(root,width=6,textvariable = default_value_CurrentRiseTimeSet)
e_CurrentRiseTimeSet.pack()
e_CurrentRiseTimeSet.place(x = 970, y = 460, anchor = NW)
####################################最大电压限值####################################
e_MaxVoltageLimit_Label=tkinter.Label(root,text="最大电压限值(0.1V)")
e_MaxVoltageLimit_Label.pack()
e_MaxVoltageLimit_Label.place(x = 780, y = 490, anchor = NW)
default_value_MaxVoltageLimit = StringVar()
default_value_MaxVoltageLimit.set('0')
e_MaxVoltageLimit=tkinter.Entry(root,width=6,textvariable = default_value_MaxVoltageLimit,state = DISABLED)
e_MaxVoltageLimit.pack()
e_MaxVoltageLimit.place(x = 900, y = 490, anchor = NW)

default_value_MaxVoltageLimitSet = StringVar()
default_value_MaxVoltageLimitSet.set('0')
e_MaxVoltageLimitSet=tkinter.Entry(root,width=6,textvariable = default_value_MaxVoltageLimitSet)
e_MaxVoltageLimitSet.pack()
e_MaxVoltageLimitSet.place(x = 970, y = 490, anchor = NW)
####################################最大电流限值####################################
e_MaxCurrentLimit_Label=tkinter.Label(root,text="最大电流限值(0.1A)")
e_MaxCurrentLimit_Label.pack()
e_MaxCurrentLimit_Label.place(x = 780, y = 520, anchor = NW)
default_value_MaxCurrentLimit = StringVar()
default_value_MaxCurrentLimit.set('0')
e_MaxCurrentLimit=tkinter.Entry(root,width=6,textvariable = default_value_MaxCurrentLimit,state = DISABLED)
e_MaxCurrentLimit.pack()
e_MaxCurrentLimit.place(x = 900, y = 520, anchor = NW)

default_value_MaxCurrentLimitSet = StringVar()
default_value_MaxCurrentLimitSet.set('0')
e_MaxCurrentLimitSet=tkinter.Entry(root,width=6,textvariable = default_value_MaxCurrentLimitSet)
e_MaxCurrentLimitSet.pack()
e_MaxCurrentLimitSet.place(x = 970, y = 520, anchor = NW)
####################################输入过压门槛####################################
e_InputOverVoltageThreshold_Label=tkinter.Label(root,text="输入过压门槛(0.1V)")
e_InputOverVoltageThreshold_Label.pack()
e_InputOverVoltageThreshold_Label.place(x = 780, y = 550, anchor = NW)
default_value_InputOverVoltageThreshold = StringVar()
default_value_InputOverVoltageThreshold.set('0')
e_InputOverVoltageThreshold=tkinter.Entry(root,width=6,textvariable = default_value_InputOverVoltageThreshold,state = DISABLED)
e_InputOverVoltageThreshold.pack()
e_InputOverVoltageThreshold.place(x = 900, y = 550, anchor = NW)

default_value_InputOverVoltageThresholdSet = StringVar()
default_value_InputOverVoltageThresholdSet.set('0')
e_InputOverVoltageThresholdSet=tkinter.Entry(root,width=6,textvariable = default_value_InputOverVoltageThresholdSet)
e_InputOverVoltageThresholdSet.pack()
e_InputOverVoltageThresholdSet.place(x = 970, y = 550, anchor = NW)
####################################车辆VIN####################################
e_VIN_Label=tkinter.Label(root,text="车辆VIN(17位)")
e_VIN_Label.pack()
e_VIN_Label.place(x = 780, y = 580, anchor = NW)
default_value_VIN = StringVar()
default_value_VIN.set('00000000000000000')
e_VIN=tkinter.Entry(root,width=20,textvariable = default_value_VIN)
e_VIN.pack()
e_VIN.place(x = 900, y = 580, anchor = NW)

#############################发电机实时数据################################
e_GeneratorRealData=tkinter.Label(root,text="发电机实时数据")
e_GeneratorRealData.pack()
e_GeneratorRealData.place(x = 500, y = 430, anchor = NW)
####################################发动机转速####################################
e_ECURpm_Label=tkinter.Label(root,text="发动机转速(0~5000)")
e_ECURpm_Label.pack()
e_ECURpm_Label.place(x = 500, y = 460, anchor = NW)
default_value_ECURpm = StringVar()
default_value_ECURpm.set('0')
e_ECURpm=tkinter.Entry(root,width=6,textvariable = default_value_ECURpm)
e_ECURpm.pack()
e_ECURpm.place(x = 620, y = 460, anchor = NW)
#####################################手刹状态0：松开；1：拉起##########################################
e_HandBrakeState_Label=tkinter.Label(root,text="手刹状态")
e_HandBrakeState_Label.pack()
e_HandBrakeState_Label.place(x = 500, y = 490, anchor = NW)

default_value_HandBrakeState = StringVar()
e_HandBrakeState=ttk.Combobox(root,textvariable = default_value_HandBrakeState)
e_HandBrakeState["values"] = ("松开0", "拉起1")
e_HandBrakeState.current(0)      # 选择第一个
e_HandBrakeState.pack()
e_HandBrakeState.place(x = 560, y = 490, anchor = NW)
#####################################取力器状态  0：未到位；1：到位##########################################
e_PTOState_Label=tkinter.Label(root,text="取力器状态")
e_PTOState_Label.pack()
e_PTOState_Label.place(x = 500, y = 520, anchor = NW)

default_value_PTOState = StringVar()
e_PTOState=ttk.Combobox(root,textvariable = default_value_PTOState)
e_PTOState["values"] = ("未到位0", "到位1")
e_PTOState.current(0)      # 选择第一个
e_PTOState.pack()
e_PTOState.place(x = 570, y = 520, anchor = NW)
#####################################离合器状态  0：松开；1：踩下##########################################
e_ClutchState_Label=tkinter.Label(root,text="离合器状态")
e_ClutchState_Label.pack()
e_ClutchState_Label.place(x = 500, y = 550, anchor = NW)

default_value_ClutchState = StringVar()
e_ClutchState=ttk.Combobox(root,textvariable = default_value_ClutchState)
e_ClutchState["values"] = ("松开0", "踩下1")
e_ClutchState.current(0)      # 选择第一个
e_ClutchState.pack()
e_ClutchState.place(x = 570, y = 550, anchor = NW)
#####################################稳压模块输出过压  0：正常； 1： 异常##########################################
e_OutOverVoltage_Label=tkinter.Label(root,text="稳压模块输出过压")
e_OutOverVoltage_Label.pack()
e_OutOverVoltage_Label.place(x = 500, y = 580, anchor = NW)

default_value_OutOverVoltage = StringVar()
e_OutOverVoltage=ttk.Combobox(root,textvariable = default_value_OutOverVoltage)
e_OutOverVoltage["values"] = ("正常0", "异常1")
e_OutOverVoltage.current(0)      # 选择第一个
e_OutOverVoltage.pack()
e_OutOverVoltage.place(x = 610, y = 580, anchor = NW)
#####################################稳压模块输出过流  0：正常； 1： 异常##########################################
e_OutOverCurrent_Label=tkinter.Label(root,text="稳压模块输出过流")
e_OutOverCurrent_Label.pack()
e_OutOverCurrent_Label.place(x = 500, y = 610, anchor = NW)

default_value_OutOverCurrent = StringVar()
e_OutOverCurrent=ttk.Combobox(root,textvariable = default_value_OutOverCurrent)
e_OutOverCurrent["values"] = ("正常0", "异常1")
e_OutOverCurrent.current(0)      # 选择第一个
e_OutOverCurrent.pack()
e_OutOverCurrent.place(x = 610, y = 610, anchor = NW)
#####################################稳压模块系统过热  0：正常； 1： 异常##########################################
e_SystemOverHeat_Label=tkinter.Label(root,text="稳压模块系统过热")
e_SystemOverHeat_Label.pack()
e_SystemOverHeat_Label.place(x = 500, y = 640, anchor = NW)

default_value_SystemOverHeat = StringVar()
e_SystemOverHeat=ttk.Combobox(root,textvariable = default_value_SystemOverHeat)
e_SystemOverHeat["values"] = ("正常0", "异常1")
e_SystemOverHeat.current(0)      # 选择第一个
e_SystemOverHeat.pack()
e_SystemOverHeat.place(x = 610, y = 640, anchor = NW)
#####################################稳压模块输出反接  0：正常； 1： 异常##########################################
e_OutputReverse_Label=tkinter.Label(root,text="稳压模块输出反接")
e_OutputReverse_Label.pack()
e_OutputReverse_Label.place(x = 500, y = 670, anchor = NW)

default_value_OutputReverse = StringVar()
e_OutputReverse=ttk.Combobox(root,textvariable = default_value_OutputReverse)
e_OutputReverse["values"] = ("正常0", "异常1")
e_OutputReverse.current(0)      # 选择第一个
e_OutputReverse.pack()
e_OutputReverse.place(x = 610, y = 670, anchor = NW)
#####################################稳压模块输出过载  0：正常； 1： 异常##########################################
e_OutputOverLoad_Label=tkinter.Label(root,text="稳压模块输出过载")
e_OutputOverLoad_Label.pack()
e_OutputOverLoad_Label.place(x = 500, y = 700, anchor = NW)

default_value_OutputOverLoad = StringVar()
e_OutputOverLoad=ttk.Combobox(root,textvariable = default_value_OutputOverLoad)
e_OutputOverLoad["values"] = ("正常0", "异常1")
e_OutputOverLoad.current(0)      # 选择第一个
e_OutputOverLoad.pack()
e_OutputOverLoad.place(x = 610, y = 700, anchor = NW)
#####################################稳压模块输出欠压  0：正常； 1： 异常##########################################
e_OutputUnderVoltage_Label=tkinter.Label(root,text="稳压模块输出欠压")
e_OutputUnderVoltage_Label.pack()
e_OutputUnderVoltage_Label.place(x = 500, y = 730, anchor = NW)

default_value_OutputUnderVoltage = StringVar()
e_OutputUnderVoltage=ttk.Combobox(root,textvariable = default_value_OutputUnderVoltage)
e_OutputUnderVoltage["values"] = ("正常0", "异常1")
e_OutputUnderVoltage.current(0)      # 选择第一个
e_OutputUnderVoltage.pack()
e_OutputUnderVoltage.place(x = 610, y = 730, anchor = NW)
#####################################稳压模块输入过压  0：正常； 1： 异常##########################################
e_InputOverVoltage_Label=tkinter.Label(root,text="稳压模块输入过压")
e_InputOverVoltage_Label.pack()
e_InputOverVoltage_Label.place(x = 500, y = 760, anchor = NW)

default_value_InputOverVoltage = StringVar()
e_InputOverVoltage=ttk.Combobox(root,textvariable = default_value_InputOverVoltage)
e_InputOverVoltage["values"] = ("正常0", "异常1")
e_InputOverVoltage.current(0)      # 选择第一个
e_InputOverVoltage.pack()
e_InputOverVoltage.place(x = 610, y = 760, anchor = NW)
#####################################稳压模块输入欠压  0：正常； 1： 异常##########################################
e_InputUnderVoltage_Label=tkinter.Label(root,text="稳压模块输入欠压")
e_InputUnderVoltage_Label.pack()
e_InputUnderVoltage_Label.place(x = 500, y = 790, anchor = NW)

default_value_InputUnderVoltage = StringVar()
e_InputUnderVoltage=ttk.Combobox(root,textvariable = default_value_InputUnderVoltage)
e_InputUnderVoltage["values"] = ("正常0", "异常1")
e_InputUnderVoltage.current(0)      # 选择第一个
e_InputUnderVoltage.pack()
e_InputUnderVoltage.place(x = 610, y = 790, anchor = NW)
#####################################稳压模块运行状态  0：停机；1：运行##########################################
e_RunningStatus_Label=tkinter.Label(root,text="稳压模块运行状态")
e_RunningStatus_Label.pack()
e_RunningStatus_Label.place(x = 880, y = 160, anchor = NW)

default_value_RunningStatus = StringVar()
e_RunningStatus=ttk.Combobox(root,textvariable = default_value_RunningStatus)
e_RunningStatus["values"] = ("停机0", "运行1")
e_RunningStatus.current(0)      # 选择第一个
e_RunningStatus.pack()
e_RunningStatus.place(x = 985, y = 160, anchor = NW)
#####################################稳压模块上电状态  0：停机；1：上电##########################################
e_ElectricStatus_Label=tkinter.Label(root,text="稳压模块上电状态")
e_ElectricStatus_Label.pack()
e_ElectricStatus_Label.place(x = 880, y = 190, anchor = NW)

default_value_ElectricStatus = StringVar()
e_ElectricStatus=ttk.Combobox(root,textvariable = default_value_ElectricStatus)
e_ElectricStatus["values"] = ("停机0", "上电1")
e_ElectricStatus.current(0)      # 选择第一个
e_ElectricStatus.pack()
e_ElectricStatus.place(x = 985, y = 190, anchor = NW)
#####################################稳压模块输入缺相  0：正常；1：缺相##########################################
e_InputPhase_Label=tkinter.Label(root,text="稳压模块输入缺相")
e_InputPhase_Label.pack()
e_InputPhase_Label.place(x = 880, y = 220, anchor = NW)

default_value_InputPhase = StringVar()
e_InputPhase=ttk.Combobox(root,textvariable = default_value_InputPhase)
e_InputPhase["values"] = ("正常0", "缺相1")
e_InputPhase.current(0)      # 选择第一个
e_InputPhase.pack()
e_InputPhase.place(x = 985, y = 220, anchor = NW)
####################################软件版本号####################################
e_ECUSoftwareVersion_Label=tkinter.Label(root,text="ECU软件版本号")
e_ECUSoftwareVersion_Label.pack()
e_ECUSoftwareVersion_Label.place(x = 880, y = 250, anchor = NW)
default_value_ECUSoftwareVersion = StringVar()
default_value_ECUSoftwareVersion.set('0')
e_ECUSoftwareVersion=tkinter.Entry(root,width=6,textvariable = default_value_ECUSoftwareVersion)
e_ECUSoftwareVersion.pack()
e_ECUSoftwareVersion.place(x = 985, y = 250, anchor = NW)
####################################稳压模块最高允许输出电压####################################
e_MaxOutputVoltage_Label=tkinter.Label(root,text="稳压模块最高允许输出电压")
e_MaxOutputVoltage_Label.pack()
e_MaxOutputVoltage_Label.place(x = 880, y = 280, anchor = NW)
default_value_MaxOutputVoltage = StringVar()
default_value_MaxOutputVoltage.set('0')
e_MaxOutputVoltage=tkinter.Entry(root,width=6,textvariable = default_value_MaxOutputVoltage,state = DISABLED)
e_MaxOutputVoltage.pack()
e_MaxOutputVoltage.place(x = 1030, y = 280, anchor = NW)
####################################稳压模块最高允许输出电流####################################
e_MaxOutputCurrent_Label=tkinter.Label(root,text="稳压模块最高允许输出电流")
e_MaxOutputCurrent_Label.pack()
e_MaxOutputCurrent_Label.place(x = 880, y = 310, anchor = NW)
default_value_MaxOutputCurrent = StringVar()
default_value_MaxOutputCurrent.set('0')
e_MaxOutputCurrent=tkinter.Entry(root,width=6,textvariable = default_value_MaxOutputCurrent,state = DISABLED)
e_MaxOutputCurrent.pack()
e_MaxOutputCurrent.place(x = 1030, y = 310, anchor = NW)
####################################稳压模块工作时间####################################
e_WorkTime_Label=tkinter.Label(root,text="稳压模块工作时间")
e_WorkTime_Label.pack()
e_WorkTime_Label.place(x = 880, y = 340, anchor = NW)
default_value_WorkTime = StringVar()
default_value_WorkTime.set('0')
e_WorkTime=tkinter.Entry(root,width=6,textvariable = default_value_WorkTime,state = DISABLED)
e_WorkTime.pack()
e_WorkTime.place(x = 1030, y = 340, anchor = NW)
####################################稳压模块工作状态####################################
e_WorkState_Label=tkinter.Label(root,text="稳压模块工作状态")
e_WorkState_Label.pack()
e_WorkState_Label.place(x = 880, y = 370, anchor = NW)
default_value_WorkState = StringVar()
default_value_WorkState.set('关机1')
e_WorkState=tkinter.Entry(root,width=6,textvariable = default_value_WorkState,state = DISABLED)
e_WorkState.pack()
e_WorkState.place(x = 1030, y = 370, anchor = NW)
####################################稳压模块UV相输入电压####################################
e_UVVoltage_Label=tkinter.Label(root,text="稳压模块UV相输入电压(0.1V)")
e_UVVoltage_Label.pack()
e_UVVoltage_Label.place(x = 750, y = 10, anchor = NW)
default_value_UVVoltage = StringVar()
default_value_UVVoltage.set('0')
e_UVVoltage=tkinter.Entry(root,width=6,textvariable = default_value_UVVoltage)
e_UVVoltage.pack()
e_UVVoltage.place(x = 920, y = 10, anchor = NW)
####################################稳压模块VW相输入电压####################################
e_VWVoltage_Label=tkinter.Label(root,text="稳压模块VW相输入电压(0.1V)")
e_VWVoltage_Label.pack()
e_VWVoltage_Label.place(x = 750, y = 40, anchor = NW)
default_value_VWVoltage = StringVar()
default_value_VWVoltage.set('0')
e_VWVoltage=tkinter.Entry(root,width=6,textvariable = default_value_VWVoltage)
e_VWVoltage.pack()
e_VWVoltage.place(x = 920, y = 40, anchor = NW)
####################################稳压模块UW相输入电压####################################
e_UWVoltage_Label=tkinter.Label(root,text="稳压模块UW相输入电压(0.1V)")
e_UWVoltage_Label.pack()
e_UWVoltage_Label.place(x = 750, y = 70, anchor = NW)
default_value_UWVoltage = StringVar()
default_value_UWVoltage.set('0')
e_UWVoltage=tkinter.Entry(root,width=6,textvariable = default_value_UWVoltage)
e_UWVoltage.pack()
e_UWVoltage.place(x = 920, y = 70, anchor = NW)
####################################稳压模块输出电压(0.1V)####################################
e_OutputVoltage_Label=tkinter.Label(root,text="稳压模块输出电压(0.1V)")
e_OutputVoltage_Label.pack()
e_OutputVoltage_Label.place(x = 750, y = 100, anchor = NW)
default_value_OutputVoltage = StringVar()
default_value_OutputVoltage.set('0')
e_OutputVoltage=tkinter.Entry(root,width=6,textvariable = default_value_OutputVoltage)
e_OutputVoltage.pack()
e_OutputVoltage.place(x = 920, y = 100, anchor = NW)
####################################稳压模块输出电流(0.1A)####################################
e_OutputCurrent_Label=tkinter.Label(root,text="稳压模块输出电流(0.1A)")
e_OutputCurrent_Label.pack()
e_OutputCurrent_Label.place(x = 750, y = 130, anchor = NW)
default_value_OutputCurrent = StringVar()
default_value_OutputCurrent.set('0')
e_OutputCurrent=tkinter.Entry(root,width=6,textvariable = default_value_OutputCurrent)
e_OutputCurrent.pack()
e_OutputCurrent.place(x = 920, y = 130, anchor = NW)
#####################################启动自动执行##########################################
chVarAutoStart = tkinter.IntVar()
check45 = tkinter.Checkbutton(root, text="启动自动执行", variable=chVarAutoStart)
check45.select()
check45.place(x = 0, y = 640, anchor = NW)
#####################################充电启动失败##########################################
chVarStartFail = tkinter.IntVar()
check46 = tkinter.Checkbutton(root, text="充电启动失败", variable=chVarStartFail)
check46.deselect()
check46.place(x = 100, y = 640, anchor = NW)


def TboxMiddleDeckTem(*args):
    TboxWarning.ID = int('0102faf9', 16)
    TboxWarning.SendType = 0
    TboxWarning.RemoteFlag = 0
    TboxWarning.ExternFlag = 1
    TboxWarning.DataLen = 5
    TboxWarning.Data[0] = 0
    TboxWarning.Data[1] = 0
    TboxWarning.Data[2] = 0
    TboxWarning.Data[3] = 0
    TboxWarning.Data[4] = 0
    TboxWarning.Data[5] = 0
    TboxWarning.Data[6] = 0
    TboxWarning.Data[7] = 0
    if e_MiddleDeckTemWarning.get() == "无告警":
        TboxWarning.Data[3] = 0x30
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x31
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x32
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x33
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x34
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x35
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
    elif e_MiddleDeckTemWarning.get() == "温度过高1级告警":
        TboxWarning.Data[3] = 0x31
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x32
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x33
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x34
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x35
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x30
        TboxWarning.Data[4] = 1
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
    elif e_MiddleDeckTemWarning.get() == "温度过高2级告警":
        TboxWarning.Data[3] = 0x30
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x32
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x33
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x34
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x35
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x31
        TboxWarning.Data[4] = 1
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
    elif e_MiddleDeckTemWarning.get() == "温度过高3级告警":
        TboxWarning.Data[3] = 0x30
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x31
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x33
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x34
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x35
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x32
        TboxWarning.Data[4] = 1
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
    elif e_MiddleDeckTemWarning.get() == "温度过低1级告警":
        TboxWarning.Data[3] = 0x30
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x31
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x32
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x34
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x35
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x33
        TboxWarning.Data[4] = 1
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
    elif e_MiddleDeckTemWarning.get() == "温度过低2级告警":
        TboxWarning.Data[3] = 0x30
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x31
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x32
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x33
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x35
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x34
        TboxWarning.Data[4] = 1
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
    elif e_MiddleDeckTemWarning.get() == "温度过低3级告警":
        TboxWarning.Data[3] = 0x30
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x31
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x32
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x33
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x34
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x35
        TboxWarning.Data[4] = 1
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)

def TboxMiddleDeckHumidity(*args):
    TboxWarning.ID = int('0102faf9', 16)
    TboxWarning.SendType = 0
    TboxWarning.RemoteFlag = 0
    TboxWarning.ExternFlag = 1
    TboxWarning.DataLen = 5
    TboxWarning.Data[0] = 0
    TboxWarning.Data[1] = 0
    TboxWarning.Data[2] = 0
    TboxWarning.Data[3] = 0
    TboxWarning.Data[4] = 0
    TboxWarning.Data[5] = 0
    TboxWarning.Data[6] = 0
    TboxWarning.Data[7] = 0
    if e_MiddleDeckHumidityWarning.get() == "无告警":
        TboxWarning.Data[3] = 0x36
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x37
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
    elif e_MiddleDeckHumidityWarning.get() == "湿度过高1级告警":
        TboxWarning.Data[3] = 0x37
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x36
        TboxWarning.Data[4] = 1
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
    elif e_MiddleDeckHumidityWarning.get() == "湿度过高2级告警":
        TboxWarning.Data[3] = 0x36
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x37
        TboxWarning.Data[4] = 1
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)

def TboxAfterDeckTem(*args):
    TboxWarning.ID = int('0102faf9', 16)
    TboxWarning.SendType = 0
    TboxWarning.RemoteFlag = 0
    TboxWarning.ExternFlag = 1
    TboxWarning.DataLen = 5
    TboxWarning.Data[0] = 0
    TboxWarning.Data[1] = 0
    TboxWarning.Data[2] = 0
    TboxWarning.Data[3] = 0
    TboxWarning.Data[4] = 0
    TboxWarning.Data[5] = 0
    TboxWarning.Data[6] = 0
    TboxWarning.Data[7] = 0
    if e_AfterDeckTemWarning.get() == "无告警":
        TboxWarning.Data[3] = 0x38
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x39
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3a
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3b
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3c
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3d
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
    elif e_AfterDeckTemWarning.get() == "温度过高1级告警":
        TboxWarning.Data[3] = 0x39
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3a
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3b
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3c
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3d
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x38
        TboxWarning.Data[4] = 1
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
    elif e_AfterDeckTemWarning.get() == "温度过高2级告警":
        TboxWarning.Data[3] = 0x38
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3a
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3b
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3c
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3d
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x39
        TboxWarning.Data[4] = 1
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
    elif e_AfterDeckTemWarning.get() == "温度过高3级告警":
        TboxWarning.Data[3] = 0x38
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x39
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3b
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3c
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3d
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3a
        TboxWarning.Data[4] = 1
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
    elif e_AfterDeckTemWarning.get() == "温度过低1级告警":
        TboxWarning.Data[3] = 0x38
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x39
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3a
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3c
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3d
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3b
        TboxWarning.Data[4] = 1
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
    elif e_AfterDeckTemWarning.get() == "温度过低2级告警":
        TboxWarning.Data[3] = 0x38
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x39
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3a
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3b
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3d
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3c
        TboxWarning.Data[4] = 1
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
    elif e_AfterDeckTemWarning.get() == "温度过低3级告警":
        TboxWarning.Data[3] = 0x38
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x39
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3a
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3b
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3c
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3d
        TboxWarning.Data[4] = 1
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)

def TboxAfterDeckHumidity(*args):
    TboxWarning.ID = int('0102faf9', 16)
    TboxWarning.SendType = 0
    TboxWarning.RemoteFlag = 0
    TboxWarning.ExternFlag = 1
    TboxWarning.DataLen = 5
    TboxWarning.Data[0] = 0
    TboxWarning.Data[1] = 0
    TboxWarning.Data[2] = 0
    TboxWarning.Data[3] = 0
    TboxWarning.Data[4] = 0
    TboxWarning.Data[5] = 0
    TboxWarning.Data[6] = 0
    TboxWarning.Data[7] = 0
    if e_AfterDeckHumidityWarning.get() == "无告警":
        TboxWarning.Data[3] = 0x3e
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3f
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
    elif e_AfterDeckHumidityWarning.get() == "湿度过高1级告警":
        TboxWarning.Data[3] = 0x3f
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3e
        TboxWarning.Data[4] = 1
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
    elif e_AfterDeckHumidityWarning.get() == "湿度过高2级告警":
        TboxWarning.Data[3] = 0x3e
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
        TboxWarning.Data[3] = 0x3f
        TboxWarning.Data[4] = 1
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)

def TboxSmoking(*args):
    TboxWarning.ID = int('0102faf9', 16)
    TboxWarning.SendType = 0
    TboxWarning.RemoteFlag = 0
    TboxWarning.ExternFlag = 1
    TboxWarning.DataLen = 5
    TboxWarning.Data[0] = 0
    TboxWarning.Data[1] = 0
    TboxWarning.Data[2] = 0
    TboxWarning.Data[3] = 0
    TboxWarning.Data[4] = 0
    TboxWarning.Data[5] = 0
    TboxWarning.Data[6] = 0
    TboxWarning.Data[7] = 0
    if e_SmokingWarning.get() == "无告警":
        TboxWarning.Data[3] = 0x41
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
    elif e_SmokingWarning.get() == "烟感告警":
        TboxWarning.Data[3] = 0x41
        TboxWarning.Data[4] = 1
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)

def IVECOBattery(*args):
    TboxWarning.ID = int('0102faf9', 16)
    TboxWarning.SendType = 0
    TboxWarning.RemoteFlag = 0
    TboxWarning.ExternFlag = 1
    TboxWarning.DataLen = 5
    TboxWarning.Data[0] = 0
    TboxWarning.Data[1] = 0
    TboxWarning.Data[2] = 0
    TboxWarning.Data[3] = 0
    TboxWarning.Data[4] = 0
    TboxWarning.Data[5] = 0
    TboxWarning.Data[6] = 0
    TboxWarning.Data[7] = 0
    if e_BatteryWarning.get() == "无告警":
        TboxWarning.Data[3] = 0x25
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)
    elif e_BatteryWarning.get() == "蓄电池馈电":
        TboxWarning.Data[3] = 0x25
        TboxWarning.Data[4] = 1
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxWarning, 1)
        my_print(TboxWarning)


#####################################TBOX中舱温度告警##########################################
e_MiddleDeckTemWarning_Label=tkinter.Label(root,text="TBOX中舱温度告警")
e_MiddleDeckTemWarning_Label.pack()
e_MiddleDeckTemWarning_Label.place(x = 1250, y = 450, anchor = NW)

default_value_MiddleDeckTemWarning = StringVar()
e_MiddleDeckTemWarning=ttk.Combobox(root,textvariable = default_value_MiddleDeckTemWarning)
e_MiddleDeckTemWarning["values"] = ("无告警", "温度过高1级告警", "温度过高2级告警", "温度过高3级告警", "温度过低1级告警", \
                                    "温度过低2级告警", "温度过低3级告警")
e_MiddleDeckTemWarning.current(0)      # 选择第一个
e_MiddleDeckTemWarning.bind("<<ComboboxSelected>>", TboxMiddleDeckTem)
e_MiddleDeckTemWarning.pack()
e_MiddleDeckTemWarning.place(x = 1370, y = 450, anchor = NW)
#####################################TBOX中舱湿度告警##########################################
e_MiddleDeckHumidityWarning_Label=tkinter.Label(root,text="TBOX中舱湿度告警")
e_MiddleDeckHumidityWarning_Label.pack()
e_MiddleDeckHumidityWarning_Label.place(x = 1250, y = 480, anchor = NW)

default_value_MiddleDeckHumidityWarning = StringVar()
e_MiddleDeckHumidityWarning=ttk.Combobox(root,textvariable = default_value_MiddleDeckHumidityWarning)
e_MiddleDeckHumidityWarning["values"] = ("无告警", "湿度过高1级告警", "湿度过高2级告警")
e_MiddleDeckHumidityWarning.current(0)      # 选择第一个
e_MiddleDeckHumidityWarning.bind("<<ComboboxSelected>>", TboxMiddleDeckHumidity)
e_MiddleDeckHumidityWarning.pack()
e_MiddleDeckHumidityWarning.place(x = 1370, y = 480, anchor = NW)
#####################################TBOX后舱温度告警##########################################
e_AfterDeckTemWarning_Label=tkinter.Label(root,text="TBOX后舱温度告警")
e_AfterDeckTemWarning_Label.pack()
e_AfterDeckTemWarning_Label.place(x = 1250, y = 510, anchor = NW)

default_value_AfterDeckTemWarning = StringVar()
e_AfterDeckTemWarning=ttk.Combobox(root,textvariable = default_value_AfterDeckTemWarning)
e_AfterDeckTemWarning["values"] = ("无告警", "温度过高1级告警", "温度过高2级告警", "温度过高3级告警", "温度过低1级告警", \
                                    "温度过低2级告警", "温度过低3级告警")
e_AfterDeckTemWarning.current(0)      # 选择第一个
e_AfterDeckTemWarning.bind("<<ComboboxSelected>>", TboxAfterDeckTem)
e_AfterDeckTemWarning.pack()
e_AfterDeckTemWarning.place(x = 1370, y = 510, anchor = NW)
#####################################TBOX后舱湿度告警##########################################
e_AfterDeckHumidityWarning_Label=tkinter.Label(root,text="TBOX后舱湿度告警")
e_AfterDeckHumidityWarning_Label.pack()
e_AfterDeckHumidityWarning_Label.place(x = 1250, y = 540, anchor = NW)

default_value_AfterDeckHumidityWarning = StringVar()
e_AfterDeckHumidityWarning=ttk.Combobox(root,textvariable = default_value_AfterDeckHumidityWarning)
e_AfterDeckHumidityWarning["values"] = ("无告警", "湿度过高1级告警", "湿度过高2级告警")
e_AfterDeckHumidityWarning.current(0)      # 选择第一个
e_AfterDeckHumidityWarning.bind("<<ComboboxSelected>>", TboxAfterDeckHumidity)
e_AfterDeckHumidityWarning.pack()
e_AfterDeckHumidityWarning.place(x = 1370, y = 540, anchor = NW)
#####################################TBOX烟感告警##########################################
e_SmokingWarning_Label=tkinter.Label(root,text="TBOX烟感告警")
e_SmokingWarning_Label.pack()
e_SmokingWarning_Label.place(x = 1250, y = 570, anchor = NW)

default_value_SmokingWarning = StringVar()
e_SmokingWarning=ttk.Combobox(root,textvariable = default_value_SmokingWarning)
e_SmokingWarning["values"] = ("无告警", "烟感告警")
e_SmokingWarning.current(0)      # 选择第一个
e_SmokingWarning.bind("<<ComboboxSelected>>", TboxSmoking)
e_SmokingWarning.pack()
e_SmokingWarning.place(x = 1370, y = 570, anchor = NW)
#####################################IVECO蓄电池馈电##########################################
e_BatteryWarning_Label=tkinter.Label(root,text="IVECO蓄电池馈电")
e_BatteryWarning_Label.pack()
e_BatteryWarning_Label.place(x = 1250, y = 600, anchor = NW)

default_value_BatteryWarning = StringVar()
e_BatteryWarning=ttk.Combobox(root,textvariable = default_value_BatteryWarning)
e_BatteryWarning["values"] = ("无告警", "蓄电池馈电")
e_BatteryWarning.current(0)      # 选择第一个
e_BatteryWarning.bind("<<ComboboxSelected>>", IVECOBattery)
e_BatteryWarning.pack()
e_BatteryWarning.place(x = 1370, y = 600, anchor = NW)
####################################海拔信息####################################
e_Altitude_Label=tkinter.Label(root,text="海拔信息")
e_Altitude_Label.pack()
e_Altitude_Label.place(x = 1250, y = 630, anchor = NW)
default_value_Altitude = StringVar()
default_value_Altitude.set('0')
e_Altitude=tkinter.Entry(root,width=6,textvariable = default_value_Altitude)
e_Altitude.pack()
e_Altitude.place(x = 1370, y = 630, anchor = NW)


def fun_timer1():
    global INKM_value
    global Time_Num
    global Time_Num1
    global Altitude_Num
    global IntrinsicParameter_Num
    global module_Num
    global StartFailFlag
    IntrinsicParameter_Num += 1
    Altitude_Num += 1
    module_Num += 1

    if StartFailFlag == 3 and module_Num == 1:
        if chVarAutoStart.get() == 1:
            e_ChargerState.current(0)
        StartFailFlag = 0

    if StartFailFlag == 1 and module_Num == 2:
        default_value_StartupFailCode.set('0')
        StartFailFlag = 2
        
    if StartFailFlag == 2 and module_Num == 1 and int(e_StartupFailCode.get(), 10) != 0:
        if chVarAutoStart.get() == 1:
            e_ChargerState.current(2)
            e_StartStatus.current(2)
            e_StopStatus.current(1)
        text.insert(END, '启动充电失败')
        text.insert(END, '\n')
        text.see(END)
        StartFailFlag = 3

    if module_Num == 2:
        module_Num = 0
        module_data.ID = int('1807f08a', 16)
        module_data.SendType = 0
        module_data.RemoteFlag = 0
        module_data.ExternFlag = 1
        module_data.DataLen = 8
        # print(moduledata_list)
        for num in range(14):
            module_data.Data[0] = num + 1
            module_data.Data[1] = moduledata_list[num][0]
            module_data.Data[2] = moduledata_list[num][1]
            module_data.Data[3] = moduledata_list[num][2]
            module_data.Data[4] = moduledata_list[num][3]
            module_data.Data[5] = moduledata_list[num][4]
            module_data.Data[6] = moduledata_list[num][5]
            module_data.Data[7] = moduledata_list[num][6]
            dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN1, module_data, 1)
            my_print(module_data)

    if IntrinsicParameter_Num == 40:
        IntrinsicParameter_Num = 0
        Data12.ID = int('1806f08a', 16)
        Data12.SendType = 0
        Data12.RemoteFlag = 0
        Data12.ExternFlag = 1
        Data12.DataLen = 8
        Data12.Data[0] = 4
        try:
            Data12.Data[1] = int(float(e_MaxOutputPowerSet.get()) * 10) % 256
            Data12.Data[2] = int(float(e_MaxOutputPowerSet.get()) * 10) // 256
        except ValueError as e:
            my_print_Warning(e)
        try:
            Data12.Data[3] = int(e_CurrentRiseTimeSet.get())
        except ValueError as e:
            my_print_Warning(e)
        try:
            Data12.Data[4] = int(float(e_MaxVoltageLimitSet.get()) * 10) % 256
            Data12.Data[5] = int(float(e_MaxVoltageLimitSet.get()) * 10) // 256
        except ValueError as e:
            my_print_Warning(e)
        try:
            Data12.Data[6] = (int((float(e_MaxCurrentLimitSet.get()) + 400) * 10)) % 256
            Data12.Data[7] = (int((float(e_MaxCurrentLimitSet.get()) + 400) * 10)) // 256
        except ValueError as e:
            my_print_Warning(e)
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN1, Data12, 1)
        my_print(Data12)

        Data13.ID = int('1806f08a', 16)
        Data13.SendType = 0
        Data13.RemoteFlag = 0
        Data13.ExternFlag = 1
        Data13.DataLen = 8
        Data13.Data[0] = 5
        try:
            Data13.Data[1] = int(float(e_InputOverVoltageThresholdSet.get()) * 10) % 256
            Data13.Data[2] = int(float(e_InputOverVoltageThresholdSet.get()) * 10) // 256
        except ValueError as e:
            my_print_Warning(e)
        try:
            Data13.Data[3] = int(e_ChargingGunTem.get()) + 40
        except ValueError as e:
            my_print_Warning(e)
        try:
            Data13.Data[4] = int(float(e_CumulativePower.get()) * 100) % 256
            tempdata = int(float(e_CumulativePower.get()) * 100) // 256
            Data13.Data[5] = tempdata % 256
            tempdata = tempdata // 256
            Data13.Data[6] = tempdata % 256
            Data13.Data[7] = tempdata // 256
        except ValueError as e:
            my_print_Warning(e)
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN1, Data13, 1)
        my_print(Data13)

        VIN_1.ID = int('1806f08a', 16)
        VIN_1.SendType = 0
        VIN_1.RemoteFlag = 0
        VIN_1.ExternFlag = 1
        VIN_1.DataLen = 8
        VIN_1.Data[0] = 1
        try:
            VIN_1.Data[1] = ord(e_VIN.get()[0])
            VIN_1.Data[2] = ord(e_VIN.get()[1])
            VIN_1.Data[3] = ord(e_VIN.get()[2])
            VIN_1.Data[4] = ord(e_VIN.get()[3])
            VIN_1.Data[5] = ord(e_VIN.get()[4])
            VIN_1.Data[6] = ord(e_VIN.get()[5])
            VIN_1.Data[7] = ord(e_VIN.get()[6])
        except ValueError as e:
            my_print_Warning(e)
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN1, VIN_1, 1)
        my_print(VIN_1)

        VIN_2.ID = int('1806f08a', 16)
        VIN_2.SendType = 0
        VIN_2.RemoteFlag = 0
        VIN_2.ExternFlag = 1
        VIN_2.DataLen = 8
        VIN_2.Data[0] = 2
        try:
            VIN_2.Data[1] = ord(e_VIN.get()[7])
            VIN_2.Data[2] = ord(e_VIN.get()[8])
            VIN_2.Data[3] = ord(e_VIN.get()[9])
            VIN_2.Data[4] = ord(e_VIN.get()[10])
            VIN_2.Data[5] = ord(e_VIN.get()[11])
            VIN_2.Data[6] = ord(e_VIN.get()[12])
            VIN_2.Data[7] = ord(e_VIN.get()[13])
        except ValueError as e:
            my_print_Warning(e)
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN1, VIN_2, 1)
        my_print(VIN_2)

        VIN_3.ID = int('1806f08a', 16)
        VIN_3.SendType = 0
        VIN_3.RemoteFlag = 0
        VIN_3.ExternFlag = 1
        VIN_3.DataLen = 8
        VIN_3.Data[0] = 3
        try:
            VIN_3.Data[1] = ord(e_VIN.get()[14])
            VIN_3.Data[2] = ord(e_VIN.get()[15])
            VIN_3.Data[3] = ord(e_VIN.get()[16])
            VIN_3.Data[4] = (ord(e_VIN.get()[0]) + ord(e_VIN.get()[1]) + ord(e_VIN.get()[2]) + ord(e_VIN.get()[3]) + \
                            ord(e_VIN.get()[4]) + ord(e_VIN.get()[5]) + ord(e_VIN.get()[6]) + ord(e_VIN.get()[7]) + \
                            ord(e_VIN.get()[8]) + ord(e_VIN.get()[9]) + ord(e_VIN.get()[10]) + ord(e_VIN.get()[11]) + \
                            ord(e_VIN.get()[12]) + ord(e_VIN.get()[13]) + ord(e_VIN.get()[14]) + ord(e_VIN.get()[15]) + \
                            ord(e_VIN.get()[16])) % 256
            VIN_3.Data[5] = (ord(e_VIN.get()[0]) + ord(e_VIN.get()[1]) + ord(e_VIN.get()[2]) + ord(e_VIN.get()[3]) + \
                            ord(e_VIN.get()[4]) + ord(e_VIN.get()[5]) + ord(e_VIN.get()[6]) + ord(e_VIN.get()[7]) + \
                            ord(e_VIN.get()[8]) + ord(e_VIN.get()[9]) + ord(e_VIN.get()[10]) + ord(e_VIN.get()[11]) + \
                            ord(e_VIN.get()[12]) + ord(e_VIN.get()[13]) + ord(e_VIN.get()[14]) + ord(e_VIN.get()[15]) + \
                            ord(e_VIN.get()[16])) // 256
            VIN_3.Data[6] = 0
            VIN_3.Data[7] = 0
        except ValueError as e:
            my_print_Warning(e)
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN1, VIN_3, 1)
        my_print(VIN_3)

    if Altitude_Num == 1800:
        Altitude_Num = 0
        TboxAltitude.ID = int('0105faf9', 16)
        TboxAltitude.SendType = 0
        TboxAltitude.RemoteFlag = 0
        TboxAltitude.ExternFlag = 1
        TboxAltitude.DataLen = 2
        try:
            TboxAltitude.Data[0] = int(e_Altitude.get()) // 256
            TboxAltitude.Data[1] = int(e_Altitude.get()) % 256
        except ValueError as e:
            my_print_Warning(e)
        TboxAltitude.Data[2] = 0
        TboxAltitude.Data[3] = 0
        TboxAltitude.Data[4] = 0
        TboxAltitude.Data[5] = 0
        TboxAltitude.Data[6] = 0
        TboxAltitude.Data[7] = 0
        dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxAltitude, 1)
        my_print(TboxAltitude)
    if Time_Num1 == 4:
        e_ChargerState.current(0)
        Time_Num = 0
        Time_Num1 = 0
    if Time_Num == 1:
        Time_Num1 += 1
    Data1.ID = int('1803f08a',16)
    Data1.SendType = 0
    Data1.RemoteFlag = 0
    Data1.ExternFlag = 1
    Data1.DataLen = 8
    Data1.Data[0] = 1
    Data1.Data[1] = int(e_ChargingGun.get()[len(e_ChargingGun.get())-1],16) * 2 + \
                    int(e_VehicleCom.get()[len(e_VehicleCom.get())-1],16)
    Data1.Data[2] = int(e_Lock.get()[len(e_Lock.get())-1],16)
    Data1.Data[3] = int(e_OutKM.get()[len(e_OutKM.get())-1],16)
    try:
        Data1.Data[4] = int(float(e_OutVoltage.get()) * 10) % 256
        Data1.Data[5] = int(float(e_OutVoltage.get()) * 10) // 256
    except ValueError as e:
        my_print_Warning(e)
    try:
        Data1.Data[6] = (int((float(e_OutCurrent.get()) + 400) * 10)) % 256
        Data1.Data[7] = (int((float(e_OutCurrent.get()) + 400) * 10)) // 256
    except ValueError as e:
        my_print_Warning(e)

    Data2.ID = int('1803f08a', 16)
    Data2.SendType = 0
    Data2.RemoteFlag = 0
    Data2.ExternFlag = 1
    Data2.DataLen = 8
    Data2.Data[0] = 2
    try:
        Data2.Data[1] = int(float(e_BMSVoltage.get()) * 10) % 256
        Data2.Data[2] = int(float(e_BMSVoltage.get()) * 10) // 256
    except ValueError as e:
        my_print_Warning(e)
    try:
        Data2.Data[3] = (int((float(e_BMSCurrent.get()) + 400) * 10)) % 256
        Data2.Data[4] = (int((float(e_BMSCurrent.get()) + 400) * 10)) // 256
    except ValueError as e:
        my_print_Warning(e)
    try:
        Data2.Data[5] = int(e_SOC.get(),10)
    except ValueError as e:
        my_print_Warning(e)
    try:
        Data2.Data[6] = int(float(e_SingleCellMaxVoltage.get()) * 100) % 256
        Data2.Data[7] = int(float(e_SingleCellMaxVoltage.get()) * 100) // 256
    except ValueError as e:
        my_print_Warning(e)

    Data3.ID = int('1803f08a', 16)
    Data3.SendType = 0
    Data3.RemoteFlag = 0
    Data3.ExternFlag = 1
    Data3.DataLen = 8
    Data3.Data[0] = 3
    try:
        Data3.Data[1] = int(e_SingleCellMaxVoltageNum.get(),10)
    except ValueError as e:
        my_print_Warning(e)
    Data3.Data[2] = 0
    try:
        Data3.Data[3] = int(float(e_ChargedPower.get()) * 10) % 256
        Data3.Data[4] = int(float(e_ChargedPower.get()) * 10) // 256
    except ValueError as e:
        my_print_Warning(e)
    try:
        Data3.Data[5] = int(e_BatteryTemMax.get(),10) + 50
        Data3.Data[6] = int(e_BatteryTemMin.get(),10) + 50
    except ValueError as e:
        my_print_Warning(e)
    Data3.Data[7] = int(e_ChargerState.get()[len(e_ChargerState.get()) - 1], 16)

    Data4.ID = int('1803f08a', 16)
    Data4.SendType = 0
    Data4.RemoteFlag = 0
    Data4.ExternFlag = 1
    Data4.DataLen = 8
    Data4.Data[0] = 4
    try:
        Data4.Data[1] = int(e_RemainChargingTime.get(),10) % 256
        Data4.Data[2] = int(e_RemainChargingTime.get(),10) // 256
    except ValueError as e:
        my_print_Warning(e)
    Data4.Data[3] = 0
    Data4.Data[4] = 0
    try:
        Data4.Data[5] = int(e_MainChargerVersionL.get(),16)
    except ValueError as e:
        my_print_Warning(e)
    try:
        Data4.Data[6] = int(e_MainChargerVersionH.get(),16)
    except ValueError as e:
        my_print_Warning(e)
    Data4.Data[7] = INKM_value

    Data5.ID = int('1803f08a', 16)
    Data5.SendType = 0
    Data5.RemoteFlag = 0
    Data5.ExternFlag = 1
    Data5.DataLen = 8
    Data5.Data[0] = 5
    Data5.Data[1] = int(e_StartStatus.get()[len(e_StartStatus.get()) - 1], 16)
    Data5.Data[2] = int(e_StopStatus.get()[len(e_StopStatus.get()) - 1], 16)
    try:
        Data5.Data[3] = int(e_StartupFailCode.get(),10)
    except ValueError as e:
        my_print_Warning(e)
    try:
        Data5.Data[4] = int(e_AssistChargerVersionL.get(),16)
    except ValueError as e:
        my_print_Warning(e)
    try:
        Data5.Data[5] = int(e_AssistChargerVersionH.get(),16)
    except ValueError as e:
        my_print_Warning(e)
    Data5.Data[6] = 0
    Data5.Data[7] = 0

    Data6.ID = int('1005f08a', 16)
    Data6.SendType = 0
    Data6.RemoteFlag = 0
    Data6.ExternFlag = 1
    Data6.DataLen = 8
    Data6.Data[0] = 1
    Data6.Data[1] = chVarESTOP.get() * 16 + chVarChargerCom.get() * 2 + chVarElecCom.get() + chVarInputUnderVoltageWarning.get() \
                    * 4 + chVarInputUnderVoltageFailure.get() * 8 + chVarInputOverVoltageWarning.get() * 32 + \
                    chVarInputOverVoltageFailure.get() * 64 + chVarInsulationResistorLowWarning.get() * 128
    Data6.Data[2] = chVarChargerLock.get() * 2 + chVarChargerFan.get() * 4 + chVarLightningArrester.get() * 8 + \
                    chVarInsulationDetect.get() * 16 + chVarReversePolarity.get() * 32
    Data6.Data[3] = chVarChargingModule1.get() + chVarChargingModule2.get() * 2 + chVarChargingModule3.get() * 4 + \
                    chVarChargingModule4.get() * 8 + chVarChargingModule5.get() * 16 + chVarChargingModule6.get() * 32 + \
                    chVarChargingModule7.get() * 64
    Data6.Data[4] = chVarChargingModuleSum.get() + chVarDCOutShort.get() * 32
    Data6.Data[5] = 0
    Data6.Data[6] = chVarBusVoltageAbnormal.get() + chVarBatteryTermination.get() * 2 + chVarSigleCellVoltageOver.get() * 4 \
                    + chVarEntranceGuardFault.get() * 8 + chVarDCOutKMAdhesion.get() * 16 + chVarINKMAdhesion.get() * 32 \
                    + chVarGunTemHigh.get() * 64 + chVarGunTemHighWarning.get() * 128
    Data6.Data[7] = 0

    Data7.ID = int('1005f08a', 16)
    Data7.SendType = 0
    Data7.RemoteFlag = 0
    Data7.ExternFlag = 1
    Data7.DataLen = 8
    Data7.Data[0] = 2
    Data7.Data[1] = chVarReachSOC.get() + chVarReachVoltage.get() * 4 + chVarReachSingleCellVoltage.get() * 16 + \
                    chVarChargerActiveStop.get() * 64
    Data7.Data[2] = chVarInsulationFail.get() + chVarOutConnectorOverTem.get() * 4 + chVarBMSOutConnectorOverTem.get() * 16 + \
                    chVarChargerConnector.get() * 64
    Data7.Data[3] = chVarBatteryTemHigh.get() + chVarHighVoltageRelay.get() * 4 + chVarPoint2Voltage.get() * 16 + \
                    chVarOtherFault.get() * 64
    Data7.Data[4] = chVarCurrentOver.get() + chVarVoltageAbnormal.get() * 4
    Data7.Data[5] = 0
    Data7.Data[6] = 0
    Data7.Data[7] = 0

    Data8.ID = int('11010002', 16)
    Data8.SendType = 0
    Data8.RemoteFlag = 0
    Data8.ExternFlag = 1
    Data8.DataLen = 8
    try:
        Data8.Data[0] = int(e_ECURpm.get(),10) // 256
        Data8.Data[1] = int(e_ECURpm.get(),10) % 256
    except ValueError as e:
        my_print_Warning(e)
    Data8.Data[2] = int(e_HandBrakeState.get()[len(e_HandBrakeState.get())-1],16) + \
                    int(e_PTOState.get()[len(e_PTOState.get())-1],16) * 2 + int(e_ClutchState.get()[len(e_ClutchState.get())-1],16) * 4
    Data8.Data[3] = int(e_OutOverVoltage.get()[len(e_OutOverVoltage.get())-1],16) + \
                    int(e_OutOverCurrent.get()[len(e_OutOverCurrent.get())-1],16) * 2 + \
                    int(e_SystemOverHeat.get()[len(e_SystemOverHeat.get())-1],16) * 4 + \
                    int(e_OutputReverse.get()[len(e_OutputReverse.get())-1],16) * 8 + \
                    int(e_OutputOverLoad.get()[len(e_OutputOverLoad.get())-1],16) * 16 + \
                    int(e_OutputUnderVoltage.get()[len(e_OutputUnderVoltage.get())-1],16) * 32 + \
                    int(e_InputOverVoltage.get()[len(e_InputOverVoltage.get())-1],16) * 64 + \
                    int(e_InputUnderVoltage.get()[len(e_InputUnderVoltage.get())-1],16) * 128
    Data8.Data[4] = int(e_ElectricStatus.get()[len(e_ElectricStatus.get())-1],16) + \
                    int(e_RunningStatus.get()[len(e_RunningStatus.get())-1],16) * 2 + \
                    int(e_InputPhase.get()[len(e_InputPhase.get())-1],16) * 4
    try:
        Data8.Data[5] = int(e_ECUSoftwareVersion.get(),10) // 256
        Data8.Data[6] = int(e_ECUSoftwareVersion.get(),10) % 256
    except ValueError as e:
        my_print_Warning(e)
    Data8.Data[7] = 0

    Data9.ID = int('11110002', 16)
    Data9.SendType = 0
    Data9.RemoteFlag = 0
    Data9.ExternFlag = 1
    Data9.DataLen = 8
    try:
        Data9.Data[0] = int(float(e_UVVoltage.get()) * 10) // 256
        Data9.Data[1] = int(float(e_UVVoltage.get()) * 10) % 256
    except ValueError as e:
        my_print_Warning(e)
    try:
        Data9.Data[2] = int(float(e_VWVoltage.get()) * 10) // 256
        Data9.Data[3] = int(float(e_VWVoltage.get()) * 10) % 256
    except ValueError as e:
        my_print_Warning(e)
    try:
        Data9.Data[4] = int(float(e_UWVoltage.get()) * 10) // 256
        Data9.Data[5] = int(float(e_UWVoltage.get()) * 10) % 256
    except ValueError as e:
        my_print_Warning(e)
    try:
        Data9.Data[6] = int(float(e_OutputVoltage.get()) * 10) // 256
        Data9.Data[7] = int(float(e_OutputVoltage.get()) * 10) % 256
    except ValueError as e:
        my_print_Warning(e)

    Data10.ID = int('11210002', 16)
    Data10.SendType = 0
    Data10.RemoteFlag = 0
    Data10.ExternFlag = 1
    Data10.DataLen = 8
    try:
        Data10.Data[0] = int(float(e_OutputCurrent.get()) * 10) // 256
        Data10.Data[1] = int(float(e_OutputCurrent.get()) * 10) % 256
    except ValueError as e:
        my_print_Warning(e)
    Data10.Data[2] = 0
    Data10.Data[3] = 0
    Data10.Data[4] = 0
    Data10.Data[5] = 0
    Data10.Data[6] = 0
    Data10.Data[7] = 0

    dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN1, Data1, 1)
    my_print(Data1)
    dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN1, Data2, 1)
    my_print(Data2)
    dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN1, Data3, 1)
    my_print(Data3)
    dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN1, Data4, 1)
    my_print(Data4)
    dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN1, Data5, 1)
    my_print(Data5)
    dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN1, Data6, 1)
    my_print(Data6)
    dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN1, Data7, 1)
    my_print(Data7)
    dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, Data8, 1)
    my_print(Data8)
    dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, Data9, 1)
    my_print(Data9)
    dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, Data10, 1)
    my_print(Data10)
    dwRel_CAN1 = dll.VCI_GetReceiveNum(DevType, DevIndex, CANIndex_CAN1)
    dwRel_CAN2 = dll.VCI_GetReceiveNum(DevType, DevIndex, CANIndex_CAN2)
    if dwRel_CAN1 >= 1:
        dll.VCI_Receive(DevType, DevIndex, CANIndex_CAN1, pointer(CAN1_Receive), 1, 50)
        my_print_Receive(CAN1_Receive)
        if CAN1_Receive.ID == 0x08018af0 and CAN1_Receive.Data[0] == 0x01 and CAN1_Receive.Data[1] == 0x01 and chVarStartFail.get() == 0:
            Data11.ID = int('0x0801f08a', 16)
            Data11.SendType = 0
            Data11.RemoteFlag = 0
            Data11.ExternFlag = 1
            Data11.DataLen = 8
            Data11.Data[0] = 1
            Data11.Data[1] = 1
            Data11.Data[2] = 0
            Data11.Data[3] = 0
            Data11.Data[4] = 0
            Data11.Data[5] = 0
            Data11.Data[6] = 0
            Data11.Data[7] = 0
            dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN1, Data11, 1)
            my_print(Data11)
            if chVarAutoStart.get() == 1:
                e_ChargerState.current(1)
                e_StartStatus.current(1)
                e_StopStatus.current(0)
            text.insert(END, '启动充电成功')
            text.insert(END, '\n')
            text.see(END)
        elif CAN1_Receive.ID == 0x08018af0 and CAN1_Receive.Data[0] == 0x01 and CAN1_Receive.Data[1] == 0x01 and chVarStartFail.get() == 1:
            Data11.ID = int('0x0801f08a', 16)
            Data11.SendType = 0
            Data11.RemoteFlag = 0
            Data11.ExternFlag = 1
            Data11.DataLen = 8
            Data11.Data[0] = 1
            Data11.Data[1] = 1
            Data11.Data[2] = 0
            Data11.Data[3] = 0
            Data11.Data[4] = 0
            Data11.Data[5] = 0
            Data11.Data[6] = 0
            Data11.Data[7] = 0
            dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN1, Data11, 1)
            my_print(Data11)
            StartFailFlag = 1
            if chVarAutoStart.get() == 1:
                e_ChargerState.current(0)
                e_StartStatus.current(0)
                e_StopStatus.current(0)

        elif CAN1_Receive.ID == 0x08018af0 and CAN1_Receive.Data[0] == 0x01 and CAN1_Receive.Data[1] == 0x02:
            Data11.ID = int('0x0801f08a', 16)
            Data11.SendType = 0
            Data11.RemoteFlag = 0
            Data11.ExternFlag = 1
            Data11.DataLen = 8
            Data11.Data[0] = 1
            Data11.Data[1] = 2
            Data11.Data[2] = 0
            Data11.Data[3] = 0
            Data11.Data[4] = 0
            Data11.Data[5] = 0
            Data11.Data[6] = 0
            Data11.Data[7] = 0
            dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN1, Data11, 1)
            my_print(Data11)
            if chVarAutoStart.get() == 1:
                e_ChargerState.current(2)
                e_StartStatus.current(0)
                e_StopStatus.current(1)
                Time_Num = 1
            text.insert(END, '停止充电成功')
            text.insert(END, '\n')
            text.see(END)
        elif CAN1_Receive.ID == 0x08018af0 and CAN1_Receive.Data[0] == 0x02 and CAN1_Receive.Data[1] == 0x01:
            Data11.ID = int('0x0801f08a', 16)
            Data11.SendType = 0
            Data11.RemoteFlag = 0
            Data11.ExternFlag = 1
            Data11.DataLen = 8
            Data11.Data[0] = 2
            Data11.Data[1] = 1
            Data11.Data[2] = 0
            Data11.Data[3] = 0
            Data11.Data[4] = 0
            Data11.Data[5] = 0
            Data11.Data[6] = 0
            Data11.Data[7] = 0
            dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN1, Data11, 1)
            my_print(Data11)
            INKM_value = 1
            text.insert(END, '闭合KM3成功')
            text.insert(END, '\n')
            text.see(END)
        elif CAN1_Receive.ID == 0x08018af0 and CAN1_Receive.Data[0] == 0x02 and CAN1_Receive.Data[1] == 0x02:
            Data11.ID = int('0x0801f08a', 16)
            Data11.SendType = 0
            Data11.RemoteFlag = 0
            Data11.ExternFlag = 1
            Data11.DataLen = 8
            Data11.Data[0] = 2
            Data11.Data[1] = 2
            Data11.Data[2] = 0
            Data11.Data[3] = 0
            Data11.Data[4] = 0
            Data11.Data[5] = 0
            Data11.Data[6] = 0
            Data11.Data[7] = 0
            dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN1, Data11, 1)
            my_print(Data11)
            INKM_value = 0
            text.insert(END, '断开KM3成功')
            text.insert(END, '\n')
            text.see(END)
        elif CAN1_Receive.ID == 0x10028af0 and CAN1_Receive.Data[0] == 0x01:
            MaxOutputPower = (CAN1_Receive.Data[2] * 256 + CAN1_Receive.Data[1])/10
            default_value_MaxOutputPower.set(str(MaxOutputPower))
            CurrentRiseTime = CAN1_Receive.Data[3]
            default_value_CurrentRiseTime.set(str(CurrentRiseTime))
            MaxVoltageLimit = (CAN1_Receive.Data[5] * 256 + CAN1_Receive.Data[4]) / 10
            default_value_MaxVoltageLimit.set(str(MaxVoltageLimit))
            MaxCurrentLimit = (CAN1_Receive.Data[7] * 256 + CAN1_Receive.Data[6]) / 10
            default_value_MaxCurrentLimit.set(str(MaxCurrentLimit))
        elif CAN1_Receive.ID == 0x10028af0 and CAN1_Receive.Data[0] == 0x02:
            InputOverVoltageThreshold = (CAN1_Receive.Data[2] * 256 + CAN1_Receive.Data[1])/10
            default_value_InputOverVoltageThreshold.set(str(InputOverVoltageThreshold))
    if dwRel_CAN2 >= 1:
        dll.VCI_Receive(DevType, DevIndex, CANIndex_CAN2, pointer(CAN2_Receive), 1, 50)
        my_print_Receive(CAN2_Receive)
        if CAN2_Receive.ID == 0x13020001:
            if CAN2_Receive.Data[6] == 0x01:
                default_value_OutputVoltage.set('0')
                default_value_OutputCurrent.set('0')
                default_value_WorkState.set('关机1')
                text.insert(END, '发电机停止成功')
                text.insert(END, '\n')
                text.see(END)
            elif CAN2_Receive.Data[6] == 0x00:
                default_value_WorkState.set('开机0')
            MaxOutputV = (CAN2_Receive.Data[0] * 256 + CAN2_Receive.Data[1])/10
            default_value_MaxOutputVoltage.set(str(MaxOutputV))
            MaxOutputC = (CAN2_Receive.Data[2] * 256 + CAN2_Receive.Data[3])/10
            default_value_MaxOutputCurrent.set(str(MaxOutputC))
            WorkTime = CAN2_Receive.Data[4] * 256 + CAN2_Receive.Data[5]
            default_value_WorkTime.set(str(WorkTime))
        if CAN2_Receive.ID == 0x0101f9fa:
            TboxHeartBeat.ID = int('0x0101faf9', 16)
            TboxHeartBeat.SendType = 0
            TboxHeartBeat.RemoteFlag = 0
            TboxHeartBeat.ExternFlag = 1
            TboxHeartBeat.DataLen = 0
            dll.VCI_Transmit(DevType, DevIndex, CANIndex_CAN2, TboxHeartBeat, 1)
            my_print(TboxHeartBeat)
    global timer1       #定义变量
    timer1 = threading.Timer(0.5,fun_timer1)   #0.5秒调用一次函数
    timer1.start()    #启用定时器

def Transmit_data():
    timer1 = threading.Timer(1, fun_timer1)  # 首次启动
    timer1.start()

def Transmit_stop():
    timer1.cancel()

b1=tkinter.Button(root,text='发送',width=7,height=1,command=Transmit_data)
b1.pack()
b1.place(x = 100, y = 30, anchor = NW)

b2=tkinter.Button(root,text='停止',width=7,height=1,command=Transmit_stop)
b2.pack()
b2.place(x = 200, y = 30, anchor = NW)

b3=tkinter.Button(root,text='模块数据',width=7,height=1,command=moduledata_UI)
b3.pack()
b3.place(x = 780, y = 610, anchor = NW)

root.mainloop()
