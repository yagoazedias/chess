install:
	pip install -r requirements.txt

echo:
	echo "Hello World"

restore:
	rm main.spec && mv main.spec-e main.spec
