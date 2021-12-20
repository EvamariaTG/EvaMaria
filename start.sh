if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Maverick080685/Maverick080685.git /Maverick080685
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Maverick080685
fi
cd /Maverick080685
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
