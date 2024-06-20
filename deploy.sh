#!/bin/bash
set +xe

CH="47289635"
wget https://github.com/TelegramPlayGround/TG-APIs/raw/${CH}/scrape.py -O scrape.py
wget https://github.com/TelegramPlayGround/TG-APIs/raw/${CH}/scrape_tg_api_schema.py -O scrape_tg_api_schema.py
wget https://github.com/TelegramPlayGround/TG-APIs/raw/${CH}/requirements.txt -O requirements.txt
wget https://github.com/TelegramPlayGround/tl-to-json/raw/578a821/bin.js
wget https://github.com/TelegramPlayGround/tl-to-json/raw/578a821/index.js

pip install -r requirements.txt

IFS="
"

python scrape.py
python scrape_tg_api_schema.py "https://core.telegram.org/schema" "core.tl"
python scrape_tg_api_schema.py "https://corefork.telegram.org/schema" "corefork.tl"
python scrape_tg_api_schema.py "https://blogfork.telegram.org/schema" "blogfork.tl"
wget -O tdesktop.tl "https://github.com/telegramdesktop/tdesktop/raw/dev/Telegram/SourceFiles/mtproto/scheme/api.tl"
wget -O tdlib.tl "https://github.com/tdlib/td/raw/master/td/generate/scheme/telegram_api.tl"
node bin.js tdesktop.tl tdesktop.json
node bin.js core.tl core.json
node bin.js corefork.tl corefork.json
node bin.js blogfork.tl blogfork.json
node bin.js tdlib.tl tdlib.json

git checkout data

git config --global user.email "johnprestonmail@gmail.com"
git config --global user.name "GitHub Action <John Preston>"
git add tdesktop.tl tdesktop.json
git commit -m "update tDesktop API scheme"

git config --global user.email "durov2005@gmail.com"
git config --global user.name "GitHub Action <Pavel Durov>"
git add *.tl *.json
git commit -m "update OW (3) API scheme"

git config --global user.email "levlam@telegram.org"
git config --global user.name "GitHub Action <Aliaksei Levin>"
git add tdlib.tl tdlib.json
git commit -m "update TDLib API scheme"

git config --global user.email "igor.beatle@gmail.com"
git config --global user.name "GitHub Action <Igor Zhukov>"
git add botapi.json botapi.min.json botapiblogfork.json botapiblogfork.min.json botapicorefork.json botapicorefork.min.json
git commit -m "update BOT API docs"

git clone https://github.com/LonamiWebs/Telethon /tmp/Telethon/
a=$(pwd)
rm -rf Telegram
mkdir -p Telegram
cd /tmp/Telethon/
git checkout v1
cp "${a}/tdesktop.tl" /tmp/Telethon/telethon_generator/data/api.tl
python setup.py gen docs
mv docs/* "${a}/Telegram/"
cd "${a}"
# there's probably better ways but we know none has spaces
rm -rf /tmp/Telethon/
cd "${a}/Telegram/"
git config --global user.email "totufals@hotmail.com"
git config --global user.name "GitHub Action <Lonami Exo>"
git add constructors/ types/ methods/ index.html 404.html js/search.js css/ img/
git commit -m "Update documentation"
cd "${a}"

git clone https://github.com/Lonami/tl-differ /tmp/tldiff/
a=$(pwd)
rm -rf TL/
mkdir -p TL/diff/
cd /tmp/tldiff/
git remote add fork1 https://github.com/TelegramPlayGround/tl-differ
git fetch fork1
git cherry-pick 34f99231c069d596460580251fbd77055406d194
git cherry-pick 94c871d69c69e3e349589de8911a97a5bf498ec7
git cherry-pick 5c6e56c78b5fa6bb9cbd4bd0b6fb66b11badd6dc
FQDN="https://telegramplayground.github.io/TG-APIs/TL/diff" GH="https://github.com/telegramdesktop/tdesktop/" python get-all-tl.py
cp app.js atom.xml diff.js "${a}/TL/diff/"
mv index.html "${a}/TL/diff/tdesktop.html"
mkdir -p "${a}/TL/diff/schemes/tDesktop"
mv schemes/* "${a}/TL/diff/schemes/tDesktop/"
rm -rf tdesktop schemes
git cherry-pick f89b89c4ca49f2d9330ea6bcbf0280cc6ce78624
FQDN="https://telegramplayground.github.io/TG-APIs/TL/diff" TDLIBGH="https://github.com/tdlib/td" python get-all-tl.py
cp tdatom.xml tddiff.js  "${a}/TL/diff/"
mv index.html "${a}/TL/diff/tdlib.html"
mv app.js "${a}/TL/diff/tdapp.js"
mkdir -p "${a}/TL/diff/schemes/TDLib"
mv schemes/* "${a}/TL/diff/schemes/TDLib/"
rm -rf tdesktop schemes
cd "${a}"
rm -rf /tmp/tldiff/
git add TL -A
# git config --global user.email "totufals@hotmail.com"
# git config --global user.email "johnprestonmail@gmail.com"
git config --global user.email "durov2005@gmail.com"
git config --global user.name "GitHub Action <Lonami Exo> | GitHub Action <John Preston>"
git commit -m "Update new Layer Diff"

git push origin data
