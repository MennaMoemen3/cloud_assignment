FROM python:3.9
RUN pip install nltk
WORKDIR /appy
COPY main_count.py /appy/
COPY cleaned_paragraphs.txt /appy/
CMD [ "python","main_count.py","cleaned_paragraphs.txt"]