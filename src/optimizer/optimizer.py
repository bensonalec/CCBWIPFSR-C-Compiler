"""
This module serves as the main interface to the optimization process in order to streamline the compiler.
"""

from inspect import getsourcefile
import os
import argparse
from importlib.machinery import SourceFileLoader

ir1 = SourceFileLoader("IR_Lv1_Builder", f"{os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))}/IR_Lv1_Builder.py").load_module()
import_ir = SourceFileLoader("import_ir", f"{os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))}/import_ir.py").load_module()

def main(args, astHead = None, symbolTable = None):
    """
    This is the function that when given an AST and a symbol table will produce linear intermediate representations for teh inputted program.

    Args:
        args: The commandline arguments that belong to the optimizer.
        astHead: The root node of the AST.
        symbolTable: The list of valid entries throughout the program.

    Returns:
        The lowest level of IR produced.
    """
    l1ir = None
    # Import IR from file
    if args.input:
        ir = import_ir.import_ir(args.input)
        ir.tokenize()
        ir.parse()
        

    # Generate IR from AST and Symbol-Table
    else:
        try:
            ir = ir1.LevelOneIR(astHead, symbolTable)
            l1ir = ir.construct()
        except IndexError as err:
            print("Issue in creating IR")
            exit()
        if(l1ir == None):
            print("Issue in creating IR")
            exit()

    ir.optimize(args.opt)

    # Output IR to a file
    if args.IRout:
        write_IR_to_file(args.IRout, ir.IR)

    # Output IR (first lvl optimization) to stdout 
    if args.ir or args.all:
        print(str(ir))

    return ir


def write_IR_to_file(filename, ir):
    """
    Outputs IR to the given file

    Args:
        filename: The given file to write to
        ir: List of irLines each containing irNodes with IR instructions
    """
    with open(filename, 'w') as f:
        for irLine in ir:
            for irNode in irLine.treeList:
                f.write(str(irNode) + '\n')


if __name__ == "__main__":
    cmd_options = argparse.ArgumentParser(description='Optimizer of the compiler. Can take in an AST and Symbol Table or a File with an IR')

    cmd_options.add_argument('--all',help='Prints out all intermediate representations as they are encountered in the compilation process', action="store_true")
    cmd_options.add_argument('-O', '--opt', type=int, choices=range(3), default=0, help='Determines the optimization level')
    cmd_options.add_argument('-ir',help='Output the first level of IR in the optimizer phase', action="store_true")
    cmd_options.add_argument('-i', action='store', dest="input", type=str, help="Used to input IR from file")
    cmd_options.add_argument('--IRout', metavar='<output-filename>', type=str, default=None, help="Used to output the final generated IR to a file")
    
    args = cmd_options.parse_args()
    mainAST(args)
