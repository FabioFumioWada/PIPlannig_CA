#%% [Análise de Histórias]

#######################################################################################
#######################################################################################
##                                 Análise de Histórias - CA                         ##   
##                                                                                   ##
## Desenvolvido por: Fábio Fumio Wada                                                ##
#######################################################################################
#######################################################################################

#######################################################################################
##                                 Informar Valores:                                 ##   
#-- Informar o nome do arquivo                                                       ##
v_nomearquivo = 'export.csv'                                                         
v_pi = 'PI09' 
##                                                                                   ##
#######################################################################################

### [Importa Bibliotecas] 
import pandas as pd #Pandas
import numpy as np #Numpy

#import datetime as dt #Datetime

### [Caminho do Arquivo]
v_diretorio_mae = 'C:\\Users\\A98718\\OneDrive - Somos Educação SA\\'
v_subdiretorio = 'python\\PI09\\'

v_caminho = (   v_diretorio_mae + 
                v_subdiretorio+
                v_nomearquivo)

### [Transforma os dados do .csv em um dataframe]
df_historias = pd.read_csv(v_caminho)
    #v_historias = pd.read_csv("C:\\Users\\A98718\\OneDrive - Somos Educação SA\\python\\PI09\\export.csv")

### [Renomeia colunas]
df_historias.rename(columns = {'Ready' : 'Lido'}, inplace = True) 
df_historias.rename(columns = {'Blocked' : 'Bloqueado'}, inplace = True)
df_historias.rename(columns = {'Feature' : 'Feature'}, inplace = True)
df_historias.rename(columns = {'Formatted ID' : 'Codigo'}, inplace = True)
df_historias.rename(columns = {'Name' : 'Nome'}, inplace = True)
df_historias.rename(columns = {'Release' : 'PI'}, inplace = True)
df_historias.rename(columns = {'Iteration' : 'Iteracao'}, inplace = True)
df_historias.rename(columns = {'Schedule State' : 'Status'}, inplace = True)
df_historias.rename(columns = {'Plan Estimate' : 'Pontos'}, inplace = True)
#Tasks
df_historias.rename(columns = {'Task Estimate Total' : 'Tasks_Horas_Estimate'}, inplace = True)
df_historias.rename(columns = {'Actual' : 'Tasks_Horas_Actual'}, inplace = True)
df_historias.rename(columns = {'To Do' : 'Tasks_Horas_ToDo'}, inplace = True)

    #Outras colunas da planilha
        #Blocked,"Ready","Feature","Formatted ID","Name","Release","Iteration","Schedule State",
        #Plan Estimate","Task Estimate Total","Actual","To Do","Tipo","Sistema Impactado","Owner",
        #"Tags","Abertura Indevida","Classificação","Acceptance Criterias","Accepted Date","Blocked Category",
        #"Creation Date","Description","Direct Children Count","Discussion Count","Display Color","Expedite",
        #"Last Update Date","Milestones","Notes","Object ID(OID)","Project","ServiceNow ID",
        #"ServiceNow Sys ID","Parent ID"

### [DataFrame de Iterações]
df_historias_it1 = df_historias.loc[df_historias['Iteracao'] == v_pi+'.1']
df_historias_it2 = df_historias.loc[df_historias['Iteracao'] == v_pi+'.2']
df_historias_it3 = df_historias.loc[df_historias['Iteracao'] == v_pi+'.3']
df_historias_it4 = df_historias.loc[df_historias['Iteracao'] == v_pi+'.4']
df_historias_it5 = df_historias.loc[df_historias['Iteracao'] == v_pi+'.5']
df_historias_it6 = df_historias.loc[df_historias['Iteracao'] == v_pi+'.6']
df_historias_it7 = df_historias.loc[df_historias['Iteracao'] == v_pi+'.7']
df_historias_itx = df_historias.loc[df_historias['Iteracao'] == v_pi+'.x']

print('----- [Histórias]')
df_historias_itx.head(100)

#%%

# %%
df_historias_iteracoes

# %%
#Análise Estatística

#Contador unique
df_historias_iteracoes = [df_historias.Iteracao.unique()]

#faz uma média geral
df_historias.describe()

#Conta Registros
pd.value_counts(df_historias['Iteracao'])

#Pesquisa simples
df_historias.loc[df_historias['Iteracao']=="PI09.2"]

#Pesquisa com AND
df_historias.loc[(df_historias['Iteracao']=="PI09.2") & (df_historias['Tipo'] == "Solicitação de Serviços")]

#Ordenação
df_historias.sort_values(by='Codigo',ascending='False')

#Somatório com os campos do dataset
df_historias[df_historias['Iteracao']=='PI09.2'].count()


# %%
# %%
df_historias['Iteracao'].plot()

# %%
df_historias_it2

# %%


# [Feature - Listagem] com "OBJETIVOS" dentro da PI (Parâmetro = PI09, PI08, PI10)
def fn_ftr_obj(v_pi):
    return df_feature[df_feature['Tags'].str.contains("OPP",na=False) & (df_feature['PI'] == v_pi)]
    #Exemplo: fn_feature_obj('PI09')

# [Feature - Listagem] - com "OBJETIVOS STRETCH" dentro da PI (Parâmetro = PI09, PI08, PI10)
def fn_ftr_obj_s(v_pi):
    return df_feature[df_feature['Tags'].str.contains("OSP",na=False) & (df_feature['PI'] == v_pi)]
    #Exemplo: fn_feature_obj_s('PI09')

# [Feature - Quantidade] - com "OBJETIVOS" dentro da PI (Parâmetro = PI09, PI08, PI10)
def fn_ftr_obj(v_pi):
    return df_feature[df_feature['Tags'].str.contains("OPP",na=False) & (df_feature['PI'] == v_pi)]
    #Exemplo: fn_feature_obj('PI09')




    """
       if v_opcao == "O": #Objetivo sem Stretch
            return df_feature[df_feature['Tags'].str.contains("OPP",na=False) & (df_feature['PI'] == v_pi)].Codigo.count()
        elif v_opcao == "S": #Objetivo Stretch
            return df_feature[df_feature['Tags'].str.contains("OSP",na=False) & (df_feature['PI'] == v_pi)].Codigo.count()
        elif v_opcao == "F": #Todos os Objetivos 
            return df_feature.loc[df_feature['PI'] == v_pi].Codigo.count()
        else:
            print('Opção Indisponível: '+'"'+v_opcao+'"')
"""
