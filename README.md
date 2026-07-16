# Llm Evaluation Engine

Scalable framework for evaluating LLM responses with hallucination detection and safety scoring.

## 🔍 TL;DR
> Automated evaluation engine for LLMs with advanced hallucination and safety metrics.

## 🏗️ Architecture
```mermaid
graph TD
    A[User/Client] -->|HTTPS/API| B{Load Balancer}
    B --> C{Microservice API}
    B --> D{Auth Middleware}
    C --> E[(Database)]
    D --> F[(Redis Cache)]
    C --> G[External API]
    
    subgraph Observability
        H[Prometheus] -.->|Metrics| C
        I[Grafana] -.->|Visualize| H
        J[Loki] -.->|Logs| C
    end

    style C fill:#f9f,stroke:#333,stroke-width:2px
    style H fill:#bbf,stroke:#333
    style I fill:#bbf,stroke:#333
```

## 🛠️ Tech Stack
Python | Pydantic | Asyncio | LLM

## 🚀 Usage / Demo
### Local Setup
```bash
git clone https://github.com/yemisalako01-code/llm-evaluation-engine.git
cd llm-evaluation-engine
# Follow instructions in docs/azure-ci-cd-pipeline.md or docs/setup.md
```

### Demo Components
- **Architecture Diagram:** See [Architecture](#-architecture) section above.
- **Screenshots:** *(Placeholder for live demo screenshots)*
  - *Dashboard View:* [Link to GitHub Pages]
  - *Pipeline Execution:* [Link to Azure/Actions Run]

## 💡 Why This Matters
> Highlights unique expertise in Generative AI quality assurance and model alignment.

## 📚 Documentation
- [Architecture Decisions](docs/ARCHITECTURE_DECISIONS.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Contributing](CONTRIBUTING.md)

## 📜 License
MIT License - see [LICENSE](LICENSE)
