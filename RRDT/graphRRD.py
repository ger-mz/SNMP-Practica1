import sys
import rrdtool
import time
tiempo_actual = int(time.time())
#Grafica desde el tiempo actual menos diez minutos
tiempo_inicial = tiempo_actual - 1800

ret = rrdtool.graphv( "practica2.png",
                     "--start",str(tiempo_inicial),
                     "--end","N",
                     "--vertical-label=Segmentos",
                     "--title=Segmentos TCP de un agente \n Usando SNMP y RRDtools",
                     "DEF:sEntrada=segmentosRed.rrd:segmentosEntrada:AVERAGE",
                     "DEF:sSalida=segmentosRed.rrd:segmentosSalida:AVERAGE",
                      "VDEF:segEntradaLast=sEntrada,LAST",
                      "VDEF:segEntradaFirst=sEntrada,FIRST",
                      "VDEF:segEntradaMax=sEntrada,MAXIMUM",
                      "VDEF:segEntradaDev=sEntrada,STDEV",
                    #   "CDEF:Nivel1=sEntrada,550,LT,0,sEntrada,IF",
                      "CDEF:Nivel1=sEntrada,213,LT,0,sEntrada,IF",
                      "PRINT:segEntradaLast:%6.2lf",
                      "PRINT:segEntradaFirst:%6.2lf",
                     "GPRINT:segEntradaMax:%6.2lf %S segEntMAX",
                     "GPRINT:segEntradaDev:%6.2lf %S STDEV",
                     "AREA:Nivel1#00FF00:Segmentos recibidos sobre el nivel",
                     "LINE3:sEntrada#FF0000:Segmentros recibidos",
                     "LINE3:sSalida#0000FF:Segmentos enviados")
print(ret)