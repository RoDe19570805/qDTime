### qDTime.py

#############################################################################################################
#
# --- qDTime ---
#
#   qDTime defines a class for date and time description in the form of @qDTime-taks'qDTime-tiks@.
#   reference datetime: 1925-11-16 
#                       M.Born, W.Heisenberg, P.Jordan submit a joint paper on the subject 
#                       “On Quantum Mechanics II”.
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

from datetime import datetime
from typing import Optional
import math

class qDTime:
    def __init__(self) :
        
        self.NULL_YEAR = 1925
        self.NULL_MONTH = 11
        self.NULL_DAY = 16
        self.NULL_HOUR = 0
        self.NULL_MIN = 0
        self.NULL_SEC = 0
        
        rdt = "@00.00.00'00.000@"
    
    def calc_qDTime(self,
                    actYear : Optional[int] = 1925,
                    actMonth : Optional[int] = 11,
                    actDay : Optional[int] = 16,
                    actHour : Optional[int] = 0,
                    actMin : Optional[int] = 0,
                    actSec : Optional[int] = 0,
                    actMicroSec : Optional[int] = 0) :
        """calculates the qDTime."""
        qDTimeTiks = str(round((actHour * 60 * 60 + actMin * 60 + actSec) / 0.864) / 1000)

        if (qDTimeTiks.index(".") == 1 or len(qDTimeTiks) == 1) :
            qDTimeTiks = "0" + qDTimeTiks 
        if (len(qDTimeTiks) <= 5) :
            if (len(qDTimeTiks) == 2) :
                qDTimeTiks = qDTimeTiks + "." 
            for i in range(len(qDTimeTiks), 6) :
                qDTimeTiks = qDTimeTiks + "0" 

        xYear = actYear - self.NULL_YEAR
     
        actDate = datetime(actYear, (actMonth), actDay)
        refDate = datetime(actYear, (self.NULL_MONTH), self.NULL_DAY)

        diff = actDate - refDate
        
        if (diff.days < 0) :
            refDate1 = datetime((actYear - 1), (self.NULL_MONTH), self.NULL_DAY)
            diff = actDate - refDate1
            xYear = xYear - 1

        xDay = diff.days
        xMonth = math.floor(xDay / 28)

        if (xMonth > 12) : 
            xMonth = 12
        
        xDay = xDay - (xMonth * 28)
        qDTimeTaks = str(xYear) + "." + "%02d" % xMonth + "." + "%02d" % xDay
        self.rdt = "@" + qDTimeTaks + "'" + qDTimeTiks + "@"
        
        return self.rdt
        
    def get_qDTime(self) :
        """get the qDTime."""
        # read current date
        actDT = datetime.now()
        actYear = actDT.year
        actMonth = actDT.month
        actDay = actDT.day
        actHour = actDT.hour
        actMin = actDT.minute
        actSec = actDT.second
        actMicroSec = actDT.microsecond

        return self.calc_qDTime(actYear, actMonth, actDay, actHour, actMin, actSec, actMicroSec)
        
    def set_qDTime(self, 
                     setYear : Optional[int] = 1925, 
                     setMonth  : Optional[int] = 11, 
                     setDay : Optional[int] = 16, 
                     setHour : Optional[int] = 0, 
                     setMin : Optional[int] = 0, 
                     setSec : Optional[int] = 0, 
                     setMicroSec : Optional[int] = 0) :
        """set the qDTime."""
        actYear = setYear
        actMonth = setMonth
        actDay = setDay
        actHour = setHour
        actMin = setMin
        actSec = setSec
        actMicroSec = setMicroSec

        return self.calc_qDTime(actYear, actMonth, actDay, actHour, actMin, actSec, actMicroSec)
    
    def __str__(self):
        return f"qDTime defines a class for date and time description and handling in the form of @qDTime-taks'qDTime-tiks@ ."