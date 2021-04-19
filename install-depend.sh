apt-get install -y python3 python3-pip python3-dev build-essential git
apt-get install -yqq unzip curl
git clone https://github.com/rlatn1234/KT_Internet_Reset_Python
cd KT_Internet_Reset_Python
wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/