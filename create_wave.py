__author__ = '2253406 北澤昇大'
__version__ = '3.11.4'
__date__ = '2024/5/25'

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import os

class CreateWave():
    """
    このクラスは、サイン波、ノコギリ波、三角波、短形波を作成し、それぞれの波形を画像と音ファイルとして出力するクラスです。
    
    """
    
    #コンストラクタ
    def __init__(self, FO, t, harmonics, Fs=48000):
       
        #基本周波数
        self.FO = FO
        #等間隔の時間
        self.t = np.linspace(0, t, int(Fs * t), endpoint=False)
        #高調波数
        self.harmonics = harmonics
        #サンプリング周波数
        self.Fs = Fs
        #ナイキスと周波数
        self.nyquist = 0.5 * self.Fs
    
    #等間隔の時間を返すメソッド
    def return_t(self):
        return self.t
    
    #サイン波を返すメソッド
    def sine_wave(self):
        #sin(2πf0t)
        return np.sin(2 * np.pi * self.FO * self.t)

    #ノコギリ波を返すメソッド
    def saw_tooth_wave(self):
        sawtooth = 0
        for n in range(1, self.harmonics + 1):
            #sin(2πf0nt)/n
            if self.FO * n <= self.nyquist:
                sawtooth += np.sin(2 * np.pi * self.FO * n * self.t) / n
        return (2 / np.pi) * sawtooth #2/πをかける
    
    #三角波を返すメソッド
    def triangle_wave(self):
        triangle = 0
        for n in range(1,self.harmonics+1):
            #sin(nπ/2)sin(2πf0nt)/n^2
            if self.FO * n <= self.nyquist:
                triangle += np.sin(n*np.pi/2) * (np.sin(2 * np.pi* self.FO * n * self.t)/n**2)
                print(n)
            print(self.nyquist)
        return (8 / np.pi ** 2) * triangle #8/π^2をかける
    
    #短形波を返すメソッド
    def square_wave(self):
        square = 0
        for n in range(1,self.harmonics+1):
            #sin((2n-1)2πf0t)/(2n-1)
            if self.FO * (2 * n - 1) <= self.nyquist:
                square += np.sin((2 * n - 1) * 2 * np.pi * self.FO * self.t)/(2 * n - 1)
        return  4/ np.pi * square #4/πをかける
    
    #波形をプロットし、wavファイルを出力するメソッド
    def output_plot(self,wave,t,name,SHOW):
        
        #波形
        self.wave = wave
        #時間
        self.t = t
        #波形の名前
        self.name = name
        #wavファイルの出力名
        filename1 =self.name +"_150" + ".wav"
        #画像ファイル名
        filename2 =self.name +"_150" + ".png"
        #画像、wavファイルのパス
        file_path1 = os.path.join("output", filename1)
        file_path2 = os.path.join("output", filename2)
    
        #画像の表示
        self.show = SHOW
        
        #outputディレクトリがない場合、作成
        os.makedirs("output", exist_ok=True)
        
        #波形のプロット
        plt.figure(figsize=(12, 4))
        plt.plot(self.t[:1000], self.wave[:1000])
        plt.title(self.name)
       
        #画像の保存
        plt.savefig(file_path2)
        
        #画像の表示
        if self.show:
            plt.show()
       
        #波形を16bitで正規化、wavファイルの出力
        self.wave = self.wave / np.max(np.abs(self.wave))
        
        #chatGpt使用 filepath改変
        #このプログラムを変更して,wavファイルに16bitで正規化したものを出力するようにしてください。
        wavfile.write(file_path1, self.Fs,np.int16(self.wave * 32767))

        return 0

   
   