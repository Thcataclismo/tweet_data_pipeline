import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs 

def executar_etl_twitter():

    chave_acesso = "" 
    segredo_acesso = "" 
    chave_consumidor = ""
    segredo_consumidor = ""


    # Autenticação no Twitter
    autenticacao = tweepy.OAuthHandler(chave_acesso, segredo_acesso)   
    autenticacao.set_access_token(chave_consumidor, segredo_consumidor) 

    # # # Criando um objeto de API 
    api = tweepy.API(autenticacao)
    tweets = api.user_timeline(screen_name='@elonmusk', 
                            # 200 é o limite máximo permitido
                            count=200,
                            include_rts = False,
                            # Necessário para obter o texto completo
                            # caso contrário, apenas os primeiros 140 caracteres são extraídos
                            tweet_mode = 'extended'
                            )

    lista = []
    for tweet in tweets:
        texto = tweet._json["full_text"]

        tweet_refinado = {"usuário": tweet.user.screen_name,
                        'texto' : texto,
                        'contagem_de_favoritos' : tweet.favorite_count,
                        'contagem_de_retweets' : tweet.retweet_count,
                        'criado_em' : tweet.created_at}
        
        lista.append(tweet_refinado)

    df = pd.DataFrame(lista)
    df.to_csv('tweets_refinados.csv')
