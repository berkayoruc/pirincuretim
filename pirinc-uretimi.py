import codecs

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import pandas as pd

# DOSYA YOLLARI
ithal_dosya_yolu = r'/Users/berkayoruc/Desktop/WORKS/ithal-pirinc.csv'
uretim_dosya_yolu = r'/Users/berkayoruc/Desktop/WORKS/uretim-pirinc.csv'
# CODECS
ithal_pirinc = codecs.open(ithal_dosya_yolu, mode='r', encoding="utf-8", errors="ignore")
uretilen_pirinc = codecs.open(uretim_dosya_yolu, mode='r', encoding="utf-8", errors="ignore")
# DATAFRAMES
df_ithal = pd.read_csv(ithal_pirinc)
df_uretim = pd.read_csv(uretilen_pirinc)
# BIRLESTIRILMIS DATAFRAME
df_birlestirilmis = pd.merge(df_ithal, df_uretim, how='inner')
cols = df_birlestirilmis.columns.tolist()
yil = df_birlestirilmis[cols[0]].values
ithal = df_birlestirilmis[cols[1]].values
uretim = df_birlestirilmis[cols[2]].values
# MATPLOTLIB
fig, ax = plt.subplots()
ithal_line, = ax.plot(yil, ithal, "w-", label='Ithal Pirinc(Ton)')
uretim_line, = ax.plot(yil, uretim, "w--", label='Uretilen Pirinc(Ton)')
# ANIMASYON FONKSIYONU
def update(num, yil, ithal, uretim, ithal_line, uretim_line):
    ithal_line.set_data(yil[:num], ithal[:num])
    uretim_line.set_data(yil[:num], uretim[:num])
    ax.set_xlabel("Yil: " + str(yil[num]) + "         " + "Uretim: " + str(uretim[num])
                    + "         " + 'Ithalat: ' + str(ithal[num]))
    return ithal_line,uretim_line,

ani = animation.FuncAnimation(fig, update, frames=len(yil), fargs=[yil, ithal, uretim,
                ithal_line, uretim_line], interval=len(yil)*10)

plt.tick_params(
    axis='x',          # degisiklikleri yapacagimiz eksen
    which='both',      # hem ana hem de ikincil cizgiler etkilenir
    bottom=False,      # alt kenar cizgilerini kapatir
    top=False,         # ust kenar cizgilerini kapatir
    labelbottom=False  # alt etiketi kapatir
    )
ax.set_ylabel('Ton')
plt.legend(fancybox=True, loc='upper left')
ax.set_facecolor('k')
plt.show()
