MAIN_FILE = "src/Main.pyw"

.PHONY: $(MAIN_FILE)

compile: $(MAIN_FILE)
		pyinstaller --onefile $^

run: $(MAIN_FILE)
		py $^