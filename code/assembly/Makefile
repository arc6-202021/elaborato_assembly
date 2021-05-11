
all: bin/postfix

bin/postfix:
	mkdir -p bin
	gcc -m32 src/main.c src/postfix.s -o bin/postfix

dev_mode:
	mkdir -p bin
	gcc -g -m32 src/main.c src/postfix.s -o bin/postfix
