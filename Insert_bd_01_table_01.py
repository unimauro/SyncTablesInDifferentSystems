###################################################################
###################################################################
##
## Insercion de Datos de Prueba a la 
##
## Datos de Prueba
##
###################################################################
###################################################################


import pyodbc

def read(conu):
    print("Read")
    cursor = conu.cursor()
    cursor.execute("select top 1 * from db_01.table01 order by Id_Me desc ")
    for row in cursor:
        print (f'row={row}')

    print()

def comparar(conz,conu):
    print("Comparar")
    cursor01 = conz.cursor()
    cursor02 = conu.cursor()
    for z in cursor01.execute("select top 1 id,log_id,create_time,pin,card_no,Id_Me from DB02.dbo.table01 order by log_id desc ").fetchall():
        for u in cursor02.execute("select top 1 * from db_01.table01 order by Id_Me desc").fetchall():
            print(z[5])
            print("###")
            print(u[0])
            print("###")
            if (z[5]==u[0]):
                print(z[5])
                print(u[0])
            else:
                print("ACTUALIZAR MARCACIONES EN DB01")

                cursor03 = conz.cursor()
                sql0p="select dni,IdAlumno from DB02.dbo.table03 where pin='"+z[3]+"'"
                ##print(sql0p) 
                ##cursor03.execute(sql0p)
                for per in cursor03.execute("select dni,IdAlumno from DB02.dbo.table03 where pin='"+z[3]+"'").fetchall():
                    ciu = conu.cursor()
                    sql00="SET IDENTITY_INSERT db_01.table01 ON"
                    ciu.execute(sql00)
                    ciu.commit()

                    sql01= "insert into db_01.table01 \
                    ( \
                           Id_Me \
                           ,IdMolinete \
                           ,IdCampus \
                           ,IdAlumno \
                           ,dni \
                           ,IdTarjeta \
                           ,FecMarcacion \
                           ,IdEstadoAcceso \
                           ,Location \
                           ,Procesado \
                    ) \
                    values \
                    ( \
                    "+str(u[0]+1)+"\
                    ,'12' \
                    ,NULL \
                    ,'"+per[1]+"' \
                    ,'"+per[0]+"' \
                    ,'"+z[4]+"'  \
                    ,'"+str(z[2])+"' \
                    ,1 \
                    ,NULL \
                    ,NULL \
                    )"
                    print(sql01)
                    ciu.execute(sql01)
                    ciu.commit()
                    print("ACTUALIZAR TRANSACCION EN DB02")

                    ciz = conz.cursor()
                    sql02="update DB02.dbo.table01 set Id_Me='"+str(u[0]+1)+"'  where id="+str(z[0])
                    ciz.execute(sql02)
                    ciz.commit()
    
conu = pyodbc.connect(
	"Driver={SQL Server Native Client 11.0};"
	"Server=LAPTOP-C8B4STK9;"
        "Database=DB01;"
        "Trusted_Connection=yes;"
        )

conz = pyodbc.connect(
	"Driver={SQL Server Native Client 11.0};"
	"Server=LAPTOP-C8B4STK9;"
        "Database=BD02;"
        "Trusted_Connection=yes;"
        )


print('### INICIO INSERCION PRUEBA DB01 ###')
read(conu)
print('### VER INI ###')
while True:
    comparar(conz,conu)
print('### FIN  ###')

conu.close()
conz.close()
