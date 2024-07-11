
__author__ = '2253406 北澤昇大'
__version__ = '3.11.4'
__date__ = '2024/5/25'


from create_wave import CreateWave

def main():
    
    """
    このプログラムは、create_wave.pyを用いて、サイン波、ノコギリ波、三角波、短形波を作成し、それぞれの波形を画像と音ファイルとして出力するプログラムです。

    """
    
     #画像の表示の選択
    SHOW = False
    FO = 440  # 基本周波数(Hz)
    t = 3     # 時間(s)
    n = 5   # 第n高調波
    
    #create_wave.pyのCreateWaveインスタンスの作成
    cw = CreateWave(FO, t, n)
    
    #サイン波、ノコギリ波、三角波、短形波の作成
    sinewave = cw.sine_wave()
    sawtoothwave = cw.saw_tooth_wave()
    trianglewave = cw.triangle_wave()
    squarewave = cw.square_wave()
    
    #それぞれの波を画像と音ファイルとして出力
    cw.output_plot(sinewave,cw.return_t(),"sine_wave",SHOW)
    cw.output_plot(sawtoothwave,cw.return_t(),"sawtooth_wave",SHOW)
    cw.output_plot(trianglewave,cw.return_t(),"triangle_wave",SHOW)
    cw.output_plot(squarewave,cw.return_t(),"square_wave",SHOW)
    
    return 0
    
if __name__ == "__main__":
    main()
