######################
##
##
##
##
#
##
##
######################


import pyodbc

def read(conz):
    print("Read")
    cursor = conz.cursor()
    cursor.execute("select * from DB02.dbo.tabl01")
    for row in cursor:
        print (f'row={row}')

    print()


def create(conn):
    print("Create")
    cursor = conn.cursor()
    ##INGRESO
    sql="insert into DB02.dbo.tabl01 ( \
    unique_key \
    ,log_id \
    ,create_operator \
    ,create_time \
    ,event_time \
    ,pin \
    ,name \
    ,last_name \
    ,dept_name \
    ,area_name \
    ,card_no \
    ,dev_id \
    ,dev_sn \
    ,dev_alias \
    ,verify_mode_no \
    ,verify_mode_name \
    ,event_no \
    ,event_name \
    ,event_point_type \
    ,event_point_id \
    ,event_point_name \
    ,reader_state \
    ,reader_name \
    ,trigger_cond \
    ,description \
    ,vid_linkage_handle \
    ,acc_zone \
    ,event_addr \
    ) values ( \
    'AJYS174660018_12700_2020-03-09 22:24:00' \
    ,12700 \
    ,NULL \
    ,'2020-03-09 22:24:00.000' \
    ,'2020-03-09 22:24:00.000' \
    ,'8000003'  \
    ,'JOSE MARIA'  \
    ,'LIBERTAD AGUIRRE' \
    ,'General'  \
    ,'Nombre de Área'  \
    ,'5603151'  \
    ,1  \
    ,'AJYS174660018'  \
    ,'192.168.1.12'  \
    ,4  \
    ,'Solo Tarjeta'  \
    ,27  \
    ,'Usuario no registrado'  \
    ,0  \
    ,1 \
    ,'192.168.1.12-1'  \
    ,0 \
    ,'192.168.1.12-1-Entrada' \
    ,NULL \
    ,'' \
    ,NULL \
    ,NULL \
    ,1 \
    )"

    
    cursor.execute(sql)
    conn.commit()
    read(conn)



  
conu = pyodbc.connect(
	"Driver={SQL Server Native Client 11.0};"
	"Server=LAPTOP-C8B4STK9;"
        "Database=DB01;"
        "Trusted_Connection=yes;"
        )

conz = pyodbc.connect(
	"Driver={SQL Server Native Client 11.0};"
	"Server=LAPTOP-C8B4STK9;"
        "Database=DB02;"
        "Trusted_Connection=yes;"
        )


print('### INICIO INSERCION  ###')
read(conz)
print('### VER  ###')
create(conz)
print('### FIN  ###')
##update()
#delete()



conu.close()
conz.close()

