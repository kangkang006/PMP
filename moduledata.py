#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import threading
from ctypes import *
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import tkinter

moduledata_list = [[0 for col in range(7)] for row in range(14)]

def moduledata_UI():
    subroot = tkinter.Toplevel()
    subroot.title('模块数据配置界面')
    # subroot.state("zoomed")
    subroot.geometry("1400x800")

    e_moduledata1_Label = tkinter.Label(subroot, text="模块1数据", font = ("Arial, 12"))
    e_moduledata1_Label.pack()
    e_moduledata1_Label.place(x=0, y=10, anchor=NW)
    ###########################Add1输出电压########################################
    e_Add1_OutVoltage_Label = tkinter.Label(subroot, text="模块1输出电压(0.1V)")
    e_Add1_OutVoltage_Label.pack()
    e_Add1_OutVoltage_Label.place(x=0, y=30, anchor=NW)
    default_value_Add1_OutVoltage = StringVar()
    default_value_Add1_OutVoltage.set('0')
    e_Add1_OutVoltage = tkinter.Entry(subroot, width=6, textvariable=default_value_Add1_OutVoltage)
    e_Add1_OutVoltage.pack()
    e_Add1_OutVoltage.place(x=120, y=30, anchor=NW)
    ###########################Add1输出电流########################################
    e_Add1_OutCurrent_Label = tkinter.Label(subroot, text="模块1输出电流(0.1A)")
    e_Add1_OutCurrent_Label.pack()
    e_Add1_OutCurrent_Label.place(x=0, y=50, anchor=NW)
    default_value_Add1_OutCurrent = StringVar()
    default_value_Add1_OutCurrent.set('0')
    e_Add1_OutCurrent = tkinter.Entry(subroot, width=6, textvariable=default_value_Add1_OutCurrent)
    e_Add1_OutCurrent.pack()
    e_Add1_OutCurrent.place(x=120, y=50, anchor=NW)
    ###########################Add1温度########################################
    e_Add1_Temperature_Label = tkinter.Label(subroot, text="模块1温度(0.1℃)")
    e_Add1_Temperature_Label.pack()
    e_Add1_Temperature_Label.place(x=0, y=70, anchor=NW)
    default_value_Add1_Temperature = StringVar()
    default_value_Add1_Temperature.set('0')
    e_Add1_Temperature = tkinter.Entry(subroot, width=6, textvariable=default_value_Add1_Temperature)
    e_Add1_Temperature.pack()
    e_Add1_Temperature.place(x=120, y=70, anchor=NW)
    ###########################Add1正半母线电压########################################
    e_Add1_PFCvP_Label = tkinter.Label(subroot, text="正半母线电压(0.1V)")
    e_Add1_PFCvP_Label.pack()
    e_Add1_PFCvP_Label.place(x=0, y=90, anchor=NW)
    default_value_Add1_PFCvP = StringVar()
    default_value_Add1_PFCvP.set('0')
    e_Add1_PFCvP = tkinter.Entry(subroot, width=6, textvariable=default_value_Add1_PFCvP)
    e_Add1_PFCvP.pack()
    e_Add1_PFCvP.place(x=120, y=90, anchor=NW)
    ###########################Add1负半母线电压########################################
    e_Add1_PFCvN_Label = tkinter.Label(subroot, text="负半母线电压(0.1V)")
    e_Add1_PFCvN_Label.pack()
    e_Add1_PFCvN_Label.place(x=0, y=110, anchor=NW)
    default_value_Add1_PFCvN = StringVar()
    default_value_Add1_PFCvN.set('0')
    e_Add1_PFCvN = tkinter.Entry(subroot, width=6, textvariable=default_value_Add1_PFCvN)
    e_Add1_PFCvN.pack()
    e_Add1_PFCvN.place(x=120, y=110, anchor=NW)
    #############################输出过压################################
    Add1_chVarOutOverVoltage = tkinter.IntVar()
    Add1_check0 = tkinter.Checkbutton(subroot, text="输出过压", variable=Add1_chVarOutOverVoltage)
    Add1_check0.deselect()
    Add1_check0.place(x=0, y=130, anchor=NW)
    #############################过温################################
    Add1_chVarOverTemperature = tkinter.IntVar()
    Add1_check1 = tkinter.Checkbutton(subroot, text="过温", variable=Add1_chVarOverTemperature)
    Add1_check1.deselect()
    Add1_check1.place(x=0, y=150, anchor=NW)
    #############################模块故障################################
    Add1_chVarModuleFault = tkinter.IntVar()
    Add1_check2 = tkinter.Checkbutton(subroot, text="模块故障", variable=Add1_chVarModuleFault)
    Add1_check2.deselect()
    Add1_check2.place(x=0, y=170, anchor=NW)
    #############################模块保护################################
    Add1_chVarModuleProtect = tkinter.IntVar()
    Add1_check3 = tkinter.Checkbutton(subroot, text="模块保护", variable=Add1_chVarModuleProtect)
    Add1_check3.deselect()
    Add1_check3.place(x=0, y=190, anchor=NW)
    #############################风扇故障################################
    Add1_chVarFanFault = tkinter.IntVar()
    Add1_check4 = tkinter.Checkbutton(subroot, text="风扇故障", variable=Add1_chVarFanFault)
    Add1_check4.deselect()
    Add1_check4.place(x=0, y=210, anchor=NW)
    #############################模块EEPROM故障################################
    Add1_chVarEEPROMFault = tkinter.IntVar()
    Add1_check5 = tkinter.Checkbutton(subroot, text="模块EEPROM故障", variable=Add1_chVarEEPROMFault)
    Add1_check5.deselect()
    Add1_check5.place(x=0, y=230, anchor=NW)
    #############################交流限功率################################
    Add1_chVarACPowerLimit = tkinter.IntVar()
    Add1_check6 = tkinter.Checkbutton(subroot, text="交流限功率", variable=Add1_chVarACPowerLimit)
    Add1_check6.deselect()
    Add1_check6.place(x=0, y=250, anchor=NW)
    #############################温度限功率################################
    Add1_chVarTemPowerLimit = tkinter.IntVar()
    Add1_check7 = tkinter.Checkbutton(subroot, text="温度限功率", variable=Add1_chVarTemPowerLimit)
    Add1_check7.deselect()
    Add1_check7.place(x=0, y=270, anchor=NW)
    #############################模块限功率################################
    Add1_chVarModulePowerLimit = tkinter.IntVar()
    Add1_check8 = tkinter.Checkbutton(subroot, text="模块限功率", variable=Add1_chVarModulePowerLimit)
    Add1_check8.deselect()
    Add1_check8.place(x=0, y=290, anchor=NW)
    #############################待机状态################################
    Add1_chVarStandbyState = tkinter.IntVar()
    Add1_check9 = tkinter.Checkbutton(subroot, text="待机状态", variable=Add1_chVarStandbyState)
    Add1_check9.deselect()
    Add1_check9.place(x=0, y=310, anchor=NW)
    #############################风扇全速################################
    Add1_chVarFanFullSpeed = tkinter.IntVar()
    Add1_check10 = tkinter.Checkbutton(subroot, text="风扇全速", variable=Add1_chVarFanFullSpeed)
    Add1_check10.deselect()
    Add1_check10.place(x=0, y=330, anchor=NW)
    #############################模块WALK-In功能使能################################
    Add1_chVarModuleWalkInEbable = tkinter.IntVar()
    Add1_check11 = tkinter.Checkbutton(subroot, text="模块WALK-In功能使能", variable=Add1_chVarModuleWalkInEbable)
    Add1_check11.deselect()
    Add1_check11.place(x=0, y=350, anchor=NW)
    #############################PFC关机################################
    Add1_chVarPFCPowerOff = tkinter.IntVar()
    Add1_check12 = tkinter.Checkbutton(subroot, text="PFC关机", variable=Add1_chVarPFCPowerOff)
    Add1_check12.deselect()
    Add1_check12.place(x=0, y=370, anchor=NW)
    #############################模块识别################################
    Add1_chVarModuleRecognition = tkinter.IntVar()
    Add1_check13 = tkinter.Checkbutton(subroot, text="模块识别", variable=Add1_chVarModuleRecognition)
    Add1_check13.deselect()
    Add1_check13.place(x=0, y=390, anchor=NW)
    #############################模块电流均流故障################################
    Add1_chVarModuleCurrentMean = tkinter.IntVar()
    Add1_check14 = tkinter.Checkbutton(subroot, text="模块电流均流故障", variable=Add1_chVarModuleCurrentMean)
    Add1_check14.deselect()
    Add1_check14.place(x=0, y=410, anchor=NW)
    #############################模块CAN错误状态################################
    Add1_chVarModuleCANErrorState = tkinter.IntVar()
    Add1_check15 = tkinter.Checkbutton(subroot, text="模块CAN错误状态", variable=Add1_chVarModuleCANErrorState)
    Add1_check15.deselect()
    Add1_check15.place(x=0, y=430, anchor=NW)
    #############################模块顺序起机功能使能################################
    Add1_chVarModuleOrderOnEnable = tkinter.IntVar()
    Add1_check16 = tkinter.Checkbutton(subroot, text="模块顺序起机功能使能", variable=Add1_chVarModuleOrderOnEnable)
    Add1_check16.deselect()
    Add1_check16.place(x=0, y=450, anchor=NW)
    #############################模块输入欠压告警################################
    Add1_chVarModuleInputUVWarning = tkinter.IntVar()
    Add1_check17 = tkinter.Checkbutton(subroot, text="模块输入欠压告警", variable=Add1_chVarModuleInputUVWarning)
    Add1_check17.deselect()
    Add1_check17.place(x=0, y=470, anchor=NW)
    #############################模块交流不平衡告警################################
    Add1_chVarModuleACInbalanceWarning = tkinter.IntVar()
    Add1_check18 = tkinter.Checkbutton(subroot, text="模块交流不平衡告警", variable=Add1_chVarModuleACInbalanceWarning)
    Add1_check18.deselect()
    Add1_check18.place(x=0, y=490, anchor=NW)
    ############################模块交流缺相告警################################
    Add1_chVarModuleACPhaseLossWarning = tkinter.IntVar()
    Add1_check19 = tkinter.Checkbutton(subroot, text="模块交流缺相告警", variable=Add1_chVarModuleACPhaseLossWarning)
    Add1_check19.deselect()
    Add1_check19.place(x=0, y=510, anchor=NW)
    ############################模块直流母线欠压################################
    Add1_chVarModuleDCUV = tkinter.IntVar()
    Add1_check20 = tkinter.Checkbutton(subroot, text="模块直流母线欠压", variable=Add1_chVarModuleDCUV)
    Add1_check20.deselect()
    Add1_check20.place(x=0, y=530, anchor=NW)
    ############################模块ID重复################################
    Add1_chVarModuleIDRepet = tkinter.IntVar()
    Add1_check21 = tkinter.Checkbutton(subroot, text="模块ID重复", variable=Add1_chVarModuleIDRepet)
    Add1_check21.deselect()
    Add1_check21.place(x=0, y=550, anchor=NW)
    ############################模块输入过压################################
    Add1_chVarModuleInputOverVoltage = tkinter.IntVar()
    Add1_check22 = tkinter.Checkbutton(subroot, text="模块输入过压", variable=Add1_chVarModuleInputOverVoltage)
    Add1_check22.deselect()
    Add1_check22.place(x=0, y=570, anchor=NW)
    ############################模块PFC故障###############################
    Add1_chVarModulePFCFault = tkinter.IntVar()
    Add1_check23 = tkinter.Checkbutton(subroot, text="模块PFC故障", variable=Add1_chVarModulePFCFault)
    Add1_check23.deselect()
    Add1_check23.place(x=0, y=590, anchor=NW)
    ############################模块直流母线过压###############################
    Add1_chVarModuleDCOverVoltage = tkinter.IntVar()
    Add1_check24 = tkinter.Checkbutton(subroot, text="模块直流母线过压", variable=Add1_chVarModuleDCOverVoltage)
    Add1_check24.deselect()
    Add1_check24.place(x=0, y=610, anchor=NW)
    ############################模块插拔故障###############################
    Add1_chVarModulePlugFault = tkinter.IntVar()
    Add1_check25 = tkinter.Checkbutton(subroot, text="模块插拔故障", variable=Add1_chVarModulePlugFault)
    Add1_check25.deselect()
    Add1_check25.place(x=0, y=630, anchor=NW)
    ############################模块重载告警###############################
    Add1_chVarModuleReloadWarning = tkinter.IntVar()
    Add1_check26 = tkinter.Checkbutton(subroot, text="模块重载告警", variable=Add1_chVarModuleReloadWarning)
    Add1_check26.deselect()
    Add1_check26.place(x=0, y=650, anchor=NW)
    ############################模块输出欠压告警###############################
    Add1_chVarModuleOutUVWarning = tkinter.IntVar()
    Add1_check27 = tkinter.Checkbutton(subroot, text="模块输出欠压告警", variable=Add1_chVarModuleOutUVWarning)
    Add1_check27.deselect()
    Add1_check27.place(x=0, y=670, anchor=NW)
    ############################模块内部通讯异常告警###############################
    Add1_chVarModuleInternalComAbnormal = tkinter.IntVar()
    Add1_check28 = tkinter.Checkbutton(subroot, text="模块内部通讯异常告警", variable=Add1_chVarModuleInternalComAbnormal)
    Add1_check28.deselect()
    Add1_check28.place(x=0, y=690, anchor=NW)
    ############################模块输出熔丝断告警###############################
    Add1_chVarModuleOutFuseWarning = tkinter.IntVar()
    Add1_check29 = tkinter.Checkbutton(subroot, text="模块输出熔丝断告警", variable=Add1_chVarModuleOutFuseWarning)
    Add1_check29.deselect()
    Add1_check29.place(x=0, y=710, anchor=NW)


    e_moduledata2_Label = tkinter.Label(subroot, text="模块2数据", font=("Arial, 12"))
    e_moduledata2_Label.pack()
    e_moduledata2_Label.place(x=200, y=10, anchor=NW)
    ###########################Add2输出电压########################################
    e_Add2_OutVoltage_Label = tkinter.Label(subroot, text="模块2输出电压(0.1V)")
    e_Add2_OutVoltage_Label.pack()
    e_Add2_OutVoltage_Label.place(x=200, y=30, anchor=NW)
    default_value_Add2_OutVoltage = StringVar()
    default_value_Add2_OutVoltage.set('0')
    e_Add2_OutVoltage = tkinter.Entry(subroot, width=6, textvariable=default_value_Add2_OutVoltage)
    e_Add2_OutVoltage.pack()
    e_Add2_OutVoltage.place(x=320, y=30, anchor=NW)
    ###########################Add2输出电流########################################
    e_Add2_OutCurrent_Label = tkinter.Label(subroot, text="模块2输出电流(0.1A)")
    e_Add2_OutCurrent_Label.pack()
    e_Add2_OutCurrent_Label.place(x=200, y=50, anchor=NW)
    default_value_Add2_OutCurrent = StringVar()
    default_value_Add2_OutCurrent.set('0')
    e_Add2_OutCurrent = tkinter.Entry(subroot, width=6, textvariable=default_value_Add2_OutCurrent)
    e_Add2_OutCurrent.pack()
    e_Add2_OutCurrent.place(x=320, y=50, anchor=NW)
    ###########################Add2温度########################################
    e_Add2_Temperature_Label = tkinter.Label(subroot, text="模块2温度(0.1℃)")
    e_Add2_Temperature_Label.pack()
    e_Add2_Temperature_Label.place(x=200, y=70, anchor=NW)
    default_value_Add2_Temperature = StringVar()
    default_value_Add2_Temperature.set('0')
    e_Add2_Temperature = tkinter.Entry(subroot, width=6, textvariable=default_value_Add2_Temperature)
    e_Add2_Temperature.pack()
    e_Add2_Temperature.place(x=320, y=70, anchor=NW)
    ###########################Add2正半母线电压########################################
    e_Add2_PFCvP_Label = tkinter.Label(subroot, text="正半母线电压")
    e_Add2_PFCvP_Label.pack()
    e_Add2_PFCvP_Label.place(x=200, y=90, anchor=NW)
    default_value_Add2_PFCvP = StringVar()
    default_value_Add2_PFCvP.set('0')
    e_Add2_PFCvP = tkinter.Entry(subroot, width=6, textvariable=default_value_Add2_PFCvP)
    e_Add2_PFCvP.pack()
    e_Add2_PFCvP.place(x=320, y=90, anchor=NW)
    ###########################Add2负半母线电压########################################
    e_Add2_PFCvN_Label = tkinter.Label(subroot, text="负半母线电压")
    e_Add2_PFCvN_Label.pack()
    e_Add2_PFCvN_Label.place(x=200, y=110, anchor=NW)
    default_value_Add2_PFCvN = StringVar()
    default_value_Add2_PFCvN.set('0')
    e_Add2_PFCvN = tkinter.Entry(subroot, width=6, textvariable=default_value_Add2_PFCvN)
    e_Add2_PFCvN.pack()
    e_Add2_PFCvN.place(x=320, y=110, anchor=NW)
    #############################输出过压################################
    Add2_chVarOutOverVoltage = tkinter.IntVar()
    Add2_check0 = tkinter.Checkbutton(subroot, text="输出过压", variable=Add2_chVarOutOverVoltage)
    Add2_check0.deselect()
    Add2_check0.place(x=200, y=130, anchor=NW)
    #############################过温################################
    Add2_chVarOverTemperature = tkinter.IntVar()
    Add2_check1 = tkinter.Checkbutton(subroot, text="过温", variable=Add2_chVarOverTemperature)
    Add2_check1.deselect()
    Add2_check1.place(x=200, y=150, anchor=NW)
    #############################模块故障################################
    Add2_chVarModuleFault = tkinter.IntVar()
    Add2_check2 = tkinter.Checkbutton(subroot, text="模块故障", variable=Add2_chVarModuleFault)
    Add2_check2.deselect()
    Add2_check2.place(x=200, y=170, anchor=NW)
    #############################模块保护################################
    Add2_chVarModuleProtect = tkinter.IntVar()
    Add2_check3 = tkinter.Checkbutton(subroot, text="模块保护", variable=Add2_chVarModuleProtect)
    Add2_check3.deselect()
    Add2_check3.place(x=200, y=190, anchor=NW)
    #############################风扇故障################################
    Add2_chVarFanFault = tkinter.IntVar()
    Add2_check4 = tkinter.Checkbutton(subroot, text="风扇故障", variable=Add2_chVarFanFault)
    Add2_check4.deselect()
    Add2_check4.place(x=200, y=210, anchor=NW)
    #############################模块EEPROM故障################################
    Add2_chVarEEPROMFault = tkinter.IntVar()
    Add2_check5 = tkinter.Checkbutton(subroot, text="模块EEPROM故障", variable=Add2_chVarEEPROMFault)
    Add2_check5.deselect()
    Add2_check5.place(x=200, y=230, anchor=NW)
    #############################交流限功率################################
    Add2_chVarACPowerLimit = tkinter.IntVar()
    Add2_check6 = tkinter.Checkbutton(subroot, text="交流限功率", variable=Add2_chVarACPowerLimit)
    Add2_check6.deselect()
    Add2_check6.place(x=200, y=250, anchor=NW)
    #############################温度限功率################################
    Add2_chVarTemPowerLimit = tkinter.IntVar()
    Add2_check7 = tkinter.Checkbutton(subroot, text="温度限功率", variable=Add2_chVarTemPowerLimit)
    Add2_check7.deselect()
    Add2_check7.place(x=200, y=270, anchor=NW)
    #############################模块限功率################################
    Add2_chVarModulePowerLimit = tkinter.IntVar()
    Add2_check8 = tkinter.Checkbutton(subroot, text="模块限功率", variable=Add2_chVarModulePowerLimit)
    Add2_check8.deselect()
    Add2_check8.place(x=200, y=290, anchor=NW)
    #############################待机状态################################
    Add2_chVarStandbyState = tkinter.IntVar()
    Add2_check9 = tkinter.Checkbutton(subroot, text="待机状态", variable=Add2_chVarStandbyState)
    Add2_check9.deselect()
    Add2_check9.place(x=200, y=310, anchor=NW)
    #############################风扇全速################################
    Add2_chVarFanFullSpeed = tkinter.IntVar()
    Add2_check10 = tkinter.Checkbutton(subroot, text="风扇全速", variable=Add2_chVarFanFullSpeed)
    Add2_check10.deselect()
    Add2_check10.place(x=200, y=330, anchor=NW)
    #############################模块WALK-In功能使能################################
    Add2_chVarModuleWalkInEbable = tkinter.IntVar()
    Add2_check11 = tkinter.Checkbutton(subroot, text="模块WALK-In功能使能", variable=Add2_chVarModuleWalkInEbable)
    Add2_check11.deselect()
    Add2_check11.place(x=200, y=350, anchor=NW)
    #############################PFC关机################################
    Add2_chVarPFCPowerOff = tkinter.IntVar()
    Add2_check12 = tkinter.Checkbutton(subroot, text="PFC关机", variable=Add2_chVarPFCPowerOff)
    Add2_check12.deselect()
    Add2_check12.place(x=200, y=370, anchor=NW)
    #############################模块识别################################
    Add2_chVarModuleRecognition = tkinter.IntVar()
    Add2_check13 = tkinter.Checkbutton(subroot, text="模块识别", variable=Add2_chVarModuleRecognition)
    Add2_check13.deselect()
    Add2_check13.place(x=200, y=390, anchor=NW)
    #############################模块电流均流故障################################
    Add2_chVarModuleCurrentMean = tkinter.IntVar()
    Add2_check14 = tkinter.Checkbutton(subroot, text="模块电流均流故障", variable=Add2_chVarModuleCurrentMean)
    Add2_check14.deselect()
    Add2_check14.place(x=200, y=410, anchor=NW)
    #############################模块CAN错误状态################################
    Add2_chVarModuleCANErrorState = tkinter.IntVar()
    Add2_check15 = tkinter.Checkbutton(subroot, text="模块CAN错误状态", variable=Add2_chVarModuleCANErrorState)
    Add2_check15.deselect()
    Add2_check15.place(x=200, y=430, anchor=NW)
    #############################模块顺序起机功能使能################################
    Add2_chVarModuleOrderOnEnable = tkinter.IntVar()
    Add2_check16 = tkinter.Checkbutton(subroot, text="模块顺序起机功能使能", variable=Add2_chVarModuleOrderOnEnable)
    Add2_check16.deselect()
    Add2_check16.place(x=200, y=450, anchor=NW)
    #############################模块输入欠压告警################################
    Add2_chVarModuleInputUVWarning = tkinter.IntVar()
    Add2_check17 = tkinter.Checkbutton(subroot, text="模块输入欠压告警", variable=Add2_chVarModuleInputUVWarning)
    Add2_check17.deselect()
    Add2_check17.place(x=200, y=470, anchor=NW)
    #############################模块交流不平衡告警################################
    Add2_chVarModuleACInbalanceWarning = tkinter.IntVar()
    Add2_check18 = tkinter.Checkbutton(subroot, text="模块交流不平衡告警", variable=Add2_chVarModuleACInbalanceWarning)
    Add2_check18.deselect()
    Add2_check18.place(x=200, y=490, anchor=NW)
    ############################模块交流缺相告警################################
    Add2_chVarModuleACPhaseLossWarning = tkinter.IntVar()
    Add2_check19 = tkinter.Checkbutton(subroot, text="模块交流缺相告警", variable=Add2_chVarModuleACPhaseLossWarning)
    Add2_check19.deselect()
    Add2_check19.place(x=200, y=510, anchor=NW)
    ############################模块直流母线欠压################################
    Add2_chVarModuleDCUV = tkinter.IntVar()
    Add2_check20 = tkinter.Checkbutton(subroot, text="模块直流母线欠压", variable=Add2_chVarModuleDCUV)
    Add2_check20.deselect()
    Add2_check20.place(x=200, y=530, anchor=NW)
    ############################模块ID重复################################
    Add2_chVarModuleIDRepet = tkinter.IntVar()
    Add2_check21 = tkinter.Checkbutton(subroot, text="模块ID重复", variable=Add2_chVarModuleIDRepet)
    Add2_check21.deselect()
    Add2_check21.place(x=200, y=550, anchor=NW)
    ############################模块输入过压################################
    Add2_chVarModuleInputOverVoltage = tkinter.IntVar()
    Add2_check22 = tkinter.Checkbutton(subroot, text="模块输入过压", variable=Add2_chVarModuleInputOverVoltage)
    Add2_check22.deselect()
    Add2_check22.place(x=200, y=570, anchor=NW)
    ############################模块PFC故障###############################
    Add2_chVarModulePFCFault = tkinter.IntVar()
    Add2_check23 = tkinter.Checkbutton(subroot, text="模块PFC故障", variable=Add2_chVarModulePFCFault)
    Add2_check23.deselect()
    Add2_check23.place(x=200, y=590, anchor=NW)
    ############################模块直流母线过压###############################
    Add2_chVarModuleDCOverVoltage = tkinter.IntVar()
    Add2_check24 = tkinter.Checkbutton(subroot, text="模块直流母线过压", variable=Add2_chVarModuleDCOverVoltage)
    Add2_check24.deselect()
    Add2_check24.place(x=200, y=610, anchor=NW)
    ############################模块插拔故障###############################
    Add2_chVarModulePlugFault = tkinter.IntVar()
    Add2_check25 = tkinter.Checkbutton(subroot, text="模块插拔故障", variable=Add2_chVarModulePlugFault)
    Add2_check25.deselect()
    Add2_check25.place(x=200, y=630, anchor=NW)
    ############################模块重载告警###############################
    Add2_chVarModuleReloadWarning = tkinter.IntVar()
    Add2_check26 = tkinter.Checkbutton(subroot, text="模块重载告警", variable=Add2_chVarModuleReloadWarning)
    Add2_check26.deselect()
    Add2_check26.place(x=200, y=650, anchor=NW)
    ############################模块输出欠压告警###############################
    Add2_chVarModuleOutUVWarning = tkinter.IntVar()
    Add2_check27 = tkinter.Checkbutton(subroot, text="模块输出欠压告警", variable=Add2_chVarModuleOutUVWarning)
    Add2_check27.deselect()
    Add2_check27.place(x=200, y=670, anchor=NW)
    ############################模块内部通讯异常告警###############################
    Add2_chVarModuleInternalComAbnormal = tkinter.IntVar()
    Add2_check28 = tkinter.Checkbutton(subroot, text="模块内部通讯异常告警", variable=Add2_chVarModuleInternalComAbnormal)
    Add2_check28.deselect()
    Add2_check28.place(x=200, y=690, anchor=NW)
    ############################模块输出熔丝断告警###############################
    Add2_chVarModuleOutFuseWarning = tkinter.IntVar()
    Add2_check29 = tkinter.Checkbutton(subroot, text="模块输出熔丝断告警", variable=Add2_chVarModuleOutFuseWarning)
    Add2_check29.deselect()
    Add2_check29.place(x=200, y=710, anchor=NW)

    e_moduledata3_Label = tkinter.Label(subroot, text="模块3数据", font=("Arial, 12"))
    e_moduledata3_Label.pack()
    e_moduledata3_Label.place(x=400, y=10, anchor=NW)
    ###########################Add3输出电压########################################
    e_Add3_OutVoltage_Label = tkinter.Label(subroot, text="模块3输出电压(0.1V)")
    e_Add3_OutVoltage_Label.pack()
    e_Add3_OutVoltage_Label.place(x=400, y=30, anchor=NW)
    default_value_Add3_OutVoltage = StringVar()
    default_value_Add3_OutVoltage.set('0')
    e_Add3_OutVoltage = tkinter.Entry(subroot, width=6, textvariable=default_value_Add3_OutVoltage)
    e_Add3_OutVoltage.pack()
    e_Add3_OutVoltage.place(x=520, y=30, anchor=NW)
    ###########################Add3输出电流########################################
    e_Add3_OutCurrent_Label = tkinter.Label(subroot, text="模块3输出电流(0.1A)")
    e_Add3_OutCurrent_Label.pack()
    e_Add3_OutCurrent_Label.place(x=400, y=50, anchor=NW)
    default_value_Add3_OutCurrent = StringVar()
    default_value_Add3_OutCurrent.set('0')
    e_Add3_OutCurrent = tkinter.Entry(subroot, width=6, textvariable=default_value_Add3_OutCurrent)
    e_Add3_OutCurrent.pack()
    e_Add3_OutCurrent.place(x=520, y=50, anchor=NW)
    ###########################Add3温度########################################
    e_Add3_Temperature_Label = tkinter.Label(subroot, text="模块3温度(0.1℃)")
    e_Add3_Temperature_Label.pack()
    e_Add3_Temperature_Label.place(x=400, y=70, anchor=NW)
    default_value_Add3_Temperature = StringVar()
    default_value_Add3_Temperature.set('0')
    e_Add3_Temperature = tkinter.Entry(subroot, width=6, textvariable=default_value_Add3_Temperature)
    e_Add3_Temperature.pack()
    e_Add3_Temperature.place(x=520, y=70, anchor=NW)
    ###########################Add3正半母线电压########################################
    e_Add3_PFCvP_Label = tkinter.Label(subroot, text="正半母线电压")
    e_Add3_PFCvP_Label.pack()
    e_Add3_PFCvP_Label.place(x=400, y=90, anchor=NW)
    default_value_Add3_PFCvP = StringVar()
    default_value_Add3_PFCvP.set('0')
    e_Add3_PFCvP = tkinter.Entry(subroot, width=6, textvariable=default_value_Add3_PFCvP)
    e_Add3_PFCvP.pack()
    e_Add3_PFCvP.place(x=520, y=90, anchor=NW)
    ###########################Add3负半母线电压########################################
    e_Add3_PFCvN_Label = tkinter.Label(subroot, text="负半母线电压")
    e_Add3_PFCvN_Label.pack()
    e_Add3_PFCvN_Label.place(x=400, y=110, anchor=NW)
    default_value_Add3_PFCvN = StringVar()
    default_value_Add3_PFCvN.set('0')
    e_Add3_PFCvN = tkinter.Entry(subroot, width=6, textvariable=default_value_Add3_PFCvN)
    e_Add3_PFCvN.pack()
    e_Add3_PFCvN.place(x=520, y=110, anchor=NW)
    #############################输出过压################################
    Add3_chVarOutOverVoltage = tkinter.IntVar()
    Add3_check0 = tkinter.Checkbutton(subroot, text="输出过压", variable=Add3_chVarOutOverVoltage)
    Add3_check0.deselect()
    Add3_check0.place(x=400, y=130, anchor=NW)
    #############################过温################################
    Add3_chVarOverTemperature = tkinter.IntVar()
    Add3_check1 = tkinter.Checkbutton(subroot, text="过温", variable=Add3_chVarOverTemperature)
    Add3_check1.deselect()
    Add3_check1.place(x=400, y=150, anchor=NW)
    #############################模块故障################################
    Add3_chVarModuleFault = tkinter.IntVar()
    Add3_check2 = tkinter.Checkbutton(subroot, text="模块故障", variable=Add3_chVarModuleFault)
    Add3_check2.deselect()
    Add3_check2.place(x=400, y=170, anchor=NW)
    #############################模块保护################################
    Add3_chVarModuleProtect = tkinter.IntVar()
    Add3_check3 = tkinter.Checkbutton(subroot, text="模块保护", variable=Add3_chVarModuleProtect)
    Add3_check3.deselect()
    Add3_check3.place(x=400, y=190, anchor=NW)
    #############################风扇故障################################
    Add3_chVarFanFault = tkinter.IntVar()
    Add3_check4 = tkinter.Checkbutton(subroot, text="风扇故障", variable=Add3_chVarFanFault)
    Add3_check4.deselect()
    Add3_check4.place(x=400, y=210, anchor=NW)
    #############################模块EEPROM故障################################
    Add3_chVarEEPROMFault = tkinter.IntVar()
    Add3_check5 = tkinter.Checkbutton(subroot, text="模块EEPROM故障", variable=Add3_chVarEEPROMFault)
    Add3_check5.deselect()
    Add3_check5.place(x=400, y=230, anchor=NW)
    #############################交流限功率################################
    Add3_chVarACPowerLimit = tkinter.IntVar()
    Add3_check6 = tkinter.Checkbutton(subroot, text="交流限功率", variable=Add3_chVarACPowerLimit)
    Add3_check6.deselect()
    Add3_check6.place(x=400, y=250, anchor=NW)
    #############################温度限功率################################
    Add3_chVarTemPowerLimit = tkinter.IntVar()
    Add3_check7 = tkinter.Checkbutton(subroot, text="温度限功率", variable=Add3_chVarTemPowerLimit)
    Add3_check7.deselect()
    Add3_check7.place(x=400, y=270, anchor=NW)
    #############################模块限功率################################
    Add3_chVarModulePowerLimit = tkinter.IntVar()
    Add3_check8 = tkinter.Checkbutton(subroot, text="模块限功率", variable=Add3_chVarModulePowerLimit)
    Add3_check8.deselect()
    Add3_check8.place(x=400, y=290, anchor=NW)
    #############################待机状态################################
    Add3_chVarStandbyState = tkinter.IntVar()
    Add3_check9 = tkinter.Checkbutton(subroot, text="待机状态", variable=Add3_chVarStandbyState)
    Add3_check9.deselect()
    Add3_check9.place(x=400, y=310, anchor=NW)
    #############################风扇全速################################
    Add3_chVarFanFullSpeed = tkinter.IntVar()
    Add3_check10 = tkinter.Checkbutton(subroot, text="风扇全速", variable=Add3_chVarFanFullSpeed)
    Add3_check10.deselect()
    Add3_check10.place(x=400, y=330, anchor=NW)
    #############################模块WALK-In功能使能################################
    Add3_chVarModuleWalkInEbable = tkinter.IntVar()
    Add3_check11 = tkinter.Checkbutton(subroot, text="模块WALK-In功能使能", variable=Add3_chVarModuleWalkInEbable)
    Add3_check11.deselect()
    Add3_check11.place(x=400, y=350, anchor=NW)
    #############################PFC关机################################
    Add3_chVarPFCPowerOff = tkinter.IntVar()
    Add3_check12 = tkinter.Checkbutton(subroot, text="PFC关机", variable=Add3_chVarPFCPowerOff)
    Add3_check12.deselect()
    Add3_check12.place(x=400, y=370, anchor=NW)
    #############################模块识别################################
    Add3_chVarModuleRecognition = tkinter.IntVar()
    Add3_check13 = tkinter.Checkbutton(subroot, text="模块识别", variable=Add3_chVarModuleRecognition)
    Add3_check13.deselect()
    Add3_check13.place(x=400, y=390, anchor=NW)
    #############################模块电流均流故障################################
    Add3_chVarModuleCurrentMean = tkinter.IntVar()
    Add3_check14 = tkinter.Checkbutton(subroot, text="模块电流均流故障", variable=Add3_chVarModuleCurrentMean)
    Add3_check14.deselect()
    Add3_check14.place(x=400, y=410, anchor=NW)
    #############################模块CAN错误状态################################
    Add3_chVarModuleCANErrorState = tkinter.IntVar()
    Add3_check15 = tkinter.Checkbutton(subroot, text="模块CAN错误状态", variable=Add3_chVarModuleCANErrorState)
    Add3_check15.deselect()
    Add3_check15.place(x=400, y=430, anchor=NW)
    #############################模块顺序起机功能使能################################
    Add3_chVarModuleOrderOnEnable = tkinter.IntVar()
    Add3_check16 = tkinter.Checkbutton(subroot, text="模块顺序起机功能使能", variable=Add3_chVarModuleOrderOnEnable)
    Add3_check16.deselect()
    Add3_check16.place(x=400, y=450, anchor=NW)
    #############################模块输入欠压告警################################
    Add3_chVarModuleInputUVWarning = tkinter.IntVar()
    Add3_check17 = tkinter.Checkbutton(subroot, text="模块输入欠压告警", variable=Add3_chVarModuleInputUVWarning)
    Add3_check17.deselect()
    Add3_check17.place(x=400, y=470, anchor=NW)
    #############################模块交流不平衡告警################################
    Add3_chVarModuleACInbalanceWarning = tkinter.IntVar()
    Add3_check18 = tkinter.Checkbutton(subroot, text="模块交流不平衡告警", variable=Add3_chVarModuleACInbalanceWarning)
    Add3_check18.deselect()
    Add3_check18.place(x=400, y=490, anchor=NW)
    ############################模块交流缺相告警################################
    Add3_chVarModuleACPhaseLossWarning = tkinter.IntVar()
    Add3_check19 = tkinter.Checkbutton(subroot, text="模块交流缺相告警", variable=Add3_chVarModuleACPhaseLossWarning)
    Add3_check19.deselect()
    Add3_check19.place(x=400, y=510, anchor=NW)
    ############################模块直流母线欠压################################
    Add3_chVarModuleDCUV = tkinter.IntVar()
    Add3_check20 = tkinter.Checkbutton(subroot, text="模块直流母线欠压", variable=Add3_chVarModuleDCUV)
    Add3_check20.deselect()
    Add3_check20.place(x=400, y=530, anchor=NW)
    ############################模块ID重复################################
    Add3_chVarModuleIDRepet = tkinter.IntVar()
    Add3_check21 = tkinter.Checkbutton(subroot, text="模块ID重复", variable=Add3_chVarModuleIDRepet)
    Add3_check21.deselect()
    Add3_check21.place(x=400, y=550, anchor=NW)
    ############################模块输入过压################################
    Add3_chVarModuleInputOverVoltage = tkinter.IntVar()
    Add3_check22 = tkinter.Checkbutton(subroot, text="模块输入过压", variable=Add3_chVarModuleInputOverVoltage)
    Add3_check22.deselect()
    Add3_check22.place(x=400, y=570, anchor=NW)
    ############################模块PFC故障###############################
    Add3_chVarModulePFCFault = tkinter.IntVar()
    Add3_check23 = tkinter.Checkbutton(subroot, text="模块PFC故障", variable=Add3_chVarModulePFCFault)
    Add3_check23.deselect()
    Add3_check23.place(x=400, y=590, anchor=NW)
    ############################模块直流母线过压###############################
    Add3_chVarModuleDCOverVoltage = tkinter.IntVar()
    Add3_check24 = tkinter.Checkbutton(subroot, text="模块直流母线过压", variable=Add3_chVarModuleDCOverVoltage)
    Add3_check24.deselect()
    Add3_check24.place(x=400, y=610, anchor=NW)
    ############################模块插拔故障###############################
    Add3_chVarModulePlugFault = tkinter.IntVar()
    Add3_check25 = tkinter.Checkbutton(subroot, text="模块插拔故障", variable=Add3_chVarModulePlugFault)
    Add3_check25.deselect()
    Add3_check25.place(x=400, y=630, anchor=NW)
    ############################模块重载告警###############################
    Add3_chVarModuleReloadWarning = tkinter.IntVar()
    Add3_check26 = tkinter.Checkbutton(subroot, text="模块重载告警", variable=Add3_chVarModuleReloadWarning)
    Add3_check26.deselect()
    Add3_check26.place(x=400, y=650, anchor=NW)
    ############################模块输出欠压告警###############################
    Add3_chVarModuleOutUVWarning = tkinter.IntVar()
    Add3_check27 = tkinter.Checkbutton(subroot, text="模块输出欠压告警", variable=Add3_chVarModuleOutUVWarning)
    Add3_check27.deselect()
    Add3_check27.place(x=400, y=670, anchor=NW)
    ############################模块内部通讯异常告警###############################
    Add3_chVarModuleInternalComAbnormal = tkinter.IntVar()
    Add3_check28 = tkinter.Checkbutton(subroot, text="模块内部通讯异常告警", variable=Add3_chVarModuleInternalComAbnormal)
    Add3_check28.deselect()
    Add3_check28.place(x=400, y=690, anchor=NW)
    ############################模块输出熔丝断告警###############################
    Add3_chVarModuleOutFuseWarning = tkinter.IntVar()
    Add3_check29 = tkinter.Checkbutton(subroot, text="模块输出熔丝断告警", variable=Add3_chVarModuleOutFuseWarning)
    Add3_check29.deselect()
    Add3_check29.place(x=400, y=710, anchor=NW)

    e_moduledata4_Label = tkinter.Label(subroot, text="模块4数据", font=("Arial, 12"))
    e_moduledata4_Label.pack()
    e_moduledata4_Label.place(x=600, y=10, anchor=NW)
    ###########################Add4输出电压########################################
    e_Add4_OutVoltage_Label = tkinter.Label(subroot, text="模块4输出电压(0.1V)")
    e_Add4_OutVoltage_Label.pack()
    e_Add4_OutVoltage_Label.place(x=600, y=30, anchor=NW)
    default_value_Add4_OutVoltage = StringVar()
    default_value_Add4_OutVoltage.set('0')
    e_Add4_OutVoltage = tkinter.Entry(subroot, width=6, textvariable=default_value_Add4_OutVoltage)
    e_Add4_OutVoltage.pack()
    e_Add4_OutVoltage.place(x=720, y=30, anchor=NW)
    ###########################Add4输出电流########################################
    e_Add4_OutCurrent_Label = tkinter.Label(subroot, text="模块4输出电流(0.1A)")
    e_Add4_OutCurrent_Label.pack()
    e_Add4_OutCurrent_Label.place(x=600, y=50, anchor=NW)
    default_value_Add4_OutCurrent = StringVar()
    default_value_Add4_OutCurrent.set('0')
    e_Add4_OutCurrent = tkinter.Entry(subroot, width=6, textvariable=default_value_Add4_OutCurrent)
    e_Add4_OutCurrent.pack()
    e_Add4_OutCurrent.place(x=720, y=50, anchor=NW)
    ###########################Add4温度########################################
    e_Add4_Temperature_Label = tkinter.Label(subroot, text="模块4温度(0.1℃)")
    e_Add4_Temperature_Label.pack()
    e_Add4_Temperature_Label.place(x=600, y=70, anchor=NW)
    default_value_Add4_Temperature = StringVar()
    default_value_Add4_Temperature.set('0')
    e_Add4_Temperature = tkinter.Entry(subroot, width=6, textvariable=default_value_Add4_Temperature)
    e_Add4_Temperature.pack()
    e_Add4_Temperature.place(x=720, y=70, anchor=NW)
    ###########################Add4正半母线电压########################################
    e_Add4_PFCvP_Label = tkinter.Label(subroot, text="正半母线电压")
    e_Add4_PFCvP_Label.pack()
    e_Add4_PFCvP_Label.place(x=600, y=90, anchor=NW)
    default_value_Add4_PFCvP = StringVar()
    default_value_Add4_PFCvP.set('0')
    e_Add4_PFCvP = tkinter.Entry(subroot, width=6, textvariable=default_value_Add4_PFCvP)
    e_Add4_PFCvP.pack()
    e_Add4_PFCvP.place(x=720, y=90, anchor=NW)
    ###########################Add4负半母线电压########################################
    e_Add4_PFCvN_Label = tkinter.Label(subroot, text="负半母线电压")
    e_Add4_PFCvN_Label.pack()
    e_Add4_PFCvN_Label.place(x=600, y=110, anchor=NW)
    default_value_Add4_PFCvN = StringVar()
    default_value_Add4_PFCvN.set('0')
    e_Add4_PFCvN = tkinter.Entry(subroot, width=6, textvariable=default_value_Add4_PFCvN)
    e_Add4_PFCvN.pack()
    e_Add4_PFCvN.place(x=720, y=110, anchor=NW)
    #############################输出过压################################
    Add4_chVarOutOverVoltage = tkinter.IntVar()
    Add4_check0 = tkinter.Checkbutton(subroot, text="输出过压", variable=Add4_chVarOutOverVoltage)
    Add4_check0.deselect()
    Add4_check0.place(x=600, y=130, anchor=NW)
    #############################过温################################
    Add4_chVarOverTemperature = tkinter.IntVar()
    Add4_check1 = tkinter.Checkbutton(subroot, text="过温", variable=Add4_chVarOverTemperature)
    Add4_check1.deselect()
    Add4_check1.place(x=600, y=150, anchor=NW)
    #############################模块故障################################
    Add4_chVarModuleFault = tkinter.IntVar()
    Add4_check2 = tkinter.Checkbutton(subroot, text="模块故障", variable=Add4_chVarModuleFault)
    Add4_check2.deselect()
    Add4_check2.place(x=600, y=170, anchor=NW)
    #############################模块保护################################
    Add4_chVarModuleProtect = tkinter.IntVar()
    Add4_check3 = tkinter.Checkbutton(subroot, text="模块保护", variable=Add4_chVarModuleProtect)
    Add4_check3.deselect()
    Add4_check3.place(x=600, y=190, anchor=NW)
    #############################风扇故障################################
    Add4_chVarFanFault = tkinter.IntVar()
    Add4_check4 = tkinter.Checkbutton(subroot, text="风扇故障", variable=Add4_chVarFanFault)
    Add4_check4.deselect()
    Add4_check4.place(x=600, y=210, anchor=NW)
    #############################模块EEPROM故障################################
    Add4_chVarEEPROMFault = tkinter.IntVar()
    Add4_check5 = tkinter.Checkbutton(subroot, text="模块EEPROM故障", variable=Add4_chVarEEPROMFault)
    Add4_check5.deselect()
    Add4_check5.place(x=600, y=230, anchor=NW)
    #############################交流限功率################################
    Add4_chVarACPowerLimit = tkinter.IntVar()
    Add4_check6 = tkinter.Checkbutton(subroot, text="交流限功率", variable=Add4_chVarACPowerLimit)
    Add4_check6.deselect()
    Add4_check6.place(x=600, y=250, anchor=NW)
    #############################温度限功率################################
    Add4_chVarTemPowerLimit = tkinter.IntVar()
    Add4_check7 = tkinter.Checkbutton(subroot, text="温度限功率", variable=Add4_chVarTemPowerLimit)
    Add4_check7.deselect()
    Add4_check7.place(x=600, y=270, anchor=NW)
    #############################模块限功率################################
    Add4_chVarModulePowerLimit = tkinter.IntVar()
    Add4_check8 = tkinter.Checkbutton(subroot, text="模块限功率", variable=Add4_chVarModulePowerLimit)
    Add4_check8.deselect()
    Add4_check8.place(x=600, y=290, anchor=NW)
    #############################待机状态################################
    Add4_chVarStandbyState = tkinter.IntVar()
    Add4_check9 = tkinter.Checkbutton(subroot, text="待机状态", variable=Add4_chVarStandbyState)
    Add4_check9.deselect()
    Add4_check9.place(x=600, y=310, anchor=NW)
    #############################风扇全速################################
    Add4_chVarFanFullSpeed = tkinter.IntVar()
    Add4_check10 = tkinter.Checkbutton(subroot, text="风扇全速", variable=Add4_chVarFanFullSpeed)
    Add4_check10.deselect()
    Add4_check10.place(x=600, y=330, anchor=NW)
    #############################模块WALK-In功能使能################################
    Add4_chVarModuleWalkInEbable = tkinter.IntVar()
    Add4_check11 = tkinter.Checkbutton(subroot, text="模块WALK-In功能使能", variable=Add4_chVarModuleWalkInEbable)
    Add4_check11.deselect()
    Add4_check11.place(x=600, y=350, anchor=NW)
    #############################PFC关机################################
    Add4_chVarPFCPowerOff = tkinter.IntVar()
    Add4_check12 = tkinter.Checkbutton(subroot, text="PFC关机", variable=Add4_chVarPFCPowerOff)
    Add4_check12.deselect()
    Add4_check12.place(x=600, y=370, anchor=NW)
    #############################模块识别################################
    Add4_chVarModuleRecognition = tkinter.IntVar()
    Add4_check13 = tkinter.Checkbutton(subroot, text="模块识别", variable=Add4_chVarModuleRecognition)
    Add4_check13.deselect()
    Add4_check13.place(x=600, y=390, anchor=NW)
    #############################模块电流均流故障################################
    Add4_chVarModuleCurrentMean = tkinter.IntVar()
    Add4_check14 = tkinter.Checkbutton(subroot, text="模块电流均流故障", variable=Add4_chVarModuleCurrentMean)
    Add4_check14.deselect()
    Add4_check14.place(x=600, y=410, anchor=NW)
    #############################模块CAN错误状态################################
    Add4_chVarModuleCANErrorState = tkinter.IntVar()
    Add4_check15 = tkinter.Checkbutton(subroot, text="模块CAN错误状态", variable=Add4_chVarModuleCANErrorState)
    Add4_check15.deselect()
    Add4_check15.place(x=600, y=430, anchor=NW)
    #############################模块顺序起机功能使能################################
    Add4_chVarModuleOrderOnEnable = tkinter.IntVar()
    Add4_check16 = tkinter.Checkbutton(subroot, text="模块顺序起机功能使能", variable=Add4_chVarModuleOrderOnEnable)
    Add4_check16.deselect()
    Add4_check16.place(x=600, y=450, anchor=NW)
    #############################模块输入欠压告警################################
    Add4_chVarModuleInputUVWarning = tkinter.IntVar()
    Add4_check17 = tkinter.Checkbutton(subroot, text="模块输入欠压告警", variable=Add4_chVarModuleInputUVWarning)
    Add4_check17.deselect()
    Add4_check17.place(x=600, y=470, anchor=NW)
    #############################模块交流不平衡告警################################
    Add4_chVarModuleACInbalanceWarning = tkinter.IntVar()
    Add4_check18 = tkinter.Checkbutton(subroot, text="模块交流不平衡告警", variable=Add4_chVarModuleACInbalanceWarning)
    Add4_check18.deselect()
    Add4_check18.place(x=600, y=490, anchor=NW)
    ############################模块交流缺相告警################################
    Add4_chVarModuleACPhaseLossWarning = tkinter.IntVar()
    Add4_check19 = tkinter.Checkbutton(subroot, text="模块交流缺相告警", variable=Add4_chVarModuleACPhaseLossWarning)
    Add4_check19.deselect()
    Add4_check19.place(x=600, y=510, anchor=NW)
    ############################模块直流母线欠压################################
    Add4_chVarModuleDCUV = tkinter.IntVar()
    Add4_check20 = tkinter.Checkbutton(subroot, text="模块直流母线欠压", variable=Add4_chVarModuleDCUV)
    Add4_check20.deselect()
    Add4_check20.place(x=600, y=530, anchor=NW)
    ############################模块ID重复################################
    Add4_chVarModuleIDRepet = tkinter.IntVar()
    Add4_check21 = tkinter.Checkbutton(subroot, text="模块ID重复", variable=Add4_chVarModuleIDRepet)
    Add4_check21.deselect()
    Add4_check21.place(x=600, y=550, anchor=NW)
    ############################模块输入过压################################
    Add4_chVarModuleInputOverVoltage = tkinter.IntVar()
    Add4_check22 = tkinter.Checkbutton(subroot, text="模块输入过压", variable=Add4_chVarModuleInputOverVoltage)
    Add4_check22.deselect()
    Add4_check22.place(x=600, y=570, anchor=NW)
    ############################模块PFC故障###############################
    Add4_chVarModulePFCFault = tkinter.IntVar()
    Add4_check23 = tkinter.Checkbutton(subroot, text="模块PFC故障", variable=Add4_chVarModulePFCFault)
    Add4_check23.deselect()
    Add4_check23.place(x=600, y=590, anchor=NW)
    ############################模块直流母线过压###############################
    Add4_chVarModuleDCOverVoltage = tkinter.IntVar()
    Add4_check24 = tkinter.Checkbutton(subroot, text="模块直流母线过压", variable=Add4_chVarModuleDCOverVoltage)
    Add4_check24.deselect()
    Add4_check24.place(x=600, y=610, anchor=NW)
    ############################模块插拔故障###############################
    Add4_chVarModulePlugFault = tkinter.IntVar()
    Add4_check25 = tkinter.Checkbutton(subroot, text="模块插拔故障", variable=Add4_chVarModulePlugFault)
    Add4_check25.deselect()
    Add4_check25.place(x=600, y=630, anchor=NW)
    ############################模块重载告警###############################
    Add4_chVarModuleReloadWarning = tkinter.IntVar()
    Add4_check26 = tkinter.Checkbutton(subroot, text="模块重载告警", variable=Add4_chVarModuleReloadWarning)
    Add4_check26.deselect()
    Add4_check26.place(x=600, y=650, anchor=NW)
    ############################模块输出欠压告警###############################
    Add4_chVarModuleOutUVWarning = tkinter.IntVar()
    Add4_check27 = tkinter.Checkbutton(subroot, text="模块输出欠压告警", variable=Add4_chVarModuleOutUVWarning)
    Add4_check27.deselect()
    Add4_check27.place(x=600, y=670, anchor=NW)
    ############################模块内部通讯异常告警###############################
    Add4_chVarModuleInternalComAbnormal = tkinter.IntVar()
    Add4_check28 = tkinter.Checkbutton(subroot, text="模块内部通讯异常告警", variable=Add4_chVarModuleInternalComAbnormal)
    Add4_check28.deselect()
    Add4_check28.place(x=600, y=690, anchor=NW)
    ############################模块输出熔丝断告警###############################
    Add4_chVarModuleOutFuseWarning = tkinter.IntVar()
    Add4_check29 = tkinter.Checkbutton(subroot, text="模块输出熔丝断告警", variable=Add4_chVarModuleOutFuseWarning)
    Add4_check29.deselect()
    Add4_check29.place(x=600, y=710, anchor=NW)

    e_moduledata5_Label = tkinter.Label(subroot, text="模块5数据", font=("Arial, 12"))
    e_moduledata5_Label.pack()
    e_moduledata5_Label.place(x=800, y=10, anchor=NW)
    ###########################Add5输出电压########################################
    e_Add5_OutVoltage_Label = tkinter.Label(subroot, text="模块5输出电压(0.1V)")
    e_Add5_OutVoltage_Label.pack()
    e_Add5_OutVoltage_Label.place(x=800, y=30, anchor=NW)
    default_value_Add5_OutVoltage = StringVar()
    default_value_Add5_OutVoltage.set('0')
    e_Add5_OutVoltage = tkinter.Entry(subroot, width=6, textvariable=default_value_Add5_OutVoltage)
    e_Add5_OutVoltage.pack()
    e_Add5_OutVoltage.place(x=920, y=30, anchor=NW)
    ###########################Add5输出电流########################################
    e_Add5_OutCurrent_Label = tkinter.Label(subroot, text="模块5输出电流(0.1A)")
    e_Add5_OutCurrent_Label.pack()
    e_Add5_OutCurrent_Label.place(x=800, y=50, anchor=NW)
    default_value_Add5_OutCurrent = StringVar()
    default_value_Add5_OutCurrent.set('0')
    e_Add5_OutCurrent = tkinter.Entry(subroot, width=6, textvariable=default_value_Add5_OutCurrent)
    e_Add5_OutCurrent.pack()
    e_Add5_OutCurrent.place(x=920, y=50, anchor=NW)
    ###########################Add5温度########################################
    e_Add5_Temperature_Label = tkinter.Label(subroot, text="模块5温度(0.1℃)")
    e_Add5_Temperature_Label.pack()
    e_Add5_Temperature_Label.place(x=800, y=70, anchor=NW)
    default_value_Add5_Temperature = StringVar()
    default_value_Add5_Temperature.set('0')
    e_Add5_Temperature = tkinter.Entry(subroot, width=6, textvariable=default_value_Add5_Temperature)
    e_Add5_Temperature.pack()
    e_Add5_Temperature.place(x=920, y=70, anchor=NW)
    ###########################Add5正半母线电压########################################
    e_Add5_PFCvP_Label = tkinter.Label(subroot, text="正半母线电压")
    e_Add5_PFCvP_Label.pack()
    e_Add5_PFCvP_Label.place(x=800, y=90, anchor=NW)
    default_value_Add5_PFCvP = StringVar()
    default_value_Add5_PFCvP.set('0')
    e_Add5_PFCvP = tkinter.Entry(subroot, width=6, textvariable=default_value_Add5_PFCvP)
    e_Add5_PFCvP.pack()
    e_Add5_PFCvP.place(x=920, y=90, anchor=NW)
    ###########################Add5负半母线电压########################################
    e_Add5_PFCvN_Label = tkinter.Label(subroot, text="负半母线电压")
    e_Add5_PFCvN_Label.pack()
    e_Add5_PFCvN_Label.place(x=800, y=110, anchor=NW)
    default_value_Add5_PFCvN = StringVar()
    default_value_Add5_PFCvN.set('0')
    e_Add5_PFCvN = tkinter.Entry(subroot, width=6, textvariable=default_value_Add5_PFCvN)
    e_Add5_PFCvN.pack()
    e_Add5_PFCvN.place(x=920, y=110, anchor=NW)
    #############################输出过压################################
    Add5_chVarOutOverVoltage = tkinter.IntVar()
    Add5_check0 = tkinter.Checkbutton(subroot, text="输出过压", variable=Add5_chVarOutOverVoltage)
    Add5_check0.deselect()
    Add5_check0.place(x=800, y=130, anchor=NW)
    #############################过温################################
    Add5_chVarOverTemperature = tkinter.IntVar()
    Add5_check1 = tkinter.Checkbutton(subroot, text="过温", variable=Add5_chVarOverTemperature)
    Add5_check1.deselect()
    Add5_check1.place(x=800, y=150, anchor=NW)
    #############################模块故障################################
    Add5_chVarModuleFault = tkinter.IntVar()
    Add5_check2 = tkinter.Checkbutton(subroot, text="模块故障", variable=Add5_chVarModuleFault)
    Add5_check2.deselect()
    Add5_check2.place(x=800, y=170, anchor=NW)
    #############################模块保护################################
    Add5_chVarModuleProtect = tkinter.IntVar()
    Add5_check3 = tkinter.Checkbutton(subroot, text="模块保护", variable=Add5_chVarModuleProtect)
    Add5_check3.deselect()
    Add5_check3.place(x=800, y=190, anchor=NW)
    #############################风扇故障################################
    Add5_chVarFanFault = tkinter.IntVar()
    Add5_check4 = tkinter.Checkbutton(subroot, text="风扇故障", variable=Add5_chVarFanFault)
    Add5_check4.deselect()
    Add5_check4.place(x=800, y=210, anchor=NW)
    #############################模块EEPROM故障################################
    Add5_chVarEEPROMFault = tkinter.IntVar()
    Add5_check5 = tkinter.Checkbutton(subroot, text="模块EEPROM故障", variable=Add5_chVarEEPROMFault)
    Add5_check5.deselect()
    Add5_check5.place(x=800, y=230, anchor=NW)
    #############################交流限功率################################
    Add5_chVarACPowerLimit = tkinter.IntVar()
    Add5_check6 = tkinter.Checkbutton(subroot, text="交流限功率", variable=Add5_chVarACPowerLimit)
    Add5_check6.deselect()
    Add5_check6.place(x=800, y=250, anchor=NW)
    #############################温度限功率################################
    Add5_chVarTemPowerLimit = tkinter.IntVar()
    Add5_check7 = tkinter.Checkbutton(subroot, text="温度限功率", variable=Add5_chVarTemPowerLimit)
    Add5_check7.deselect()
    Add5_check7.place(x=800, y=270, anchor=NW)
    #############################模块限功率################################
    Add5_chVarModulePowerLimit = tkinter.IntVar()
    Add5_check8 = tkinter.Checkbutton(subroot, text="模块限功率", variable=Add5_chVarModulePowerLimit)
    Add5_check8.deselect()
    Add5_check8.place(x=800, y=290, anchor=NW)
    #############################待机状态################################
    Add5_chVarStandbyState = tkinter.IntVar()
    Add5_check9 = tkinter.Checkbutton(subroot, text="待机状态", variable=Add5_chVarStandbyState)
    Add5_check9.deselect()
    Add5_check9.place(x=800, y=310, anchor=NW)
    #############################风扇全速################################
    Add5_chVarFanFullSpeed = tkinter.IntVar()
    Add5_check10 = tkinter.Checkbutton(subroot, text="风扇全速", variable=Add5_chVarFanFullSpeed)
    Add5_check10.deselect()
    Add5_check10.place(x=800, y=330, anchor=NW)
    #############################模块WALK-In功能使能################################
    Add5_chVarModuleWalkInEbable = tkinter.IntVar()
    Add5_check11 = tkinter.Checkbutton(subroot, text="模块WALK-In功能使能", variable=Add5_chVarModuleWalkInEbable)
    Add5_check11.deselect()
    Add5_check11.place(x=800, y=350, anchor=NW)
    #############################PFC关机################################
    Add5_chVarPFCPowerOff = tkinter.IntVar()
    Add5_check12 = tkinter.Checkbutton(subroot, text="PFC关机", variable=Add5_chVarPFCPowerOff)
    Add5_check12.deselect()
    Add5_check12.place(x=800, y=370, anchor=NW)
    #############################模块识别################################
    Add5_chVarModuleRecognition = tkinter.IntVar()
    Add5_check13 = tkinter.Checkbutton(subroot, text="模块识别", variable=Add5_chVarModuleRecognition)
    Add5_check13.deselect()
    Add5_check13.place(x=800, y=390, anchor=NW)
    #############################模块电流均流故障################################
    Add5_chVarModuleCurrentMean = tkinter.IntVar()
    Add5_check14 = tkinter.Checkbutton(subroot, text="模块电流均流故障", variable=Add5_chVarModuleCurrentMean)
    Add5_check14.deselect()
    Add5_check14.place(x=800, y=410, anchor=NW)
    #############################模块CAN错误状态################################
    Add5_chVarModuleCANErrorState = tkinter.IntVar()
    Add5_check15 = tkinter.Checkbutton(subroot, text="模块CAN错误状态", variable=Add5_chVarModuleCANErrorState)
    Add5_check15.deselect()
    Add5_check15.place(x=800, y=430, anchor=NW)
    #############################模块顺序起机功能使能################################
    Add5_chVarModuleOrderOnEnable = tkinter.IntVar()
    Add5_check16 = tkinter.Checkbutton(subroot, text="模块顺序起机功能使能", variable=Add5_chVarModuleOrderOnEnable)
    Add5_check16.deselect()
    Add5_check16.place(x=800, y=450, anchor=NW)
    #############################模块输入欠压告警################################
    Add5_chVarModuleInputUVWarning = tkinter.IntVar()
    Add5_check17 = tkinter.Checkbutton(subroot, text="模块输入欠压告警", variable=Add5_chVarModuleInputUVWarning)
    Add5_check17.deselect()
    Add5_check17.place(x=800, y=470, anchor=NW)
    #############################模块交流不平衡告警################################
    Add5_chVarModuleACInbalanceWarning = tkinter.IntVar()
    Add5_check18 = tkinter.Checkbutton(subroot, text="模块交流不平衡告警", variable=Add5_chVarModuleACInbalanceWarning)
    Add5_check18.deselect()
    Add5_check18.place(x=800, y=490, anchor=NW)
    ############################模块交流缺相告警################################
    Add5_chVarModuleACPhaseLossWarning = tkinter.IntVar()
    Add5_check19 = tkinter.Checkbutton(subroot, text="模块交流缺相告警", variable=Add5_chVarModuleACPhaseLossWarning)
    Add5_check19.deselect()
    Add5_check19.place(x=800, y=510, anchor=NW)
    ############################模块直流母线欠压################################
    Add5_chVarModuleDCUV = tkinter.IntVar()
    Add5_check20 = tkinter.Checkbutton(subroot, text="模块直流母线欠压", variable=Add5_chVarModuleDCUV)
    Add5_check20.deselect()
    Add5_check20.place(x=800, y=530, anchor=NW)
    ############################模块ID重复################################
    Add5_chVarModuleIDRepet = tkinter.IntVar()
    Add5_check21 = tkinter.Checkbutton(subroot, text="模块ID重复", variable=Add5_chVarModuleIDRepet)
    Add5_check21.deselect()
    Add5_check21.place(x=800, y=550, anchor=NW)
    ############################模块输入过压################################
    Add5_chVarModuleInputOverVoltage = tkinter.IntVar()
    Add5_check22 = tkinter.Checkbutton(subroot, text="模块输入过压", variable=Add5_chVarModuleInputOverVoltage)
    Add5_check22.deselect()
    Add5_check22.place(x=800, y=570, anchor=NW)
    ############################模块PFC故障###############################
    Add5_chVarModulePFCFault = tkinter.IntVar()
    Add5_check23 = tkinter.Checkbutton(subroot, text="模块PFC故障", variable=Add5_chVarModulePFCFault)
    Add5_check23.deselect()
    Add5_check23.place(x=800, y=590, anchor=NW)
    ############################模块直流母线过压###############################
    Add5_chVarModuleDCOverVoltage = tkinter.IntVar()
    Add5_check24 = tkinter.Checkbutton(subroot, text="模块直流母线过压", variable=Add5_chVarModuleDCOverVoltage)
    Add5_check24.deselect()
    Add5_check24.place(x=800, y=610, anchor=NW)
    ############################模块插拔故障###############################
    Add5_chVarModulePlugFault = tkinter.IntVar()
    Add5_check25 = tkinter.Checkbutton(subroot, text="模块插拔故障", variable=Add5_chVarModulePlugFault)
    Add5_check25.deselect()
    Add5_check25.place(x=800, y=630, anchor=NW)
    ############################模块重载告警###############################
    Add5_chVarModuleReloadWarning = tkinter.IntVar()
    Add5_check26 = tkinter.Checkbutton(subroot, text="模块重载告警", variable=Add5_chVarModuleReloadWarning)
    Add5_check26.deselect()
    Add5_check26.place(x=800, y=650, anchor=NW)
    ############################模块输出欠压告警###############################
    Add5_chVarModuleOutUVWarning = tkinter.IntVar()
    Add5_check27 = tkinter.Checkbutton(subroot, text="模块输出欠压告警", variable=Add5_chVarModuleOutUVWarning)
    Add5_check27.deselect()
    Add5_check27.place(x=800, y=670, anchor=NW)
    ############################模块内部通讯异常告警###############################
    Add5_chVarModuleInternalComAbnormal = tkinter.IntVar()
    Add5_check28 = tkinter.Checkbutton(subroot, text="模块内部通讯异常告警", variable=Add5_chVarModuleInternalComAbnormal)
    Add5_check28.deselect()
    Add5_check28.place(x=800, y=690, anchor=NW)
    ############################模块输出熔丝断告警###############################
    Add5_chVarModuleOutFuseWarning = tkinter.IntVar()
    Add5_check29 = tkinter.Checkbutton(subroot, text="模块输出熔丝断告警", variable=Add5_chVarModuleOutFuseWarning)
    Add5_check29.deselect()
    Add5_check29.place(x=800, y=710, anchor=NW)

    e_moduledata6_Label = tkinter.Label(subroot, text="模块6数据", font=("Arial, 12"))
    e_moduledata6_Label.pack()
    e_moduledata6_Label.place(x=1000, y=10, anchor=NW)
    ###########################Add6输出电压########################################
    e_Add6_OutVoltage_Label = tkinter.Label(subroot, text="模块6输出电压(0.1V)")
    e_Add6_OutVoltage_Label.pack()
    e_Add6_OutVoltage_Label.place(x=1000, y=30, anchor=NW)
    default_value_Add6_OutVoltage = StringVar()
    default_value_Add6_OutVoltage.set('0')
    e_Add6_OutVoltage = tkinter.Entry(subroot, width=6, textvariable=default_value_Add6_OutVoltage)
    e_Add6_OutVoltage.pack()
    e_Add6_OutVoltage.place(x=1120, y=30, anchor=NW)
    ###########################Add6输出电流########################################
    e_Add6_OutCurrent_Label = tkinter.Label(subroot, text="模块6输出电流(0.1A)")
    e_Add6_OutCurrent_Label.pack()
    e_Add6_OutCurrent_Label.place(x=1000, y=50, anchor=NW)
    default_value_Add6_OutCurrent = StringVar()
    default_value_Add6_OutCurrent.set('0')
    e_Add6_OutCurrent = tkinter.Entry(subroot, width=6, textvariable=default_value_Add6_OutCurrent)
    e_Add6_OutCurrent.pack()
    e_Add6_OutCurrent.place(x=1120, y=50, anchor=NW)
    ###########################Add6温度########################################
    e_Add6_Temperature_Label = tkinter.Label(subroot, text="模块6温度(0.1℃)")
    e_Add6_Temperature_Label.pack()
    e_Add6_Temperature_Label.place(x=1000, y=70, anchor=NW)
    default_value_Add6_Temperature = StringVar()
    default_value_Add6_Temperature.set('0')
    e_Add6_Temperature = tkinter.Entry(subroot, width=6, textvariable=default_value_Add6_Temperature)
    e_Add6_Temperature.pack()
    e_Add6_Temperature.place(x=1120, y=70, anchor=NW)
    ###########################Add6正半母线电压########################################
    e_Add6_PFCvP_Label = tkinter.Label(subroot, text="正半母线电压")
    e_Add6_PFCvP_Label.pack()
    e_Add6_PFCvP_Label.place(x=1000, y=90, anchor=NW)
    default_value_Add6_PFCvP = StringVar()
    default_value_Add6_PFCvP.set('0')
    e_Add6_PFCvP = tkinter.Entry(subroot, width=6, textvariable=default_value_Add6_PFCvP)
    e_Add6_PFCvP.pack()
    e_Add6_PFCvP.place(x=1120, y=90, anchor=NW)
    ###########################Add6负半母线电压########################################
    e_Add6_PFCvN_Label = tkinter.Label(subroot, text="负半母线电压")
    e_Add6_PFCvN_Label.pack()
    e_Add6_PFCvN_Label.place(x=1000, y=110, anchor=NW)
    default_value_Add6_PFCvN = StringVar()
    default_value_Add6_PFCvN.set('0')
    e_Add6_PFCvN = tkinter.Entry(subroot, width=6, textvariable=default_value_Add6_PFCvN)
    e_Add6_PFCvN.pack()
    e_Add6_PFCvN.place(x=1120, y=110, anchor=NW)
    #############################输出过压################################
    Add6_chVarOutOverVoltage = tkinter.IntVar()
    Add6_check0 = tkinter.Checkbutton(subroot, text="输出过压", variable=Add6_chVarOutOverVoltage)
    Add6_check0.deselect()
    Add6_check0.place(x=1000, y=130, anchor=NW)
    #############################过温################################
    Add6_chVarOverTemperature = tkinter.IntVar()
    Add6_check1 = tkinter.Checkbutton(subroot, text="过温", variable=Add6_chVarOverTemperature)
    Add6_check1.deselect()
    Add6_check1.place(x=1000, y=150, anchor=NW)
    #############################模块故障################################
    Add6_chVarModuleFault = tkinter.IntVar()
    Add6_check2 = tkinter.Checkbutton(subroot, text="模块故障", variable=Add6_chVarModuleFault)
    Add6_check2.deselect()
    Add6_check2.place(x=1000, y=170, anchor=NW)
    #############################模块保护################################
    Add6_chVarModuleProtect = tkinter.IntVar()
    Add6_check3 = tkinter.Checkbutton(subroot, text="模块保护", variable=Add6_chVarModuleProtect)
    Add6_check3.deselect()
    Add6_check3.place(x=1000, y=190, anchor=NW)
    #############################风扇故障################################
    Add6_chVarFanFault = tkinter.IntVar()
    Add6_check4 = tkinter.Checkbutton(subroot, text="风扇故障", variable=Add6_chVarFanFault)
    Add6_check4.deselect()
    Add6_check4.place(x=1000, y=210, anchor=NW)
    #############################模块EEPROM故障################################
    Add6_chVarEEPROMFault = tkinter.IntVar()
    Add6_check5 = tkinter.Checkbutton(subroot, text="模块EEPROM故障", variable=Add6_chVarEEPROMFault)
    Add6_check5.deselect()
    Add6_check5.place(x=1000, y=230, anchor=NW)
    #############################交流限功率################################
    Add6_chVarACPowerLimit = tkinter.IntVar()
    Add6_check6 = tkinter.Checkbutton(subroot, text="交流限功率", variable=Add6_chVarACPowerLimit)
    Add6_check6.deselect()
    Add6_check6.place(x=1000, y=250, anchor=NW)
    #############################温度限功率################################
    Add6_chVarTemPowerLimit = tkinter.IntVar()
    Add6_check7 = tkinter.Checkbutton(subroot, text="温度限功率", variable=Add6_chVarTemPowerLimit)
    Add6_check7.deselect()
    Add6_check7.place(x=1000, y=270, anchor=NW)
    #############################模块限功率################################
    Add6_chVarModulePowerLimit = tkinter.IntVar()
    Add6_check8 = tkinter.Checkbutton(subroot, text="模块限功率", variable=Add6_chVarModulePowerLimit)
    Add6_check8.deselect()
    Add6_check8.place(x=1000, y=290, anchor=NW)
    #############################待机状态################################
    Add6_chVarStandbyState = tkinter.IntVar()
    Add6_check9 = tkinter.Checkbutton(subroot, text="待机状态", variable=Add6_chVarStandbyState)
    Add6_check9.deselect()
    Add6_check9.place(x=1000, y=310, anchor=NW)
    #############################风扇全速################################
    Add6_chVarFanFullSpeed = tkinter.IntVar()
    Add6_check10 = tkinter.Checkbutton(subroot, text="风扇全速", variable=Add6_chVarFanFullSpeed)
    Add6_check10.deselect()
    Add6_check10.place(x=1000, y=330, anchor=NW)
    #############################模块WALK-In功能使能################################
    Add6_chVarModuleWalkInEbable = tkinter.IntVar()
    Add6_check11 = tkinter.Checkbutton(subroot, text="模块WALK-In功能使能", variable=Add6_chVarModuleWalkInEbable)
    Add6_check11.deselect()
    Add6_check11.place(x=1000, y=350, anchor=NW)
    #############################PFC关机################################
    Add6_chVarPFCPowerOff = tkinter.IntVar()
    Add6_check12 = tkinter.Checkbutton(subroot, text="PFC关机", variable=Add6_chVarPFCPowerOff)
    Add6_check12.deselect()
    Add6_check12.place(x=1000, y=370, anchor=NW)
    #############################模块识别################################
    Add6_chVarModuleRecognition = tkinter.IntVar()
    Add6_check13 = tkinter.Checkbutton(subroot, text="模块识别", variable=Add6_chVarModuleRecognition)
    Add6_check13.deselect()
    Add6_check13.place(x=1000, y=390, anchor=NW)
    #############################模块电流均流故障################################
    Add6_chVarModuleCurrentMean = tkinter.IntVar()
    Add6_check14 = tkinter.Checkbutton(subroot, text="模块电流均流故障", variable=Add6_chVarModuleCurrentMean)
    Add6_check14.deselect()
    Add6_check14.place(x=1000, y=410, anchor=NW)
    #############################模块CAN错误状态################################
    Add6_chVarModuleCANErrorState = tkinter.IntVar()
    Add6_check15 = tkinter.Checkbutton(subroot, text="模块CAN错误状态", variable=Add6_chVarModuleCANErrorState)
    Add6_check15.deselect()
    Add6_check15.place(x=1000, y=430, anchor=NW)
    #############################模块顺序起机功能使能################################
    Add6_chVarModuleOrderOnEnable = tkinter.IntVar()
    Add6_check16 = tkinter.Checkbutton(subroot, text="模块顺序起机功能使能", variable=Add6_chVarModuleOrderOnEnable)
    Add6_check16.deselect()
    Add6_check16.place(x=1000, y=450, anchor=NW)
    #############################模块输入欠压告警################################
    Add6_chVarModuleInputUVWarning = tkinter.IntVar()
    Add6_check17 = tkinter.Checkbutton(subroot, text="模块输入欠压告警", variable=Add6_chVarModuleInputUVWarning)
    Add6_check17.deselect()
    Add6_check17.place(x=1000, y=470, anchor=NW)
    #############################模块交流不平衡告警################################
    Add6_chVarModuleACInbalanceWarning = tkinter.IntVar()
    Add6_check18 = tkinter.Checkbutton(subroot, text="模块交流不平衡告警", variable=Add6_chVarModuleACInbalanceWarning)
    Add6_check18.deselect()
    Add6_check18.place(x=1000, y=490, anchor=NW)
    ############################模块交流缺相告警################################
    Add6_chVarModuleACPhaseLossWarning = tkinter.IntVar()
    Add6_check19 = tkinter.Checkbutton(subroot, text="模块交流缺相告警", variable=Add6_chVarModuleACPhaseLossWarning)
    Add6_check19.deselect()
    Add6_check19.place(x=1000, y=510, anchor=NW)
    ############################模块直流母线欠压################################
    Add6_chVarModuleDCUV = tkinter.IntVar()
    Add6_check20 = tkinter.Checkbutton(subroot, text="模块直流母线欠压", variable=Add6_chVarModuleDCUV)
    Add6_check20.deselect()
    Add6_check20.place(x=1000, y=530, anchor=NW)
    ############################模块ID重复################################
    Add6_chVarModuleIDRepet = tkinter.IntVar()
    Add6_check21 = tkinter.Checkbutton(subroot, text="模块ID重复", variable=Add6_chVarModuleIDRepet)
    Add6_check21.deselect()
    Add6_check21.place(x=1000, y=550, anchor=NW)
    ############################模块输入过压################################
    Add6_chVarModuleInputOverVoltage = tkinter.IntVar()
    Add6_check22 = tkinter.Checkbutton(subroot, text="模块输入过压", variable=Add6_chVarModuleInputOverVoltage)
    Add6_check22.deselect()
    Add6_check22.place(x=1000, y=570, anchor=NW)
    ############################模块PFC故障###############################
    Add6_chVarModulePFCFault = tkinter.IntVar()
    Add6_check23 = tkinter.Checkbutton(subroot, text="模块PFC故障", variable=Add6_chVarModulePFCFault)
    Add6_check23.deselect()
    Add6_check23.place(x=1000, y=590, anchor=NW)
    ############################模块直流母线过压###############################
    Add6_chVarModuleDCOverVoltage = tkinter.IntVar()
    Add6_check24 = tkinter.Checkbutton(subroot, text="模块直流母线过压", variable=Add6_chVarModuleDCOverVoltage)
    Add6_check24.deselect()
    Add6_check24.place(x=1000, y=610, anchor=NW)
    ############################模块插拔故障###############################
    Add6_chVarModulePlugFault = tkinter.IntVar()
    Add6_check25 = tkinter.Checkbutton(subroot, text="模块插拔故障", variable=Add6_chVarModulePlugFault)
    Add6_check25.deselect()
    Add6_check25.place(x=1000, y=630, anchor=NW)
    ############################模块重载告警###############################
    Add6_chVarModuleReloadWarning = tkinter.IntVar()
    Add6_check26 = tkinter.Checkbutton(subroot, text="模块重载告警", variable=Add6_chVarModuleReloadWarning)
    Add6_check26.deselect()
    Add6_check26.place(x=1000, y=650, anchor=NW)
    ############################模块输出欠压告警###############################
    Add6_chVarModuleOutUVWarning = tkinter.IntVar()
    Add6_check27 = tkinter.Checkbutton(subroot, text="模块输出欠压告警", variable=Add6_chVarModuleOutUVWarning)
    Add6_check27.deselect()
    Add6_check27.place(x=1000, y=670, anchor=NW)
    ############################模块内部通讯异常告警###############################
    Add6_chVarModuleInternalComAbnormal = tkinter.IntVar()
    Add6_check28 = tkinter.Checkbutton(subroot, text="模块内部通讯异常告警", variable=Add6_chVarModuleInternalComAbnormal)
    Add6_check28.deselect()
    Add6_check28.place(x=1000, y=690, anchor=NW)
    ############################模块输出熔丝断告警###############################
    Add6_chVarModuleOutFuseWarning = tkinter.IntVar()
    Add6_check29 = tkinter.Checkbutton(subroot, text="模块输出熔丝断告警", variable=Add6_chVarModuleOutFuseWarning)
    Add6_check29.deselect()
    Add6_check29.place(x=1000, y=710, anchor=NW)

    e_moduledata7_Label = tkinter.Label(subroot, text="模块7数据", font=("Arial, 12"))
    e_moduledata7_Label.pack()
    e_moduledata7_Label.place(x=1200, y=10, anchor=NW)
    ###########################Add7输出电压########################################
    e_Add7_OutVoltage_Label = tkinter.Label(subroot, text="模块7输出电压(0.1V)")
    e_Add7_OutVoltage_Label.pack()
    e_Add7_OutVoltage_Label.place(x=1200, y=30, anchor=NW)
    default_value_Add7_OutVoltage = StringVar()
    default_value_Add7_OutVoltage.set('0')
    e_Add7_OutVoltage = tkinter.Entry(subroot, width=6, textvariable=default_value_Add7_OutVoltage)
    e_Add7_OutVoltage.pack()
    e_Add7_OutVoltage.place(x=1320, y=30, anchor=NW)
    ###########################Add7输出电流########################################
    e_Add7_OutCurrent_Label = tkinter.Label(subroot, text="模块7输出电流(0.1A)")
    e_Add7_OutCurrent_Label.pack()
    e_Add7_OutCurrent_Label.place(x=1200, y=50, anchor=NW)
    default_value_Add7_OutCurrent = StringVar()
    default_value_Add7_OutCurrent.set('0')
    e_Add7_OutCurrent = tkinter.Entry(subroot, width=6, textvariable=default_value_Add7_OutCurrent)
    e_Add7_OutCurrent.pack()
    e_Add7_OutCurrent.place(x=1320, y=50, anchor=NW)
    ###########################Add7温度########################################
    e_Add7_Temperature_Label = tkinter.Label(subroot, text="模块7温度(0.1℃)")
    e_Add7_Temperature_Label.pack()
    e_Add7_Temperature_Label.place(x=1200, y=70, anchor=NW)
    default_value_Add7_Temperature = StringVar()
    default_value_Add7_Temperature.set('0')
    e_Add7_Temperature = tkinter.Entry(subroot, width=6, textvariable=default_value_Add7_Temperature)
    e_Add7_Temperature.pack()
    e_Add7_Temperature.place(x=1320, y=70, anchor=NW)
    ###########################Add7正半母线电压########################################
    e_Add7_PFCvP_Label = tkinter.Label(subroot, text="正半母线电压")
    e_Add7_PFCvP_Label.pack()
    e_Add7_PFCvP_Label.place(x=1200, y=90, anchor=NW)
    default_value_Add7_PFCvP = StringVar()
    default_value_Add7_PFCvP.set('0')
    e_Add7_PFCvP = tkinter.Entry(subroot, width=6, textvariable=default_value_Add7_PFCvP)
    e_Add7_PFCvP.pack()
    e_Add7_PFCvP.place(x=1320, y=90, anchor=NW)
    ###########################Add7负半母线电压########################################
    e_Add7_PFCvN_Label = tkinter.Label(subroot, text="负半母线电压")
    e_Add7_PFCvN_Label.pack()
    e_Add7_PFCvN_Label.place(x=1200, y=110, anchor=NW)
    default_value_Add7_PFCvN = StringVar()
    default_value_Add7_PFCvN.set('0')
    e_Add7_PFCvN = tkinter.Entry(subroot, width=6, textvariable=default_value_Add7_PFCvN)
    e_Add7_PFCvN.pack()
    e_Add7_PFCvN.place(x=1320, y=110, anchor=NW)
    #############################输出过压################################
    Add7_chVarOutOverVoltage = tkinter.IntVar()
    Add7_check0 = tkinter.Checkbutton(subroot, text="输出过压", variable=Add7_chVarOutOverVoltage)
    Add7_check0.deselect()
    Add7_check0.place(x=1200, y=130, anchor=NW)
    #############################过温################################
    Add7_chVarOverTemperature = tkinter.IntVar()
    Add7_check1 = tkinter.Checkbutton(subroot, text="过温", variable=Add7_chVarOverTemperature)
    Add7_check1.deselect()
    Add7_check1.place(x=1200, y=150, anchor=NW)
    #############################模块故障################################
    Add7_chVarModuleFault = tkinter.IntVar()
    Add7_check2 = tkinter.Checkbutton(subroot, text="模块故障", variable=Add7_chVarModuleFault)
    Add7_check2.deselect()
    Add7_check2.place(x=1200, y=170, anchor=NW)
    #############################模块保护################################
    Add7_chVarModuleProtect = tkinter.IntVar()
    Add7_check3 = tkinter.Checkbutton(subroot, text="模块保护", variable=Add7_chVarModuleProtect)
    Add7_check3.deselect()
    Add7_check3.place(x=1200, y=190, anchor=NW)
    #############################风扇故障################################
    Add7_chVarFanFault = tkinter.IntVar()
    Add7_check4 = tkinter.Checkbutton(subroot, text="风扇故障", variable=Add7_chVarFanFault)
    Add7_check4.deselect()
    Add7_check4.place(x=1200, y=210, anchor=NW)
    #############################模块EEPROM故障################################
    Add7_chVarEEPROMFault = tkinter.IntVar()
    Add7_check5 = tkinter.Checkbutton(subroot, text="模块EEPROM故障", variable=Add7_chVarEEPROMFault)
    Add7_check5.deselect()
    Add7_check5.place(x=1200, y=230, anchor=NW)
    #############################交流限功率################################
    Add7_chVarACPowerLimit = tkinter.IntVar()
    Add7_check6 = tkinter.Checkbutton(subroot, text="交流限功率", variable=Add7_chVarACPowerLimit)
    Add7_check6.deselect()
    Add7_check6.place(x=1200, y=250, anchor=NW)
    #############################温度限功率################################
    Add7_chVarTemPowerLimit = tkinter.IntVar()
    Add7_check7 = tkinter.Checkbutton(subroot, text="温度限功率", variable=Add7_chVarTemPowerLimit)
    Add7_check7.deselect()
    Add7_check7.place(x=1200, y=270, anchor=NW)
    #############################模块限功率################################
    Add7_chVarModulePowerLimit = tkinter.IntVar()
    Add7_check8 = tkinter.Checkbutton(subroot, text="模块限功率", variable=Add7_chVarModulePowerLimit)
    Add7_check8.deselect()
    Add7_check8.place(x=1200, y=290, anchor=NW)
    #############################待机状态################################
    Add7_chVarStandbyState = tkinter.IntVar()
    Add7_check9 = tkinter.Checkbutton(subroot, text="待机状态", variable=Add7_chVarStandbyState)
    Add7_check9.deselect()
    Add7_check9.place(x=1200, y=310, anchor=NW)
    #############################风扇全速################################
    Add7_chVarFanFullSpeed = tkinter.IntVar()
    Add7_check10 = tkinter.Checkbutton(subroot, text="风扇全速", variable=Add7_chVarFanFullSpeed)
    Add7_check10.deselect()
    Add7_check10.place(x=1200, y=330, anchor=NW)
    #############################模块WALK-In功能使能################################
    Add7_chVarModuleWalkInEbable = tkinter.IntVar()
    Add7_check11 = tkinter.Checkbutton(subroot, text="模块WALK-In功能使能", variable=Add7_chVarModuleWalkInEbable)
    Add7_check11.deselect()
    Add7_check11.place(x=1200, y=350, anchor=NW)
    #############################PFC关机################################
    Add7_chVarPFCPowerOff = tkinter.IntVar()
    Add7_check12 = tkinter.Checkbutton(subroot, text="PFC关机", variable=Add7_chVarPFCPowerOff)
    Add7_check12.deselect()
    Add7_check12.place(x=1200, y=370, anchor=NW)
    #############################模块识别################################
    Add7_chVarModuleRecognition = tkinter.IntVar()
    Add7_check13 = tkinter.Checkbutton(subroot, text="模块识别", variable=Add7_chVarModuleRecognition)
    Add7_check13.deselect()
    Add7_check13.place(x=1200, y=390, anchor=NW)
    #############################模块电流均流故障################################
    Add7_chVarModuleCurrentMean = tkinter.IntVar()
    Add7_check14 = tkinter.Checkbutton(subroot, text="模块电流均流故障", variable=Add7_chVarModuleCurrentMean)
    Add7_check14.deselect()
    Add7_check14.place(x=1200, y=410, anchor=NW)
    #############################模块CAN错误状态################################
    Add7_chVarModuleCANErrorState = tkinter.IntVar()
    Add7_check15 = tkinter.Checkbutton(subroot, text="模块CAN错误状态", variable=Add7_chVarModuleCANErrorState)
    Add7_check15.deselect()
    Add7_check15.place(x=1200, y=430, anchor=NW)
    #############################模块顺序起机功能使能################################
    Add7_chVarModuleOrderOnEnable = tkinter.IntVar()
    Add7_check16 = tkinter.Checkbutton(subroot, text="模块顺序起机功能使能", variable=Add7_chVarModuleOrderOnEnable)
    Add7_check16.deselect()
    Add7_check16.place(x=1200, y=450, anchor=NW)
    #############################模块输入欠压告警################################
    Add7_chVarModuleInputUVWarning = tkinter.IntVar()
    Add7_check17 = tkinter.Checkbutton(subroot, text="模块输入欠压告警", variable=Add7_chVarModuleInputUVWarning)
    Add7_check17.deselect()
    Add7_check17.place(x=1200, y=470, anchor=NW)
    #############################模块交流不平衡告警################################
    Add7_chVarModuleACInbalanceWarning = tkinter.IntVar()
    Add7_check18 = tkinter.Checkbutton(subroot, text="模块交流不平衡告警", variable=Add7_chVarModuleACInbalanceWarning)
    Add7_check18.deselect()
    Add7_check18.place(x=1200, y=490, anchor=NW)
    ############################模块交流缺相告警################################
    Add7_chVarModuleACPhaseLossWarning = tkinter.IntVar()
    Add7_check19 = tkinter.Checkbutton(subroot, text="模块交流缺相告警", variable=Add7_chVarModuleACPhaseLossWarning)
    Add7_check19.deselect()
    Add7_check19.place(x=1200, y=510, anchor=NW)
    ############################模块直流母线欠压################################
    Add7_chVarModuleDCUV = tkinter.IntVar()
    Add7_check20 = tkinter.Checkbutton(subroot, text="模块直流母线欠压", variable=Add7_chVarModuleDCUV)
    Add7_check20.deselect()
    Add7_check20.place(x=1200, y=530, anchor=NW)
    ############################模块ID重复################################
    Add7_chVarModuleIDRepet = tkinter.IntVar()
    Add7_check21 = tkinter.Checkbutton(subroot, text="模块ID重复", variable=Add7_chVarModuleIDRepet)
    Add7_check21.deselect()
    Add7_check21.place(x=1200, y=550, anchor=NW)
    ############################模块输入过压################################
    Add7_chVarModuleInputOverVoltage = tkinter.IntVar()
    Add7_check22 = tkinter.Checkbutton(subroot, text="模块输入过压", variable=Add7_chVarModuleInputOverVoltage)
    Add7_check22.deselect()
    Add7_check22.place(x=1200, y=570, anchor=NW)
    ############################模块PFC故障###############################
    Add7_chVarModulePFCFault = tkinter.IntVar()
    Add7_check23 = tkinter.Checkbutton(subroot, text="模块PFC故障", variable=Add7_chVarModulePFCFault)
    Add7_check23.deselect()
    Add7_check23.place(x=1200, y=590, anchor=NW)
    ############################模块直流母线过压###############################
    Add7_chVarModuleDCOverVoltage = tkinter.IntVar()
    Add7_check24 = tkinter.Checkbutton(subroot, text="模块直流母线过压", variable=Add7_chVarModuleDCOverVoltage)
    Add7_check24.deselect()
    Add7_check24.place(x=1200, y=610, anchor=NW)
    ############################模块插拔故障###############################
    Add7_chVarModulePlugFault = tkinter.IntVar()
    Add7_check25 = tkinter.Checkbutton(subroot, text="模块插拔故障", variable=Add7_chVarModulePlugFault)
    Add7_check25.deselect()
    Add7_check25.place(x=1200, y=630, anchor=NW)
    ############################模块重载告警###############################
    Add7_chVarModuleReloadWarning = tkinter.IntVar()
    Add7_check26 = tkinter.Checkbutton(subroot, text="模块重载告警", variable=Add7_chVarModuleReloadWarning)
    Add7_check26.deselect()
    Add7_check26.place(x=1200, y=650, anchor=NW)
    ############################模块输出欠压告警###############################
    Add7_chVarModuleOutUVWarning = tkinter.IntVar()
    Add7_check27 = tkinter.Checkbutton(subroot, text="模块输出欠压告警", variable=Add7_chVarModuleOutUVWarning)
    Add7_check27.deselect()
    Add7_check27.place(x=1200, y=670, anchor=NW)
    ############################模块内部通讯异常告警###############################
    Add7_chVarModuleInternalComAbnormal = tkinter.IntVar()
    Add7_check28 = tkinter.Checkbutton(subroot, text="模块内部通讯异常告警", variable=Add7_chVarModuleInternalComAbnormal)
    Add7_check28.deselect()
    Add7_check28.place(x=1200, y=690, anchor=NW)
    ############################模块输出熔丝断告警###############################
    Add7_chVarModuleOutFuseWarning = tkinter.IntVar()
    Add7_check29 = tkinter.Checkbutton(subroot, text="模块输出熔丝断告警", variable=Add7_chVarModuleOutFuseWarning)
    Add7_check29.deselect()
    Add7_check29.place(x=1200, y=710, anchor=NW)

    def getdata():
        try:
            moduledata_list[0][0] = int(float(e_Add1_OutVoltage.get()) * 10) % 256
            moduledata_list[0][1] = int(float(e_Add1_OutVoltage.get()) * 10) // 256
            moduledata_list[0][2] = int(float(e_Add1_OutCurrent.get()) * 10) % 256
            moduledata_list[0][3] = int(float(e_Add1_OutCurrent.get()) * 10) // 256
            moduledata_list[0][4] = int(float(e_Add1_Temperature.get()) * 10) % 256
            moduledata_list[0][5] = int(float(e_Add1_Temperature.get()) * 10) // 256
            moduledata_list[0][6] = Add1_chVarOutOverVoltage.get() * 128 + Add1_chVarOverTemperature.get() * 64 \
                                    + Add1_chVarModuleFault.get() * 32 + Add1_chVarModuleProtect.get() * 16 + \
                                    Add1_chVarFanFault.get() * 8 + Add1_chVarEEPROMFault.get() * 4 + \
                                    Add1_chVarACPowerLimit.get() * 2 + Add1_chVarTemPowerLimit.get()
            moduledata_list[1][0] = int(float(e_Add1_PFCvP.get()) * 10) % 256
            moduledata_list[1][1] = int(float(e_Add1_PFCvP.get()) * 10) // 256
            moduledata_list[1][2] = int(float(e_Add1_PFCvN.get()) * 10) % 256
            moduledata_list[1][3] = int(float(e_Add1_PFCvN.get()) * 10) // 256
            moduledata_list[1][4] = Add1_chVarModuleDCOverVoltage.get() * 128 + Add1_chVarModulePlugFault.get() * 64 \
                                    + Add1_chVarModuleReloadWarning.get() * 32 + Add1_chVarModuleOutUVWarning.get() * 16 + \
                                    Add1_chVarModuleInternalComAbnormal.get() * 8 + Add1_chVarModuleOutFuseWarning.get() * 4
            moduledata_list[1][5] = Add1_chVarModuleOrderOnEnable.get() * 128 + Add1_chVarModuleInputUVWarning.get() * 64 \
                                    + Add1_chVarModuleACInbalanceWarning.get() * 32 + Add1_chVarModuleACPhaseLossWarning.get() * 16 + \
                                    Add1_chVarModuleDCUV.get() * 8 + Add1_chVarModuleIDRepet.get() * 4 + \
                                    Add1_chVarModuleInputOverVoltage.get() * 2 + Add1_chVarModulePFCFault.get()
            moduledata_list[1][6] = Add1_chVarModulePowerLimit.get() * 128 + Add1_chVarStandbyState.get() * 64 \
                                    + Add1_chVarFanFullSpeed.get() * 32 + Add1_chVarModuleWalkInEbable.get() * 16 + \
                                    Add1_chVarPFCPowerOff.get() * 8 + Add1_chVarModuleRecognition.get() * 4 + \
                                    Add1_chVarModuleCurrentMean.get() * 2 + Add1_chVarModuleCANErrorState.get()

            moduledata_list[2][0] = int(float(e_Add2_OutVoltage.get()) * 10) % 256
            moduledata_list[2][1] = int(float(e_Add2_OutVoltage.get()) * 10) // 256
            moduledata_list[2][2] = int(float(e_Add2_OutCurrent.get()) * 10) % 256
            moduledata_list[2][3] = int(float(e_Add2_OutCurrent.get()) * 10) // 256
            moduledata_list[2][4] = int(float(e_Add2_Temperature.get()) * 10) % 256
            moduledata_list[2][5] = int(float(e_Add2_Temperature.get()) * 10) // 256
            moduledata_list[2][6] = Add2_chVarOutOverVoltage.get() * 128 + Add2_chVarOverTemperature.get() * 64 \
                                    + Add2_chVarModuleFault.get() * 32 + Add2_chVarModuleProtect.get() * 16 + \
                                    Add2_chVarFanFault.get() * 8 + Add2_chVarEEPROMFault.get() * 4 + \
                                    Add2_chVarACPowerLimit.get() * 2 + Add2_chVarTemPowerLimit.get()
            moduledata_list[3][0] = int(float(e_Add2_PFCvP.get()) * 10) % 256
            moduledata_list[3][1] = int(float(e_Add2_PFCvP.get()) * 10) // 256
            moduledata_list[3][2] = int(float(e_Add2_PFCvN.get()) * 10) % 256
            moduledata_list[3][3] = int(float(e_Add2_PFCvN.get()) * 10) // 256
            moduledata_list[3][4] = Add2_chVarModuleDCOverVoltage.get() * 128 + Add2_chVarModulePlugFault.get() * 64 \
                                    + Add2_chVarModuleReloadWarning.get() * 32 + Add2_chVarModuleOutUVWarning.get() * 16 + \
                                    Add2_chVarModuleInternalComAbnormal.get() * 8 + Add2_chVarModuleOutFuseWarning.get() * 4
            moduledata_list[3][5] = Add2_chVarModuleOrderOnEnable.get() * 128 + Add2_chVarModuleInputUVWarning.get() * 64 \
                                    + Add2_chVarModuleACInbalanceWarning.get() * 32 + Add2_chVarModuleACPhaseLossWarning.get() * 16 + \
                                    Add2_chVarModuleDCUV.get() * 8 + Add2_chVarModuleIDRepet.get() * 4 + \
                                    Add2_chVarModuleInputOverVoltage.get() * 2 + Add2_chVarModulePFCFault.get()
            moduledata_list[3][6] = Add2_chVarModulePowerLimit.get() * 128 + Add2_chVarStandbyState.get() * 64 \
                                    + Add2_chVarFanFullSpeed.get() * 32 + Add2_chVarModuleWalkInEbable.get() * 16 + \
                                    Add2_chVarPFCPowerOff.get() * 8 + Add2_chVarModuleRecognition.get() * 4 + \
                                    Add2_chVarModuleCurrentMean.get() * 2 + Add2_chVarModuleCANErrorState.get()

            moduledata_list[4][0] = int(float(e_Add3_OutVoltage.get()) * 10) % 256
            moduledata_list[4][1] = int(float(e_Add3_OutVoltage.get()) * 10) // 256
            moduledata_list[4][2] = int(float(e_Add3_OutCurrent.get()) * 10) % 256
            moduledata_list[4][3] = int(float(e_Add3_OutCurrent.get()) * 10) // 256
            moduledata_list[4][4] = int(float(e_Add3_Temperature.get()) * 10) % 256
            moduledata_list[4][5] = int(float(e_Add3_Temperature.get()) * 10) // 256
            moduledata_list[4][6] = Add3_chVarOutOverVoltage.get() * 128 + Add3_chVarOverTemperature.get() * 64 \
                                    + Add3_chVarModuleFault.get() * 32 + Add3_chVarModuleProtect.get() * 16 + \
                                    Add3_chVarFanFault.get() * 8 + Add3_chVarEEPROMFault.get() * 4 + \
                                    Add3_chVarACPowerLimit.get() * 2 + Add3_chVarTemPowerLimit.get()
            moduledata_list[5][0] = int(float(e_Add3_PFCvP.get()) * 10) % 256
            moduledata_list[5][1] = int(float(e_Add3_PFCvP.get()) * 10) // 256
            moduledata_list[5][2] = int(float(e_Add3_PFCvN.get()) * 10) % 256
            moduledata_list[5][3] = int(float(e_Add3_PFCvN.get()) * 10) // 256
            moduledata_list[5][4] = Add3_chVarModuleDCOverVoltage.get() * 128 + Add3_chVarModulePlugFault.get() * 64 \
                                    + Add3_chVarModuleReloadWarning.get() * 32 + Add3_chVarModuleOutUVWarning.get() * 16 + \
                                    Add3_chVarModuleInternalComAbnormal.get() * 8 + Add3_chVarModuleOutFuseWarning.get() * 4
            moduledata_list[5][5] = Add3_chVarModuleOrderOnEnable.get() * 128 + Add3_chVarModuleInputUVWarning.get() * 64 \
                                    + Add3_chVarModuleACInbalanceWarning.get() * 32 + Add3_chVarModuleACPhaseLossWarning.get() * 16 + \
                                    Add3_chVarModuleDCUV.get() * 8 + Add3_chVarModuleIDRepet.get() * 4 + \
                                    Add3_chVarModuleInputOverVoltage.get() * 2 + Add3_chVarModulePFCFault.get()
            moduledata_list[5][6] = Add3_chVarModulePowerLimit.get() * 128 + Add3_chVarStandbyState.get() * 64 \
                                    + Add3_chVarFanFullSpeed.get() * 32 + Add3_chVarModuleWalkInEbable.get() * 16 + \
                                    Add3_chVarPFCPowerOff.get() * 8 + Add3_chVarModuleRecognition.get() * 4 + \
                                    Add3_chVarModuleCurrentMean.get() * 2 + Add3_chVarModuleCANErrorState.get()

            moduledata_list[6][0] = int(float(e_Add4_OutVoltage.get()) * 10) % 256
            moduledata_list[6][1] = int(float(e_Add4_OutVoltage.get()) * 10) // 256
            moduledata_list[6][2] = int(float(e_Add4_OutCurrent.get()) * 10) % 256
            moduledata_list[6][3] = int(float(e_Add4_OutCurrent.get()) * 10) // 256
            moduledata_list[6][4] = int(float(e_Add4_Temperature.get()) * 10) % 256
            moduledata_list[6][5] = int(float(e_Add4_Temperature.get()) * 10) // 256
            moduledata_list[6][6] = Add4_chVarOutOverVoltage.get() * 128 + Add4_chVarOverTemperature.get() * 64 \
                                    + Add4_chVarModuleFault.get() * 32 + Add4_chVarModuleProtect.get() * 16 + \
                                    Add4_chVarFanFault.get() * 8 + Add4_chVarEEPROMFault.get() * 4 + \
                                    Add4_chVarACPowerLimit.get() * 2 + Add4_chVarTemPowerLimit.get()
            moduledata_list[7][0] = int(float(e_Add4_PFCvP.get()) * 10) % 256
            moduledata_list[7][1] = int(float(e_Add4_PFCvP.get()) * 10) // 256
            moduledata_list[7][2] = int(float(e_Add4_PFCvN.get()) * 10) % 256
            moduledata_list[7][3] = int(float(e_Add4_PFCvN.get()) * 10) // 256
            moduledata_list[7][4] = Add4_chVarModuleDCOverVoltage.get() * 128 + Add4_chVarModulePlugFault.get() * 64 \
                                    + Add4_chVarModuleReloadWarning.get() * 32 + Add4_chVarModuleOutUVWarning.get() * 16 + \
                                    Add4_chVarModuleInternalComAbnormal.get() * 8 + Add4_chVarModuleOutFuseWarning.get() * 4
            moduledata_list[7][5] = Add4_chVarModuleOrderOnEnable.get() * 128 + Add4_chVarModuleInputUVWarning.get() * 64 \
                                    + Add4_chVarModuleACInbalanceWarning.get() * 32 + Add4_chVarModuleACPhaseLossWarning.get() * 16 + \
                                    Add4_chVarModuleDCUV.get() * 8 + Add4_chVarModuleIDRepet.get() * 4 + \
                                    Add4_chVarModuleInputOverVoltage.get() * 2 + Add4_chVarModulePFCFault.get()
            moduledata_list[7][6] = Add4_chVarModulePowerLimit.get() * 128 + Add4_chVarStandbyState.get() * 64 \
                                    + Add4_chVarFanFullSpeed.get() * 32 + Add4_chVarModuleWalkInEbable.get() * 16 + \
                                    Add4_chVarPFCPowerOff.get() * 8 + Add4_chVarModuleRecognition.get() * 4 + \
                                    Add4_chVarModuleCurrentMean.get() * 2 + Add4_chVarModuleCANErrorState.get()

            moduledata_list[8][0] = int(float(e_Add5_OutVoltage.get()) * 10) % 256
            moduledata_list[8][1] = int(float(e_Add5_OutVoltage.get()) * 10) // 256
            moduledata_list[8][2] = int(float(e_Add5_OutCurrent.get()) * 10) % 256
            moduledata_list[8][3] = int(float(e_Add5_OutCurrent.get()) * 10) // 256
            moduledata_list[8][4] = int(float(e_Add5_Temperature.get()) * 10) % 256
            moduledata_list[8][5] = int(float(e_Add5_Temperature.get()) * 10) // 256
            moduledata_list[8][6] = Add5_chVarOutOverVoltage.get() * 128 + Add5_chVarOverTemperature.get() * 64 \
                                    + Add5_chVarModuleFault.get() * 32 + Add5_chVarModuleProtect.get() * 16 + \
                                    Add5_chVarFanFault.get() * 8 + Add5_chVarEEPROMFault.get() * 4 + \
                                    Add5_chVarACPowerLimit.get() * 2 + Add5_chVarTemPowerLimit.get()
            moduledata_list[9][0] = int(float(e_Add5_PFCvP.get()) * 10) % 256
            moduledata_list[9][1] = int(float(e_Add5_PFCvP.get()) * 10) // 256
            moduledata_list[9][2] = int(float(e_Add5_PFCvN.get()) * 10) % 256
            moduledata_list[9][3] = int(float(e_Add5_PFCvN.get()) * 10) // 256
            moduledata_list[9][4] = Add5_chVarModuleDCOverVoltage.get() * 128 + Add5_chVarModulePlugFault.get() * 64 \
                                    + Add5_chVarModuleReloadWarning.get() * 32 + Add5_chVarModuleOutUVWarning.get() * 16 + \
                                    Add5_chVarModuleInternalComAbnormal.get() * 8 + Add5_chVarModuleOutFuseWarning.get() * 4
            moduledata_list[9][5] = Add5_chVarModuleOrderOnEnable.get() * 128 + Add5_chVarModuleInputUVWarning.get() * 64 \
                                    + Add5_chVarModuleACInbalanceWarning.get() * 32 + Add5_chVarModuleACPhaseLossWarning.get() * 16 + \
                                    Add5_chVarModuleDCUV.get() * 8 + Add5_chVarModuleIDRepet.get() * 4 + \
                                    Add5_chVarModuleInputOverVoltage.get() * 2 + Add5_chVarModulePFCFault.get()
            moduledata_list[9][6] = Add5_chVarModulePowerLimit.get() * 128 + Add5_chVarStandbyState.get() * 64 \
                                    + Add5_chVarFanFullSpeed.get() * 32 + Add5_chVarModuleWalkInEbable.get() * 16 + \
                                    Add5_chVarPFCPowerOff.get() * 8 + Add5_chVarModuleRecognition.get() * 4 + \
                                    Add5_chVarModuleCurrentMean.get() * 2 + Add5_chVarModuleCANErrorState.get()

            moduledata_list[10][0] = int(float(e_Add6_OutVoltage.get()) * 10) % 256
            moduledata_list[10][1] = int(float(e_Add6_OutVoltage.get()) * 10) // 256
            moduledata_list[10][2] = int(float(e_Add6_OutCurrent.get()) * 10) % 256
            moduledata_list[10][3] = int(float(e_Add6_OutCurrent.get()) * 10) // 256
            moduledata_list[10][4] = int(float(e_Add6_Temperature.get()) * 10) % 256
            moduledata_list[10][5] = int(float(e_Add6_Temperature.get()) * 10) // 256
            moduledata_list[10][6] = Add6_chVarOutOverVoltage.get() * 128 + Add6_chVarOverTemperature.get() * 64 \
                                     + Add6_chVarModuleFault.get() * 32 + Add6_chVarModuleProtect.get() * 16 + \
                                     Add6_chVarFanFault.get() * 8 + Add6_chVarEEPROMFault.get() * 4 + \
                                     Add6_chVarACPowerLimit.get() * 2 + Add6_chVarTemPowerLimit.get()
            moduledata_list[11][0] = int(float(e_Add6_PFCvP.get()) * 10) % 256
            moduledata_list[11][1] = int(float(e_Add6_PFCvP.get()) * 10) // 256
            moduledata_list[11][2] = int(float(e_Add6_PFCvN.get()) * 10) % 256
            moduledata_list[11][3] = int(float(e_Add6_PFCvN.get()) * 10) // 256
            moduledata_list[11][4] = Add6_chVarModuleDCOverVoltage.get() * 128 + Add6_chVarModulePlugFault.get() * 64 \
                                     + Add6_chVarModuleReloadWarning.get() * 32 + Add6_chVarModuleOutUVWarning.get() * 16 + \
                                     Add6_chVarModuleInternalComAbnormal.get() * 8 + Add6_chVarModuleOutFuseWarning.get() * 4
            moduledata_list[11][5] = Add6_chVarModuleOrderOnEnable.get() * 128 + Add6_chVarModuleInputUVWarning.get() * 64 \
                                     + Add6_chVarModuleACInbalanceWarning.get() * 32 + Add6_chVarModuleACPhaseLossWarning.get() * 16 + \
                                     Add6_chVarModuleDCUV.get() * 8 + Add6_chVarModuleIDRepet.get() * 4 + \
                                     Add6_chVarModuleInputOverVoltage.get() * 2 + Add6_chVarModulePFCFault.get()
            moduledata_list[11][6] = Add6_chVarModulePowerLimit.get() * 128 + Add6_chVarStandbyState.get() * 64 \
                                     + Add6_chVarFanFullSpeed.get() * 32 + Add6_chVarModuleWalkInEbable.get() * 16 + \
                                     Add6_chVarPFCPowerOff.get() * 8 + Add6_chVarModuleRecognition.get() * 4 + \
                                     Add6_chVarModuleCurrentMean.get() * 2 + Add6_chVarModuleCANErrorState.get()

            moduledata_list[12][0] = int(float(e_Add7_OutVoltage.get()) * 10) % 256
            moduledata_list[12][1] = int(float(e_Add7_OutVoltage.get()) * 10) // 256
            moduledata_list[12][2] = int(float(e_Add7_OutCurrent.get()) * 10) % 256
            moduledata_list[12][3] = int(float(e_Add7_OutCurrent.get()) * 10) // 256
            moduledata_list[12][4] = int(float(e_Add7_Temperature.get()) * 10) % 256
            moduledata_list[12][5] = int(float(e_Add7_Temperature.get()) * 10) // 256
            moduledata_list[12][6] = Add7_chVarOutOverVoltage.get() * 128 + Add7_chVarOverTemperature.get() * 64 \
                                     + Add7_chVarModuleFault.get() * 32 + Add7_chVarModuleProtect.get() * 16 + \
                                     Add7_chVarFanFault.get() * 8 + Add7_chVarEEPROMFault.get() * 4 + \
                                     Add7_chVarACPowerLimit.get() * 2 + Add7_chVarTemPowerLimit.get()
            moduledata_list[13][0] = int(float(e_Add7_PFCvP.get()) * 10) % 256
            moduledata_list[13][1] = int(float(e_Add7_PFCvP.get()) * 10) // 256
            moduledata_list[13][2] = int(float(e_Add7_PFCvN.get()) * 10) % 256
            moduledata_list[13][3] = int(float(e_Add7_PFCvN.get()) * 10) // 256
            moduledata_list[13][4] = Add7_chVarModuleDCOverVoltage.get() * 128 + Add7_chVarModulePlugFault.get() * 64 \
                                     + Add7_chVarModuleReloadWarning.get() * 32 + Add7_chVarModuleOutUVWarning.get() * 16 + \
                                     Add7_chVarModuleInternalComAbnormal.get() * 8 + Add7_chVarModuleOutFuseWarning.get() * 4
            moduledata_list[13][5] = Add7_chVarModuleOrderOnEnable.get() * 128 + Add7_chVarModuleInputUVWarning.get() * 64 \
                                     + Add7_chVarModuleACInbalanceWarning.get() * 32 + Add7_chVarModuleACPhaseLossWarning.get() * 16 + \
                                     Add7_chVarModuleDCUV.get() * 8 + Add7_chVarModuleIDRepet.get() * 4 + \
                                     Add7_chVarModuleInputOverVoltage.get() * 2 + Add7_chVarModulePFCFault.get()
            moduledata_list[13][6] = Add7_chVarModulePowerLimit.get() * 128 + Add7_chVarStandbyState.get() * 64 \
                                     + Add7_chVarFanFullSpeed.get() * 32 + Add7_chVarModuleWalkInEbable.get() * 16 + \
                                     Add7_chVarPFCPowerOff.get() * 8 + Add7_chVarModuleRecognition.get() * 4 + \
                                     Add7_chVarModuleCurrentMean.get() * 2 + Add7_chVarModuleCANErrorState.get()
        except ValueError as e:
            print(e)

    b3 = tkinter.Button(subroot, text='确认', width=7, height=1, command=getdata)
    b3.pack()
    b3.place(x=600, y=750, anchor=NW)



