FROM python:3

ADD TicTacToe.py /

RUN pip3 install pygame

CMD [ "python3", "./TicTacToe.py" ]
