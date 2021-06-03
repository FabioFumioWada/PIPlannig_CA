#%% [Cria/Importa objetos da PI Planning]

#######################################################################################
#######################################################################################
##                 Cria/Importa objetos da PI Planning - PI/CA                       ##
##                                                                                   ##
## Desenvolvido por: Fábio Fumio Wada                                                ##
#######################################################################################
#######################################################################################

#######################################################################################
# Copie todo este texto e cole em um novo arquivo do Jupyter                          #
# Modelo                                                                              #
#######################################################################################

### [Importa Bibliotecas] 
import pandas as pd #Pandas
import numpy as np #Numpy



#######################################################################################
##                                 Informar Valores:                                 ##   
#######################################################################################

### [Define Parâmetros]                                                              ##
v_pi = 'PI09' 
v_cod_obj = 'OP' #Inicial do código do objetivo associado na feature
v_cod_obj_s = 'OS' #Inicial do código do objetivo stretch associado na feature

### --> [Caminho do Arquivo]                                                         ##
v_diretorio_mae = 'C:\\Users\\A98718\\OneDrive - Somos Educação SA\\'
v_subdiretorio = 'python\\'+v_pi+'\\'

### --> [Informar os nomes dos arquivos]  *.csv                                      ##
v_nomearquivo_objetivos = 'Objetivos2.csv'   #arquivo não extraído do CA
v_nomearquivo_feature = 'feature.csv'      

#######################################################################################   
#######################################################################################



#######################################################################################
### [GLOBAL] - INÍCIO                                                               ###
#######################################################################################

#Limpa o campo TAGS das Features
def fn_limpa_tags(v_tags_origem):
    v_tags = v_tags_origem
    v_tags = v_tags.replace('Revisado','',regex=True)
    v_tags = v_tags.replace('(SM)','',regex=True)
    v_tags = v_tags.replace(r"\(.*?\)","",regex=True)
    v_tags = v_tags.replace('Apprendi!','',regex=True)
    v_tags = v_tags.replace('Stretch','',regex=True)
    v_tags = v_tags.replace(';','',regex=True)
    v_tags = v_tags.replace('#EP394','',regex=True)
    v_tags = v_tags.replace('#EP395','',regex=True)
    return (v_tags)


#######################################################################################
### [GLOBAL] - FIM                                                                  ###
#######################################################################################




#######################################################################################
### [OBJETIVOS] - INÍCIO                                                            ###
#######################################################################################

### [Define endereço do arquivo]
v_caminho_objetivos = ( v_diretorio_mae + 
                        v_subdiretorio+
                        v_nomearquivo_objetivos)

### [Transforma os dados do .csv em um dataframe]
df_objetivos = pd.read_csv(v_caminho_objetivos , sep = ",")
    #v_historias = pd.read_csv("C:\\Users\\A98718\\OneDrive - Somos Educação SA\\python\\PI09\\export.csv")

### [Renomeia colunas]
df_objetivos.rename(columns = {'Release' : 'PI'}, inplace = True)
df_objetivos.rename(columns = {'Trem' : 'Trem'}, inplace = True)
df_objetivos.rename(columns = {'Time' : 'Time'}, inplace = True)
df_objetivos.rename(columns = {'Objetivo' : 'Nome'}, inplace = True)
df_objetivos.rename(columns = {'Tipo do Objetivo' : 'Tipo'}, inplace = True)
df_objetivos.rename(columns = {'BV Planejado' : 'BV'}, inplace = True)
df_objetivos.rename(columns = {'Nota BV' : 'Nota'}, inplace = True)
df_objetivos.rename(columns = {'Pontos Planejados' : 'Pontos Planejados'}, inplace = True)
df_objetivos.rename(columns = {'Pontos Entregues' : 'Pontos Entregues'}, inplace = True)
df_objetivos.rename(columns = {'Chave' : 'Codigo'}, inplace = True)

### [Cria Funções]

### [Objetivos - Listagem] - Lista Objetivos
def fn_obj_listagem(v_pi):
    return df_objetivos[df_objetivos['PI'] == v_pi]


#######################################################################################
### [OBJETIVOS] - FIM                                                               ###
#######################################################################################



#######################################################################################
### [FEATURE] - INÍCIO                                                              ###
#######################################################################################

### [Define endereço do arquivo]
v_caminho_feature = (   v_diretorio_mae + 
                        v_subdiretorio+
                        v_nomearquivo_feature)

### [Transforma os dados do .csv em um dataframe]
df_feature = pd.read_csv(v_caminho_feature , sep = ",")
    # v_historias = pd.read_csv("C:\\Users\\A98718\\OneDrive - Somos Educação SA\\python\\PI09\\export.csv")
    # pd.read_csv('nome_do_arquivo.csv', encoding='ISO-8859-1')

