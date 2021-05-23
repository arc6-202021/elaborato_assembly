
SOURCE_FILES= src/main.c src/postfix.s src/addizione.s src/sottrazione.s src/divisione.s src/prodotto.s src/itoa.s src/write_result.s src/is_valid_char.s src/is_operand.s src/is_operator.s

all: clean bin/postfix

bin/postfix:
	mkdir -p bin
	gcc -m32 $(SOURCE_FILES) -o bin/postfix

dev_mode:
	mkdir -p bin
	gcc -g -m32 $(SOURCE_FILES) -o bin/postfix

clean:
	rm -rf bin/postfix
