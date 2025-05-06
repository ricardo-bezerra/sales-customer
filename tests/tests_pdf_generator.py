from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Guia de Estudo - Certificação Google Cloud Database Engineer", ln=True, align="C")
        self.ln(10)

    def chapter_title(self, title):
        title = self._sanitize(title)
        self.set_font("Arial", "B", 12)
        self.multi_cell(0, 8, title)
        self.ln(2)

    def chapter_body(self, body):
        body = self._sanitize(body)
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, body)
        self.ln()

    def _sanitize(self, text):
        # Remove caracteres que causam erro no latin-1
        return (text.replace("–", "-")
                    .replace("“", '"')
                    .replace("”", '"')
                    .replace("’", "'")
                    .replace("•", "-"))

# Inicia o PDF
pdf = PDF()
pdf.add_page()

content = [
    ("1. Projetar soluções de banco de dados escaláveis e altamente disponíveis (~42%)", [
        ("Planejamento de capacidade e uso",
         "Objetivo: Dimensionar recursos com base em métricas atuais e crescimento esperado.\n\n"
         "Exemplo: Para uma aplicação de e-commerce com picos de tráfego, usar o Cloud Monitoring para acompanhar uso de CPU, memória e conexões. Com base nesses dados, dimensionar instâncias do Cloud SQL ou definir throughput inicial no Cloud Spanner."),
        ("Alta disponibilidade e recuperação de desastres",
         "Objetivo: Garantir continuidade mesmo em falhas de zona ou região.\n\n"
         "Exemplo: Ativar replicação síncrona entre zonas no Cloud SQL (HA), backups automáticos e RTO/RPO definidos. Usar replicação multi-regional no Cloud Spanner."),
        ("Otimização de custo e desempenho",
         "Objetivo: Ajustar recursos para equilibrar performance e custo.\n\n"
         "Exemplo: Migrar de SSD para HDD em workloads menos críticos, desligar instâncias ociosas ou usar BigQuery em vez de sobrecarregar banco OLTP."),
        ("Automação de tarefas de banco de dados",
         "Objetivo: Reduzir esforço manual e erros em tarefas rotineiras.\n\n"
         "Exemplo: Usar Cloud Scheduler para backups e exportações automáticas, ou Cloud Functions + Pub/Sub para tarefas sob demanda.")
    ]),
    ("2. Gerenciar soluções que abrangem múltiplos bancos de dados (~24%)", [
        ("Conectividade e segurança",
         "Objetivo: Assegurar conexões seguras.\n\n"
         "Exemplo: Cloud SQL Auth Proxy, criptografia CMEK, certificados SSL."),
        ("Gerenciamento de usuários e acesso",
         "Objetivo: Permissões baseadas em função e auditoria.\n\n"
         "Exemplo: IAM + Cloud Audit Logs."),
        ("Integração de soluções de banco de dados",
         "Objetivo: Fluxo de dados entre bancos distintos.\n\n"
         "Exemplo: Cloud SQL -> BigQuery com Dataflow.")
    ]),
    ("3. Migrar soluções de dados (~14%)", [
        ("Planejamento e execução de migrações",
         "Objetivo: Minimizar downtime e risco.\n\n"
         "Exemplo: DMS com replicação contínua e plano de rollback."),
        ("Ferramentas de migração",
         "Objetivo: Usar as ferramentas adequadas.\n\n"
         "Exemplo: Schema Conversion Tool + DMS."),
        ("Captura de dados alterados (CDC)",
         "Objetivo: Replicação em tempo real.\n\n"
         "Exemplo: DMS com CDC para sincronizar Cloud SQL -> BigQuery.")
    ]),
    ("4. Implantar bancos de dados escaláveis e altamente disponíveis na Google Cloud (~10%)", [
        ("Provisionamento de soluções de banco de dados",
         "Exemplo:\n- Cloud SQL para MySQL/PostgreSQL\n- Cloud Spanner para escala global\n- Bigtable para NoSQL com alta carga."),
        ("Estratégias de recuperação de desastres",
         "Exemplo: Cloud SQL com replicação cross-region + testes de RTO/RPO."),
        ("Automação de provisionamento",
         "Exemplo: Terraform para instanciar Cloud SQL, Spanner e permissões IAM.")
    ])
]

# Preenche o PDF
for section_title, topics in content:
    pdf.chapter_title(section_title)
    for topic_title, topic_body in topics:
        pdf.chapter_title(f" - {topic_title}")
        pdf.chapter_body(topic_body)

# Salva o arquivo PDF
pdf.output("Guia_Completo_Certificacao_Google_Cloud_Database_Engineer.pdf")
