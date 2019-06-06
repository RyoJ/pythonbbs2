データベース構築手順（大枠、プロジェクト、アプリ、モデル、データベース）
mkdir xxx
cd xxx
django-admin startproject yyy .
python3 manage.py migrate =>sqlite3の作成
python3 manage.py startapp zzz
yyy/setting.pyのINSTALLED_APPに’zzz’を追加
zzz/models.pyにモデルを作成
python3 manage.py makemigrations zzz => 0001_initial.pyを作成
python3 manage.py migrate zzz => モデルにそってデータベースが作られた
zzz/admin.pyに登録フォームのテンプレを表示できるようにする
編集表示でモデル通りの設計(titileのみ)になっているのを確認

＝＞Pythonでログイン機構のある簡単なデータベースを作成（GitHub案件）
