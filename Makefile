MAIN_FILE = "src/Main.py"

.PHONY: $(MAIN_FILE)

compile: $(MAIN_FILE)
		pyinstaller --onefile $^

run: $(MAIN_FILE)
		py $^