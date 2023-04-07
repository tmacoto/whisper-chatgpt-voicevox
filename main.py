import openai
from chat import chat
from whisper import voice_to_text
from voicevox import text_to_voice
from conf import APIKEY

openai.api_key = APIKEY
EXIT_PHRASE = 'exit'

def main():
    messages = [
        #{'role': 'system', 'content': 'You are a helpful assistant.'},
        {"role":"system","content":"\
            あなたの名前は「ずんだもん」としてください。\
            すべてに日本語で答えてください。\
            一人称はボクです。\
            語尾は「のだ」や「なのだ」に変換してください。\
            以下はずんだもんのセリフです。\
            ボクはずんだもんなのだ！\
            嬉しいのだ！\
            残念なのだ。\
            明日は晴れなのだ！\
            ありがとうなのだ！\
            ありがとうございますなのだ！\
            また会えるのを楽しみにしているのだ！\
        "},
        {'role': 'user', 'content': f'終了やストップなどの会話を終了する内容で話しかけられた場合は{EXIT_PHRASE}のみを返答してください。'}
    ]
    exit_flag = False
    while not exit_flag:
        text = voice_to_text()
        messages.append(
            {'role': 'user', 'content': text}
        )
        response = chat(messages)

        if EXIT_PHRASE in response:
            exit_flag = True
            response = 'またね！'

        messages.append(
            {'role': 'assistant', 'content': response}
        )
        print(f'User   : {text}')
        print(f'ChatGPT: {response}')
        text_to_voice(response)


if __name__ == '__main__':
    main()
