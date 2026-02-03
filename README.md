# Politics Backend - Automated Testing Setup

This repository contains a Django-based politics backend with a comprehensive automated testing pipeline.

## 🚀 Testing Pipeline Overview

Our automated testing setup includes:

- ✅ **Unit Tests** - Pytest for model and business logic validation
- ✅ **API Tests** - Postman collection for API endpoint validation  
- ✅ **Load Tests** - K6 for performance and stress testing
- ✅ **Security Tests** - Bandit for vulnerability scanning
- ✅ **Code Quality** - Linting and coverage analysis
- ✅ **Docker Integration** - Containerized testing environment

## 📋 Prerequisites

- Docker and Docker Compose
- Python 3.10+
- Node.js (for Newman) - optional
- K6 (for load testing) - optional

## 🛠️ Quick Start

### Option 1: Run Everything in Docker (Recommended)

```bash
# Clone and navigate to the project directory
cd politics_backend

# Build and run the complete testing pipeline
docker-compose up --build
```

This will:
- Spin up a PostgreSQL database
- Install all dependencies
- Run migrations
- Execute all test suites (unit, API, security, load)
- Generate reports

### Option 2: Local Development & Testing

```bash
# Install dependencies
pip install -r politics_backend/requirements.txt

# Run unit tests
make unit-test

# Run Django tests
make django-test

# Run security tests
make security-test

# Run all tests
make test

# Run complete pipeline
make docker-test
```

## 🧪 Test Structure

```
tests/
├── test_models.py      # Model-level unit tests
└── test_api.py         # API endpoint tests
```

```
postman/
└── collection.json     # API test collection
```

```
load/
└── k6_script.js        # Load testing script
```

## 📊 Test Reports

After running tests, you'll get:

- **Coverage Report**: Shows code coverage percentage
- **Security Report**: Lists potential vulnerabilities
- **Performance Metrics**: Load test results
- **API Test Results**: Endpoint validation status

## 🔧 Customization

### Adding New Tests

To add new unit tests, create test files in the `tests/` directory following the pattern `test_*.py`.

### Modifying Load Tests

Update the K6 script in `load/k6_script.js` to simulate your specific usage patterns.

### Adjusting Security Tests

Modify the Bandit configuration by updating security checks in the testing pipeline.

## 🚦 CI/CD Ready

This setup is designed for continuous integration. In a CI environment, you can run:

```bash
# Run all tests
./run_tests.sh

# Or use make commands
make test
```

## 🛡️ Security Testing

The pipeline includes automatic security scanning with Bandit:

- Checks for common Python security issues
- Identifies potential vulnerabilities
- Provides remediation suggestions

## 📈 Performance Testing

Using K6 for load testing:

- Simulates concurrent users
- Measures response times
- Tests system stability under load

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

---

Made with ❤️ for robust backend testing.