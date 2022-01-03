#-----------FARMADOR DE COIN NA BETFURY-----------#

from PIL import Image # pip install Pillow
from time import sleep # Já vem com o python
import pyautogui as at # pip install PyAutoGUI

#-----------VALORES RGB IDENTIFICADOS-------------# VALORES(RGB) ALTERÁVEIS
sw = (207, 226, 228) # VALOR RGB | SILVER WIN
sw1 = (206, 225, 228) # VALOR RGB | SILVER WIN1
sl = (81, 94, 107) # VALOR RGB | SILVER DERROTA
gw = (230, 193, 84) # VALOR RGB | GOLD WIN
gl = (87, 86, 71) # GOLD VALOR | RGB GOLD LOSS

#---------TIRANDO PRINT DA ULTIMA MOEDA-----------# VALOR(REGION) ALTERÁVEL
while True:   
    sc = at.screenshot(region=(480,260,20,20))
    sc.getpixel
    sc.save('lastcoin.png')

    #---------EXTRAINDO VALOR RGB DO PRINT--------#
    def rgb_of_pixel (img_path, x, y):
        im = Image.open(img_path).convert('RGB')
        r, g ,b = im.getpixel((x, y))
        a = (r, g, b)
        return a
    img = "lastcoin.png"
    rgbvalue = (rgb_of_pixel (img, 5, 5))
    print (rgbvalue) # VALOR RGB DA MOEDA

    #------------------EXECUCAO-------------------# VALORES(CLICK,DOUBLECLICK) ALTERÁVEIS
    if rgbvalue == sw :       
        print("cliquei no Prata 1.0")
        at.click(474, 619) #MIN
        at.doubleClick(1085,645) #4X
        at.doubleClick(1085,645) #4X    
        at.doubleClick(1085,645) #4X
        at.doubleClick(1085,645) #4X
        at.doubleClick(1085,645) #4X
        at.doubleClick(1085,645) #4X
        at.click(1085,645) #4X
        at.click(940, 735) #APOSTAR NO PRATA
    if rgbvalue == sw1 :
        print("cliquei no Prata 2.0")
        at.click(474, 619) #MIN
        at.doubleClick(1085,645) #4X
        at.doubleClick(1085,645) #4X
        at.doubleClick(1085,645) #4X
        at.doubleClick(1085,645) #4X
        at.doubleClick(1085,645) #4X
        at.doubleClick(1085,645) #4X
        at.click(1085,645) #4X
        at.click(940, 735) #APOSTAR NO PRATA 
    if rgbvalue == sl:
        print('Cliquei no Prata (SL)+(MG)')
        at.click(1085,654) #MG
        at.click(940, 735) #APOSTAR NO PRATA
    if rgbvalue == gw:
        print("cliquei no Gold 1.0")
        at.click(474, 619) #MIN
        at.doubleClick(1085,645) #4X
        at.doubleClick(1085,645) #4X
        at.doubleClick(1085,645) #4X
        at.doubleClick(1085,645) #4X
        at.doubleClick(1085,645) #4X
        at.doubleClick(1085,645) #4X
        at.click(1085,645) #4X
        at.click(684,754) #APOSTAR NO GOLD
    if rgbvalue == gl:
        print("cliquei no Gold (GL)+(MG)")
        at.click(1085,654) #MG
        at.click(684,754) #APOSTAR NO GOLD

    #------INDICAÇÃO DE VARIACAO DE COR------#
    else:
        print('Nova variação {}'.format(rgbvalue))
        print('Ou dê o primeiro flip!')
    sleep(1.9)

#----------------------ATENÇÃO-----------------------#

# O CÓDIGO FOI CRIADO POR PADRÃO EM RESOLUÇÃO 1920X1080.
# FEITO COM MEDIDAS EXATAS DO NAVEGADOR GOOGLE CHROME (SEM NENHUMA TOOLBAR).
# PARA READAPTAÇÃO DE RESOLUÇÃO APENAS ALTERE OS VALORES DE CORDENADA, COM AS TAGS (ALTERÁVEL):
    # 1- TIRANDO PRINT DA ULTIMA MOEDA.
    # 2- EXECUÇÃO.
