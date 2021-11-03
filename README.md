# CloudComputer

## _Estruturas de aprendizagem em Computação em Nuvem, BI e POO_


Etapa Avaliativas:

- Dashboard BI (realização das etapas de ETL para um dashboard utilizando o Power BI)
- Container(es) de uma aplicação (Linguagem de escolha livre) que consiga realizar operações com os dados presentes em outro container de banco de dados.
- Container(es) de Banco de Dados (MYSQL) que receberá em suas tabela os dados do conteiner acima. 

| Itens      | Descrição     |
| ------------- |:-------------:|
| Dashboard BI     | realizar as etapas de ETL para um dashboard utilizando o Power BI). |
| Container BD     | Container(es) de Banco de Dados (MYSQL) que receberá em suas tabela os dados do conteiner acima.     |
| APP Conatiner    | Container(es) de uma aplicação (Linguagem de escolha livre) que consiga realizar operações com os dados presentes em outro container de banco de dados.   |


Encontro do dia 01/11: 

- [x] Container BD realizado.

Consultar arquivo na pasta MYSQL "docker-compose.yaml"

- Observem o nome de nosso arquivo, para execução execute em seu terminal o seguinte comando:

```
docker-compose up -d
```


Encontro do dia 03/11: 

- [x] Fontes para construção do container (diretório flask)
  - links importantes:
    Python / Flsk : https://www.youtube.com/watch?v=9qDTCIY3tK4
    
- [x] Teste de Integração APP com Banco de Dados
   - diretório app

Prõximo encontro:
- [ ] Build do APP
- [ ] Imagem do APP
- [ ] Container APP realizado.

Fontes de consulta para o item APPContainer:

https://docs.docker.com/compose/gettingstarted/

https://docs.microsoft.com/pt-br/azure/cognitive-services/containers/container-image-tags?tabs=current


Encontro do dia 05/11: 

- [ ] preparação de medidas e itens
- [ ] Dashboard BI: Concurso de Dashboard mais rápido e com layout agradável 



**Para o sucesso desta atividade e aprendizado será necessário realizar o seguinte treinamento (Todas as etapas) presentes no seguinte container:**


```
 docker run -d -p 80:80 docker/getting-started
 ```
