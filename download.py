import os
from gppt import GetPixivToken
from pixivpy3 import AppPixivAPI
from time import sleep

# フォルダの作成
if not os.path.exists("./pixiv_images"):
    os.mkdir("./pixiv_images")

# pixivのrefresh_tokenの取得
print('認証の開始')
g = GetPixivToken()

# userにメールアドレス, pass_パスワードを入れる
res = g.login(headless=True, user="ここにメールアドレスを入れる", pass_="ここにパスワードを入れる")
refresh_token = res['refresh_token']
user_id = res['user']['id']

# login
api = AppPixivAPI()
api.auth(refresh_token=refresh_token)
print('認証終了')

# ブックマークした画像のjsonを取得
users_data = api.user_bookmarks_illust(user_id, restrict='public')

# なぜかAPIが30枚分の情報しかとってこないので30枚ごとを確認する変数
count = 1

#全体の画像の枚数をカウントする変数
allCount = 1

def downloadImage(users_data, count, allCount):

    # イラストの数だけ繰り返す
    ilustNum = len(users_data.illusts)
    for illust in users_data.illusts[:ilustNum]:
        author = illust.user.name.replace("/", "-")

        # ダウンロードフォルダなかったら作る(作者ごとにフォルダを分ける場合)
        # if not os.path.exists("./pixiv_images/" + author):
        #     os.mkdir("./pixiv_images/" + author)
        # savepath = "./pixiv_images/" + author

        # 保存先の指定
        savepath = "./pixiv_images/"

        # 保存
        api.download(illust.image_urls.large, path = savepath)
        print(str(allCount) + "枚目の画像: " + str(author)+"  " + str(illust.title))
        count += 1
        allCount += 1
        sleep(1)

        #30回目以降
        if count > 30:
            next_url = users_data.next_url
            next_qs = api.parse_qs(next_url)

            # users_dataに30以降のjsonデータを再代入
            users_data = api.user_bookmarks_illust(**next_qs)
            count = 1
            downloadImage(users_data, count, allCount)

downloadImage(users_data, count, allCount)

print("ダウンロード終了")
