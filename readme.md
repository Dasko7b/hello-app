# Projeto: Pipeline CI/CD com GitHub Actions, ArgoCD e FastAPI

[cite_start]Este projeto demonstra a automação do ciclo completo de desenvolvimento, build, deploy e execução de uma aplicação web simples em FastAPI[cite: 107]. [cite_start]O objetivo é implementar um fluxo de trabalho de CI/CD (Integração Contínua e Entrega Contínua) robusto, garantindo entregas de código com velocidade, segurança e consistência[cite: 100, 101].

[cite_start]A metodologia utilizada é o **GitOps**, onde o repositório Git atua como a única "fonte da verdade" para a infraestrutura e os deploys no Kubernetes[cite: 104].

## Tecnologias Utilizadas

* **Aplicação:** Python com FastAPI
* **Containerização:** Docker & Docker Hub
* **Orquestração:** Kubernetes
* **Ambiente Local K8s:** Rancher Desktop
* [cite_start]**CI/CD (Automação):** GitHub Actions [cite: 102]
* [cite_start]**Entrega Contínua (GitOps):** ArgoCD [cite: 102]
* **Controle de Versão:** Git & GitHub

## Pré-requisitos

Para replicar este ambiente, é necessário ter:
* [cite_start]Conta no GitHub (repositório público) [cite: 109]
* [cite_start]Conta no Docker Hub com um token de acesso [cite: 110]
* [cite_start]Rancher Desktop com Kubernetes habilitado [cite: 111]
* [cite_start]`kubectl` configurado corretamente para acessar o cluster [cite: 112]
* [cite_start]ArgoCD instalado no cluster local [cite: 113]
* [cite_start]Git, Python 3 e Docker instalados localmente [cite: 114, 115]

## Arquitetura do Projeto

O projeto é estruturado em dois repositórios Git distintos para seguir as melhores práticas de GitOps:

1.  **`hello-app` (Repositório da Aplicação):**
    * [cite_start]Contém o código-fonte da aplicação FastAPI (`main.py`)[cite: 118].
    * [cite_start]Inclui o `Dockerfile` para construir a imagem da aplicação[cite: 119].
    * [cite_start]Armazena o workflow do GitHub Actions (`.github/workflows/ci-cd.yaml`) que automatiza o processo de CI[cite: 124].

2.  **`hello-manifests` (Repositório de Manifestos):**
    * [cite_start]Contém os manifestos Kubernetes (`deployment.yaml` e `service.yaml`) que descrevem o estado desejado da aplicação no cluster[cite: 120, 129].
    * [cite_start]Este repositório é monitorado pelo ArgoCD, que aplica qualquer alteração diretamente no ambiente[cite: 130].

## Fluxo do CI/CD

O processo automatizado funciona da seguinte maneira:

1.  **Commit & Push:** O desenvolvedor faz uma alteração no código da aplicação e envia (`git push`) para a branch `main` do repositório `hello-app`.

2.  **Disparo do GitHub Actions:** O push aciona automaticamente a pipeline de CI/CD definida no GitHub Actions.

3.  **Build & Push da Imagem:** A pipeline faz o build de uma nova imagem Docker da aplicação. A imagem é tagueada com o hash do commit para garantir versionamento e imutabilidade. [cite_start]Em seguida, a imagem é enviada para o Docker Hub[cite: 124].

4.  [cite_start]**Abertura de Pull Request (PR):** Após o envio da imagem, a pipeline clona o repositório `hello-manifests` e atualiza o arquivo `deployment.yaml`, alterando a tag da imagem para a nova versão recém-criada[cite: 125]. Um Pull Request com essa alteração é aberto automaticamente no repositório de manifestos.

5.  **Aprovação e Merge:** Um responsável revisa o PR e faz o merge para a branch `main` do `hello-manifests`. Este passo manual garante um controle sobre o que é liberado em produção.

6.  [cite_start]**Sincronização do ArgoCD:** O ArgoCD, que está constantemente monitorando o repositório `hello-manifests`, detecta a alteração na branch `main`[cite: 130].

7.  **Deploy Contínuo:** O ArgoCD inicia o processo de sincronização, comparando o estado desejado (definido nos manifestos do Git) com o estado atual do cluster. Ele atualiza o `Deployment`, fazendo com que o Kubernetes baixe a nova imagem do Docker Hub e atualize os pods da aplicação sem downtime (rolling update).

## Como Acessar a Aplicação

[cite_start]Para acessar a aplicação que está rodando no cluster Kubernetes local, utilize o `port-forward` do `kubectl`[cite: 135].

1.  Abra um terminal e execute o comando abaixo. Ele criará um túnel de comunicação entre sua máquina e o serviço no cluster.
    ```bash
    kubectl port-forward svc/hello-app-service 8080:8080
    ```
    **Nota:** Mantenha este terminal aberto enquanto desejar acessar a aplicação.

2.  [cite_start]Abra seu navegador ou utilize `curl` para acessar o seguinte endereço[cite: 144]:
    ```bash
    http://localhost:8080/
    ```

A resposta esperada é a mensagem definida no arquivo `main.py`, como `{"message": "Hello World"}`.

## Autor

* [cite_start]Dyego Dasko [cite: 98]



