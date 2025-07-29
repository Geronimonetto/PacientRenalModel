# <div align="center">
  <h1 align="center">
    <br />
    <br />
    <img src="https://media.istockphoto.com/id/1218610779/pt/vetorial/an-unhealthy-kidney-mascot-renal-failure.jpg?s=612x612&w=0&k=20&c=4Y_lTzU5K2e1kgGkQyXkJvzutq4RFpPTAwInOJnkLgo=" alt="Patient Renal Classifier">
  </h1>
</div>

# 📘 Introdução

Este projeto foi desenvolvido utilizando um modelo de **Regressão Logistica (RegressionClassifier)** e implementado com **Streamlit** para visualização interativa.  
O objetivo principal é **classificar pacientes com doença renal crônica (CKD)** com base em características clínicas relevantes, como:

- Idade  
- Creatinina sanguínea  
- Presença de diabetes  
- Hipertensão  
- Taxa de filtração glomerular  
- Produção de urina  

Com esses dados, o modelo obteve resultados expressivos:

- **Acurácia**: 87,85%  
- **Precisão**: 91,30%  
- **Recall**: 83,26%  
- **min_samples_leaf**: 10  

### **Matriz de confusão:**

```python
TN = 216    FP = 18  
FN = 36     TP = 191
```


# Arquitetura do Projeto ⛏️⚙️


### 📦 Dados

Os dados foram obtidos diretamente da API do Kaggle.  
No entanto, para garantir a continuidade do projeto mesmo que o dataset original seja descontinuado, uma cópia foi incluída na pasta `data/raw`.

### 🔁 Carregando os dados via API (KaggleHub)

```python
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "miadul/kidney-disease-risk-dataset",
    file_path,
    # Documentação completa:
    # https://github.com/Kaggle/kagglehub#kaggledatasetadapterpandas
)
```
### 💾 Carregando o dataset localmente
```
df = pd.read_csv('../data/raw/kidney_disease_dataset.csv')
```

### Instruções para uso do projeto 👨‍💻

🚀 Instruções para uso do projeto 👨‍💻
Siga os passos abaixo para executar o projeto localmente:

1. Clone o repositório
```git
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Crie um ambiente virtual

### Para sistemas Unix (Linux/macOS)
```
python3 -m venv .venv
source .venv/bin/activate
```

### Para Windows
```
python -m venv .venv
.venv\Scripts\activate
```
3. Instale as dependências
```
pip install --upgrade pip
pip install -r requirements.txt
```
4. Execute o projeto com Streamlit
```
streamlit run app.py
```

📌 Certifique-se de estar com o ambiente virtual ativado ao rodar esse comando.

5. Acesse no navegador
Geralmente no endereço:
```
http://localhost:8501
```
### Decisão de Seleção do Modelo

Ao comparar os modelos aplicados, o **Logistic Regression** apresentou resultados mais realistas e consistentes. Suas métricas foram:

- **Acurácia**: 84,16%  
- **Precisão**: 83,19%  
- **Recall**: 85,02%

Esses valores indicam uma boa capacidade de generalização do modelo, com equilíbrio entre acertos nas classes positivas e negativas. A **curva ROC** também demonstrou uma boa separação entre as classes, reforçando a eficácia do modelo.

Por outro lado, o modelo de **Árvore de Decisão**, apesar de ter apresentado uma acurácia média próxima de **100%** nos folds da **validação cruzada**, mostrou sinais evidentes de **overfitting**, aprendendo demais os dados de treino e generalizando mal para novos dados. Isso ficou evidente tanto na complexidade da árvore (com apenas 3 divisões) quanto nos resultados inflados do cross-validation.

> ✅ **Conclusão**: O modelo de **Regressão Logística** foi selecionado como o mais adequado, por apresentar desempenho consistente, boa generalização e métricas realistas frente aos dados analisados.

### 📄 Licença
Este projeto está licenciado sob a MIT License.

### ✅ Próximos Passos
#### Coleta de Novos Dados
Continuar a coleta e integração de novos dados relevantes ao problema para enriquecer o dataset atual, melhorando a variabilidade e robustez do modelo.

#### Atualização do Dataset e Pré-processamento

Realizar limpeza, tratamento de valores faltantes e encoding dos novos dados conforme o pipeline atual.

Verificar a distribuição das classes para garantir o balanceamento.

Reavaliação do Modelo (Regressão Logística)

#### Reajustar o modelo com os dados atualizados.

Avaliar se há ganho em métricas de performance como acurácia, precisão, recall, F1-score e AUC-ROC.

Validação Cruzada e Testes de Generalização

Executar validação cruzada (k-fold) para testar a consistência do modelo.

Comparar os resultados do modelo antigo com o modelo reentrenado.

#### Monitoramento do Desempenho em Produção

Implementar rotinas para monitoramento contínuo do modelo em produção (ex: conceito de model drift).

Validar previsões com dados reais, sempre que possível.

#### Documentação e Versionamento

Registrar as versões do modelo, alterações nas features e nas métricas obtidas.

Garantir reprodutibilidade com versionamento do código e dos dados.

#### Avaliar Novas Abordagens (Opcional)

Testar modelos adicionais como Árvore de Decisão, Random Forest, ou XGBoost para fins comparativos, caso o desempenho da Regressão Logística estagne.

#### Automatização da Pipeline

Criar um fluxo automatizado de ingestão de dados, treinamento e avaliação periódica do modelo, utilizando frameworks como Airflow ou scripts agendados.
