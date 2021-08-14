FROM garima-rathore/Phoenix:latest

#clonning repo 
RUN git clone https://github.com/garima-rathore/Probable-garuda.git /root/Phoenix

#working directory 
WORKDIR /root/Phoenix

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","Phoenix"]
