###################################################################
###################################################################
##
## Insercion de Datos de Prueba 
##
## Datos de Prueba
##('090028','LOYOLA PARCO, MARY MARILUZ','98997149','5603178','1','UNEPG','','','00000009461','','','','F','','','')
##
##
###################################################################
###################################################################


import pyodbc

def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select * from DB01.dbo.tabla01")
    for row in cursor:
        print (f'row={row}')

    print()

def create(conn):
    print("Create")
    cursor = conn.cursor()
    cursor.execute(
        'insert into DB01.dbo.tabla01 (pl.Idtabla01,pl.DatosCompletos,pl.dni,pl.IdTarjeta,pl.IdEstado,pl.Institution,pl.ACAD_CAREER,pl.STRM,pl.EMPLID,pl.FecIni,FecFin,pl.DESCRSHORT,pl.SEX,pl.App,pl.Unidad,pl.TipoEmpleado) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);',
        ('090017','MARCA PARCO, ROSAS MARILUZ','98997138','5603167','1','UNEPG','','','00000009450','','','','F','','','')
        )
    conn.commit()
    read(conn)


  
conn = pyodbc.connect(
	"Driver={SQL Server Native Client 11.0};"
	"Server=LAPTOP-C8B4STK9;"
        "Database=DB01;"
        "Trusted_Connection=yes;"
        )

print('### INICIO INSERCION PRUEBA DB01 ###')
read(conn)
print('### VER DB01 ###')
create(conn)
print('### FIN DB01 ###')

conn.close()
