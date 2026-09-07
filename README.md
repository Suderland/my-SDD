# my-SDD

**Uma base de engenharia de software orientada a agentes para começar novos projetos com um padrão sênior/master, em vez de partir de um repositório vazio e reconstruir as mesmas decisões de qualidade a cada projeto.**

`my-SDD` combina governança para agentes de IA, Agent Skills reutilizáveis, especificações persistentes do projeto, estratégia de testes, rastreabilidade de requisitos e packs opcionais para backend e frontend.

A proposta é simples: **o projeto pode começar do zero em regras de negócio, mas não precisa começar do zero em engenharia**.

---

## Por que usar

Ao iniciar um projeto tradicionalmente, várias decisões precisam ser relembradas ou reexplicadas ao agente:

- como levantar requisitos antes de implementar;
- como estruturar arquitetura e responsabilidades;
- quando aplicar Clean Architecture, DDD, SOLID e TDD;
- quais testes são obrigatórios;
- como validar uma implementação antes de considerá-la concluída;
- como documentar decisões e manter o estado do projeto entre sessões;
- como evitar que o agente carregue documentação desnecessária e desperdice tokens.

`my-SDD` transforma essas expectativas em uma **camada reutilizável de engenharia**.

Com isso, um novo sistema já nasce com uma base consistente para:

- descoberta e clarificação de requisitos;
- planejamento e rastreabilidade;
- arquitetura e design de software;
- testes unitários, E2E e mutation por padrão;
- segurança;
- qualidade e refatoração;
- debugging baseado em evidências;
- documentação;
- observabilidade e APIs no pack backend;
- acessibilidade e engenharia frontend no pack frontend;
- verificação antes de declarar uma tarefa como concluída.

> `my-SDD` não substitui decisões específicas do domínio. Ele estabelece um **piso de qualidade** para que cada projeto comece em um nível de engenharia mais alto.

---

## Modelo mental

A arquitetura possui um tronco e dois galhos principais:

```text
                         AGENTS.md
                             │
                  contrato de engenharia
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
       .agents/skills/               .agents/specs/
       COMO engenheirar              O QUE este sistema exige
       reutilizável                  específico do projeto
              │                             │
              └──────────────┬──────────────┘
                             ▼
                 planejar → implementar → verificar
```

### `AGENTS.md`

É o **contrato raiz de execução**.

Define:

- precedência de instruções;
- princípios gerais de engenharia;
- política de carregamento de contexto;
- como descobrir Skills;
- como consultar Specs;
- regras de planejamento e implementação;
- política de testes e verificação;
- Definition of Done.

O arquivo é propositalmente compacto. Ele funciona como **governança + roteador**, não como uma enciclopédia.

### `.agents/skills/`

Contém conhecimento reutilizável sobre **como desenvolver**.

As Skills seguem *progressive disclosure*: o agente carrega apenas a Skill necessária e lê referências adicionais somente quando a tarefa exigir.

Isso reduz repetição de prompts e ajuda a economizar contexto/tokens.

### `.agents/specs/`

Contém conhecimento exclusivo do sistema atual:

- requisitos;
- critérios de aceitação;
- decisões arquiteturais;
- planos;
- tarefas;
- regras de negócio;
- contratos de API;
- banco de dados;
- restrições de segurança;
- estado atual das features.

A pasta começa vazia em um novo projeto e cresce somente conforme o sistema é especificado.

---

# O que existe no projeto

## Core Skills

O Core é instalado em todo projeto.

| Skill | Responsabilidade |
|---|---|
| `requirements-discovery` | Investigar o pedido, o código e as Specs e perguntar apenas quando houver incerteza relevante |
| `spec-lifecycle` | Criar e manter Spec, plano, tarefas, estado e rastreabilidade |
| `architecture` | Decisões de arquitetura, boundaries, dependências, Clean Architecture/DDD quando adequados |
| `software-design` | Coesão, acoplamento, SOLID, abstrações e design sustentável |
| `testing` | Estratégia de testes unitários, integração, contrato, E2E, mutation e outros |
| `security` | Segurança por design, validação de entradas, autorização, segredos e riscos |
| `code-quality` | Manutenibilidade, refatoração e controle de complexidade |
| `debugging` | Diagnóstico baseado em reprodução, evidências e causa raiz |
| `verification` | Build, análise estática, testes e evidência antes do encerramento |
| `documentation` | Documentação útil, proporcional e sincronizada com o comportamento |
| `delivery` | Mudanças pequenas, reversíveis e prontas para integração/deploy |

