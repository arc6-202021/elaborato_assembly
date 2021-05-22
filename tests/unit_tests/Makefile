
ASSEMBLY_FOLDER=../../code/assembly/src
OBJ_FILES=obj/test_is_operator.o obj/is_operator.o obj/test_is_operand.o obj/is_operand.o obj/test_is_valid_char.o obj/is_valid_char.o obj/test_addizione.o obj/addizione.o obj/test_sottrazione.o obj/sottrazione.o obj/test_divisione.o obj/divisione.o obj/test_prodotto.o obj/prodotto.o obj/test_itoa.o obj/itoa.o obj/test_all.o

all: clean bin/test_all bin/test_validations

# VERIFICA CORRETTEZZA

obj/test_is_operator.o:
	mkdir -p obj
	gcc -g -c -m32 test_is_operator.c -o obj/test_is_operator.o

obj/is_operator.o:
	mkdir -p obj
	gcc -g -c -m32 $(ASSEMBLY_FOLDER)/is_operator.s -o obj/is_operator.o


obj/test_is_operand.o:
	mkdir -p obj
	gcc -g -c -m32 test_is_operand.c -o obj/test_is_operand.o

obj/is_operand.o:
	mkdir -p obj
	gcc -g -c -m32 $(ASSEMBLY_FOLDER)/is_operand.s -o obj/is_operand.o


obj/test_is_valid_char.o:
	mkdir -p obj
	gcc -g -c -m32 test_is_valid_char.c -o obj/test_is_valid_char.o

obj/is_valid_char.o:
	mkdir -p obj
	gcc -g -c -m32 $(ASSEMBLY_FOLDER)/is_valid_char.s -o obj/is_valid_char.o


# OPERAZIONI MATEMATICHE

obj/test_addizione.o:
	mkdir -p obj
	gcc -g -c -m32 test_addizione.c -o obj/test_addizione.o

obj/addizione.o:
	mkdir -p obj
	gcc -g -c -m32 $(ASSEMBLY_FOLDER)/addizione.s -o obj/addizione.o


obj/test_sottrazione.o:
	mkdir -p obj
	gcc -g -c -m32 test_sottrazione.c -o obj/test_sottrazione.o

obj/sottrazione.o:
	mkdir -p obj
	gcc -g -c -m32 $(ASSEMBLY_FOLDER)/sottrazione.s -o obj/sottrazione.o


obj/test_divisione.o:
	mkdir -p obj
	gcc -g -c -m32 test_divisione.c -o obj/test_divisione.o

obj/divisione.o:
	mkdir -p obj
	gcc -g -c -m32 $(ASSEMBLY_FOLDER)/divisione.s -o obj/divisione.o


obj/test_prodotto.o:
	mkdir -p obj
	gcc -g -c -m32 test_prodotto.c -o obj/test_prodotto.o

obj/prodotto.o:
	mkdir -p obj
	gcc -g -c -m32 $(ASSEMBLY_FOLDER)/prodotto.s -o obj/prodotto.o


obj/test_itoa.o:
	mkdir -p obj
	gcc -g -c -m32 test_itoa.c -o obj/test_itoa.o

obj/itoa.o:
	mkdir -p obj
	gcc -g -c -m32 $(ASSEMBLY_FOLDER)/itoa.s -o obj/itoa.o


# MAIN

obj/test_all.o:
	mkdir -p obj
	gcc -g -c -m32 test_all.c -o obj/test_all.o

bin/test_all: $(OBJ_FILES)
	mkdir -p bin
	gcc -m32 $(OBJ_FILES) -o bin/test_all


obj/test_validations.o:
	mkdir -p obj
	gcc -g -c -m32 test_validations.c -o obj/test_validations.o

bin/test_validations: obj/is_operand.o obj/is_operator.o obj/is_valid_char.o obj/test_is_operand.o obj/test_is_operator.o obj/test_is_valid_char.o obj/test_validations.o
	mkdir -p bin
	gcc -m32 obj/is_operand.o obj/is_operator.o obj/is_valid_char.o obj/test_is_operand.o obj/test_is_operator.o obj/test_is_valid_char.o obj/test_validations.o -o bin/test_validations

clean:
	rm -rf obj/*.o
	rm -rf bin/*