### [Renomeia colunas]
df_feature.rename(columns = {'Formatted ID' : 'Codigo'}, inplace = True)
df_feature.rename(columns = {'Name' : 'Nome'}, inplace = True)
df_feature.rename(columns = {'Release' : 'PI'}, inplace = True)
df_feature.rename(columns = {'State' : 'Status'}, inplace = True)
df_feature.rename(columns = {'Percent Done By Story Plan Estimate' : 'Percent_por_PlanEstimate'}, inplace = True)
df_feature.rename(columns = {'Percent Done By Story Count' : 'Percent_por_QtdHistoria'}, inplace = True)
df_feature.rename(columns = {'Project' : 'Time'}, inplace = True)
df_feature.rename(columns = {'Owner' : 'Responsavel'}, inplace = True)
df_feature.rename(columns = {'Parent' : 'Epico'}, inplace = True)
df_feature.rename(columns = {'Tags' : 'Tags'}, inplace = True)

### [Cria coluna Codigo_Objetivo]
df_feature['Codigo_Objetivo'] = 'NaN'
df_feature['Codigo_Objetivo'] = fn_limpa_tags(df_feature['Tags'])

### [Cria Funções]

### [Feature - Listagem] - Lista Features
#    Parâmetros:    "O" - Somente Objetivos (Sem Objetivos Stretch) 
#                   "S" - Somente Objetivos Stretch
#                   "F" - Todos os Objetivos
def fn_ftr_listagem(v_pi,v_opcao):
    if v_opcao == "O": #Objetivo sem Stretch
        return df_feature[df_feature['Tags'].str.contains((v_cod_obj+v_pi),na=False) & (df_feature['PI'] == v_pi)]
    elif v_opcao == "S": #Objetivo Stretch
        return df_feature[df_feature['Tags'].str.contains((v_cod_obj_s+v_pi),na=False) & (df_feature['PI'] == v_pi)]
    elif v_opcao == "F": #Todos os Objetivos 
        return df_feature.loc[df_feature['PI'] == v_pi]
    else:
        print('Opção Indisponível: '+'"'+v_opcao+'"')

### [Feature - Listagem] - Soma Features
def fn_ftr_quantidade(v_pi):
    print('Features (Sem Obj Stretch): ',df_feature[df_feature['Tags'].str.contains((v_cod_obj+v_pi),na=False) & (df_feature['PI'] == v_pi)].Codigo.count())
    print('Features (Com Obj Stretch): ',df_feature[df_feature['Tags'].str.contains((v_cod_obj_s+v_pi),na=False) & (df_feature['PI'] == v_pi)].Codigo.count())    
    print('Features (Com Erros Cadastrais - A): ',df_feature[~df_feature['Tags'].str.contains((v_pi),na=False) & (df_feature['PI'] == v_pi)].Codigo.count())      
    print('Features (Com Erros Cadastrais - B): ',df_feature[df_feature['Tags'].str.contains((v_pi),na=False) & (df_feature['PI'] != v_pi)].Codigo.count())      
    print('---------------------------------')
    print('Features (Total): ',df_feature.loc[df_feature['PI'] == v_pi].Codigo.count())
    print('')
    print('')
    print('** Features (Com Erros Cadastrais - A) = "Ausência de Objetivo e/ou Objetivo pertencente a outra PI"')
    print('** Features (Com Erros Cadastrais - B) = "Objetivo da PI atual vinculado a uma Feature de outra PI"')

### [Feature - Listagem] - Lista Erros Cadastrais
# Ex: 1) Feature sem um objetivo da "PI" vinculado. Ex: PI09 é oficial e possui objetivo da PI08
#     2) Feature sem objetivo
def fn_ftr_erros(v_pi):
    return df_feature[~df_feature['Tags'].str.contains((v_pi),na=False) & (df_feature['PI'] == v_pi)]
    return df_feature[df_feature['Tags'].str.contains((v_pi),na=False) & (df_feature['PI'] != v_pi)]
    
#######################################################################################
### [FEATURE] - FIM                                                                 ###
#######################################################################################


#######################################################################################
### [ANALITICO] - INICIO                                                            ###
#######################################################################################

# Monta um novo dataframe com base em um dataframe já existente
df_obj_resumo = pd.DataFrame(df_objetivos, columns = ['Codigo','Trem','Time','Tipo','BV'])
df_obj_resumo['Qtd_Features'] = 0

# Dataframe temporario com os dados da Feature
#df_tmp_ftr = pd.DataFrame(df_feature, columns = ['Codigo','Codigo_Objetivo'])
#zz = df_tmp_ftr.groupby['Codigo_Objetivo','Codigo'].count()



#######################################################################################
### [ANALITICO] - FIM                                                               ###
#######################################################################################



# %%