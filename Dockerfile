FROM python:3.8

ADD sunbot.py /
ADD key /

RUN pip install requests
RUN pip install discord.py
RUN pip install markovchain

CMD [ "python", "./sunbot.py" ]
