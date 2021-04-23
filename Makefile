install:
	pip install -r requirements.txt


restore:
	rm main.spec && mv main.spec-e main.spec
