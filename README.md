onion
=====

onion code - small site management tools.

*使い方*

まだ諸々テスト中ですし、onionコメントの書き方次第ではサイトを壊す可能性がありますので、ご利用の際にはサイトのバックアップを行なってからお願いします。

以下のようなディレクトリ構成で、サイトを作成しているとして、

/var/www/html/（ここがドキュメントルート）

**/var/www/onion/に onion code 一式を置く**

つまり、ドキュメントルートの１個上の階層にonionディレクトリ一式を置きます。
そして、ドキュメントルートの１個上の階層に移動しておきます。

cd /var/www

**onion code にドキュメントルートのディレクトリ名を登録する**

ドキュメントルートのディレクトリ名が「html」であれば、特に何もする必要が無いですが、それ以外のディレクトリ名の場合は、configを登録します。

書式
python onion/config.py path ディレクトリ名

例：ドキュメントルートのディレクトリ名がhtmlではなくhtdocsの場合
python onion/config.py path htdocs

**HTMLの共通パーツにonion-code用コメントを埋め込む**

ヘッダー部やメニュー部やフッター部等の共通パーツを使いまわす為の準備として、onion-codeを埋め込みます。

書式は、
<!–onion_tpl:name–>
コード部
<!–/onion_tpl:name–>

こんな感じではさんだところが共通パーツとして更新されます。
いくつ登録してもOK。ただしnameはユニークなものにします。

**共通パーツを onion code に登録する**

書式
python onion/make.py HTMLファイル名

例として、共通パーツを埋め込んだHTMLファイルが /var/www/html/index.html だとして、以下を実行します。

python onion/make.py html/index.html
もしくは
python onion/make.py index.html

エラーが無ければ、これで共通パーツが登録されます。
また、複数ファイルに異なる共通パーツがある場合でも、それぞれをmake.pyすればOKです。

**その他HTMLファイルにも onion code 用コメントを埋め込む**

書式は上記のものと同一です。
ただし、ここではコメント内は空でもOK。

**共通パーツを一括更新する**

以下を実行する事で、ドキュメントルート内の onion code 用コメント内コンテンツが一括更新されます。

python onion/refresh.py

**その後、共通パーツに更新があった場合のフロー**

例として、
/var/www/html/index.html
の共通パーツ内を更新したり、共通パーツを増やして onion code 用コメントを増やした場合は、都度、

python onion/make.py index.html
python onion/refresh.py

と実行すると、サイト内HTMLが全て更新されます。

