import sys
import os

# 将项目根目录添加到 sys.path 中，以便导入 src 模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import hello_world

def test_hello_world():
    assert hello_world() == "Hello, Python_test!"