Veja [`docs/SKILL-CATALOG.md`](docs/SKILL-CATALOG.md) para o catálogo.

## Backend Pack

Opcional para projetos com backend:

- `backend-development`;
- `api-design`;
- `database-design`;
- `observability`.

## Frontend Pack

Opcional para projetos com interface:

- `frontend-development`;
- `accessibility`.

## Stack Packs

`packs/stacks/` é o ponto de extensão para convenções específicas de tecnologia, por exemplo:

- .NET;
- Java/Spring;
- Node/NestJS;
- Python/FastAPI;
- React/Next.js;
- Angular;
- outras stacks.

A política universal permanece no Core; detalhes de framework ficam no pack específico para evitar contexto desnecessário.

## Maintainer Skills

Não são instaladas em sistemas comuns. Servem para evoluir a própria `my-SDD`:

- `skill-authoring`;
- `skill-evaluation`;
- `sdd-release`.

---

# Specs e controle de progresso

`my-SDD` separa o **requisito estável** do **estado volátil da execução**.

Uma feature pode ter:

```text
SPEC.md    → o que precisa existir
PLAN.md    → como será construído
TASKS.md   → trabalho executável
STATE.json → estado atual e evidências
```

Estados principais:

```text
not_started → in_progress → implemented → verified
```

Estados laterais podem incluir:

```text
blocked
 deferred
 cancelled
```

A regra central é:

> **Implemented não é Done. Done significa Verified.**

Um requisito somente deve chegar a `verified` quando seus critérios de aceitação e evidências de teste/verificação sustentarem essa conclusão.

Isso cria uma trilha rastreável:

```text
Requisito
   ↓
Tarefa
   ↓
Código
   ↓
Testes
   ↓
Evidência
   ↓
Verified
```

---

# Política de testes

Para **sistemas executáveis**, três categorias são obrigatórias por padrão:

1. **Unit tests** — comportamento determinístico e regras de negócio.
2. **E2E tests** — jornadas críticas através da interface pública relevante do sistema.
3. **Mutation testing** — verificar se a suíte realmente detecta alterações semânticas em lógica significativa.

Também entram quando aplicáveis:

- integração;
- contract testing;
- regression testing;
- property-based testing;
- segurança;
- performance/load;
- resiliência;
- acessibilidade;
- migração e compatibilidade.

A estratégia não usa porcentagem de coverage como sinônimo de qualidade. Coverage é um sinal; mutation testing ajuda a avaliar a capacidade dos testes de detectar falhas reais.

Quando uma categoria obrigatória for estruturalmente inaplicável, a ausência deve ser registrada por **waiver explícito e justificado**, nunca simplesmente ignorada.

Veja [`docs/TESTING-POLICY.md`](docs/TESTING-POLICY.md).

---

# Fluxo de desenvolvimento

Um fluxo típico fica assim:

```text
Pedido do usuário
      │
      ▼
requirements-discovery
      │
      ▼
Spec + critérios de aceitação
      │
      ▼
Arquitetura / plano
      │
      ▼
Tasks
      │
      ▼
Implementação
      │
      ▼
Testes necessários
      │
      ▼
Verification
      │
      ▼
STATE = verified
```

O agente deve primeiro consultar Specs e código existentes. Perguntas são feitas quando a resposta altera materialmente comportamento, arquitetura, segurança, modelo de dados, critérios de aceitação ou outra decisão cara de reverter.

A intenção é **enriquecer requisitos importantes sem transformar toda tarefa simples em uma entrevista**.

---

# Instalação

## 1. Clone a `my-SDD`

O repositório é público. Você pode cloná-lo diretamente via SSH ou HTTPS.

Via SSH:

```bash
git clone git@github.com:Suderland/my-SDD.git
cd my-SDD
```

Ou via HTTPS:

```bash
git clone https://github.com/Suderland/my-SDD.git
cd my-SDD
```

O instalador atual usa apenas a biblioteca padrão do Python.

