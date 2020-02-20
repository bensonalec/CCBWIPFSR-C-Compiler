"""
This module acts as the interface for running all the seperate portions of the front end. It allows
for command line arguments that can be used to determine which portion is run.
"""
import argparse
import importlib
import traceback
import sys

from rply.errors import LexingError
from copy import deepcopy

lex = importlib.import_module("lexer", __name__)
par = importlib.import_module("parser", __name__)
btp = importlib.import_module("bnfToParser", __name__)
ast = importlib.import_module("AST_builder", __name__)
sem = importlib.import_module("semantics", __name__)


def getTree(head,level):
    """
    Outputs a string version of the ParseTree that can be used in unit testing. Calls itself recursively

    Args:
        head: The head node of the tree.
        level: The current level of the tree.
    
    Returns:
        A string of the nodes in the tree.
    """
    level += 1
    token = head.token
    content = head.content
    li = []
    out = ""
    for node in content:
        if(type(node) != type(par.ParseTree("sample","sample"))):
            li.append(node)
        else:
            li.append(node.token)
    
    out = (level,li)


    #iterate through the components of the BNF
    for node in content:
        if(type(node) == type(par.ParseTree("sample","sample"))):
            out += getTree(node,level)
    return out


def print_tokens(tokens):
    """
    Prints tokens returned from Lexer

    Args:
        tokens: Tokens generated from the Lexer
    """
    print(lex.tokensToString(deepcopy(tokens)))


def print_list_view(head,level):
    """
    Prints a simple list version of the tree for output. Calls itself recursively

    Args:
        head: The head node of the tree.
        level: The current level of the tree.
    """
    level += 1
    token = head.token
    content = head.content
    li = []
    out = ""
    for node in content:
        if(type(node) != type(par.ParseTree("sample","sample"))):
            li.append(node)
        else:
            li.append(node.token)
    
    print(level,":",li)


    #iterate through the components of the BNF
    for node in content:
        if(type(node) == type(par.ParseTree("sample","sample"))):
            print_list_view(node,level)


def pprint_tree(node, file=None, _prefix="", _last=True):
    """
    Prints the ParseTree in depth first order

    Args: 
        node: The head node of the tree.
        file: The file to be written to (Defaults to Stdout).
        _prefix: A string indicating the spacing from the left side of the screen.
        _last: A boolean that indicates if a node is the last in it's immediate surroundings.
    """
    if type(node) == type(par.ParseTree("test", "test")):
        print(_prefix, "`-- " if _last else "|-- ", node.token, sep="", file=file)
        _prefix += "    " if _last else "|   "
        child_count = len(node.content)
        for i, child in enumerate(node.content):
            _last = i == (child_count - 1)
            pprint_tree(child, file, _prefix, _last)
    else:
        print(_prefix, "`-- " if _last else "|-- ", node, sep="", file=file)

def main(args, fi):
    """
    The main function of the frontend, takes in command line input via an object from argparse, and the name of the file.
    
    Args:
        args: The object that contains the command line arguements.
        fi: The file object that is open.
    """

    if args.bnf:
        btp.main(args.bnf)
        importlib.reload(par)
    

    try:

        #print(sys.modules)

        #Read in file
        text_input = fi.read()
        fi.close()

        #setup lexer, produce tokens, check for invalid tokens
        lexer = lex.Lexer().get_lexer()
        tokens = lexer.lex(text_input)
        lex.validateTokens(tokens)
        
        if args.lex or args.all:
            # Print the tokens from the lexer 
            print_tokens(tokens)

        #set up parser and parse the given tokens
        pg = par.Parser()
        pg.parse()
        parser = pg.get_parser()
        parser.parse(tokens)

        # Retrieve the head of the parse tree
        head = pg.getTree()

        if args.tree or args.all:
            # Represent parse tree as a list with levels
            print_list_view(head, 0)

        if args.all:
            # Represent parse tree as single line (mainly for unit testing)
            print(getTree(head, 0)) 

        if args.pretty or args.all:
            # Pretty print parse tree
            pprint_tree(head)

        # Build Abstract Syntax Tree
        astree = ast.buildAST(head)

        if args.ast or args.all:
            # Pretty print AST
            ast.print_AST(astree)

        # Initialize symbol table and begin semantic analysis
        sym = sem.symbol_table(astree)
        sym.analyze()

        if args.symbol_table or args.all:
            sym.print_symbol_table()
            print ("")
            sym.print_unknown_symbols()

    except LexingError as err:
        print("Received error(s) from token validation. Exiting...")
        exit()

    except AssertionError as err:
        # parser has it's own detailed error printing
        pg.print_error()
        print("Received AssertionError(s) from parser, continuing with what was parsed...\n")

    except BaseException as err:
        traceback.print_exc()
        print(f"Unrecoverable exception occured. Exiting...")
        exit()

    return astree, sym

if __name__ == "__main__":
    #command line arguements

    #decription of the comiler
    cmd_options = argparse.ArgumentParser(description='Frontend of the compiler. Can produce tokens and syntax tree')
    
    cmd_options.add_argument('--all',help='Prints out all intermediate representations as they are encountered in the compilation process', action="store_true")

    #input file option
    cmd_options.add_argument('input_file', metavar='<filename.c>', type=str, help='Input c file.')
    
    #Arguement to print tokens from lexer
    cmd_options.add_argument('-l','--lex', help='Prints out tokens from lexer', action='store_true')

    #Prints string representation of parse tree....
    cmd_options.add_argument('-t','--tree', help='Prints string representation of parse tree.', action="store_true")

    cmd_options.add_argument('-p','--pretty',help='Prints a pretty verision of the tree, and does not print the tokens', action="store_true")

    #Print all output from lexer, parser, etc....
    cmd_options.add_argument('-a','--ast', help='Prints out the abstract syntax tree.', action="store_true")

    cmd_options.add_argument('-s','--symbol_table', help='Prints out the known and unknown symbols encountered during semantic analysis.', action="store_true")

    cmd_options.add_argument('-b', '--bnf', nargs='?', const='./BNF_definition', type=str, help='Rebuilds the parser using the current BNF grammar')


    #generate arguements
    args = cmd_options.parse_args()


    #open file and pass into main.
    if args.input_file and args.input_file.endswith(".c"):
        fi = open(args.input_file, "r")
    else:
        #if not c file.
        if not args.input_file.endswith(".c"):
            print("Error file must end with .c")
        cmd_options.print_help()
        exit()
    main(args, fi)

