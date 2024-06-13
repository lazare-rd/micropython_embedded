SRC = merge_sort.py
TARGET = micropython_embed/python_script.h

build:
	python3 py_to_txt.py $(SRC) $(TARGET)