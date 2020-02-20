
"""
This module contains definitions for the ParseTree and Parser classes, as well as some ansillary functions to assist.
"""
from rply import ParserGenerator
from rply.errors import ParserGeneratorWarning
from warnings import simplefilter
from rply.token import Token

#we get werid 'non-descriptive' warnings from ParserGenerator, this ignores those
simplefilter('ignore', ParserGeneratorWarning)

class ParseTree():
    """
    ParseTree is a class that acts as each node in an ParseTree
    """
    def __init__(self, token, content):
        """
        Construct a new ParseTree object

        Args:
            token: The token type of the node.
            content: The content of that is tokenized.
        """
        self.token = token
        self.content = content


#setup parser class
class Parser():
    """
    Definition for the Parser object, works off of rply. Contains rules for parsing.
    """
    
    def __init__(self):
        """
        Initializes the parser and tells it the allowed tokens

        """

        self.pg = ParserGenerator(
            ['SEMICOLON','TYPE','SELF_DEFINED','OPEN_PAREN','CLOSE_PAREN','COMMA','OPEN_BRACE','CLOSE_BRACE','COMMENT','WHILE_LOOP','FOR_LOOP','DO_LOOP','IF_BRANCH','ELSE_BRANCH','SWITCH_BRANCH','CASE','COLON','DEFAULT','RETURN','GOTO','BREAK','CONTINUE','MUL','OPEN_BRACK','INTEGER','CLOSE_BRACK','AEQ','SEQ','MEQ','DEQ','LSEQ','RSEQ','BOEQ','BAEQ','XEQ','CEQ','SET','EQ','LEQ','GEQ','NEQ','LT','GT','OR','AND','BOR','XOR','BAND','LSH','RSH','ADD','SUB','DIV','MOD','NOT','COMP','INC','DEC','PRECISION','CHAR','HEX','OCT','BIN','NULL'] , 
            precedence=[
                ('right', ['SET', 'AEQ', 'SEQ', 'MEQ', 'DEQ', 'MODEQ', 'LSEQ', 'RSEQ', 'BAEQ', 'XEQ', 'BOEQ']),
                ('left',  ['OR']),
                ('left',  ['AND']),
                ('left',  ['BOR']),
                ('left',  ['XOR']),
                ('left',  ['BAND']),
                ('left',  ['EQ', 'NEQ']),
                ('left',  ['GE', 'GEQ']),
                ('left',  ['LE', 'LEQ']),
                ('left',  ['LSH', 'RSH']),
                ('left',  ['ADD', 'SUB']),
                ('left',  ['MUL', 'DIV', 'MOD']),
                ('right', ['INC', 'DEC', 'NOT', 'COMP']),
            ]
        )
        #initialzie head and current node
        self.Head = None


    def parse(self):
        """
        The list of BNF functions and their behavior
        """
        
        @self.pg.production('program : definitionList ')
        def program(p):
            """
            Tells the parser which BNF will be the head of the tree
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("program",p)
            self.Head = newNode
            return newNode

        @self.pg.production('definitionList : functionDefinition definitionList ')
        def definitionList___functionDefinition_definitionList_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("definitionList",p)
            self.Head = newNode
            return newNode

        @self.pg.production('definitionList : functionDeclaration definitionList ')
        def definitionList___functionDeclaration_definitionList_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("definitionList",p)
            self.Head = newNode
            return newNode

        @self.pg.production('definitionList : initialization SEMICOLON definitionList ')
        def definitionList___initialization_SEMICOLON_definitionList_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("definitionList",p)
            self.Head = newNode
            return newNode

        @self.pg.production('definitionList : ')
        def definitionList___(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("definitionList",p)
            self.Head = newNode
            return newNode

        @self.pg.production('functionDefinition : TYPE SELF_DEFINED OPEN_PAREN args CLOSE_PAREN block ')
        def functionDefinition___TYPE_SELF_DEFINED_OPEN_PAREN_args_CLOSE_PAREN_block_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("function definition",p)
            self.Head = newNode
            return newNode

        @self.pg.production('functionDefinition : TYPE SELF_DEFINED OPEN_PAREN CLOSE_PAREN block ')
        def functionDefinition___TYPE_SELF_DEFINED_OPEN_PAREN_CLOSE_PAREN_block_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("function definition",p)
            self.Head = newNode
            return newNode

        @self.pg.production('functionDeclaration : TYPE SELF_DEFINED OPEN_PAREN args CLOSE_PAREN SEMICOLON ')
        def functionDeclaration___TYPE_SELF_DEFINED_OPEN_PAREN_args_CLOSE_PAREN_SEMICOLON_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("functionDeclaration",p)
            self.Head = newNode
            return newNode

        @self.pg.production('functionDeclaration : TYPE SELF_DEFINED OPEN_PAREN CLOSE_PAREN SEMICOLON ')
        def functionDeclaration___TYPE_SELF_DEFINED_OPEN_PAREN_CLOSE_PAREN_SEMICOLON_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("functionDeclaration",p)
            self.Head = newNode
            return newNode

        @self.pg.production('args : arg_terminal COMMA args ')
        def args___arg_terminal_COMMA_args_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("args",p)
            self.Head = newNode
            return newNode

        @self.pg.production('args : arg_terminal ')
        def args___arg_terminal_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("args",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arg_terminal : TYPE SELF_DEFINED ')
        def arg_terminal___TYPE_SELF_DEFINED_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("arg_terminal",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arg_terminal : TYPE ')
        def arg_terminal___TYPE_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("arg_terminal",p)
            self.Head = newNode
            return newNode

        @self.pg.production('block : OPEN_BRACE block block CLOSE_BRACE ')
        def block___OPEN_BRACE_block_block_CLOSE_BRACE_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("block",p)
            self.Head = newNode
            return newNode

        @self.pg.production('block : OPEN_BRACE block content CLOSE_BRACE ')
        def block___OPEN_BRACE_block_content_CLOSE_BRACE_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("block",p)
            self.Head = newNode
            return newNode

        @self.pg.production('block : OPEN_BRACE content block CLOSE_BRACE ')
        def block___OPEN_BRACE_content_block_CLOSE_BRACE_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("block",p)
            self.Head = newNode
            return newNode

        @self.pg.production('block : OPEN_BRACE content CLOSE_BRACE ')
        def block___OPEN_BRACE_content_CLOSE_BRACE_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("block",p)
            self.Head = newNode
            return newNode

        @self.pg.production('block : OPEN_BRACE CLOSE_BRACE ')
        def block___OPEN_BRACE_CLOSE_BRACE_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("block",p)
            self.Head = newNode
            return newNode

        @self.pg.production('content : content_terminal content ')
        def content___content_terminal_content_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("content",p)
            self.Head = newNode
            return newNode

        @self.pg.production('content : content_terminal ')
        def content___content_terminal_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("content",p)
            self.Head = newNode
            return newNode

        @self.pg.production('content_terminal : single_line ')
        def content_terminal___single_line_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("content_terminal",p)
            self.Head = newNode
            return newNode

        @self.pg.production('content_terminal : loop ')
        def content_terminal___loop_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("content_terminal",p)
            self.Head = newNode
            return newNode

        @self.pg.production('content_terminal : branch ')
        def content_terminal___branch_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("content_terminal",p)
            self.Head = newNode
            return newNode

        @self.pg.production('content_terminal : goto ')
        def content_terminal___goto_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("content_terminal",p)
            self.Head = newNode
            return newNode

        @self.pg.production('content_terminal : COMMENT ')
        def content_terminal___COMMENT_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("content_terminal",p)
            self.Head = newNode
            return newNode

        @self.pg.production('single_line : initialization SEMICOLON ')
        def single_line___initialization_SEMICOLON_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("single_line",p)
            self.Head = newNode
            return newNode

        @self.pg.production('single_line : function_call SEMICOLON ')
        def single_line___function_call_SEMICOLON_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("single_line",p)
            self.Head = newNode
            return newNode

        @self.pg.production('single_line : designation SEMICOLON ')
        def single_line___designation_SEMICOLON_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("single_line",p)
            self.Head = newNode
            return newNode

        @self.pg.production('single_line : response SEMICOLON ')
        def single_line___response_SEMICOLON_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("single_line",p)
            self.Head = newNode
            return newNode

        @self.pg.production('single_line : arithmetic SEMICOLON ')
        def single_line___arithmetic_SEMICOLON_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("single_line",p)
            self.Head = newNode
            return newNode

        @self.pg.production('single_line : SEMICOLON ')
        def single_line___SEMICOLON_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("single_line",p)
            self.Head = newNode
            return newNode

        @self.pg.production('function_call : SELF_DEFINED OPEN_PAREN param CLOSE_PAREN ')
        def function_call___SELF_DEFINED_OPEN_PAREN_param_CLOSE_PAREN_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("function call",p)
            self.Head = newNode
            return newNode

        @self.pg.production('function_call : SELF_DEFINED OPEN_PAREN CLOSE_PAREN ')
        def function_call___SELF_DEFINED_OPEN_PAREN_CLOSE_PAREN_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("function call",p)
            self.Head = newNode
            return newNode

        @self.pg.production('param : param_terminal ')
        def param___param_terminal_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("paramater",p)
            self.Head = newNode
            return newNode

        @self.pg.production('param : param_terminal COMMA param ')
        def param___param_terminal_COMMA_param_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("parameter",p)
            self.Head = newNode
            return newNode

        @self.pg.production('param_terminal : arithmetic ')
        def param_terminal___arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("param_terminal",p)
            self.Head = newNode
            return newNode

        @self.pg.production('loop : WHILE_LOOP OPEN_PAREN collation CLOSE_PAREN block ')
        def loop___WHILE_LOOP_OPEN_PAREN_collation_CLOSE_PAREN_block_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("while loop",p)
            self.Head = newNode
            return newNode

        @self.pg.production('loop : WHILE_LOOP OPEN_PAREN collation CLOSE_PAREN content_terminal ')
        def loop___WHILE_LOOP_OPEN_PAREN_collation_CLOSE_PAREN_content_terminal_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("while loop",p)
            self.Head = newNode
            return newNode

        @self.pg.production('loop : FOR_LOOP OPEN_PAREN for_part_1 SEMICOLON for_part_2 SEMICOLON for_part_3 CLOSE_PAREN block ')
        def loop___FOR_LOOP_OPEN_PAREN_for_part_1_SEMICOLON_for_part_2_SEMICOLON_for_part_3_CLOSE_PAREN_block_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("for loop",p)
            self.Head = newNode
            return newNode

        @self.pg.production('loop : FOR_LOOP OPEN_PAREN for_part_1 SEMICOLON for_part_2 SEMICOLON for_part_3 CLOSE_PAREN content_terminal ')
        def loop___FOR_LOOP_OPEN_PAREN_for_part_1_SEMICOLON_for_part_2_SEMICOLON_for_part_3_CLOSE_PAREN_content_terminal_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("for loop",p)
            self.Head = newNode
            return newNode

        @self.pg.production('loop : DO_LOOP block WHILE_LOOP OPEN_PAREN collation CLOSE_PAREN SEMICOLON ')
        def loop___DO_LOOP_block_WHILE_LOOP_OPEN_PAREN_collation_CLOSE_PAREN_SEMICOLON_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("do loop",p)
            self.Head = newNode
            return newNode

        @self.pg.production('loop : DO_LOOP content_terminal WHILE_LOOP OPEN_PAREN collation CLOSE_PAREN SEMICOLON ')
        def loop___DO_LOOP_content_terminal_WHILE_LOOP_OPEN_PAREN_collation_CLOSE_PAREN_SEMICOLON_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("do loop",p)
            self.Head = newNode
            return newNode

        @self.pg.production('branch : IF_BRANCH OPEN_PAREN collation CLOSE_PAREN if_body')
        def branch___IF_BRANCH_OPEN_PAREN_collation_CLOSE_PAREN_if_body(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("if",p)
            self.Head = newNode
            return newNode

        @self.pg.production('branch : IF_BRANCH OPEN_PAREN collation CLOSE_PAREN if_body if_expansion ')
        def branch___IF_BRANCH_OPEN_PAREN_collation_CLOSE_PAREN_if_body_if_expansion_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("if",p)
            self.Head = newNode
            return newNode

        @self.pg.production('if_body : block ')
        def if_body___block_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("if_body",p)
            self.Head = newNode
            return newNode

        @self.pg.production('if_body : content_terminal ')
        def if_body___content_terminal_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("if_body",p)
            self.Head = newNode
            return newNode

        @self.pg.production('if_expansion : ELSE_BRANCH if_body ')
        def if_expansion___ELSE_BRANCH_if_body_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("if_expansion",p)
            self.Head = newNode
            return newNode

        @self.pg.production('branch : SWITCH_BRANCH OPEN_PAREN arithmetic CLOSE_PAREN switch_body ')
        def branch___SWITCH_BRANCH_OPEN_PAREN_arithmetic_CLOSE_PAREN_switch_body_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("switch",p)
            self.Head = newNode
            return newNode

        @self.pg.production('switch_body : OPEN_BRACE case CLOSE_BRACE ')
        def switch_body___OPEN_BRACE_case_CLOSE_BRACE_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("switch_body",p)
            self.Head = newNode
            return newNode

        @self.pg.production('switch_body : OPEN_BRACE case COMMA cases CLOSE_BRACE ')
        def switch_body___OPEN_BRACE_case_COMMA_cases_CLOSE_BRACE_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("switch_body",p)
            self.Head = newNode
            return newNode

        @self.pg.production('cases : case COMMA cases ')
        def cases___case_COMMA_cases_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("cases",p)
            self.Head = newNode
            return newNode

        @self.pg.production('cases : case ')
        def cases___case_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("cases",p)
            self.Head = newNode
            return newNode

        @self.pg.production('cases : default ')
        def cases___default_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("cases",p)
            self.Head = newNode
            return newNode

        @self.pg.production('case : CASE value COLON ')
        def case___CASE_value_COLON_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("case",p)
            self.Head = newNode
            return newNode

        @self.pg.production('case : CASE value COLON case_body ')
        def case___CASE_value_COLON_case_body_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("case",p)
            self.Head = newNode
            return newNode

        @self.pg.production('default : DEFAULT COLON case_body ')
        def default___DEFAULT_COLON_case_body_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("default",p)
            self.Head = newNode
            return newNode

        @self.pg.production('case_body : block ')
        def case_body___block_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("case_body",p)
            self.Head = newNode
            return newNode

        @self.pg.production('case_body : content ')
        def case_body___content_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("case_body",p)
            self.Head = newNode
            return newNode

        @self.pg.production('goto : SELF_DEFINED COLON block ')
        def goto___SELF_DEFINED_COLON_block_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("goto",p)
            self.Head = newNode
            return newNode

        @self.pg.production('goto : SELF_DEFINED COLON content_terminal ')
        def goto___SELF_DEFINED_COLON_content_terminal_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("goto",p)
            self.Head = newNode
            return newNode

        @self.pg.production('goto : SELF_DEFINED COLON ')
        def goto___SELF_DEFINED_COLON_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("goto",p)
            self.Head = newNode
            return newNode

        @self.pg.production('response : RETURN arithmetic ')
        def response___RETURN_arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("return",p)
            self.Head = newNode
            return newNode

        @self.pg.production('response : RETURN function_call ')
        def response___RETURN_function_call_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("return",p)
            self.Head = newNode
            return newNode

        @self.pg.production('response : RETURN SELF_DEFINED ')
        def response___RETURN_SELF_DEFINED_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("return",p)
            self.Head = newNode
            return newNode

        @self.pg.production('response : RETURN ')
        def response___RETURN_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("return",p)
            self.Head = newNode
            return newNode

        @self.pg.production('response : GOTO SELF_DEFINED ')
        def response___GOTO_SELF_DEFINED_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("jump",p)
            self.Head = newNode
            return newNode

        @self.pg.production('response : BREAK ')
        def response___BREAK_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("break",p)
            self.Head = newNode
            return newNode

        @self.pg.production('response : CONTINUE ')
        def response___CONTINUE_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("continue",p)
            self.Head = newNode
            return newNode

        @self.pg.production('initialization : TYPE designation ')
        def initialization___TYPE_designation_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("initialization",p)
            self.Head = newNode
            return newNode

        @self.pg.production('initialization : TYPE SELF_DEFINED ')
        def initialization___TYPE_SELF_DEFINED_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("initialization",p)
            self.Head = newNode
            return newNode

        @self.pg.production('initialization : TYPE MUL designation ')
        def initialization___TYPE_MUL_designation_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("initialization",p)
            self.Head = newNode
            return newNode

        @self.pg.production('for_part_1 : initialization ')
        def for_part_1___initialization_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("for param 1",p)
            self.Head = newNode
            return newNode

        @self.pg.production('for_part_1 : ')
        def for_part_1___(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("for param 1",p)
            self.Head = newNode
            return newNode

        @self.pg.production('for_part_1 : designation ')
        def for_part_1___designation_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("for param 1",p)
            self.Head = newNode
            return newNode

        @self.pg.production('for_part_2 : collation ')
        def for_part_2___collation_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("for param 2",p)
            self.Head = newNode
            return newNode

        @self.pg.production('for_part_2 : ')
        def for_part_2___(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("for param 2",p)
            self.Head = newNode
            return newNode

        @self.pg.production('for_part_3 : designation ')
        def for_part_3___designation_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("for param 3",p)
            self.Head = newNode
            return newNode

        @self.pg.production('for_part_3 : ')
        def for_part_3___(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("for param 3",p)
            self.Head = newNode
            return newNode

        @self.pg.production('designation : SELF_DEFINED assignment arithmetic ')
        def designation___SELF_DEFINED_assignment_arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("designation",p)
            self.Head = newNode
            return newNode

        @self.pg.production('designation : SELF_DEFINED assignment function_call ')
        def designation___SELF_DEFINED_assignment_function_call_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("designation",p)
            self.Head = newNode
            return newNode

        @self.pg.production('designation : SELF_DEFINED OPEN_BRACK INTEGER CLOSE_BRACK assignment arithmetic ')
        def designation___SELF_DEFINED_OPEN_BRACK_INTEGER_CLOSE_BRACK_assignment_arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("designation",p)
            self.Head = newNode
            return newNode

        @self.pg.production('assignment : AEQ ')
        def assignment___AEQ_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("assignment",p)
            self.Head = newNode
            return newNode

        @self.pg.production('assignment : SEQ ')
        def assignment___SEQ_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("assignment",p)
            self.Head = newNode
            return newNode

        @self.pg.production('assignment : MEQ ')
        def assignment___MEQ_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("assignment",p)
            self.Head = newNode
            return newNode

        @self.pg.production('assignment : DEQ ')
        def assignment___DEQ_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("assignment",p)
            self.Head = newNode
            return newNode

        @self.pg.production('assignment : LSEQ ')
        def assignment___LSEQ_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("assignment",p)
            self.Head = newNode
            return newNode

        @self.pg.production('assignment : RSEQ ')
        def assignment___RSEQ_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("assignment",p)
            self.Head = newNode
            return newNode

        @self.pg.production('assignment : BOEQ ')
        def assignment___BOEQ_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("assignment",p)
            self.Head = newNode
            return newNode

        @self.pg.production('assignment : BAEQ ')
        def assignment___BAEQ_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("assignment",p)
            self.Head = newNode
            return newNode

        @self.pg.production('assignment : XEQ ')
        def assignment___XEQ_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("assignment",p)
            self.Head = newNode
            return newNode

        @self.pg.production('assignment : CEQ ')
        def assignment___CEQ_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("assignment",p)
            self.Head = newNode
            return newNode

        @self.pg.production('assignment : SET ')
        def assignment___SET_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("assignment",p)
            self.Head = newNode
            return newNode

        @self.pg.production('collation : collation comparison collation ')
        def collation___collation_comparison_collation_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("collation",p)
            self.Head = newNode
            return newNode

        @self.pg.production('collation : arithmetic ')
        def collation___arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("collation",p)
            self.Head = newNode
            return newNode

        @self.pg.production('comparison : EQ ')
        def comparison___EQ_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("comparison",p)
            self.Head = newNode
            return newNode

        @self.pg.production('comparison : LEQ ')
        def comparison___LEQ_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("comparison",p)
            self.Head = newNode
            return newNode

        @self.pg.production('comparison : GEQ ')
        def comparison___GEQ_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("comparison",p)
            self.Head = newNode
            return newNode

        @self.pg.production('comparison : NEQ ')
        def comparison___NEQ_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("comparison",p)
            self.Head = newNode
            return newNode

        @self.pg.production('comparison : LT ')
        def comparison___LT_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("comparison",p)
            self.Head = newNode
            return newNode

        @self.pg.production('comparison : GT ')
        def comparison___GT_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("comparison",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : arithmetic OR arithmetic ')
        def arithmetic___arithmetic_OR_arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("arithmetic",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : arithmetic AND arithmetic ')
        def arithmetic___arithmetic_AND_arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("arithmetic",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : arithmetic BOR arithmetic ')
        def arithmetic___arithmetic_BOR_arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("arithmetic",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : arithmetic XOR arithmetic ')
        def arithmetic___arithmetic_XOR_arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("arithmetic",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : arithmetic BAND arithmetic ')
        def arithmetic___arithmetic_BAND_arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("arithmetic",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : arithmetic LSH arithmetic ')
        def arithmetic___arithmetic_LSH_arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("arithmetic",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : arithmetic RSH arithmetic ')
        def arithmetic___arithmetic_RSH_arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("arithmetic",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : arithmetic ADD arithmetic ')
        def arithmetic___arithmetic_ADD_arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("arithmetic",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : arithmetic SUB arithmetic ')
        def arithmetic___arithmetic_SUB_arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("arithmetic",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : arithmetic MUL arithmetic ')
        def arithmetic___arithmetic_MUL_arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("arithmetic",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : arithmetic DIV arithmetic ')
        def arithmetic___arithmetic_DIV_arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("arithmetic",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : arithmetic MOD arithmetic ')
        def arithmetic___arithmetic_MOD_arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("arithmetic",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : ADD arithmetic ')
        def arithmetic___ADD_arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("unary",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : SUB arithmetic ')
        def arithmetic___SUB_arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("unary",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : NOT arithmetic ')
        def arithmetic___NOT_arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("unary",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : COMP arithmetic ')
        def arithmetic___COMP_arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("unary",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : OPEN_PAREN TYPE CLOSE_PAREN arithmetic ')
        def arithmetic___OPEN_PAREN_TYPE_CLOSE_PAREN_arithmetic_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("unary",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : INC SELF_DEFINED ')
        def arithmetic___INC_SELF_DEFINED_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("unary",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : DEC SELF_DEFINED ')
        def arithmetic___DEC_SELF_DEFINED_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("unary",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : SELF_DEFINED INC ')
        def arithmetic___SELF_DEFINED_INC_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("unary",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : SELF_DEFINED DEC ')
        def arithmetic___SELF_DEFINED_DEC_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("unary",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : OPEN_PAREN arithmetic CLOSE_PAREN ')
        def arithmetic___OPEN_PAREN_arithmetic_CLOSE_PAREN_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("arithmetic",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : value ')
        def arithmetic___value_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("arithmetic",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : SELF_DEFINED ')
        def arithmetic___SELF_DEFINED_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("arithmetic",p)
            self.Head = newNode
            return newNode

        @self.pg.production('arithmetic : function_call ')
        def arithmetic___function_call_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("arithmetic",p)
            self.Head = newNode
            return newNode

        @self.pg.production('value : INTEGER ')
        def value___INTEGER_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("value",p)
            self.Head = newNode
            return newNode

        @self.pg.production('value : PRECISION ')
        def value___PRECISION_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("value",p)
            self.Head = newNode
            return newNode

        @self.pg.production('value : CHAR ')
        def value___CHAR_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("value",p)
            self.Head = newNode
            return newNode

        @self.pg.production('value : HEX ')
        def value___HEX_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("value",p)
            self.Head = newNode
            return newNode

        @self.pg.production('value : OCT ')
        def value___OCT_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("value",p)
            self.Head = newNode
            return newNode

        @self.pg.production('value : BIN ')
        def value___BIN_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("value",p)
            self.Head = newNode
            return newNode

        @self.pg.production('value : NULL ')
        def value___NULL_(p):
            """
            Boilerplate BNF function
            
            Args:
                p: The matching set of tokens.

            Returns:
                The node of the ParseTree.
            """
            newNode = ParseTree("value",p)
            self.Head = newNode
            return newNode

    
        @self.pg.error
        def error_handle(token):
            """
            Boilerplate error handling function
            
            Args:
                token: The token that caused an error.
            """
            return ValueError(token)

    #boilerplate function
    def get_parser(self):
        """
        Retrieves the built version of the parser.

        Returns:
            The built parser.
        """
        return self.pg.build()

    #retrieve the trees head
    def getTree(self):
        """
        Getter for the head of the tree.

        Returns:
            The head of the tree.
        """

        return self.Head

    def print_error(self):
        """
        Prints parser error message. This function ultimately iterates through the ParseTree that was returned after the parser found an error. ParseTree's consist of tokens as well as other ParseTree's so we need to iterate to find the first token and then print its source position.
        """
        # TODO: add some more in-depth error processing to print
        # out a more detailed description of what went wrong, and possibly some suggestions 
        # at to why there was a parse/syntax error. (i.e. suggest a missing semicolon)

        head = self.getTree()
        token = 0 # token hasn't been found yet, so we set value to 0

        while True and head:
            # Iterate through list of elements
            for i in head.content:

                # Could be a Token
                if(type(i) == type(Token("sample", "sample"))):

                    # Found a Token
                    token = i
                    break

            # Check again (to break out of while loop and not iterate again)		
            if (type(token) == type(Token("sample", "sample"))):
                break
            else:
                # Set head to last element.
                # If this code executes then I can assume that the 
                # last element is an ParseTree.
                head = head.content[len(head.content)-1]

        if token:
            print(f"ParsingError: Last token  \'{token.value}\' parsed successfully at, {token.source_pos}\n")
        else:
            # Never found a token to report, need to exit
            print("ParsingError: No ParseTree obtained\n")
            exit()



    