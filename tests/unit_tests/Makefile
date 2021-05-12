
ASSEMBLY_FOLDER=../../code/assembly/src
OBJ_FILES=obj/test_is_operator.o obj/is_operator.o obj/test_all.o

all: clean bin/test_all

obj/test_is_operator.o:
	mkdir -p obj
	gcc -g -c -m32 test_is_operator.c -o obj/test_is_operator.o

obj/is_operator.o:
	mkdir -p obj
	gcc -g -c -m32 $(ASSEMBLY_FOLDER)/is_operator.s -o obj/is_operator.o

obj/test_all.o:
	mkdir -p obj
	gcc -g -c -m32 test_all.c -o obj/test_all.o

bin/test_all: $(OBJ_FILES)
	mkdir -p bin
	gcc -m32 $(OBJ_FILES) -o bin/test_all

clean:
	rm -rf obj/*.o
	rm -rf bin/*
