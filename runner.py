import sys
try:
    import tagscript
    from tagscript import Interpreter
    from tagscript.blocks import MathBlock, RandomBlock, ReplaceBlock

    blocks = [MathBlock(), RandomBlock(), ReplaceBlock()]
    engine = Interpreter(blocks)
    
    with open(sys.argv[1], "r") as f:
        content = f.read()

    result = engine.process(content)
    print("Output:", result.body)
except ImportError:
    print("TagScript-Engine is not installed. Please install it using 'pip install TagScript-Engine'.")
