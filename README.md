<div align="center">
<img src="assets/banner.svg" alt="Banner">
</div>

# Awesome Blockchain-Based Prediction Markets: A Comprehensive Guide & Open Source Directory

<div align="center">
<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>
## Top Blockchain-Based Prediction Markets & Open-Source Alternatives

Prediction markets allow users to trade contracts on the outcomes of real-world events such as elections, sports, economics, and more. Blockchain-based platforms bring decentralization, transparency, censorship resistance, and global accessibility, often leveraging oracles for resolution.

This README focuses on prominent platforms (including regulated ones like Kalshi for context) while **emphasizing open-source software, protocols, and self-hostable alternatives** for building, forking, or deploying your own prediction markets.

## 🏢 SaaS/Hosted Platforms

- ### Polymarket
  - **Description**: Leading decentralized prediction market on Polygon with high trading volume on politics, crypto, sports, and events. Uses USDC and a central limit order book (CLOB) model.
  - **Website**: [polymarket.com](https://polymarket.com)
  - **Blockchain**: Polygon (Ethereum L2)
  - **Key Features**: Excellent liquidity, intuitive UI, real-time trading.
  - **Open-Source**: Trading bots and tools available on GitHub.

- ### Kalshi
  - **Description**: CFTC-regulated U.S. prediction market platform for event contracts across sports, politics, economics, and more.
  - **Website**: [kalshi.com](https://kalshi.com)
  - **Key Features**: Legally accessible in the U.S., strong order book mechanics.
  - **Open-Source**: Primarily proprietary.

- ### Augur
  - **Description**: Pioneering fully decentralized prediction market protocol with a decentralized oracle and dispute resolution system.
  - **Website**: [augur.net](https://augur.net)
  - **Blockchain**: Ethereum
  - **Open-Source**: Fully open-source (GitHub: [AugurProject/augur](https://github.com/AugurProject/augur)). Solidity smart contracts under GPL/MIT licenses.

- ### Gnosis Omen (Conditional Tokens Framework)
  - **Description**: Infrastructure layer for prediction markets using conditional tokens. Omen provides a user-facing market interface.
  - **Blockchain**: Ethereum / Gnosis Chain
  - **Open-Source**: Yes — Core contracts and framework are open-source and widely used as building blocks.

- ### Drift Protocol
  - **Description**: Solana-based perpetuals DEX that expanded into prediction markets and event-based trading.
  - **Website**: [drift.trade](https://drift.trade)
  - **Blockchain**: Solana
  - **Open-Source**: Core protocol components are open-sourced.

- ### Azuro
  - **Description**: Decentralized infrastructure protocol providing liquidity, oracles, and tooling for prediction markets and betting apps.
  - **Website**: [azuro.org](https://azuro.org)
  - **Blockchain**: EVM-compatible (Polygon, Base, etc.)
  - **Open-Source**: Strong emphasis — [GitHub: Azuro-protocol](https://github.com/Azuro-protocol). Includes SDKs and Liquidity Tree design.

- ### Hyperliquid
  - **Description**: High-performance on-chain perp DEX (own L1) that added outcome/prediction markets via HIP-4 upgrade.
  - **Website**: [hyperliquid.xyz](https://hyperliquid.xyz)
  - **Blockchain**: Hyperliquid L1
  - **Key Features**: Permissionless market deployment options, high speed, integrated with perps.
  - **Open-Source**: HIP proposals and documentation public; core trading engine varies.

- ### Zeitgeist
  - **Description**: Dedicated prediction market blockchain built on Polkadot/Substrate. Supports complex markets and futarchy governance.
  - **Website**: [zeitgeist.pm](https://zeitgeist.pm)
  - **Open-Source**: Yes — Full protocol, UI, and SDK [](https://github.com/zeitgeistpm).

### Other Notables

**Limitless Exchange**, **Trueo**, **Hedgehog Markets**, **MetaDAO**: Specialized or emerging platforms focused on niches like sports, DAOs, or specific event types.

## 💻 Open-Source Software & Self-Hosted Solutions (Primary Emphasis)

- **Augur** [](https://github.com/AugurProject/augur): Complete decentralized protocol and client for self-deployment.
- **Zeitgeist** ([zeitgeistpm/zeitgeist](https://github.com/zeitgeistpm/zeitgeist) + UI): Production-ready Substrate chain optimized for prediction markets. Includes SDK for custom implementations.
- **Azuro Protocol** [](https://github.com/Azuro-protocol): Modular SDKs, liquidity pools (Liquidity Tree), and tools for building scalable prediction apps.
- **SocialPredict** [](https://github.com/openpredictionmarkets/socialpredict): Easy-to-deploy, MIT-licensed full-stack platform with React frontend and secure contracts. Ideal for communities and organizations.
- **Kuest**: Open-source infrastructure for launching Polymarket-like deployments (e.g., on Polygon).
- **Gnosis Conditional Tokens Framework**: Foundational open contracts for conditional prediction markets.
- **Open Prediction Markets Organization** [](https://github.com/openpredictionmarkets): Hub for multiple production-ready repos and forks.
- **Additional Repos**:
  - Ethereum/Solidity templates under GitHub "prediction-market" topic.
  - Rust trading bot toolkits for Polymarket/Kalshi/etc.
  - Custom implementations (e.g., Arc Prediction Markets with UMA Oracle).

See the [Awesome-Prediction-Market-Tools](https://github.com/aarora4/Awesome-Prediction-Market-Tools) list for more SDKs, bots, and infrastructure.

## 📊 Comparison Table

| Platform/Protocol     | Blockchain              | Trading Model          | Open-Source Level | Key Strengths                     | Best For                     | Pricing | Free Tier Limit | Company Size |
|-----------------------|-------------------------|------------------------|-------------------|-----------------------------------|------------------------------|---------|-----------------|--------------|
| Polymarket           | Polygon                | CLOB                  | Partial          | Liquidity & UX                   | High-volume trading         | Free    | N/A (Trading fees apply) | ~$1 Billion  |
| Hyperliquid          | Hyperliquid L1         | Outcomes (HIP-4)      | Partial          | Speed, perps integration         | On-chain high-throughput    | Free    | N/A (Trading fees apply) | ~$1 Billion  |
| Gnosis/Omen          | Ethereum/Gnosis        | Conditional Tokens    | High             | Modular infrastructure           | Custom market building      | Free    | N/A (Open Source)        | ~$400 Million|
| Kalshi               | Regulated (Off-chain)  | Order Book            | Low              | U.S. regulatory compliance       | Legal U.S. events           | Free    | N/A (Trading fees apply) | ~$100 Million|
| Augur                | Ethereum               | Oracle + Disputes     | Full             | Full decentralization            | Permissionless oracles      | Free    | N/A (Open Source)        | ~$30 Million |
| Azuro                | EVM                    | AMM / Liquidity Pool  | High             | SDKs, liquidity tools            | Sports & developer apps     | Free    | N/A (Open Source)        | ~$20 Million |
| Zeitgeist            | Polkadot/Substrate     | Dedicated Chain       | Full             | Futarchy, scalability            | Governance & complex PMs    | Free    | N/A (Open Source)        | ~$5 Million  |
| SocialPredict        | Flexible               | Full Stack            | Full (MIT)       | Easy deployment                  | Self-hosted / communities   | Free    | N/A (Open Source)        | N/A (OSS)    |

## 🚀 Getting Started with Open-Source Projects

1. **Choose a Base** — SocialPredict or Zeitgeist for quick starts; Azuro/Augur for EVM depth.
2. **Tech Stack** — Solidity/Rust smart contracts, React frontends, Chainlink/UMA oracles.
3. **Deployment** — Testnets first (Sepolia, Polygon Mumbai, etc.), then mainnet.
4. **Key Considerations** — Liquidity provision, oracle reliability, dispute mechanisms, gas fees, and regulatory compliance.
5. **Tools** — Subgraphs for indexing, SDKs for integration, bots for trading automation.

## 📚 Resources & Community

- GitHub Topic: [prediction-market](https://github.com/topics/prediction-market)
- Awesome List: [Awesome-Prediction-Market-Tools](https://github.com/aarora4/Awesome-Prediction-Market-Tools)
- Project Discords, Telegrams, and forums (e.g., Effective Altruism forecasting groups)
- Documentation: Each project's GitHub README and official docs

**Disclaimer**: Trading involves risk of loss. Always DYOR. Open-source projects require technical knowledge for secure deployment. Respect local regulations.

---

*Contributions welcome! Add more open-source projects, fix details, or improve sections via PRs.*

## ⭐ Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007/Awesome-Blockchain-Based-Prediction-Markets&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Blockchain-Based-Prediction-Markets&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Blockchain-Based-Prediction-Markets&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Blockchain-Based-Prediction-Markets&type=date&legend=bottom-right" />
</picture>
</a>
</div>
