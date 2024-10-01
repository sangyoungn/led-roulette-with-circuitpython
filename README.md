# LED Roulette with CircuitPython

This is a project to build an LED roulette with CircuitPython on EFR32xG24 Explorer Kit.

## Contents

"**hardware**" directory contains files for the hardware design including schematic and gerber output.
"**code**" directry contains scripts written in CircuitPython, which run on EFR32xG24 Explorer Kit.

## Directory Structure

.   
├── **hardware**   
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── **roulette** (KiCad Design Directory)   
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── **gerber** (PCB Gerber Plot Directory)   
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── **pdf** (PCB PDF Polt Directory)   
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── *roulette.dxf* (PCB Outline and Decoration Silk DXF)   
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── *roulette.kicad_pcb* (PCB Design File)   
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── *roulette.kicad_pro* (KiCad Project File)   
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── *roulette.pdf* (PDF Plot File of Whole Schematic)   
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── *roulette.kicad_sch* (Schematic File #1)   
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── *LEDs.kicad_sch* (Schematic File #2)    
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── *xg24_explorer_kit.kicad_sch* (Schematic File #3)   
└── **code**   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── *code.py*   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── *led_roulette.py*   

