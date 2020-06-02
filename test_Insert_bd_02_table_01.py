######################
##
##
##
##
##
##
######################

import pyodbc

def readz(conz):
    print("Read")
    cursor = conz.cursor()
    cursor.execute("select * from DB02.dbo.tabla02")
    for row in cursor:
        print (f'row={row}')

    print()

def readu(conu):
    print("Read")
    cursor = conu.cursor()
    cursor.execute("select * from DB01.dbo.tabla04")
    for row in cursor:
        print (f'row={row}')

    print()

def comparando(conu,conz):
    cz = conz.cursor()
    ciz = conz.cursor()
    cu = conu.cursor()
    cu.execute("select * from DB01.dbo.tabla04")
    print("select * from DB01.dbo.tabla04")
    for rowu in cu:
        #print (rowu[0])
        print ('#####')
        print("select count(*) from DB02.dbo.tabla02 where Idtabla04= "+rowu[0])
        for rowz in cz.execute("select count(*) from DB02.dbo.tabla02 where Idtabla04= "+rowu[0]).fetchall():#cz:
            if rowz[0]==0:
                id=0
                pin=0
                ciz.execute("select top 1 id,pin from DB02.dbo.tabla02 order by 1 desc")
                for me in ciz:
                    print (me[0])
                    print (me[1])
                    id=int(me[0])+1
                    pin=int(me[1])+1
                print (id)
                print ('FALTA EL DATO')
                print (f'rowu={rowu}')
                print (rowu[0])
                print (rowu[1].split(',')[0])
                print (rowu[1].split(',')[1].lstrip())
                print (rowu[2])
                print (rowu[3])
                print (rowu[4])
                print (rowu[5])
                print (rowu[6])
                print (rowu[7])
                print (rowu[8])
                print (rowu[9])
                print (rowu[10])
                print (rowu[11])
                print (rowu[12])
                print (rowu[13])
                print (rowu[14])
                print (rowu[15])
                sql0="SET IDENTITY_INSERT [DB02].[dbo].[tabla02] on"
                ciz.execute(sql0)
                ciz.commit()
                sql="INSERt INTO DB02.dbo.tabla02 \
                ( \
                id, \
                dept_id,\
                position_id,\
                create_operator,\
                change_time,\
                pin,\
                name,\
                last_name,\
                gender,\
                photo_path,\
                status,\
                name_spell,\
                person_type,\
                birthday,\
                mobile_phone,\
                email,\
                person_pwd,\
                ssn,\
                car_plate,\
                self_pwd,\
                create_time,\
                exception_flag,\
                is_sendmail,\
                hire_date,\
                id_card,\
                id_card_physical_no,\
                is_from \
                ,Idtabla04 \
                ,DatosCompletos \
                ,dni \
                ,ACAD_CAREER \
                ,EMPLID \
                ) \
                 VALUES \
                ( \
                "+str(id)+" \
                ,1 \
                ,2 \
                ,'' \
                ,Convert(datetime, getdate(),103) \
                ,'"+str(pin)+"' \
                ,'"+rowu[1].split(',')[1].lstrip()+"' \
                ,'"+rowu[1].split(',')[0]+"' \
                ,'"+rowu[12]+"' \
                ,'' \
                ,0 \
                ,'"+rowu[1]+"' \
                ,0 \
                ,'' \
                ,'' \
                ,'' \
                ,'3000009' \
                ,'' \
                ,'' \
                ,'3000009' \
                ,Convert(datetime, getdate(),103) \
                ,0 \
                ,'0'  \
                ,''\
                ,''\
                ,''\
                ,''\
                ,'"+rowu[0]+"' \
                ,'"+rowu[1]+"' \
                ,'"+rowu[2]+"' \
                ,'"+rowu[5]+"' \
               ,'"+rowu[8] +"' ) "
                print (sql)
                ciz.execute(sql)
                ciz.commit()
                sql0="SET IDENTITY_INSERT DB02.dbo.tabla02 off"
                ciz.execute(sql0)
                ciz.commit()
                #read(conu)
                #########
                sql_card_certificate01="SET IDENTITY_INSERT DB02.dbo.tabla12 ON"
                ciz.execute(sql_card_certificate01)
                ciz.commit()
                sql_card_certificate02="insert into DB02.dbo.tabla12 ( \
                id \
                ,person_id \
                ,card_type \
                ,card_state \
                ,card_no \
                ,issue_time) VALUES ( "+str(id)+",'"+str(id)+"' ,0,1,'"+rowu[3]+"','2020-02-24 11:48:56.517')"
                ciz.execute(sql_card_certificate02)
                ciz.commit()
                sql_card_certificate03="SET IDENTITY_INSERT DB02.dbo.tabla12 OFF"
                ciz.execute(sql_card_certificate03)
                ciz.commit()
                #########
                #########
                sql_tabla0501="SET IDENTITY_INSERT DB02.dbo.tabla05 OFF"
                ciz.execute(sql_tabla0501)
                ciz.commit()
                sql_tabla0502="insert into DB02.dbo.tabla05 ( \
                person_id \
                ,cert_type \
                ,cert_number \
                ,cert_status) VALUES ( "+str(id)+" ,'1','"+rowu[2]+"',0)"
                ciz.execute(sql_tabla0502)
                ciz.commit()
                #########
                sql_tabla06="insert into DB02.dbo.tabla06 VALUES ("+str(id)+")"
                ciz.execute(sql_tabla06)
                ciz.commit()
                #########
                sql_tabla07="INSERT into DB02.dbo.tabla07 VALUES ("+str(id)+",'1',0,0,null)"
                ciz.execute(sql_tabla07)
                ciz.commit()
                #########
                sql_tabla08="INSERT INTO DB02.dbo.tabla08 VALUES ("+str(id)+",'0',NULL,NULL,'0',NULL,NULL,'0',NULL,'1')"
                ciz.execute(sql_tabla08)
                ciz.commit()
                #########
                sql_tabla0901="SET IDENTITY_INSERT DB02.dbo.tabla09 ON"
                ciz.execute(sql_tabla0901)
                ciz.commit()
                sql_tabla0902="INSERT INTO DB02.dbo.tabla09 (id,area_id,person_id) VALUES ("+str(id+3)+",1 ,"+str(id)+")"
                print(sql_tabla0902) 
                ciz.execute(sql_tabla0902)
                ciz.commit()
                sql_tabla0903="SET IDENTITY_INSERT DB02.dbo.tabla09 OFF"
                ciz.execute(sql_tabla0903)
                ciz.commit()                
                #########
                sql_tabla10="INSERT INTO DB02.dbo.tabla10 VALUES("+str(id)+",'0',NULL,NULL,'0',NULL)"
                ciz.execute(sql_tabla10)
                print("INSERT INTO DB02.dbo.tabla10 VALUES("+str(id)+",'0',NULL,NULL,'0',NULL)")
                ciz.commit()
                #########
                sql_tabla1101="SET IDENTITY_INSERT DB02.dbo.tabla11 ON"
                ciz.execute(sql_tabla1101)
                ciz.commit()
                sql_tabla1102="INSERT INTO DB02.dbo.tabla11 (ID,PERSON_ID)  VALUES  ("+str(id)+ ","+str(id)+")"
                ciz.execute(sql_tabla1102)
                print("INSERT INTO DB02.dbo.tabla11 (ID,PERSON_ID)  VALUES  ("+str(id)+ ","+str(id)+")")
                ciz.commit()
                sql_tabla1103="SET IDENTITY_INSERT DB02.dbo.tabla11 OFF"
                ciz.execute(sql_tabla1103)
                ciz.commit()
                print("#####")
                print("INSERCION TERMINADA")
                print("#####")
            else:
                print("No hay Usuarios Nuevos")


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

#print('### INICIO LECTURA TABLA tabla04S DB01 ###')
#readu(conu)
#print('### INICIO LECTURA TABLA PERSONAS ZK ###')
#readz(conz)
print('### COMPARANDO ###')
while True:
    comparando(conu,conz)
#print('### VER DB01 ###')
#create(conz)
print('### FIN DB01 ###')
##update()
#delete()



conu.close()
conz.close()

