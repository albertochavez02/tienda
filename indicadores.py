from PIL import Image

menu = """
Menu
1   - Meta de IMU
2   - COMSER
3   - SC Satisfaccion del Cliente
4   - Indicadores
5   - Objetivo de Cadena de Valor
6   - Solicitudes APS-EAS-PF
7   - PF  Perfepcion de la Facturacion
8   - PGC Percepcion Global del Cliente
9   - APS Aclaracion de Solicitude de Pago SSB
10  - EAS Efectividad en Atencion de Solicitudes
11  - TAP Tiempo Comprimiso en Atencion Personalizada
12  - CAP Calidad en la Atencion Personalizada
13  - ECP Efectividad en la Conciliacion PROFECO
14  - CMP Cero Multas PROFECO
0   - Terminar
"""
continua=True

while continua:
    print(menu)
    op =input("Selecciona la opcion deseada:")
    print("Opcion:",op)
    if op == "1":
        print("""La meta de IMU es: 4.1
        Interpretacion: Es el resultado de multiplicar por 1000, al cociente
        del numero total de inconformidades acumuladas presentadas por los usuarios
        entre el numero acumulado de usuarios atendidos por una area especifica en
        un periodo de tiempo. 
        """)
        print("Presiona 's' y da enter para ver imagen Etapas de Macroproceso")
        resp=input()
        if resp=="s":
            img1 = Image.open("imagenes/IMU.png")
            img1.show()   
            img2 = Image.open("imagenes/metasIMU.png")
            img2.show()
            img3 = Image.open("imagenes/clasificacionIMU.png")
            img3.show()            
            input("Presiona enter para continuar")                          
    if op =="2":
        print("La meta de COMSER es: 97.0")
        print("""
        Interpretacion: Es el valor que resulta de promedio de porcentaje de los eventos
        atendidos en tiempo comprometido entre el numero de eventos totales registrados
        en un periodo de evaluacion por cada compromiso descrito. Representa el grado
        de cumplimiento de las especificaciones minimas de la calidad del servicio que
        el cliente debe esperar de CFE SSB. 
        """)
        print("Presiona 's' y da enter para ver imagen")
        resp=input()
        if resp=="s":
            img1 = Image.open("imagenes/COMSER1.png")
            img1.show()
            img2 = Image.open("imagenes/COMSER2.png")
            img2.show()            
            input("Presiona enter para continuar")              
    if op =="3":
        print("La meta de SC es: 93.0")
        print("""
        Interpretacion: 

        """)
        print("Presiona 's' y da enter para ver imagen")
        resp=input()
        if resp=="s":
            img1 = Image.open("imagenes/SC1.png")
            img1.show()
            img2 = Image.open("imagenes/SC2.png")
            img2.show()
            img3 = Image.open("imagenes/SC3.png")
            img3.show()
            input("Presiona enter para continuar")              
    if op == "4":
        print("""
        Indicadores:
        """)
        print("Presiona 's' y da enter para ver imagen")
        resp=input()
        if resp=="s":
            img = Image.open("imagenes/indicadores.png")
            img.show()           
            input("Presiona enter para continuar")              
    if op =="5":
        print("Ojetivo de cadena de valor:")
        print("""
        El objetivo de definir la cadena de valor entre las subsidiarias, es para establecer las
        actividades que se llevan a cabo dentro de cada una de las empresas, asi como de las que
        presentan interrelación, definiendo actividades clave que agregan valor en el logro de
        las metas establecidas, formulando mecanismos de control que permitan asegurar la oportunidad
        y calidad en el servicio al cliente.
        """)
        print("Presiona 's' y da enter para ver imagen Etapas de Macroproceso")
        resp=input()
        if resp=="s":
            img = Image.open("imagenes/cadenaDeValor.png")
            img.show()   
            input("Presiona enter para continuar")              
        else:
            print("Intente de nuevo")
            print(menu)
            input("Presiona enter para continuar")              
            continue    
    if op =="6":
        print("Ordenes:")
        print("""
	CLAVE  DESCRIPCIÓN	                        DIAS   TERMINACIÓN	        IMPROCEDENCIA	INDICADOR			
			                                U	R						
1	C06	   CONEXIÓN CARGA AUTO ELÉCTRICO	2	5	C06	        NO APLICA	                DACGs- CRE
2	QC3	   RECIBO EXTRAVIADO	                3	5	QC3	        QC4		    EAS		
3	QC6	   CARGOS MAL APLICADOS                 10	10	QC6	        QC4	        APS	EAS		
4	SC5	   MODIFICACIÓN DE DATOS EN SICOM	2	2	SC5	        NO APLICA       EAS		
5	SC9	   PAGO NO PROCESADO	                10	10	SC9	        NO APLICA	APS	EAS		
6	SCA	   PAGO ELECTRÓNICO NO PROCESADO	10	10	SC9	        NO APLICA	APS	EAS		
7	SCB	   FALLA CFEMATICO	                3	3	SCB	        NO APLICA	APS	EAS		
8	SCC	   PAGO DOBLE	                        10	10	SCC	        NO APLICA	APS	EAS		
9	SCG	   DEVOLUCIÓN DEPOSITO EN GARANTÍA	15	15	SCG	        NO APLICA		EAS	DACGs- CRE
10	SCH	   DIAGNOSTICO ATENCIÓN DOMICILIARIA    5	5	SCH	        NO APLICA               EAS		
11	SCL	   ACLARACION RECIBO MT/AT	        5	5	SCL	        NO APLICA		EAS		
12	SCN	   ASESORÍA TÉCNICA MT/AT	        5	5	SCN	        NO APLICA	    EAS		
13	SCS	   ACLARACION DE SALDO APP	        4	5	SCS	        NO APLICA	        EAS	PF	
14	SMK	   REVISIÓN DE MEDIDOR	                5	10	QC4/SMC/SM2	QO6			    PF	
15		   SOLINFO 200							                                    PF	
16	QC1	   CONSUMO ANORMAL                      QC1/QC5	QC5				                        DACGs- CRE

        """)
        print("Presiona 's' y da enter para ver imagen Etapas de Macroproceso")
        resp=input()
        if resp=="s":
            img = Image.open("imagenes/solicitudes_APS-EAS-PF.png")
            img.show()   
            input("Presiona enter para continuar")                          
        else:
            print("Intente de nuevo")
            print(menu)
            input("Presiona enter para continuar")                          
            continue    
    if op == "7":
        print("""
        PF: Percepción de la Facturación:
        Descripcion:
        Es el número de inconformidades a la facturación presentadas por los clientes
        sin importar su condición de procedencia o improcedencia, entre el número de
        clientes domésticos facturados del mes anterior.

        Objetivo del Indicador:
        Medir las inconformidades a la facturación que presentan nuestros clientes
        en los diferentes medios de contacto. 

        5  APS: QC6,SC9,SCA,SCB,SCC
        12 EAS: APS,QC3,SC5,SCG,SCH,SCL,SCN,SCS
        3  PF : SCS,SMK,SOLINFO200
        """)
        print("Presiona 's' y da enter para ver imagen")
        resp=input()
        if resp=="s":
            img = Image.open("imagenes/PF.png")
            img.show()   
            input("Presiona enter para continuar")                          
    if op == "8":
        print("""
        PGC: Percepción Global del Cliente:
        Descripción:
        Implementar el índice de percepción global del cliente doméstico mediante la
        integración de resultados de tres encuestas de salida (CAC, Telefónica, Twitter)
        y una de satisfacción  ( aplicada por externo)  para medir la percepción de los clientes,
        usuarios y sociedad en general. La información obtenida por los diversos canales será
        de gran relevancia para la realización de estrategias y planes enforcados a la mejora continua.  
        """)
        print("Presiona 's' y da enter para ver imagen")
        resp=input()
        if resp=="s":
            img = Image.open("imagenes/PGC.png")
            img.show()
            input("Presiona enter para continuar")                          
    if op == "9":
        print("""
        ASP: Aclaración de Solicitudes de Pago SSB:
        Descripción:
        Es la medición realizada a la atención de las solicitudes de servicio
        relacionadas con la aclaración de un pago efectuado por el cliente.  
        Objetivo del Indicador:
        Medir el cumplimiento de la atención de las solicitudes de servicio
        del cliente conforme a los tiempos compromisos establecidos en el manual de SICOSS.
        """)
        print("Presiona 's' y da enter para ver imagen")
        resp=input()
        if resp=="s":
            img = Image.open("imagenes/APS.png")
            img.show()
            input("Presiona enter para continuar")                          
    if op == "10":
        print("""
        EAS: Efectividad en la Atención de Solicitudes SSB:
        Descripcion:
        Es la medición efectiva en la atención a las solicitudes de servicio
        correspondientes a CFE Suministrador de Servicios Básicos.
        Objetivo del indicador-:
        Medir el índice de atención de las solicitudes de Suministro Básico.
        """)
        print("Presiona 's' y da enter para ver imagen")
        resp=input()
        if resp=="s":
            img = Image.open("imagenes/EAS.png")
            img.show()
            input("Presiona enter para continuar")                          
    if op == "11":
        print("""
        TAP: Tiempo Compromiso de Atención Personalizada:
        Descripcion:
        Es la medición de las atenciones brindadas dentro del tiempo
        compromiso por tipo de trámite o servicio.
        Objetivo del indicador:
        Medir el tiempo de atención que se brinda por tipo de trámite o servicio.
        """)
        print("Presiona 's' y da enter para ver imagen")
        resp=input()
        if resp=="s":
            img = Image.open("imagenes/EAS.png")
            img.show()
            input("Presiona enter para continuar")                          
    if op == "12":
        print("""
        CAP: Calidad en la Atención Personalizada:
        Descripcion:
        Es la evaluación  del proceso de atención que se brinda al cliente
        desde el registro del turno, el protocolo de atención utilizado,
        hasta el correcto registro de la Solinfo o solicitud de servicio
        que corresponda al trámite o servicio.         
        Objetivo del indicador:
        Medir la calidad del proceso de atención brindado al cliente
        """)
        print("Presiona 's' y da enter para ver imagen")
        resp=input()
        if resp=="s":
            img = Image.open("imagenes/CAP.png")
            img.show()
            input("Presiona enter para continuar")                          
    if op == "13":
        print("""
        ECP: Efectividad en la Conciliacion PROFECO:
        Descripcion:
        Medir la efectividad de resolución en un proceso conciliatorio mediante
        un análisis previo del motivo de queja, que permita realizar las acciones
        necesarias y/o propuestas de solución a presentar ante el consumidor y
        conciliador para poder cerrar el proceso conciliatorio desde la primera audiencia.
        Objetivo del indicador:
        Medir la efectividad de la conciliación ante PROFECO para el cierre
        del proceso conciliatorio desde la primera audiencia.
        """)
        print("Presiona 's' y da enter para ver imagen")
        resp=input()
        if resp=="s":
            img = Image.open("imagenes/ECP.png")
            img.show()
            input("Presiona enter para continuar")                          
    if op == "14":
        print("""
        CMP: Cero Multas PROFECO:
        Descripcion:
        Dar seguimiento a las multas notificadas por PROFECO derivadas de
        incumplimientos en los procesos conciliatorios a partir de 2021.
        Las multas que sean notificadas derivadas de un PIL o no correspondan
        a CFE SSB se evaluaran para determinar su procedencia y descontar del indicador.
        Objetivo del indicador:
        Evitar ser sujetos a multas interpuestas por PROFECO derivadas de
        incumplimientos en los procesos conciliatorios asi como dar seguimiento
        a las mismas hasta su pago o impugnación.
        """)
        print("Presiona 's' y da enter para ver imagen")
        resp=input()
        if resp=="s":
            img = Image.open("imagenes/CMP.png")
            img.show()            
            input("Presiona enter para continuar")                          
    if op == "0":
        print("Fue un placer ayudarte")
        continua=False
        exit
