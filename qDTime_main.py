### qDTime_main.py

#############################################################################################################
#
# --- qDTime_main ---
#
#   qDTime defines a class for date and time description in the form of @qDTime-taks'qDTime-tiks@ .
#   qDTime_main shows the usage of qDTime.
#
# copyright: 
#   
#   (c) by Roland Degelmann, takatoa 
#   Mail : rode@takatoa.net
#   Web  : takatoa.net
#   
# created | last modified | version:
#
#   2024-12-01 | 2025-01-28 | version: 0.1.0
#
#############################################################################################################

from qDTime import qDTime

if __name__ == '__main__':
    rdt = qDTime()
    print("\n\nshow the usage of qDTime\n")
    print('***', rdt, '***\n')
    myRdt = rdt.get_qDTime()
    print("get actual qDTime\t:", myRdt)
    myRdt = rdt.set_qDTime(2024, 1, 13, 15, 40, 13, 37)
    print("set qDTime\t\t:", myRdt, "\t<-- Input data: '2024, 1, 13, 15, 40, 13, 37'")
    myRdt = rdt.set_qDTime(1993, 11, 11, 8, 15, 52, 37)
    print("set qDTime\t\t:", myRdt, "\t<-- Input data: '1993, 11, 11, 8, 15, 52, 37'")
    myRdt = rdt.set_qDTime(1959, 12, 22, 16, 29, 53, 11)
    print("set qDTime\t\t:", myRdt, "\t<-- Input data: '1959, 12, 22, 16, 29, 53, 11'")
    myRdt = rdt.set_qDTime(1897, 4)
    print("set qDTime\t\t:", myRdt, "\t<-- Input data: '1897, 4'")
