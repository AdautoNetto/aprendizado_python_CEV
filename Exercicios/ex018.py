import math

ang = float(input('Digite o angulo que voce deseja: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O seno do seu angulo é: {:.2f}' .format(sen))
print('O cosseno do seu angulo é: {:.2f}' .format(cos))
print('A tangente do seu angulo é: {:.2f}' .format(tan))

