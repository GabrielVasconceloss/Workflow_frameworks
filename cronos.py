from discord_webhook import DiscordWebhook, DiscordEmbed
import schedule
import time
from datetime import datetime
import sqlite3



con = sqlite3.connect("/home/icetar/workflow/banco.db")



def job():
    print("Ação sendo disparada!")
    descc = 'Jonas'
    webhook = DiscordWebhook(
        url='https://discord.com/api/webhooks/1051894884191174658/e1cKSppl0PwI8sP61V6EBwq9d5hf2vjqvAZtnlNbmQOOwTs7pNx6-MhBA8Lle3E0vvIx')
    embed = DiscordEmbed(title='Lista de Follow-up para fazer hoje', description='%s' % (descc), color='ffe793')


    busca_lead = con.execute('SELECT * FROM leads WHERE status = 5 AND user_id_res = 5')
    for cada_lead in busca_lead:
        tem = None
        flw = None
        tem_flw_query = con.execute(
            f'SELECT data, data_prox, max(id), lead_id  FROM flw WHERE lead_id = {cada_lead[0]} AND cod_acao = 12')
        for flw in tem_flw_query:
            tem = flw[0]
        if tem:
            calculo = (datetime.strptime(flw[1], '%Y-%m-%d') - datetime.now()).days
            if calculo < 0:
                embed.add_embed_field(name=str(cada_lead[7]), value='%s' % ("Atrasado"), inline=False)
                print("Atrasado")

            else:
                print("Atualizado")

        else:
            embed.add_embed_field(name=str(cada_lead[7]), value='%s' % ("Sem Atualização"), inline=False)
            print('Sem Atualização')

    webhook.add_embed(embed)
    response = webhook.execute(embed)


schedule.every().day.at("11:10").do(job)

while True:
    schedule.run_pending()
    print(datetime.now())
    time.sleep(1)



