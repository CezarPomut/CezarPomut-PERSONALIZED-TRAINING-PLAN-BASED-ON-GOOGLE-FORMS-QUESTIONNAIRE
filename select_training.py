from list_training import lista_ant_sala,lista_ant_acasa
# import lista_antrenamente
# from lista_antrenamente import *

def selectare_antrenament(obj):
    if obj.get_sex()=="Masculin":
        if obj.get_scop()=="Acumulare tesut muscular":
            if obj.get_tip_antrenament()=="sala":
                if obj.get_numar_sedinte()==1:
                    obj.antrenament.append(lista_ant_sala[0])
                elif obj.get_numar_sedinte()==2:
                    for x in range(0,int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_sala[x])
                elif obj.get_numar_sedinte()==3:
                    for x in range(0,int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_sala[x])
                elif obj.get_numar_sedinte()==4:
                    for x in range(0,int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_sala[x])
                elif obj.get_numar_sedinte()==5:
                    for x in range(0,int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_sala[x])

            elif obj.get_tip_antrenament()=="acasa":
                if obj.get_numar_sedinte()==1:
                    obj.antrenament.append(lista_ant_sala[0])
                elif obj.get_numar_sedinte()==2:
                    for x in range(0,int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_sala[x])
                elif obj.get_numar_sedinte()==3:
                    for x in range(0,int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_sala[x])
                elif obj.get_numar_sedinte()==4:
                    for x in range(0,int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_sala[x])
                elif obj.get_numar_sedinte()==5:
                    for x in range(0,int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_sala[x])

        elif obj.get_scop() == "Pierdere tesut adipos":
            if obj.get_tip_antrenament() == "sala":
                if obj.get_numar_sedinte() ==1:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte() ==2:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte() ==3:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte() ==4:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte() ==5:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])

            elif obj.get_tip_antrenament()=="acasa":
                if obj.get_numar_sedinte()==1:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte()==2:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte()==3:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte()==4:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte()==5:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])


    elif obj.get_sex()=="Feminin":
        print("a intrat in fe")
        print(obj.get_scop())
        if obj.get_scop()=="Acumulare tesut muscular":
            if obj.get_tip_antrenament()=="sala":
                if obj.get_numar_sedinte()==1:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte()==2:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte()==3:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte()==4:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte()==5:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])

            elif obj.get_tip_antrenament()=="acasa":
                if obj.get_numar_sedinte()==1:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte()==2:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte()==3:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte()==4:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte()==5:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])

        elif obj.get_scop()=="Pierdere testut adipos":
            print("a intrat in ta")
            if obj.get_tip_antrenament()=="sala":
                if obj.get_numar_sedinte()==1:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte()==2:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte()==3:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte()==4:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte()==5:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])

            elif obj.get_tip_antrenament()=="acasa":
                print("a intrat acasa")
                if obj.get_numar_sedinte()==1:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte()==2:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte()==3:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte()==4:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
                elif obj.get_numar_sedinte()==5:
                    for x in range(0, int(obj.get_numar_sedinte())):
                        obj.antrenament.append(lista_ant_acasa[x])