## 2. Instale no projeto desejado

### Core

```bash
python scripts/my_sdd.py init /caminho/do/projeto
```

### Core + Backend

```bash
python scripts/my_sdd.py init /caminho/do/projeto --backend
```

### Core + Frontend

```bash
python scripts/my_sdd.py init /caminho/do/projeto --frontend
```

### Core + Backend + Frontend

```bash
python scripts/my_sdd.py init /caminho/do/projeto --backend --frontend
```

Exemplo:

```bash
python scripts/my_sdd.py init ../meu-saas --backend --frontend
```

Depois da instalação:

```text
meu-saas/
├── AGENTS.md
├── .my-sdd.json
└── .agents/
    ├── skills/
    │   └── ...
    └── specs/
```

`.agents/specs/` começa vazia.

---

# Atualização

Quando a `my-SDD` evoluir, atualize sua cópia local:

```bash
git pull
```

Depois atualize um projeto já inicializado:

```bash
python scripts/my_sdd.py update /caminho/do/projeto
```

A atualização mantém os packs registrados na instalação e atualiza somente arquivos gerenciados pela `my-SDD`.

**Ela não sobrescreve:**

```text
.agents/specs/
```

As Specs pertencem ao projeto e são preservadas.

---

# Consultar a instalação

```bash
python scripts/my_sdd.py status /caminho/do/projeto
```

O comando mostra a versão instalada, packs e quantidade de Specs de features detectadas.

O `spec-lifecycle` também possui tooling para derivar uma visão compacta de progresso a partir dos arquivos de estado das features.

---

# Precedência de instruções

De forma simplificada:

```text
1. Pedido explícito do usuário
2. Project Specs
3. AGENTS.md
4. Skills aplicáveis
5. Convenções do framework
6. Conhecimento geral do agente
```

Portanto uma Skill fornece um **default de engenharia**, enquanto a Spec representa a decisão real daquele produto.

---

# Estrutura do repositório

```text
my-SDD/
├── AGENTS.md
├── README.md
├── CHANGELOG.md
├── VERSION
├── .agents/
│   └── skills/                 # Core
├── packs/
│   ├── backend/skills/
│   ├── frontend/skills/
│   └── stacks/
├── maintainer/
│   └── skills/
├── scripts/
│   ├── my_sdd.py
│   └── validate_repo.py
├── tests/
├── docs/
└── .github/workflows/
```

---

# Validação da própria my-SDD

Validar Skills e estrutura:

```bash
python scripts/validate_repo.py
```

Executar testes automatizados:

```bash
python -m unittest discover -s tests -v
```

A CI executa essas verificações para impedir regressões estruturais.

---

# Princípios de design

1. **Progressive disclosure** — carregar somente o contexto necessário.
2. **Specs over assumptions** — fatos específicos do projeto vencem defaults genéricos.
3. **Questions by impact** — perguntar quando a incerteza realmente importa.
4. **Behavior over implementation details** — testes protegem comportamento e contratos.
5. **Verified over merely implemented** — implementação sem evidência não fecha requisito.
6. **Reusable engineering, project-specific state** — Skills são portáveis; Specs pertencem ao produto.
7. **Quality floor, not dogma** — defaults fortes, com exceções explícitas quando tecnicamente justificadas.
8. **Evaluation-driven Skills** — Skills devem melhorar com casos reais e avaliações, não crescer apenas em documentação.

---

# Benefício estratégico

A `my-SDD` existe para transformar isto:

```text
novo projeto
    ↓
reexplicar arquitetura
    ↓
reexplicar testes
    ↓
reexplicar qualidade
    ↓
reexplicar requisitos
    ↓
reconstruir padrões
```

nisto:

```text
novo projeto
    ↓
instalar my-SDD
    ↓
registrar Specs do domínio
    ↓
começar a desenvolver sobre uma base de engenharia madura
```

O resultado esperado é menos trabalho repetitivo, menos decisões esquecidas, melhor continuidade entre sessões de agentes e uma **baseline de qualidade sênior/master desde o início do sistema**.

---

## Versão

Versão atual: **0.1.0**.

Esta é a baseline arquitetural inicial. As Skills devem continuar sendo avaliadas e refinadas com uso real antes de uma versão estável `1.0`.
