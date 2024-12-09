import sys
from compiler import init_logging as il

from compiler.jack_tokenizer import JackTokenizer
from compiler.compilation_engine import CompilationEngine
from compiler.enumerations.SubRoutineType import SubRoutineType

def main(path, log_level, dest_path):
    print(f"path: {path}\nlog_level: {log_level}\ndest_path: {dest_path}")
    il.set_level(log_level)
    with CompilationEngine(dest_path) as ce, JackTokenizer(path) as jt:
        try:
            ce.set_tokenizer(jt)
        except Exception as e:
            print(e)
        ce.compile()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])


# py JackAnalyzer.py C:\Users\samue\Documents\Nand2Tetris\06-08_10-11\10\test\test.jack i .\output.xml
# cd C:\Users\samue\Documents\Nand2Tetris\06-08_10-11\compiler
# py JackAnalyzer.py C:\Users\samue\Documents\Nand2Tetris\06-08_10-11\10\Square\Main.jack d .\output.xml
# py JackAnalyzer.py C:\Users\samue\Documents\Nand2Tetris\06-08_10-11\10\ArrayTest\Main.jack i .\output.xml
# py JackAnalyzer.py C:\Users\samue\Documents\Nand2Tetris\06-08_10-11\10\ExpressionLessSquare\Main.jack i .\output.xml

# py -m compiler.JackAnalyzer C:\Users\samue\Documents\Nand2Tetris\06-08_10-11\10\ExpressionLessSquare\Main.jack i .\output.xml
# py -m unittest test.compiler.test_intgn