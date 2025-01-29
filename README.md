![...](takatoa_head-img_1920-200.jpg)

# qDTime

   qDTime defines a class for date and time description in the form of @qDTime-taks'qDTime-tiks@ 

### basic information

   On June 7, 1925, Werner Heisenberg went to Helgoland. There he completed the quantum-theoretical calculation of the anharmonic oscillator by determining the missing motion constant. In particular, he used a new quantum condition, which he later called the “Canonical commutation relation”. Together with Max Born and Pascual Jordan, Heisenberg proved that his new theory led to stationary states of the oscillator and thus ensured energy conservation. After returning from Helgoland on June 19, 1925, he wrote his fundamental work “On the Quantum-Theoretical Reinterpretation of Kinetic and Mechanical Relationships” in Göttingen. He completed this study on July 9 and used the philosophical principle that only observable quantities could be included in the theoretical description of atoms. 

   After Born and Jordan had formulated the content of Heisenberg's work in a consistent mathematical theory with infinite Hermitian matrices in August and September 1925, Heisenberg helped to complete and apply this new “matrix mechanics” from September onwards. __A joint paper entitled “On Quantum Mechanics II” was submitted on November 16, 1925.__

   These events mark the decisive turning point in the history of quantum mechanics.

   (Above informations are taken from: www.heisenberg-gesellschaft.de)

   qDTime shows that a new era began on November 16, 1925, by displaying the time that has passed since then. However, qDTime does not display the time in the usual form of years, months, days, hours, minutes and seconds, but in qDTime-taks and qDTime-tiks.

### qDTime format

![...](qDTime_img_1920-200.jpg)
shown datetime: January 13, 2025; 15:40:13
># &nbsp;&nbsp;&nbsp;&nbsp;@qDTime-taks'qDTime-tiks@ --> @YY.MM.DD'TT.TTT@

   | &nbsp; | value |
   | ---: | :----------- |
   | YY [0 - ...] | past qDTime-tak years |
   | MM [0 - 12]  | past qDTime-tak months </br>13 units of 28 days each, last unit in a leap year has 29 days |
   | DD  [0 - 27 bzw. 28] | past qDTime-tak days |
   | TT.TTT [00.000 - 99.999] | past qDTime-tiks since the start of the day 100000 units per day |
 
   Reference time: 16.11.1925 0.00 Uhr (Born, Heisenberg, Jordan: “On Quantum Mechanics II”)

### implementations in upcoming releases

- __redefine time zones__

    So far, the definition of time zones in 24 segments remains unaffected. This leads to jumps of the qDTime-tiks by 4166.666667 when the time zone changes. 
    It would make more sense to redefine and set the number of time zones to 20. This would result in qDTime-tik jumps of 5000 when the time zone changes. 
    At the same time, however, the assignment of the associated time zone would have to be checked and, if necessary, corrected for all countries worldwide.

### copyright notice 

   see LICENSE

### implemented by takatoa
    
   Name      : Roland Degelmann  
   Adress    : Hofmillerstraße 12, 85356 Freising   
   Mail      : rode@takatoa.net</br>
   Web       : takatoa.net
 
### created | last modified | version

   2024-12-01 | 2024-01-13 | version: 0.1.0