# SEU MONITOR É 1920X1080 E NÃO ESTA FUNCIONANDO?
    # 1- ESTEJA ATENTO AO VALOR RGB QUE O EXTRATOR SOLTA, TALVEZ SEJA NECESSÁRIO ALTERAR:
        # 1.1- POR QUE O VALOR RGB NÃO É O MESMO PARA TODOS?
            # R - GPU/CPUS TRATAM IMAGENS DE JEITO DIFERENTE, POR ISSO PODE OCORRER VARIAÇÃES RGB.
        # 1.2- COMO SOLUCIONAR?
            # R -  FIQUE ATENTO AO VALOR EXTRAIDO EM: EXTRAINDO VALOR RGB DO PRINT > VALOR RGB DA MOEDA.
            #      DEPOIS QUE VOCÊ PEGOU O VALOR RGB EXATO DE CADA MOEDA (SW,SL,GW,GL), É SÓ SUBSTITUIR OS VALORES EM:
            #      VALORES RGB IDENTIFICADOS > VALOR RGB | SILVER WIN, VALOR RGB | SILVER LOSS, VALOR RGB | GOLD WIN...
    # 2- OS VALORES RGBS ESTÃO CORRETOS, E NÃO ESTA FUNCIONANDO?
        # 2.1 - PODE SER QUE OS VALORES DE RESOLUÇÃO NÃO ESTEJAM DEVIDAMENTE CORRETOS PARA SEU MONITOR.
        # 2.2 - SE VOCÊ NÃO SABE ALTERAR POR CONTA PRÓPRIA, LEIA A TAG "AJUDA" LOGO A BAIXO.
# COMO EU SEI SE MEU MONITOR É 1920X1080?
    # 1- NA AREA DE TRABALHO(DESKTOP), CLIQUE COM O BOTÃO DIREITO, VÁ NA OPÇÃO "CONFIGURAÇÃO DE EXIBIÇÃO" VAI TER LÁ "RESOLUÇÃO DE TELA" + A RESOLUÇÃO EM BAIXO.
# VISHHHH, MEU MONITOR NÃO É 1920X1080, ACABOU PRA MIM?
    # CALMA MEU CONSAGRADO, PRA TUDO NA VIDA EXISTE UMA SOLUÇÃO! VOCÊ PODE UTILIZAR A MATEMATICA PARA REDIMENCIONAR PARA SUA RESOLUÇÃO,
        # VEJA A DIFERENÇA DA ALTURA DA SUA RESOLUÇÃO PARA A MINHA, EXEMPLO: ALTURA DO MEU É 1080 E A SUA 720, ENTÃO (1080-720) = 360 CONCLUSÃO:
        # (3X360) = 1080, (2X360) = 720, A ALTURA DO MEU MONITOR É 1/3 MAIOR DO QUE A SUA, APARTIR DISSO É SÓ APLICAR PORCENTAGEM E DIMINUIR PROPORCIONAL.
        # OU SE VOCÊ NÃO QUISER FAZER MATÉMATICA É SÓ FICAR CHUTANDO OS NÚMEROS ATÉ CHEGAR AS PROPORÇÕES EXATAS (DOIDERA KKKKKKK).
       
#-----------------------AJUDA?-----------------------#

# SE VOCÊ TEM ALGUMA DÚVIDA AINDA EU VOU POSTAR UM VIDEO EM BREVE NO CANAL A BAIXO:
# https://www.youtube.com/channel/UCAGdA4ObM5AhfoJ5YBHCILQ
# DESCULPA SE PARECE BAGUNÇADO, ESSE É UM DOS MEUS PRIMEIROS PROJETOS <3
