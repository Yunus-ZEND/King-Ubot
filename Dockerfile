# Docker Tag Images, Using Python Slim Buster.
FROM apiskinguserbot/kingubot:Buster
# ===========================================
#               King - Ubot
# ===========================================
RUN git clone -b King-Ubot https://github.com/apisuserbot/King-Ubot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --no-cache-dir --upgrade pip setuptools
WORKDIR /root/userbot

# Install Requirements Packages
RUN pip3 install --no-cache-dir -r https://raw.githubusercontent.com/apisuserbot/King-Ubot/King-Ubot/requirements.txt

# Finishim
CMD ["python3","-m","userbot"]
