CC = gcc
COMPILE_PATH = $(shell pwd)
#!using shell to get the path of the folder
#NOPRINT_SUPPORT    ?= yes

SRC = $(wildcard *.c) 
#!get all XXX.c files
SRC += $(wildcard $(COMPILE_PATH)/src/*.c)
OBJ = $(SRC:%.c=%.o)
#!turn them to object and save in OBJ

CFLAGS = -g
CFLAGS += -I $(COMPILE_PATH)/inc/
#!-I help compiler find the headers

ifeq ($(NOPRINT_SUPPORT), yes)
CFLAGS += -DNOPRINT_SUPPORT
endif
#!-D equals to define in C  

#LIBS +=

all:depend goBalance

#sinclude $(SRC:%.c=%.d)
depend:
#!automatically getting all headers that need 2 be include
#	$(CC) $(CFLAGS) -MM -MP -MT $@ -MF $(@:%.o=%.d) $<
	$(CC) -MM $(CFLAGS) $(SRC) > .depend

-include .depend

goBalance:$(OBJ)
#!linking
#	$(LINK.c) $^ -o $@	
	$(CC) $(CFLAGS) -o $@ $(OBJ)

#$(OBJ):$(SRC)
#!wrong one
%.o:%.c
#!compiling
#	$(COMPILE.c) $(CFLAGS) $< -o $@
	$(CC) -c $(CFLAGS) $< -o $@
#	$(CC) -c $< -o $@

.PHONY: clean all
clean:
	@rm -f $(OBJ)
	@rm -f goBalance
	@rm -f .depend
