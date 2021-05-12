
SOURCE_FILES= src/main.c src/postfix.s src/is_operator.s

all: clean bin/postfix

bin/postfix:
	mkdir -p bin
	gcc -m32 $(SOURCE_FILES) -o bin/postfix

dev_mode:
	mkdir -p bin
	gcc -g -m32 $(SOURCE_FILES) -o bin/postfix

clean:
	rm bin/postfix
