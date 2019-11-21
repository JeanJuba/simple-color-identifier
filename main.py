import imageio
import colorsys


def is_green(val=()):
    if (val[0]*360 > 80) and (val[0]*360 < 180):
        return True
    else:
        return False


def is_red(val=()):
    if(0 < val[0] * 360 < 20) or (350 < val[0] * 360 < 360):
        return True
    else:
        return False


def is_yellow(val=()):
    if (val[0]*360 > 30) and (val[0]*360 < 70):
        return True
    else:
        return False


def is_blank(v=[]):
    return v[0] == 0 and v[1] == 0 and v[2] == 0


im = imageio.imread('pimentoes.png')

counter_red = 0
counter_yellow = 0
counter_green = 0
counter_valid = 0

print('Executando...')
for i in range(0, len(im)):
    for j in range(0, len(im[i])):
        #print(im[i][j])
        if not is_blank(im[i][j]):
            counter_valid += 1
            v = colorsys.rgb_to_hsv(im[i][j][0]/255, im[i][j][1]/255, im[i][j][2]/255)
            if is_red(v):
                counter_red += 1
                im[i][j][0] = 255
                im[i][j][1] = 0
                im[i][j][2] = 0

            elif is_green(v):
                counter_green += 1
                im[i][j][0] = 0
                im[i][j][1] = 255
                im[i][j][2] = 0

            elif is_yellow(v):
                counter_yellow += 1
                im[i][j][0] = 255
                im[i][j][1] = 255
                im[i][j][2] = 0

            else:
                im[i][j][0] = 255
                im[i][j][1] = 255
                im[i][j][2] = 255

imageio.imwrite('im.png', im)
tamanho = len(im) * len(im[0])
por_red = (counter_red/counter_valid)*100
por_green = (counter_green/counter_valid)*100
por_yellow = (counter_yellow/counter_valid)*100

print('Por. Vermelho: %f %%  Por. Verde: %f %%  Por. Amarelo: %f %%' % (por_red, por_green, por_yellow))

por_min = 30
if por_red < por_min and por_green < por_min and por_yellow < por_min:
    print('Nenhuma cor atinge a porcentagem mínima de %d' % por_min)
elif por_red > por_green and por_red > por_yellow:
    print('Vermelho')
elif por_green > por_red and por_green > por_yellow:
    print('Verde')
else:
    print('Amarelo')



