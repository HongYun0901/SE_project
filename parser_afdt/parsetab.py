
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CASE COLON COM CONTENT DEFAULT DO ELSE FOR GOTO IF LBRACE LCOM LP RBRACE RCOM RP SEMI SPACE SWITCH WHILEstmts : stmt\n             | stmt stmtsstmt :\n            | expr\n            | ifstmt\n            | whilestmt\n            | forstmt\n            | switch_stmtswitch_stmt : SWITCH LP bool_expr RP LBRACE case_stmt RBRACE stmtcase_stmt : CASE bool_expr COLON stmts\n                 | DEFAULT COLON stmts\n                 | CASE bool_expr COLON stmts case_stmtifstmt : IF LP bool_expr RP stmt_block elifs stmt\n              | IF LP bool_expr RP stmt_block stmt stmt_block :  LBRACE stmts RBRACE\n                    | stmt elifs : else\n             | elif\n             | elif elifs elif : ELSE IF LP bool_expr RP stmt_blockelse : ELSE stmt_blockwhilestmt : WHILE LP bool_expr RP stmt_block stmtforstmt : FOR LP for_expr RP stmt_block stmtfor_expr : contents SEMI contents SEMI contentsbool_expr : contentsexpr : contents SEMI\n            | func_expr SEMIfunc_expr : contents LP params RPparam : contents\n             | func_expr params : param\n              | param params contents : CONTENT \n                 | CONTENT contents'
    
