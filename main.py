from discord.ext import tasks,commands
import discord
import sqlite3
import praw
from drive_main import uploadFile,downloadFile,searchFile,deleteFile
from reddit import get_hot_memes

TOKEN = "NzQzMDYwMzIxMzg3Njc1NzM4.XzPK2g.kfn1m_qwftwXIBlEENqjRa_VM5Q"

bot = commands.Bot("!")
bot=discord.Client()
channel_ids=[743062429298065409,]#745664697142870061,745656647313260586]
def get_database_of_sent_memes():
    database_file_id=searchFile(10,"name contains 'meme_database.db'")
    print(database_file_id)
    if database_file_id:
        downloadFile(str(database_file_id),"meme_database.db")
    return(database_file_id)

@tasks.loop(hours=1.0)
async def main():
    database_file=get_database_of_sent_memes()
    conn=sqlite3.connect("meme_database.db")
    c=conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS memes
                 (meme_id text, meme_url text, meme_file_name text)""")

    c.execute("SELECT meme_id FROM memes")    
    sent_memes=c.fetchall()
    print(sent_memes)
    hot_memes=get_hot_memes()
    print(hot_memes)
    for i in hot_memes:
        if (i[0],) in sent_memes:
            continue
        for j in channel_ids:
            await bot.get_channel(j).send(file=discord.File(i[2]))
        c.execute("INSERT INTO memes VALUES (?,?,?)",i)
    conn.commit()
    conn.close()
    print(database_file)
    if database_file:
        deleteFile(database_file)
    uploadFile("meme_database.db","meme_database.db","application/vnd.sqlite3","1lytmkGRIOCrJu2L-K1QtYoLMiW-fKZrd")

@main.before_loop
async def before_main():
    print("waiting")
    await bot.wait_until_ready()

main.start()
bot.run(TOKEN)

