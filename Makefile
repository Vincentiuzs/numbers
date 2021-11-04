JAVAC  = javac
SRCDIR = src
BINDIR = bin

.SUFFIXES: .java .class

$(BINDIR)/%.class:$(SRCDIR)/%.java
	$(JAVAC) -d $(BINDIR)/ -cp $(BINDIR) $<

CLASSES = Palindrome.class
CLASS_FILES = $(CLASSES:%.class=$(BINDIR)/%.class)

default: $(CLASS_FILES)

clean:
	rm $(BINDIR)/*
	rmdir $(BINDIR)/

palindrome:
	java -cp bin Palindrome


