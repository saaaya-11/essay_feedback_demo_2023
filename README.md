# essay_feedback_demo_2023

## 使用技術
* Python
* Django
* OpenAI GPT-4

## スクリーンショット
![Screenshot 2023-06-25 142516](https://github.com/saaaya-11/essay_feedback_demo_2023/assets/39193854/1e6bfd73-d264-4003-aa17-1c7bdfb03fe2)
![Screenshot 2023-06-25 142542](https://github.com/saaaya-11/essay_feedback_demo_2023/assets/39193854/e708a888-8edb-40a4-9cbe-86a09d9a8932)

GPTの生成中は読み込み中のGIFを上から表示する

## Limitation
* GPTとのチャット機能はデモ用にとりあえず作ったものになっているため，実用化するには再検討の余地がある．
* 攻撃的プロンプトへの対策などが不十分である．実用化するには対策が必要．
* OpenAIのAPIキーは mysite/essayReview/mySet/setVal.py に入力が必要
* mysite/mysite/settings.pyにSECRET_KEYが必要
