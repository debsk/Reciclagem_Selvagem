# rect = (x, y, largura, altura)
# colisoes
def collision(rect1, rect2):
    logic = False
    if(rect1[0] + rect1[2] > rect2[0] and rect1[0] < rect2[0] + rect2[2] 
    and rect1[1] + rect1[3] > rect2[1] and rect1[1] < rect2[1] + rect2[3]):
        logic = True
    return logic

# lixo na tela
def lixo_show(v):
    from random import randint
    for i in range(100):
        v.append([randint(1,740), randint(-2500, 0)])
    return v

