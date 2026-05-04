# 🚀 Engineering Portfolio: Python, APIs & Data Automation

Este repositório consolida quatro projetos fundamentais que demonstram a aplicação de padrões de engenharia de software, integração de sistemas e automação de fluxos de dados.

---

## 🛠️ Projetos

### 1. Arquitetura de Frota (OOP)
Modelagem de um sistema de gestão utilizando os pilares da **Programação Orientada a Objetos**.
*   **Aplicação:** Uso de classes, herança e polimorfismo para organizar entidades de negócio de forma escalável.
*   **Destaque:** Abstração de tipos de veículos para facilitar a manutenção e evolução do código.

### 2. Persistência de Dados (SQLAlchemy & SQL Server)
Criação de uma camada de mapeamento objeto-relacional (ORM) para integração com bancos de dados.
*   **Aplicação:** Implementação de **Idempotência** para criação automática de esquemas e gestão de transações seguras.
*   **Destaque:** Garantia de integridade dos tipos de dados antes da carga no SQL Server.

### 3. Micro-Pipeline de ETL (Flask & ViaCEP)
Serviço para extração, transformação e carga incremental de endereços.
*   **Aplicação:** Ingestão de API REST, enriquecimento com metadados de auditoria (`data_carga`) e persistência em **SQLite**.
*   **Destaque:** Interface web para controle de ingestão e visualização de dados em tempo real.

### 4. Automação de Documentos & Comunicação (PDF + SMTP)
Fluxo completo de automação para geração de documentos oficiais e notificações por e-mail.
*   **Aplicação:** Geração dinâmica de PDFs (ReportLab) e envio automatizado via protocolo **SMTP** do Gmail.
*   **Destaque:** Uso de **Streams de Memória** (`io.BytesIO`) e compactação ZIP para otimizar a performance do servidor sem gerar arquivos temporários residuais.