_lr_action_items = {'IF':([0,2,3,4,5,6,7,16,18,36,37,38,41,42,43,44,45,48,49,50,51,52,54,55,60,61,62,64,66,68,70,71,75,77,],[10,10,-4,-5,-6,-7,-8,-26,-27,10,10,10,10,-16,10,10,10,10,-14,-17,-18,63,-22,-23,-13,-19,-21,-15,10,10,-9,10,10,10,]),'WHILE':([0,2,3,4,5,6,7,16,18,36,37,38,41,42,43,44,45,48,49,50,51,52,54,55,60,61,62,64,66,68,70,71,75,77,],[11,11,-4,-5,-6,-7,-8,-26,-27,11,11,11,11,-16,11,11,11,11,-14,-17,-18,11,-22,-23,-13,-19,-21,-15,11,11,-9,11,11,11,]),'FOR':([0,2,3,4,5,6,7,16,18,36,37,38,41,42,43,44,45,48,49,50,51,52,54,55,60,61,62,64,66,68,70,71,75,77,],[12,12,-4,-5,-6,-7,-8,-26,-27,12,12,12,12,-16,12,12,12,12,-14,-17,-18,12,-22,-23,-13,-19,-21,-15,12,12,-9,12,12,12,]),'SWITCH':([0,2,3,4,5,6,7,16,18,36,37,38,41,42,43,44,45,48,49,50,51,52,54,55,60,61,62,64,66,68,70,71,75,77,],[13,13,-4,-5,-6,-7,-8,-26,-27,13,13,13,13,-16,13,13,13,13,-14,-17,-18,13,-22,-23,-13,-19,-21,-15,13,13,-9,13,13,13,]),'CONTENT':([0,2,3,4,5,6,7,14,16,17,18,19,20,21,22,23,24,26,27,34,36,37,38,39,41,42,43,44,45,48,49,50,51,52,54,55,56,58,60,61,62,64,66,68,69,70,71,75,77,],[14,14,-4,-5,-6,-7,-8,14,-26,14,-27,14,14,14,14,-34,-29,14,-30,-28,14,14,14,14,14,-16,14,14,14,14,-14,-17,-18,14,-22,-23,14,14,-13,-19,-21,-15,14,14,14,-9,14,14,14,]),'$end':([0,1,2,3,4,5,6,7,15,16,18,36,37,38,41,42,44,45,48,49,50,51,52,54,55,60,61,62,64,66,70,75,77,],[-3,0,-1,-4,-5,-6,-7,-8,-2,-26,-27,-3,-3,-3,-3,-16,-3,-3,-3,-14,-17,-18,-3,-22,-23,-13,-19,-21,-15,-3,-9,-3,-3,]),'RBRACE':([2,3,4,5,6,7,15,16,18,36,37,38,41,42,43,44,45,48,49,50,51,52,53,54,55,57,60,61,62,64,66,68,70,71,72,74,75,76,77,],[-1,-4,-5,-6,-7,-8,-2,-26,-27,-3,-3,-3,-3,-16,-3,-3,-3,-3,-14,-17,-18,-3,64,-22,-23,66,-13,-19,-21,-15,-3,-3,-9,-3,-11,-10,-3,-12,-3,]),'CASE':([2,3,4,5,6,7,15,16,18,36,37,38,41,42,44,45,47,48,49,50,51,52,54,55,60,61,62,64,66,70,71,74,75,77,],[-1,-4,-5,-6,-7,-8,-2,-26,-27,-3,-3,-3,-3,-16,-3,-3,58,-3,-14,-17,-18,-3,-22,-23,-13,-19,-21,-15,-3,-9,-3,58,-3,-3,]),'DEFAULT':([2,3,4,5,6,7,15,16,18,36,37,38,41,42,44,45,47,48,49,50,51,52,54,55,60,61,62,64,66,70,71,74,75,77,],[-1,-4,-5,-6,-7,-8,-2,-26,-27,-3,-3,-3,-3,-16,-3,-3,59,-3,-14,-17,-18,-3,-22,-23,-13,-19,-21,-15,-3,-9,-3,59,-3,-3,]),'ELSE':([3,4,5,6,7,16,18,36,37,38,41,42,44,45,48,49,50,51,52,54,55,60,61,62,64,66,70,75,77,],[-4,-5,-6,-7,-8,-26,-27,-3,-3,-3,52,-16,-3,-3,-3,-14,-17,52,-3,-22,-23,-13,-19,-21,-15,-3,-9,-3,52,]),'SEMI':([8,9,14,23,32,34,46,],[16,18,-33,-34,39,-28,56,]),'LP':([8,10,11,12,13,14,23,24,63,],[17,19,20,21,22,-33,-34,17,69,]),'RP':([14,23,24,25,26,27,28,29,30,31,33,34,35,65,73,],[-33,-34,-29,34,-31,-30,36,-25,37,38,40,-28,-32,-24,75,]),'COLON':([14,23,29,59,67,],[-33,-34,-25,68,71,]),'LBRACE':([36,37,38,40,52,75,],[43,43,43,47,43,43,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'stmts':([0,2,43,68,71,],[1,15,53,72,74,]),'stmt':([0,2,36,37,38,41,43,44,45,48,52,66,68,71,75,77,],[2,2,42,42,42,49,2,54,55,60,42,70,2,2,42,49,]),'expr':([0,2,36,37,38,41,43,44,45,48,52,66,68,71,75,77,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'ifstmt':([0,2,36,37,38,41,43,44,45,48,52,66,68,71,75,77,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'whilestmt':([0,2,36,37,38,41,43,44,45,48,52,66,68,71,75,77,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'forstmt':([0,2,36,37,38,41,43,44,45,48,52,66,68,71,75,77,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'switch_stmt':([0,2,36,37,38,41,43,44,45,48,52,66,68,71,75,77,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'contents':([0,2,14,17,19,20,21,22,26,36,37,38,39,41,43,44,45,48,52,56,58,66,68,69,71,75,77,],[8,8,23,24,29,29,32,29,24,8,8,8,46,8,8,8,8,8,8,65,29,8,8,29,8,8,8,]),'func_expr':([0,2,17,26,36,37,38,41,43,44,45,48,52,66,68,71,75,77,],[9,9,27,27,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'params':([17,26,],[25,35,]),'param':([17,26,],[26,26,]),'bool_expr':([19,20,22,58,69,],[28,30,33,67,73,]),'for_expr':([21,],[31,]),'stmt_block':([36,37,38,52,75,],[41,44,45,62,77,]),'elifs':([41,51,77,],[48,61,48,]),'else':([41,51,77,],[50,50,50,]),'elif':([41,51,77,],[51,51,51,]),'case_stmt':([47,74,],[57,76,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> stmts","S'",1,None,None,None),
  ('stmts -> stmt','stmts',1,'p_stmts','se.py',174),
  ('stmts -> stmt stmts','stmts',2,'p_stmts','se.py',175),
  ('stmt -> <empty>','stmt',0,'p_stmt','se.py',205),
  ('stmt -> expr','stmt',1,'p_stmt','se.py',206),
  ('stmt -> ifstmt','stmt',1,'p_stmt','se.py',207),
  ('stmt -> whilestmt','stmt',1,'p_stmt','se.py',208),
  ('stmt -> forstmt','stmt',1,'p_stmt','se.py',209),
  ('stmt -> switch_stmt','stmt',1,'p_stmt','se.py',210),
  ('switch_stmt -> SWITCH LP bool_expr RP LBRACE case_stmt RBRACE stmt','switch_stmt',8,'p_switch_stmt','se.py',227),
  ('case_stmt -> CASE bool_expr COLON stmts','case_stmt',4,'p_case_stmt','se.py',296),
  ('case_stmt -> DEFAULT COLON stmts','case_stmt',3,'p_case_stmt','se.py',297),
  ('case_stmt -> CASE bool_expr COLON stmts case_stmt','case_stmt',5,'p_case_stmt','se.py',298),
  ('ifstmt -> IF LP bool_expr RP stmt_block elifs stmt','ifstmt',7,'p_ifstmt','se.py',331),
  ('ifstmt -> IF LP bool_expr RP stmt_block stmt','ifstmt',6,'p_ifstmt','se.py',332),
  ('stmt_block -> LBRACE stmts RBRACE','stmt_block',3,'p_stmt_block','se.py',355),
  ('stmt_block -> stmt','stmt_block',1,'p_stmt_block','se.py',356),
  ('elifs -> else','elifs',1,'p_elseif_s','se.py',364),
  ('elifs -> elif','elifs',1,'p_elseif_s','se.py',365),
  ('elifs -> elif elifs','elifs',2,'p_elseif_s','se.py',366),
  ('elif -> ELSE IF LP bool_expr RP stmt_block','elif',6,'p_elseif','se.py',379),
  ('else -> ELSE stmt_block','else',2,'p_else','se.py',388),
  ('whilestmt -> WHILE LP bool_expr RP stmt_block stmt','whilestmt',6,'p_whilestmt','se.py',395),
  ('forstmt -> FOR LP for_expr RP stmt_block stmt','forstmt',6,'p_forstmt','se.py',420),
  ('for_expr -> contents SEMI contents SEMI contents','for_expr',5,'p_for_expr','se.py',438),
  ('bool_expr -> contents','bool_expr',1,'p_bool_expr','se.py',455),
  ('expr -> contents SEMI','expr',2,'p_expr','se.py',469),
  ('expr -> func_expr SEMI','expr',2,'p_expr','se.py',470),
  ('func_expr -> contents LP params RP','func_expr',4,'p_func','se.py',495),
  ('param -> contents','param',1,'p_param','se.py',500),
  ('param -> func_expr','param',1,'p_param','se.py',501),
  ('params -> param','params',1,'p_params','se.py',506),
  ('params -> param params','params',2,'p_params','se.py',507),
  ('contents -> CONTENT','contents',1,'p_contents','se.py',512),
  ('contents -> CONTENT contents','contents',2,'p_contents','se.py',513),
]
