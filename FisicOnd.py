print('\n1 - onde\n2 - suono\n3 - luce\n4 - gr. fotometriche e formule..')
mode = int(input('select mode: '))
  
if mode == 1:
 print('\nv=sqrt(Ft/dl);\n(tens/dens linear=m/L)')
 print('y=a cos(2pi/T+fi0)\n=a cos(omega t+fi\n=a cos(2 x/lambda+fi)\n=a cos[2pi(x-vt)/lambda+fi]')
 print('y=A cos(omega t+fi/2);\nA=2a cos(fi/2)')
 print('S1P-S2P=(k or k+1) lambda')
    
if mode == 2:
 print('\nint.sonora I(W/m^2)\n=E/(A del t)=P/A\n=Ps/(4pi r^2)')
 print('liv.int.son.\nLs(dB)\n=10log(I/I 0);\nI 0=10^-12')
 print('eco: delta t=2d/v')
 print('modi norm:lambda di n=2L/n\n(n mezze oscillaz;nodi=n+1)')
    
if mode == 3:
 print('\nn(rifraz.)=c/v')
 print('Snell(rifl):\nsen(i)/sen(r)=n2/n1')
 print('angl lim: // con r=90')
 print('Young:lambda/d=y/l')
 print('S1Bk-S2Bk=k lambda')
 print('d sen(alfa k)=k lambda')
 print('scura:d sen=(m-1/2)lambda')
    
if mode == 4:
 print('\nIrrad Er(W/m^2)=Energia/(A del t)\n=Ps/(4pi r^2)')
 print('Intens radiaz Ir=Energ/(omega del t);\nomega=A/r^2')
 print('Intens luminosa=Ir soggettiva')
 print('candela(cd)=Int.lum.,f=5.4x10^14,Ir=1/683(W/sr(seradianti))')
 print('flusso lumin phi(grande)L (lm)=quantit luce emessa/s, soggettiva;(lumen=1cd sr')
 print('illuminam EL(lx)=phi(big)/(4pi r^3);')