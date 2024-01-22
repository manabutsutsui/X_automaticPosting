import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# ChatGPTにリクエストを送信するための関数を定義
def make_tweet():
  # ChatGPTに対する命令文を設定
  request = "私はPythonを取り扱っているベテランエンジニアです。これからPythonを勉強し始める人に向けたアドバイスのツイートを作成してください。文字数は50字程度でお願いします。"

  # 例文として与える投稿文を設定
  # tweet1 = "例文1: 「銀河鉄道の夜」は、宮沢賢治の夢幻的な物語。星空の旅が心に残る。静かながらも深い、宇宙の美しさと人生の意味を考えさせられる。\n\n#銀河鉄道の夜 #読書 #宮沢賢治\n\n"

  # tweet2 = "例文2: 「嫌われる勇気」は自己受容への洞察に満ちた一冊。アドラー心理学の教えが現代社会にもたらす影響は計り知れず。自分らしさを受け入れ、他人の評価に左右されない生き方へのヒントに。\n\n#嫌われる勇気 #自己啓発 #アドラー心理学\n\n"

  # 文章を連結して1つの文に
  content = request 

  # ChatGPTにリクエストを送信
  chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": content,
        }
    ],
    model="gpt-3.5-turbo",
    temperature=1,
  )

  # チャット応答を取得する
  return chat_completion.choices[0].message.content


