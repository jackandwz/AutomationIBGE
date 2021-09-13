import unidecode
import re
def UpToLower(strSeccao,strDivisao,strGrupo,strClasse,strSubClasse):
    strSeccao = strSeccao.lower()
    strDivisao = strDivisao.lower()
    strGrupo = strGrupo.lower()
    strClasse = strClasse.lower()
    strSubClasse = strSubClasse.lower()
    return strSeccao,strDivisao,strGrupo,strClasse,strSubClasse

def CodCorrections(strCodDivisao,strCodGrupo,strCodClasse,strCodSubClasse):
    strCodDivisao = strCodDivisao.replace(".","").replace("-","").replace("/","")
    strCodGrupo = strCodGrupo.replace(".","").replace("-","").replace("/","")
    strCodClasse = strCodClasse.replace(".","").replace("-","").replace("/","")
    strCodSubClasse = strCodSubClasse.replace(".","").replace("-","").replace("/","")
    return strCodDivisao,strCodGrupo,strCodClasse,strCodSubClasse
def FixColumnName(strColumnName):
    strColumnName = unidecode.unidecode(strColumnName)
    return strColumnName
