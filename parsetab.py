
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "DN FASTER HIGHCHORD JOIN MACRO NOTE PAUSE RUNMACRO SLOWER UP VAL  music  :   action    music  :  music action   action : MACRO '[' music ']'  action : RUNMACRO  action : NOTE  action : up\n                   | dn\n                   | faster\n                   | slower  action : PAUSE  action : NOTE JOIN NOTE\n                   | NOTE JOIN faster NOTE\n                   | NOTE JOIN slower NOTE  action : highchord  up : UP  up : up val dn : DN  dn : dn val val : VAL  faster : FASTER  slower : SLOWER  highchord : HIGHCHORD "
    
_lr_action_items = {'MACRO':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,27,28,29,],[3,3,-1,-4,-5,-6,-7,-8,-9,-10,-14,-15,-17,-20,-21,-22,-2,3,-16,-19,-18,3,-11,-3,-12,-13,]),'RUNMACRO':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,27,28,29,],[4,4,-1,-4,-5,-6,-7,-8,-9,-10,-14,-15,-17,-20,-21,-22,-2,4,-16,-19,-18,4,-11,-3,-12,-13,]),'NOTE':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,],[5,5,-1,-4,-5,-6,-7,-8,-9,-10,-14,-15,-17,-20,-21,-22,-2,5,24,-16,-19,-18,5,-11,28,29,-3,-12,-13,]),'PAUSE':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,27,28,29,],[10,10,-1,-4,-5,-6,-7,-8,-9,-10,-14,-15,-17,-20,-21,-22,-2,10,-16,-19,-18,10,-11,-3,-12,-13,]),'UP':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,27,28,29,],[12,12,-1,-4,-5,-6,-7,-8,-9,-10,-14,-15,-17,-20,-21,-22,-2,12,-16,-19,-18,12,-11,-3,-12,-13,]),'DN':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,27,28,29,],[13,13,-1,-4,-5,-6,-7,-8,-9,-10,-14,-15,-17,-20,-21,-22,-2,13,-16,-19,-18,13,-11,-3,-12,-13,]),'FASTER':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28,29,],[14,14,-1,-4,-5,-6,-7,-8,-9,-10,-14,-15,-17,-20,-21,-22,-2,14,14,-16,-19,-18,14,-11,-3,-12,-13,]),'SLOWER':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28,29,],[15,15,-1,-4,-5,-6,-7,-8,-9,-10,-14,-15,-17,-20,-21,-22,-2,15,15,-16,-19,-18,15,-11,-3,-12,-13,]),'HIGHCHORD':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,27,28,29,],[16,16,-1,-4,-5,-6,-7,-8,-9,-10,-14,-15,-17,-20,-21,-22,-2,16,-16,-19,-18,16,-11,-3,-12,-13,]),'$end':([1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,20,21,22,24,27,28,29,],[0,-1,-4,-5,-6,-7,-8,-9,-10,-14,-15,-17,-20,-21,-22,-2,-16,-19,-18,-11,-3,-12,-13,]),']':([2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,20,21,22,23,24,27,28,29,],[-1,-4,-5,-6,-7,-8,-9,-10,-14,-15,-17,-20,-21,-22,-2,-16,-19,-18,27,-11,-3,-12,-13,]),'[':([3,],[18,]),'JOIN':([5,],[19,]),'VAL':([6,7,12,13,20,21,22,],[21,21,-15,-17,-16,-19,-18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'music':([0,18,],[1,23,]),'action':([0,1,18,23,],[2,17,2,17,]),'up':([0,1,18,23,],[6,6,6,6,]),'dn':([0,1,18,23,],[7,7,7,7,]),'faster':([0,1,18,19,23,],[8,8,8,25,8,]),'slower':([0,1,18,19,23,],[9,9,9,26,9,]),'highchord':([0,1,18,23,],[11,11,11,11,]),'val':([6,7,],[20,22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> music","S'",1,None,None,None),
  ('music -> action','music',1,'p_music0','Parser.py',49),
  ('music -> music action','music',2,'p_music1','Parser.py',54),
  ('action -> MACRO [ music ]','action',4,'p_action_def_macro','Parser.py',61),
  ('action -> RUNMACRO','action',1,'p_action_run_macro','Parser.py',66),
  ('action -> NOTE','action',1,'p_action0','Parser.py',71),
  ('action -> up','action',1,'p_action1','Parser.py',77),
  ('action -> dn','action',1,'p_action1','Parser.py',78),
  ('action -> faster','action',1,'p_action1','Parser.py',79),
  ('action -> slower','action',1,'p_action1','Parser.py',80),
  ('action -> PAUSE','action',1,'p_action2','Parser.py',96),
  ('action -> NOTE JOIN NOTE','action',3,'p_action3','Parser.py',102),
  ('action -> NOTE JOIN faster NOTE','action',4,'p_action3','Parser.py',103),
  ('action -> NOTE JOIN slower NOTE','action',4,'p_action3','Parser.py',104),
  ('action -> highchord','action',1,'p_action4','Parser.py',119),
  ('up -> UP','up',1,'p_up0','Parser.py',124),
  ('up -> up val','up',2,'p_up1','Parser.py',129),
  ('dn -> DN','dn',1,'p_dn0','Parser.py',134),
  ('dn -> dn val','dn',2,'p_dn1','Parser.py',139),
  ('val -> VAL','val',1,'p_val','Parser.py',144),
  ('faster -> FASTER','faster',1,'p_faster0','Parser.py',149),
  ('slower -> SLOWER','slower',1,'p_slower0','Parser.py',154),
  ('highchord -> HIGHCHORD','highchord',1,'p_highchord','Parser.py',159),
]
