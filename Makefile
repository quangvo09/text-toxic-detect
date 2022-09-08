install:
	pip3 install -r requirements.txt

run:
	export FLASK_APP=main.py && python3 -m flask run

train:
	cd profanity_check && python3 train.py && cd ..