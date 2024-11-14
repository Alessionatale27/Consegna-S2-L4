

Figura = input('Scegli la figura della quale vuoi il perimetro tra quadrato, cerchio o rettangolo: ')

if Figura == 'quadrato':

 lato = float (input ('dimmi la misura del lato: '))
 print (f'il perimetro del quadrato è:{lato*4}')
 
elif Figura == 'rettangolo':
 altezza = float (input('dimmi la misura dell altezza: '))
 base = float (input('dimmi la misura della base: '))
 print (f'il perimetro del rettangolo è {(base+altezza)*2}')

elif Figura == 'cerchio':
 raggio = float(input('dimmi il raggio del cerchio: '))
 print(f'il perimetro del cerchio è {2*3.14*raggio}')
 
else :
 print ('Questa non la so , non sono così forte!')