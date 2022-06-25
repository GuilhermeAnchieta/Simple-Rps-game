from random import randint
import pyautogui as py


pts = 0
ptsresult = ''
player = ''

while player is not None:
    player = py.confirm(text=f"{'=' * 25}\n          Pedra Papel Tesoura\n{'=' * 25}"
                             f"\n\nO número de vitórias será contado, você é capaz de vencer seu próprio recorde?!\n"
                             f"\n\nFaça Sua escolha e tente vencer a máquina!!!\n\n",
                        title='===== JOGO RPS =====', buttons=['Pedra', 'Papel', 'Tesoura', 'Dev'])

    if player == 'Dev':
        py.alert(text='Gmail: guilherme.anchietass@gmail.com\n\nGitHub: https://github.com/GuilhermeAnchieta\n\n'
                      'linkedin: https://www.linkedin.com/in/guilherme-anchieta-silva-siqueira-de-almeida-b2192a232/',
                 title='Desenvolvedor', button='OK')
        continue
    else:
        break

while player is not None:
    ops = {1: "Pedra", 2: "Papel", 3: "Tesoura"}
    bot = randint(1, 3)
    if player == ops[bot]:
        result = "\nUAU!!! Aconteceu um empate!"
        ptsresult = f'total de pontos: {pts}'
    elif (player == 'Pedra' and ops[bot] == 'Tesoura') or (player == 'Papel' and ops[bot] == 'Pedra') \
            or (player == 'Tesoura' and ops[bot] == 'Papel'):
        result = "\nPARABÉNS!!! Você ganhou!\n\n"
        pts += 1
        ptsresult = f'total de pontos: {pts}'
    else:
        result = "\nNÂOOOO!!! Você perdeu!\n\n"
        if pts == 0:
            ptsresult = 'Parece que você está sem sorte, nenhum ponto.'
        else:
            ptsresult = f'Sua pontuação maxima foi de {pts} pontos!'
        pts = 0

    player = py.confirm(text=f"\nVocê escolheu → {player}\nmaquina escolheu → {ops[bot]}\n\n"
                             f"{ptsresult}\n"
                             f"{result}\n\nQual será sua próxima escolha?\n",
                        title='===== JOGO RPS =====', buttons=['Pedra', 'Papel', 'Tesoura'])
