# -*- coding=UTF-8 -*-
from pydub import AudioSegment
import sys, os, random

time = 400


rootPath = '../resource/abs'
key1 = AudioSegment.from_mp3(rootPath + '/D/D3.MP3')
key2 = AudioSegment.from_mp3(rootPath + '/E/E3.MP3')
key3 = AudioSegment.from_mp3(rootPath + '/#F/#F3.MP3')
key4 = AudioSegment.from_mp3(rootPath + '/G/G3.MP3')
key5 = AudioSegment.from_mp3(rootPath + '/A/A3.MP3')


#3345 5432 1123 3·2_2- 3345 5432 
song = key3[:time * 1]
song += key3[:time * 1]
song += key4[:time * 1]
song += key5[:time * 1]

song += key5[:time * 1]
song += key4[:time * 1]
song += key3[:time * 1]
song += key2[:time * 1]

song += key1[:time * 1]
song += key1[:time * 1]
song += key2[:time * 1]
song += key3[:time * 1]

song += key3[:time * 1.5]
song += key2[:time * 0.5]
song += key2[:time * 2]
# song += key2[:time * 1]

song += key3[:time * 1]
song += key3[:time * 1]
song += key4[:time * 1]
song += key5[:time * 1]

song += key5[:time * 1]
song += key4[:time * 1]
song += key3[:time * 1]
song += key2[:time * 1]
#1123 2·1_1- 
song += key1[:time * 1]
song += key1[:time * 1]
song += key2[:time * 1]
song += key3[:time * 1]

song += key2[:time * 1.5]
song += key1[:time * 0.5]
song += key1[:time * 2]
# song += key1[:time * 1]
#(2231 23_4_31 23_4_32 125,3 3345 5434_2_ 1123 2·1_1-)*2
song += key2[:time * 1]
song += key2[:time * 1]
song += key3[:time * 1]
song += key1[:time * 1]

song += key2[:time * 1]
song += key3[:time * 0.5]
song += key4[:time * 0.5]
song += key3[:time * 1]
song += key1[:time * 1]

song += key2[:time * 1]
song += key3[:time * 0.5]
song += key4[:time * 0.5]
song += key3[:time * 1]
song += key2[:time * 1]

song += key1[:time * 1]
song += key2[:time * 1]
song += key5[:time * 1] #低音
song += key3[:time * 2]

# song += key3[:time * 1]
song += key3[:time * 1]
song += key4[:time * 1]
song += key5[:time * 1]

song += key5[:time * 1]
song += key4[:time * 1]
song += key3[:time * 1]
song += key4[:time * 0.5]
song += key2[:time * 0.5]

song += key1[:time * 1]
song += key1[:time * 1]
song += key2[:time * 1]
song += key3[:time * 1]

song += key2[:time * 1.5]
song += key1[:time * 0.5]
song += key1[:time * 2]
# song += key1[:time * 1]

song += key2[:time * 1]
song += key2[:time * 1]
song += key3[:time * 1]
song += key1[:time * 1]

song += key2[:time * 1]
song += key3[:time * 0.5]
song += key4[:time * 0.5]
song += key3[:time * 1]
song += key1[:time * 1]

song += key2[:time * 1]
song += key3[:time * 0.5]
song += key4[:time * 0.5]
song += key3[:time * 1]
song += key2[:time * 1]

song += key1[:time * 1]
song += key2[:time * 1]
song += key5[:time * 1] #低音
song += key3[:time * 2]

# song += key3[:time * 1]
song += key3[:time * 1]
song += key4[:time * 1]
song += key5[:time * 1]

song += key5[:time * 1]
song += key4[:time * 1]
song += key3[:time * 1]
song += key4[:time * 0.5]
song += key2[:time * 0.5]

song += key1[:time * 1]
song += key1[:time * 1]
song += key2[:time * 1]
song += key3[:time * 1]

song += key2[:time * 1.5]
song += key1[:time * 0.5]
song += key1[:time * 2]
# song += key1[:time * 1]

song.export('test.mp3', format="mp3") #导出为MP3格式